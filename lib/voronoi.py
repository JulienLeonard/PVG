#!/usr/bin/env python
#coding:utf-8
"""
Voronoi diagram calculator/Delaunay triangulator

Calculate Delaunay triangulation and the Voronoi polygons for a set of
2D input points.
"""
#  Translated to Python by Bill Simons
#  September, 2005
#  Derived from code bearing the following notice:
#
#  The author of this software is Steven Fortune.  Copyright (c) 1994 by AT&T
#  Bell Laboratories.
#  Permission to use, copy, modify, and distribute this software for any
#  purpose without fee is hereby granted, provided that this entire notice
#  is included in all copies of any software which is or includes a copy
#  or modification of this software and in all copies of the supporting
#  documentation for such software.
#  THIS SOFTWARE IS BEING PROVIDED "AS IS", WITHOUT ANY EXPRESS OR IMPLIED
#  WARRANTY.  IN PARTICULAR, NEITHER THE AUTHORS NOR AT&T MAKE ANY
#  REPRESENTATION OR WARRANTY OF ANY KIND CONCERNING THE MERCHANTABILITY
#  OF THIS SOFTWARE OR ITS FITNESS FOR ANY PARTICULAR PURPOSE.
#
#  Comments were incorporated from Shane O'Sullivan's translation of the
#  original code into C++ (http://mapviewer.skynet.ie/voronoi.html)
#
#  Steve Fortune's homepage: http://netlib.bell-labs.com/cm/cs/who/sjf/index.html
#
#  Python code refactoring by mozman
#  April, 2010

import math
from basics import *

__all__ = ['voronoi']

TOLERANCE = 1e-9
BIG_FLOAT = 1e38

def voronoi(points):
    """ Takes a list of 2d points like [(1, 2), (5, 7), (12, 6.7), ...].

    Returns a Context object with following attributes:

    vertices -- a list of point-tuples, which are the x, y coordinates of the
        Voronoi diagram vertices
    lines -- a list of 3-tuples (a, b, c) which are the equations of the
        lines in the Voronoi diagram: a*x + b*y = c
    edges -- a list of 3-tuples, (l, v1, v2) representing edges of the
        Voronoi diagram.  l is the index of the line, v1 and v2 are
        the indices of the vertices at the end of the edge.  If
        v1 or v2 is -1, the line extends to infinity.
    triangles -- a list of 3-tuples: the indices of the points that form a
        Delaunay triangle.
    """

    context = Context(points)
    sites = Sites(points)
    edges = Edges(sites.xmin, sites.xmax, len(sites))
    priority_queue = PriorityQueue(sites.ymin, sites.ymax, len(sites))
    itersites = iter(sites)

    bottomsite = next(itersites)
    newsite = next(itersites)
    min_point = Site((-BIG_FLOAT, -BIG_FLOAT))
    while True:
        if not priority_queue.is_empty():
            min_point = priority_queue.get_min_point()

        if (newsite and (priority_queue.is_empty() or (newsite < min_point))):
            # newsite is smallest - this is a site event
            # get first Halfedge to the LEFT and RIGHT of the new site
            lbnd = edges.leftbnd(newsite)
            rbnd = lbnd.right

            # if this halfedge has no edge, bot = bottom site (whatever that is)
            # create a new edge that bisects
            bot = lbnd.right_reg(bottomsite)
            edge = Edge.bisect(bot, newsite)
            context.out_bisector(edge)

            # create a new Halfedge, setting its marker field to 0 and insert
            # this new bisector edge between the left and right vectors in
            # a linked list
            bisector = Halfedge(edge, Edge.LEFT)
            edges.insert(lbnd, bisector)

            # if the new bisector intersects with the left edge, remove
            # the left edge's vertex, and put in the new one
            point = lbnd.intersect(bisector)
            if point is not None:
                priority_queue.delete(lbnd)
                priority_queue.insert(lbnd, point, newsite.distance(point))

            # create a new Halfedge, setting its marker field to 1
            # insert the new Halfedge to the right of the original bisector
            lbnd = bisector
            bisector = Halfedge(edge, Edge.RIGHT)
            edges.insert(lbnd, bisector)

            # if this new bisector intersects with the right Halfedge
            point = bisector.intersect(rbnd)
            if point is not None:
                # push the Halfedge into the ordered linked list of vertices
                priority_queue.insert(bisector, point, newsite.distance(point))

            try:
                newsite = next(itersites)
            except StopIteration:
                newsite = None

        elif not priority_queue.is_empty():
            # intersection is smallest - this is a vector (circle) event.
            # Pop the Halfedge with the lowest vector off the ordered list of
            # vectors.
            # Get the Halfedge to the left and right of the above HE
            # and also the Halfedge to the right of the right HE
            lbnd  = priority_queue.pop_min_halfedge()
            llbnd = lbnd.left
            rbnd  = lbnd.right
            rrbnd = rbnd.right

            # get the Site to the left of the left HE and to the right of
            # the right HE which it bisects
            bot = lbnd.left_reg(bottomsite)
            top = rbnd.right_reg(bottomsite)

            # output the triple of sites, stating that a circle goes through
            # them
            mid = lbnd.right_reg(bottomsite)
            context.out_triple(bot, top, mid)

            # get the vertex that caused this event and set the vertex number
            # couldn't do this earlier since we didn't know when it would be
            # processed
            vertex = lbnd.vertex
            context.out_vertex(vertex)

            # set the endpoint of the left and right Halfedge to be this vector
            if lbnd.edge.set_endpoint(lbnd.marker, vertex):
                context.out_edge(lbnd.edge)

            if rbnd.edge.set_endpoint(rbnd.marker, vertex):
                context.out_edge(rbnd.edge)

            # delete the lowest HE, remove all vertex events to do with the
            # right HE and delete the right HE
            edges.delete(lbnd)
            priority_queue.delete(rbnd)
            edges.delete(rbnd)

            # if the site to the left of the event is higher than the Site
            # to the right of it, then swap them and set 'marker' to RIGHT
            marker = Edge.LEFT
            if bot.y > top.y:
                bot, top = top, bot
                marker = Edge.RIGHT

            # Create an Edge (or line) that is between the two Sites.  This
            # creates the formula of the line, and assigns a line number to it
            edge = Edge.bisect(bot, top)
            context.out_bisector(edge)

            # create a HE from the edge
            bisector = Halfedge(edge, marker)

            # insert the new bisector to the right of the left HE
            # set one endpoint to the new edge to be the vector point 'v'
            # If the site to the left of this bisector is higher than the right
            # Site, then this endpoint is put in position 0; otherwise in pos 1
            edges.insert(llbnd, bisector)
            if edge.set_endpoint(Edge.RIGHT - marker, vertex):
                context.out_edge(edge)

            # if left HE and the new bisector don't intersect, then delete
            # the left HE, and reinsert it
            point = llbnd.intersect(bisector)
            if point is not None:
                priority_queue.delete(llbnd)
                priority_queue.insert(llbnd, point, bot.distance(point))

            # if right HE and the new bisector don't intersect, then reinsert it
            point = bisector.intersect(rrbnd)
            if point is not None:
                priority_queue.insert(bisector, point, bot.distance(point))
        else:
            break

    halfedge = edges.leftend.right
    while halfedge is not edges.rightend:
        context.out_edge(halfedge.edge)
        halfedge = halfedge.right

    return context

class Context(object):
    def __init__(self, points):
        # list of vertex 2-tuples: (x,y)
        self.input_points = points

        # list of vertex 2-tuples: (x,y)
        self.vertices = []

        # equation of line 3-tuple (a b c), for the equation of the
        # line a*x+b*y = c
        self.lines = []

        # edge 3-tuple: (line index, vertex 1 index, vertex 2 index)
        # if either vertex index is -1, the edge extends to infinity
        self.edges = []

        # 3-tuple of vertiex indices of the input_points!
        self.triangles = []

    def out_vertex(self, site):
        site.sitenum = len(self.vertices)
        self.vertices.append((site.x, site.y))

    def out_triple(self, site1, site2, site3):
        self.triangles.append((site1.sitenum, site2.sitenum, site3.sitenum))

    def out_bisector(self, edge):
        self.lines.append((edge.a, edge.b, edge.c))

    def out_edge(self, edge):
        sitenum_left = -1
        if edge.points[Edge.LEFT] is not None:
            sitenum_left = edge.points[Edge.LEFT].sitenum
        sitenum_right = -1
        if edge.points[Edge.RIGHT] is not None:
            sitenum_right = edge.points[Edge.RIGHT].sitenum
        self.edges.append((edge.edgenum, sitenum_left, sitenum_right))

    def get_triangle(self, index):
        """Get Delaunay-Triangle-Points as list of indices.

        example: (index1, index2, index3)
        index1,... is the index to the input_points list
        """
        return self.triangles[index]

    def iter_triangles(self):
        return iter(self.triangles)

    def get_triangle_vertices(self, index):
        """Get Delaunay-Triangle-Points as list of (x, y)-tuples
        """
        triangle = self.get_triangle(index)
        return [self.input_points[index] for index in triangle]

    def iter_triangle_vertices(self):
        for index in range(len(self.triangles)):
            yield self.get_triangle_vertices(index)

    def get_vertex(self, index):
        """Get Voronoi-Point at index as (x, y)-tuple.
        """
        if index != -1:
            return self.vertices[index]
        else:
            return None

    def iter_vertices(self):
        return iter(self.vertices)

    def get_edge(self, index):
        """Get edge at <index>.
        """
        edgenum, p0, p1 = self.edges[index]
        vertex0 = self.get_vertex(p0)
        vertex1 = self.get_vertex(p1)
        if (vertex0 is not None) and (vertex1 is not None):
            return (vertex0, vertex1)
        else:
            return None

    def iter_edges(self):
        for index in range(len(self.edges)):
            yield self.get_edge(index)


def almost_equal(a, b, relative_error=TOLERANCE):
    # is almost equal to within the allowed relative error
    norm = max(abs(a), abs(b))
    return (norm < relative_error) or (abs(a - b) < (relative_error * norm))


class Site(object):
    __slots__ = ['x', 'y', 'sitenum']
    def __init__(self, point, sitenum=0):
        self.x = point[0]
        self.y = point[1]
        self.sitenum = sitenum

    def __eq__(self, other):
        return self.y == other.y and \
            self.x == other.x

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        else:
            return self.y < other.y


    def getsortkey(self):
        return (self.y, self.x)

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx*dx + dy*dy)


class Sites(list):
    def __init__(self, points):
        super(Sites, self).__init__()
        self.xmin, self.ymin = points[0]
        self.xmax, self.ymax = points[0]

        for num, point in enumerate(points):
            self.append(Site(point, num))
            x, y = point
            if x < self.xmin:
                self.xmin = x
            if y < self.ymin:
                self.ymin = y
            if x > self.xmax:
                self.xmax = x
            if y > self.ymax:
                self.ymax = y
        self.sort(key=lambda x: x.getsortkey())


class Edge(object):
    LEFT = 0
    RIGHT = 1
    EDGE_NUM = 0
    DELETED = {}   # marker value

    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.points = [None, None]
        self.reg = [None, None]
        self.edgenum = 0

    def set_endpoint(self, position, site):
        self.points[position] = site
        if self.points[Edge.RIGHT - position] is None:
            return False
        return True

    @staticmethod
    def bisect(site1, site2):
        newedge = Edge()
        newedge.reg[0] = site1 # store the sites that this edge is bisecting
        newedge.reg[1] = site2

        # to begin with, there are no endpoints on the bisector - it goes to
        # infinity, points[0] and points[1] are None
        # get the difference in x dist between the sites
        dx = float(site2.x - site1.x)
        dy = float(site2.y - site1.y)
        adx = abs(dx)  # make sure that the difference in positive
        ady = abs(dy)

        # puts("site2",site2.x,site2.y,"site1",site1.x,site1.y)

        # get the slope of the line
        newedge.c = float(site1.x * dx + site1.y * dy + (dx*dx + dy*dy)*0.5)
        if adx > ady :
            # set formula of line, with x fixed to 1
            newedge.a = 1.0
            newedge.b = dy / dx
            newedge.c /= dx
        else:
            # set formula of line, with y fixed to 1
            newedge.b = 1.0
            newedge.a = dx / dy
            newedge.c /= dy

        newedge.edgenum = Edge.EDGE_NUM
        Edge.EDGE_NUM += 1
        return newedge

class Halfedge(object):
    def __init__(self, edge=None, marker=Edge.LEFT):
        self.left = None    # left Halfedge in the edge list
        self.right = None   # right Halfedge in the edge list
        self.qnext = None   # priority queue linked list pointer
        self.edge = edge    # edge list Edge
        self.marker = marker
        self.vertex = None  # Site()
        self.ystar = BIG_FLOAT

    def __eq__(self, other):
        return self.ystar == other.ystar and \
               self.vertex.x == other.vertex.x

    def __lt__(self, other):
        if self.ystar  == other.ystar:
            return self.vertex.x < other.vertex.x
        else:
            return self.ystar < other.ystar

    def left_reg(self, default):
        if not self.edge:
            return default
        elif self.marker == Edge.LEFT:
            return self.edge.reg[Edge.LEFT]
        else:
            return self.edge.reg[Edge.RIGHT]

    def right_reg(self, default):
        if not self.edge:
            return default
        elif self.marker == Edge.LEFT:
            return self.edge.reg[Edge.RIGHT]
        else:
            return self.edge.reg[Edge.LEFT]

    def is_point_right_of(self, point):
        """Returns True if <point> is to right of halfedge.
        """
        edge = self.edge
        topsite = edge.reg[1]
        right_of_site = point.x > topsite.x

        if(right_of_site and self.marker == Edge.LEFT):
            return True

        if(not right_of_site and self.marker == Edge.RIGHT):
            return False

        if(edge.a == 1.0):
            dyp = point.y - topsite.y
            dxp = point.x - topsite.x
            fast = 0
            if ((not right_of_site and edge.b < 0.0) or \
                (right_of_site and edge.b >= 0.0)):
                above = dyp >= edge.b * dxp
                fast = above
            else:
                above = point.x + point.y * edge.b > edge.c
                if(edge.b < 0.0):
                    above = not above
                if (not above):
                    fast = 1
            if (not fast):
                dxs = topsite.x - (edge.reg[0]).x
                above = (edge.b * (dxp*dxp - dyp*dyp)) < \
                        (dxs*dyp*(1.0+2.0*dxp/dxs + edge.b*edge.b))
                if(edge.b < 0.0):
                    above = not above
        else:  # edge.b == 1.0
            yl = edge.c - edge.a * point.x
            t1 = point.y - yl
            t2 = point.x - topsite.x
            t3 = yl - topsite.y
            above = t1*t1 > t2*t2 + t3*t3

        if(self.marker == Edge.LEFT):
            return above
        else:
            return not above

    def intersect(self, other):
        """Create a new site where the Halfedges edge1 and edge2 intersect.
        """
        edge1 = self.edge
        edge2 = other.edge
        if (edge1 is None) or (edge2 is None):
            return None

        # if the two edges bisect the same parent return None
        if edge1.reg[1] is edge2.reg[1]:
            return None

        d = edge1.a * edge2.b - edge1.b * edge2.a
        if almost_equal(d, 0.0):
            return None

        intersect_x = (edge1.c * edge2.b - edge2.c * edge1.b) / d
        intersect_y = (edge2.c * edge1.a - edge1.c * edge2.a) / d
        if edge1.reg[1] < edge2.reg[1]:
            halfedge = self
            edge = edge1
        else:
            halfedge = other
            edge = edge2

        right_of_site = intersect_x >= edge.reg[1].x
        if ((right_of_site and halfedge.marker == Edge.LEFT) or
            (not right_of_site and halfedge.marker == Edge.RIGHT)):
            return None

        # create a new site at the point of intersection - this is a new
        # vector event waiting to happen
        return Site((intersect_x, intersect_y))


class Edges(object):
    def __init__(self, xmin, xmax, nsites):
        if xmin > xmax:
            xmin, xmax = xmax, xmin
        self.hashsize = int(2 * math.sqrt(nsites + 4))

        self.xmin = xmin
        self.deltax = float(xmax - xmin)
        self.queues = [None] * self.hashsize

        self.leftend = Halfedge()
        self.rightend = Halfedge()
        self.leftend.right = self.rightend
        self.rightend.left = self.leftend
        self.queues[0] = self.leftend
        self.queues[-1] = self.rightend

    def insert(self, left, halfedge):
        halfedge.left = left
        halfedge.right = left.right
        left.right.left = halfedge
        left.right = halfedge

    def delete(self, halfedge):
        halfedge.left.right = halfedge.right
        halfedge.right.left = halfedge.left
        halfedge.edge = Edge.DELETED

    def gethash(self, b):
        """Get entry from hash table, pruning any deleted nodes.
        """
        if(b < 0) or (b >= self.hashsize):
            return None
        halfedge = self.queues[b]
        if (halfedge is None) or (halfedge.edge is not Edge.DELETED):
            return halfedge

        # Hash table points to deleted half edge.  Patch as necessary.
        self.queues[b] = None
        return None

    def leftbnd(self, point):
        # Use hash table to get close to desired halfedge
        bucket = int(((point.x - self.xmin) / self.deltax * self.hashsize))

        if(bucket < 0):
            bucket = 0

        if(bucket >= self.hashsize):
            bucket = self.hashsize - 1

        halfedge = self.gethash(bucket)
        if(halfedge is None):
            i = 1
            while True:
                halfedge = self.gethash(bucket - i)
                if (halfedge is not None):
                    break
                halfedge = self.gethash(bucket + i)
                if (halfedge is not None):
                    break
                i += 1

        # Now search linear list of halfedges for the correct one
        if (halfedge is self.leftend) or \
           ((halfedge is not self.rightend) and halfedge.is_point_right_of(point)):
            halfedge = halfedge.right
            while (halfedge is not self.rightend) and (halfedge.is_point_right_of(point)):
                halfedge = halfedge.right
            halfedge = halfedge.left
        else:
            halfedge = halfedge.left
            while (halfedge is not self.leftend) and \
                  not halfedge.is_point_right_of(point):
                halfedge = halfedge.left

        # Update hash table and reference counts
        if(bucket > 0 and bucket < self.hashsize-1):
            self.queues[bucket] = halfedge
        return halfedge


class PriorityQueue(object):
    def __init__(self, ymin, ymax, nsites):
        self.ymin = ymin
        self.deltay = ymax - ymin
        self.hashsize = int(4 * math.sqrt(nsites))
        self.count = 0
        self.min_index = 0
        self.queues = [Halfedge()] * self.hashsize

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def insert(self, halfedge, site, offset):
        halfedge.vertex = site
        halfedge.ystar  = site.y + offset
        last = self.queues[self.get_bucket(halfedge)]
        qnext = last.qnext
        while (qnext is not None) and (halfedge > qnext):
            last = qnext
            qnext = last.qnext
        halfedge.qnext = last.qnext
        last.qnext = halfedge
        self.count += 1

    def delete(self, halfedge):
        if (halfedge.vertex is not None):
            last = self.queues[self.get_bucket(halfedge)]
            while last.qnext is not halfedge:
                last = last.qnext
            last.qnext = halfedge.qnext
            self.count -= 1
            halfedge.vertex = None

    def get_bucket(self, halfedge):
        """Returns the index of queue which contains <halfedge>.
        """
        bucket = int(((halfedge.ystar - self.ymin) / self.deltay) * self.hashsize)
        if bucket < 0:
            bucket = 0
        if bucket >= self.hashsize:
            bucket = self.hashsize-1
        if bucket < self.min_index:
            self.min_index = bucket
        return bucket

    def get_min_point(self):
        while(self.queues[self.min_index].qnext is None):
            self.min_index += 1
        halfedge = self.queues[self.min_index].qnext
        x = halfedge.vertex.x
        y = halfedge.ystar
        return Site((x, y))

    def pop_min_halfedge(self):
        curr = self.queues[self.min_index].qnext
        self.queues[self.min_index].qnext = curr.qnext
        self.count -= 1
        return curr


