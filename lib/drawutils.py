import color
from geoutils import *
from circle import *
import socket
import sys
import subprocess
import time
import os

def gbbox(polygon,itype):
    if itype == "polygon":
        return bbox(polygon)
    else:
        return circleviewbox(polygon)


class Render:
    def __init__(self,viewport,imagesize,filename,backcolor=color.white()):
        self.width,self.height = imagesize
        self.xc,self.yc,self.size = viewport
        self.xmin = self.xc - self.size/2.0
        self.ymin = self.yc - self.size/2.0
        self.filename = filename
        self.backcolor = backcolor

    def drawpolygon( self, polygon, colorc ):
        pointcoords = [[p.x(),p.y()] for p in polygon]
        self.drawpolygonpicture(pointcoords,colorc)

    def drawpolygonpicture( self, polygon, colorc ):
        if len(polygon) < 2:
            print "error: polygon",polygon,"too small"
            return
        colorc = color.trimcolor(colorc)
        puts("Render drawpolygonpicture not defined")

    def initpicture(self):
        puts("Render initpicture not defined")

    def endpicture(self):
        puts("endpicture")

    def drawpolyline(self, polyline, width, colorc):
        self.drawpolygon(line(polyline.points(),width),colorc)

    def end(self):
        self.endpicture()

    def drawpolylines(self,polylines,width,color):
        for polyline in polylines:
            self.drawpolyline(polyline,width,color)
        
    def drawpolygons(self,polygons,color):
        for poly in polygons:
            self.drawpolygon(poly,color)

    def drawcircle(self,circle,color=color.white(),ratio=1.0):
        self.drawpolygon(circlepolygon(cscale(circle,ratio),30),color)

    def drawcircles(self,circles,color=color.white(),ratio = 1.0):
        for circle in circles:
            self.drawcircle(circle,color,ratio)

    def drawcirclescolors(self,circles,colors):
        for i in range(len(circles)):
            self.drawcircle(circles[i],circular(colors,i))

# class RenderAGG:
#     def __init__(self,viewport,imagesize,filename,backcolor=color.white()):
#         from AGGPROXY import *
#         self.AGGrender = AGGRender()
#         self.initpicture()

#     def drawpolygonpicture( self, polygon, colorc ):
#         self.AGGrender.polygonfill(lflatten(polygon),colorc[0],colorc[1],colorc[2],colorc[3],1)

#     def initpicture(self):
#         self.AGGrender = AGGRender()
#         self.AGGrender.initrender(self.width,self.height,self.mfilename,self.mbackcolor[0],self.mbackcolor[1],self.mbackcolor[2],self.mbackcolor[3])
#         self.AGGrender.initviewport(self.xmin,self.ymin,self.size,self.size)

#     def endpicture(self):
#         self.AGGrender.end()

class RenderTCL(Render):
    def initpicture(self,width,height,filename,backcolor):
        self.p = subprocess.Popen("tclsh C:/DEV/CVG/scripts/drawclient.tcl")
        puts("after call")
        while 1:
            try:
                self.sock, addr = self.s.accept()
                puts("Connection from", self.sock.getpeername())
                break
            except socket.error, ex:
                puts(ex)
                pass
            except KeyboardInterrupt:
                self.sock.close()
                break
        
        if fileexists(self.filename):
            os.remove(self.filename)
        self.sock.sendall("drawinit " + str(width) + " " + str(height) + " " + filename + " {" + ' '.join([str(i) for i in backcolor]) +"} \n")

    def setviewport(self,xc,yc,radius):
        self.sock.sendall("focus " + str(xc) + " " + str(yc) + " " + str(radius) + " \n")

    def selfinit(self):
        self.openacceptsocket()
        self.initpicture(self.width,self.height,self.filename,self.backcolor)
        self.setviewport(self.xc,self.yc,self.size)

    def openacceptsocket(self):
        host = ''
        port = 45000
        self.s = socket.socket()
        self.s.bind((host, port))
        self.s.listen(1)
        puts("Listening on port ", port)

    def endpicture(self):
        self.sock.sendall("end\n")
        while not fileexists(self.filename):
            time.sleep(1)
        self.sock.close()
        self.p.terminate()

    def drawpolygonpicture(self,polygon,colorc):
        self.sock.sendall("drawpolygon {" + ' '.join([str(i) for i in lflatten(polygon)]) + "} {" + ' '.join([str(i) for i in colorc]) + "} \n")

            
class RenderTCLSVG(Render):
    def initpicture(self,width,height,filename,backcolor):
        self.p = subprocess.Popen("tclsh C:/DEV/CVG/scripts/drawclientsvg.tcl")
        puts("after call")
        while 1:
            try:
                self.sock, addr = self.s.accept()
                puts("Connection from", self.sock.getpeername())
                break
            except socket.error, ex:
                puts(ex)
                pass
            except KeyboardInterrupt:
                self.sock.close()
                break
        
        if fileexists(self.filename):
            os.remove(self.filename)
        self.sock.sendall("drawinit " + str(width) + " " + str(height) + " " + filename + " {" + ' '.join([str(i) for i in backcolor]) +"} \n")

    def getsock(self):
        return self.sock

    def setviewport(self,xc,yc,radius):
        self.sock.sendall("focus " + str(xc) + " " + str(yc) + " " + str(radius) + " \n")

    def selfinit(self):
        self.openacceptsocket()
        self.initpicture(self.width,self.height,self.filename,self.backcolor)
        self.setviewport(self.xc,self.yc,self.size)

    def openacceptsocket(self):
        host = ''
        port = 45000
        self.s = socket.socket()
        self.s.bind((host, port))
        self.s.listen(1)
        puts("Listening on port ", port)

    def endpicture(self):
        self.sock.sendall("end\n")
        # while not fileexists(self.filename):
        time.sleep(10)
        self.sock.close()
        self.p.terminate()

    def drawpolygonpicture(self,polygon,colorc):
        self.sock.sendall("drawpolygon {" + ' '.join([str(i) for i in lflatten(polygon)]) + "} {" + ' '.join([str(i) for i in colorc]) + "} \n")

    def drawcirclepicture(self,circle,colorc=color.white(),ratio=1.0):
        newc = (circle.x(),circle.y(),circle.r() * ratio)
        self.sock.sendall("drawcircle {" + ' '.join([str(i) for i in newc]) + "} {" + ' '.join([str(i) for i in colorc]) + "} \n")


class RenderCenter(RenderTCL):
    def __init__(self,imagesize,filename,backcolor=color.white()):
        self.mitems     = []
        self.width,self.height = imagesize
        self.filename = filename
        self.backcolor = backcolor

    def drawpolygon( self, polygon, colorc ):
        if len(polygon) > 0:
            self.mitems.append((polygon,colorc))

    def end(self):
        xc,yc,size = self.viewport()
        self.openacceptsocket()
        self.initpicture(self.width,self.height,self.filename,self.backcolor)
        # self.setviewport(self,xc,yc,size)
        for item in self.mitems:
            polygon,color = item
            self.drawpolygonpicture(polygon,color)
        self.endpicture()

    def viewport(self):
        result = bbox(self.mitems[0][0])
        for item in self.mitems[1:]:
            result = bbunion(result,bbox(item[0]))
        result = bboxresize(result,1.25)
        xmin,ymin,xmax,ymax = result
        xcenter = lmean([xmin,xmax])
        ycenter = lmean([ymin,ymax])
        size    = lmax([xmax-xmin,ymax-ymin])
        return (xcenter,ycenter,size)

class RenderViewport(RenderCenter):
    def __init__(self,viewport_,imagesize,filename,backcolor=color.white()):
        self.mitems     = []
        self.mviewport = viewport_
        self.width,self.height = imagesize
        self.filename = filename
        self.backcolor = backcolor

    def viewport(self):
        return self.mviewport

    def end(self):
        xc,yc,size = self.viewport()
        self.openacceptsocket()
        self.initpicture(self.width,self.height,self.filename,self.backcolor)
        self.setviewport(xc,yc,size)
        for item in self.mitems:
            polygon,color = item
            self.drawpolygonpicture(polygon,color)
        self.endpicture()


class RenderCenterSVG(RenderTCLSVG):
    def __init__(self,imagesize,filename,backcolor=color.white()):
        self.mitems     = []
        self.width,self.height = imagesize
        self.filename = filename
        self.backcolor = backcolor

    def drawpolygon( self, polygon, colorc ):
        if len(polygon) > 0:
            self.mitems.append((polygon,colorc,"polygon"))

    def drawcircle( self, circle, colorc ):
        if not circle == None:
            self.mitems.append((circle,colorc,"circle"))


    def end(self):
        xc,yc,size = self.viewport()
        self.openacceptsocket()
        self.initpicture(self.width,self.height,self.filename,self.backcolor)
        self.setviewport(xc,yc,size*2.0)
        self.drawpolygonpicture(square((xc,yc),size),self.backcolor)
        for item in self.mitems:
            polygon,color,itype = item
            if itype == "polygon":
                self.drawpolygonpicture(polygon,color)
            else:
                self.drawcirclepicture(polygon,color)
        self.endpicture()

    def viewport(self):
        result = gbbox(self.mitems[0][0],self.mitems[0][2])
        for item in self.mitems[1:]:
            result = bbunion(result,gbbox(item[0],item[2]))
        result = bboxresize(result,1.25)
        xmin,ymin,xmax,ymax = result
        xcenter = lmean([xmin,xmax])
        ycenter = lmean([ymin,ymax])
        size    = lmax([xmax-xmin,ymax-ymin])
        return (xcenter,ycenter,size)


class RenderCenterMulti(RenderCenter):
    def __init__(self,imagesize,nsubs,filename,backcolor=color.white()):
        self.mitems     = []
        self.width,self.height = imagesize
        self.filename = filename
        self.backcolor = backcolor
        self.nsubs = nsubs

    def end(self):
        axc,ayc,asize = self.viewport()
        axmin = axc - asize/2.0
        aymin = ayc - asize/2.0
        size = asize / self.nsubs
        realfilename = self.filename
        self.openacceptsocket()
        filelists = []
        for i in range(self.nsubs):
            filelist = []
            for j in range(self.nsubs):
                xc = axmin + size * (float(j) + 0.5)
                yc = aymin + size * (float(i) + 0.5)
                self.filename = realfilename + "." + str(i) + str(j) + ".ppm"
                filelist.append(self.filename)
                self.initpicture(self.width/self.nsubs,self.height/self.nsubs,self.filename,self.backcolor)
                self.setviewport(xc,yc,size/2.0)
                for item in self.mitems:
                    polygon,color = item
                    self.drawpolygonpicture(polygon,color)
                self.endpicture()
            filelists.append(filelist)
        # now create real image with rconvert
        columnfiles = []    
        for (i,filelist) in enumerate(filelists):
            for filename in filelist:
                # output = "d:/dev/cvg/output/tmp" + filename + ".png"
                output = filename + ".png"
                columnfiles.append(output)
                #cmd = "rconvert -append " + " ".join(filelist) + " " + output
                cmd = "rconvert " + filename + " " + output
                self.p = subprocess.call(cmd)
        # cmd = "rconvert +append " + " ".join(columnfiles) + " " + realfilename + ".png"
        cmd = "montage  -limit memory 1280000000 -limit map 1280000000 " + " ".join(columnfiles) + " -tile 10x10 -geometry +0+0" + " " + realfilename + ".png"
        self.p = subprocess.call(cmd)

