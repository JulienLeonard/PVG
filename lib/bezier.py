from utils    import *
from geoutils import *
from polygon  import *

class Bezier:
	def __init__(self,p1,p2,p3,p4):
		self.points    = [p1,p2,p3,p4]
		self.factors   = [None,None,None,None]
		self.tfactors  = [None,None,None]
		self.afactors  = [None,None]
		self.factorok  = 0
		self.msegments = []
		self.mlength = 0
		self.msegerror = 0.0;

	def firstpoint(self):
		return self.points[0]

	def lastpoint(self):
		return self.points[-1]

	def firstvector(self):
		return self.points[1].sub(self.points[0])

	def lastvector(self):
		return self.points[2].sub(self.points[3])

	def compute_factors(self):
		x0,y0 = self.points[0].coords()
		x1,y1 = self.points[1].coords()
		x2,y2 = self.points[2].coords()
		x3,y3 = self.points[3].coords()

		self.factors[0] = ((x0 - x1 * 3.0 + x2 * 3.0 - x3) * -1.0,
				   (y0 - y1 * 3.0 + y2 * 3.0 - y3) * -1.0)
		self.factors[1] = ((x0 - x1 * 2.0 + x2 ) * 3.0,
				   (y0 - y1 * 2.0 + y2 ) * 3.0)		
		self.factors[2] = ((x1 - x0 ) * 3.0,
				   (y1 - y0 ) * 3.0)
		self.factors[3] = (x0,y0)

		self.tfactors[0] = self.factors[0]
		self.tfactors[1] = vscale(self.factors[1], 2.0 / 3.0)
		self.tfactors[2] = vscale(self.factors[2], 1.0/3.0)
		
		self.afactors[0] = vscale(self.tfactors[0], 2.0 )
		self.afactors[1] = self.tfactors[1]
		
		self.factorok = 1
				  
	def _point(self,t):
		if not self.factorok:
			self.compute_factors()

		t2 = t*t
		t3 = t2*t
		f0x,f0y = self.factors[0]
		f1x,f1y = self.factors[1]
		f2x,f2y = self.factors[2]
		f3x,f3y = self.factors[3]
		
		result = Point(f3x + t * f2x + t2 * f1x + t3 * f0x,
			       f3y + t * f2y + t2 * f1y + t3 * f0y)
		return result

	def _tangent(self,t):
		if not self.factorok:
			self.compute_factors()

		t2 = t * t
		tf0x,tf0y = self.tfactors[0]
		tf1x,tf1y = self.tfactors[1]
		tf2x,tf2y = self.tfactors[2]
		result = Vector(tf2x + t*tf1x +t2 * tf0x,
				tf2y + t*tf1y +t2 * tf0y)
		return result

	def acc(self,t):
		if not self.factorok:
			self.compute_factors()

		return padd(self.afactors[1],vscale(self.afactors[0],t))

	def subtangents(self,t1, t2):
		v1 = self.tangent(t1).scale((t2 - t1))
		v2 = self.tangent(t2).scale((t1 - t2))
		return (v1,v2)

	def subbezzier(self,t1,t2):
		v1,v2 = self.subtangents(t1,t1)
		p1,p2 = [self._point(t) for t in (t1,t2)]
		return bezierfrompointvector(p1,v1,p2,v1)

	def reverse(self):
		return Bezier(self.points[3],self.points[2],self.points[1],self.points[0])

	def translate(self,v):
		return bezierfrompointlist([p.add(v) for p in self.points])

	def rotate(self,center, angle):
		return bezierfrompointlist([p.rotate(center,angle) for p in self.points])
	
	def sym(self,center):
		return bezierfrompointlist([p.sym(center) for p in self.points])

	def symx(self,symx):
		return bezierfrompointlist([p.symx(symx) for p in self.points])

	def _frame(self,t):
		return (self._point(t),self._tangent(t))

	def frame(self,t):
		self.checksegments()
		return self.mpolygon.frame(t)

	def tangent(self,t):
		self.checksegments()
		return self.mpolygon.tangent(t)

	def point(self,t):
		self.checksegments()
		result = self.mpolygon.point(t)
		# puts("point t",t,"result",result)
		return result

	def computesegments(self,error):
		roots = [(t,self._frame(t)) for t in samples((0.0,1.0),10)]
		front = []
		for r1,r2 in pairs(roots):
			front.extend([r1,r2])
		result = {}
		while len(front):
			d1,d2 = front[:2]
			t1,f1 = d1
			t2,f2 = d2
			# print "t1",t1,"t2",t2
			front = front[2:]
			dev1 = vsangle(f2[1],vector(f1[0],f2[0]))
			if dev1 > 3.0:
				dev1 -= (2.0 * 3.14159)
			dev2 = vsangle(f1[1],vector(f1[0],f2[0]))			
			if dev2 > 3.0:
				dev2 -= (2.0 * 3.14159)
			if (abs(dev1)+abs(dev2) > error and abs(t1 - t2) > 0.01):
				middle = (t1+t2)/2.0
				dmiddle = (middle,self._frame(middle))
				front.extend([d1,dmiddle])
				front.extend([dmiddle,d2])
			else:
				result[t1] = f1
				result[t2] = f2
		
		ts = result.keys()
		ts.sort()
		# print "ts",ts
		segpoints = [result[t][0] for t in ts]  
		self.msegments = segpoints
		self.msegerror = error
		self.mlength = self.computelength(self.msegments)
		self.mpolygon = Polygon(self.msegments)
		
	def computelength(self,segments):
		return ladd([dist(p1,p2) for (p1,p2) in pairs(segments)])

	def polygon(self,error=0.01):
		return Polygon(self.segments(error))

	def length(self,error=0.01):
		self.checksegments(error)
		return self.mlength

	def segments(self,error = 0.01):
		self.checksegments(error)
		return self.msegments

	def checksegments(self,error = 0.01):
		if len(self.msegments) == 0 or error != self.msegerror:
			self.computesegments(error)

	def viewbox(self):
		self.checksegments()
		return points2bbox(self.msegments)
		
		
def bezierfrompointvector(p1,v1,p4,v4):
	p2 = p1.add(v1)
	p3 = p4.add(v4)
	return Bezier(p1,p2,p3,p4)

def bezierfrompointlist(points):
	p1,p2,p3,p4 = points
	return Bezier(p1,p2,p3,p4)

def bezierfrompointsangle(p1,p2,angle,factor=1.0):
	v1 = vector(p1,p2).rotate( angle).scale(1.0/3.0*factor)
	v2 = vector(p2,p1).rotate(-angle).scale(1.0/3.0*factor)
	return bezierfrompointvector(p1,v1,p2,v2)

# pvlist is of the form (p1,v1,p2,v2,...,pn,vn)
# to give beziers ((p1,p1+v1,p2 - v2,p2), (p2,p2+v2,p3-v3,p3),...,(pn-1,pn-1 + vn-1, pn-vn,pn)).polygon()
def bezierpolygonfrompointsvectors(pvlist):
	beziers = []
	i = 0
	while i < len(pvlist)-3:
		p1 = pvlist[i]
		p2 = p1.add(pvlist[i+1])
		p4 = pvlist[i+2]
		p3 = p4.add(vscale(pvlist[i+3],-1.0))
		# print "list ",p1,p2,p3,p4
		beziers.append(Bezier(p1,p2,p3,p4))
		i += 2
	# print "beziers length",len(beziers)
	result = beziers[0].polygon()
	for bezier in beziers[1:]:
		result = result.concat(bezier.polygon())

	return result

def regularbezierpolygonfrompointsvectors(pvlist):
	beziers = []
	i = 0
	while i < len(pvlist)-3:
		p1 = pvlist[i]
		p2 = pvlist[i+2]
		d  = dist(p1,p2)
		v1 = pvlist[i+1].normalize().scale( d/3.0)
		v2 = pvlist[i+3].normalize().scale(-d/3.0)
		beziers.append(bezierfrompointvector(p1,v1,p2,v2))
		i += 2
	# print "beziers length",len(beziers)
	#result = beziers[0].polygon()
	#for bezier in beziers[1:]:
	#	result = result.concat(bezier.polygon())
	result = PolyBezier().adds(beziers)	
	return result

def regularbezierfrompoints(plist):
	beziers = []
	i = 0
	
	pvlist = []
	vectors = {}

	for p in plist:
		vectors[p] = []
	
	for (p1,p2) in pairs(plist):
		v = vector(p1,p2)
		vectors[p1].append(v)
		vectors[p2].append(v)
		
	pvlist = []
	for p in plist:
		pvlist.append(p)
		pvlist.append(pmiddle(vectors[p]))
		
	return regularbezierpolygonfrompointsvectors(pvlist)

		

def closingbezier(poly1,poly2):
    f1 = poly1.frame(1.0)
    f2 = poly2.frame(0.0)
    p1,v1 = f1
    p2,v2 = f2
    tan2 = v1.normalize().scale(vector(p1,p2).length() *  1.0/3.0)
    tan2 = v2.normalize().scale(vector(p1,p2).length() * -1.0/3.0)
    bezier = bezierfrompointvector(p1,tan1,p2,tan2)
    return bezier.polygon()


def bezierconcat(polygons,close=False):
    result = []
    if close:
        polygons.append(polygons[0])
    for poly1,poly2 in pairs(polygons):
        result.extend(poly1.points())
        result.extend(closingbezier(poly1,poly2).points())
    result.extend(poly2.points())
    return result

#
# parse svg bezier path and create the corresponding object
#
# result = list of bezier curves (several if closed or 1 if not)
#
def svg2bezier(svgpath,coords0=(0.0,0.0)):
	result = []
	cbeziers = []
	ccbezier = []
	ref = coords0
	isrelative = True
	ctype = ""
	lastpoint = ""
	resetpoint = False
	isfirstm = True
	for data in svgpath.split(" "):
		values = data.split(",")
		if len(values) == 1:
			instruction = values[0]
			# puts("instruction",instruction)
			resetpoint = "True"
			if lastpoint != "":
				ref = lastpoint
			
			if instruction == "m" or instruction == "M":
				isrelative = True
				if instruction == "M":
					isrelative = False
				ctype = "m"
				isfirstm = True
		
			if instruction == "c" or instruction == "C":
				isrelative = True
				if instruction == "C":
					isrelative = False
				ctype = "c"
				
			if instruction == "l" or instruction == "L":
				isrelative = True
				if instruction == "L":
					isrelative = False
				ctype = "l"

			if instruction == "z" or instruction == "Z":
				#puts("cbeziers[0][0]",cbeziers[0][0],"ref",ref)
				cbeziers.append([ref,cbeziers[0][0],ref,cbeziers[0][0]])
				result.append(cbeziers)
				cbeziers = []
				ccbezier = []

		else:
			# coords
			(x,y) = values
			(x,y) = (float(x),float(y))
			# puts("coords",values,"isrelative",isrelative,"x,y",(x,y))

			if isrelative:
				(x,y) = (x + ref[0], y + ref[1])
			newpoint = (x,y)

			if ctype == "m":
				ref = newpoint
				if isfirstm:
					isfirstm = False
				else:
					ccbezier = [lastpoint,newpoint,lastpoint,newpoint]
					cbeziers.append(ccbezier)
					ccbezier = []

			if ctype == "c":	
				if len(ccbezier) == 0:
					ccbezier = [lastpoint,newpoint]
				else:
					ccbezier.append(newpoint)
					if len(ccbezier) == 4:
						cbeziers.append(ccbezier)
						ccbezier = [newpoint]
						ref = newpoint
			
			if ctype == "l":	
				ccbezier = [lastpoint,newpoint,lastpoint,newpoint]
				cbeziers.append(ccbezier)
				ccbezier = []
				ref = newpoint
			lastpoint = newpoint

	if len(cbeziers):
		result.append(cbeziers)

	# puts("parsing svg finished. Build polybeziers ...")	
	# here result containt either list of list of atomic beziers or atomic lines: just concat and create bezier objects
	fresult = []
	fpoints = []
	for bezierlist in result:
		beziers = []
		for pointlist in bezierlist:
			fpoints.extend(pointlist)
			beziers.append(bezierfrompointlist([Point().coords(p) for p in pointlist]))
		if len(beziers) > 0:
			polybezier = PolyBezier()
			polybezier.adds(beziers)
			fresult.append(polybezier)
	return (fpoints,fresult)


class PolyBezier:
	def __init__(self):
		self.mbeziers = []
		self.mlength = 0

	def beziers(self):
		return self.mbeziers

	def add(self,newbezier):
		self.mbeziers.append(newbezier)
		self.recomputeranges()
		return self

	def adds(self,newbeziers):
		self.mbeziers.extend(newbeziers)
		self.recomputeranges()
		return self

	def recomputeranges(self):
		lengths = lsum([bezier.length() for bezier in self.mbeziers])
		# puts("lengths",lengths)
		sumlength = lengths[-1]
		lengths = [0.0] + [length/sumlength for length in lengths]
		ibezier = 0
		self.mranges = []
		for (r1,r2) in pairs(lengths):
			self.mranges.append((r1,r2,self.mbeziers[ibezier]))
			ibezier += 1
		# puts("ranges",self.mranges)
		self.mlength = sumlength

	def length(self):
		return self.mlength

	def viewbox(self):
		return bbunions([bezier.viewbox() for bezier in self.mbeziers])

	def bbox(self):
		return self.viewbox()

	def point(self,t):
		for (rmin,rmax,bezier) in self.mranges:
			if rmin <= t and t < rmax:
				tabs = abscissa((rmin,rmax),t)
				return bezier.point(tabs)
		if t >= 1.0:
			return self.mbeziers[-1].point(1.0)


	def points(self,error=0.01):
		return [point for bezier in self.mbeziers for point in bezier.polygon(error).points()]

	def polygon(self,error=0.01):
		return Polygon(self.points(error))
	
	def reverse(self):
		return PolyBezier().adds([bezier.reverse() for bezier in lreverse(self.mbeziers)])

	def symx(self,symx):
		return PolyBezier().adds([bezier.symx(symx) for bezier in self.mbeziers])
	
	def clockwise(self):
		if self.polygon().isClockwise():
			return self
		else:
			return self.reverse()

	# return an list of segments approximating the poybezier 
	def segments(self,maxsizeratio=0.001):
		maxsize = self.length() * maxsizeratio
		maxsize2 = maxsize * maxsize
		allpoints = self.points(10.0)
		result = []
		for (p1,p2) in pairs(allpoints):
			if dist(p1,p2) > 0.0001:
				# result.append((p1,p2))
				nsize = int(dist(p1,p2)/maxsize)
				if nsize < 2:
					result.append((p1,p2))
				else:
					newpoints = Segment(p1,p2).samples(nsize)
					result.extend(pairs(newpoints))
		return result
		


def roundpolygon(polygon,factor):
    # first compute new intermediate points
    newpoints = []    
    for (p1,p2) in pairs(polygon + [polygon[0]]):
	    # puts("p1",p1,"p2",p2)    
        if factor == 0.5:
            newpoints.append(Segment(p1,p2).sample(0.5))
        else:
            for cabs in [factor,1.0-factor]:
                newpoints.append(Segment(p1,p2).sample(cabs))
    
    # then build regular bezier from the new points
    return regularbezierfrompoints(newpoints)
    
