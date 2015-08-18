import color
from geoutils import *
from circle import *
import socket
import sys
import subprocess
import time
import os

def gbbox(shape):
    return shape.viewbox()

class ImageDim:
    def __init__(self,width,height):
        self.mwidth  = width
        self.mheight = height
        
    def width(self):
        return self.mwidth

    def height(self):
        return self.mheight
    

class Render:
    def __init__(self,viewport,imagedim,filename,backcolor=color.white()):
        self.mimagedim  = imagedim
        self.mviewport  = viewport
        self.mfilename  = filename
        self.mbackcolor = backcolor

    def drawpolygon( self, polygon, colorc ):
        pointcoords = [coord for p in polygon.points() for coord in p.coords()]
        self.drawpolygonpicture(pointcoords,colorc)

    def drawpolygonpicture( self, pointcoords, colorc ):
        if len(pointcoords) < 2:
            print "error: pointcoords",pointcoords,"too small"
            return
        colorc = color.trimcolor(colorc)
        puts("Render drawpolygonpicture not defined")

    def initpicture(self):
        puts("Render initpicture not defined")

    def endpicture(self):
        puts("endpicture")

    def strokepolygon(self, polygon, width, colorc):
        self.drawpolygon(line(polygon.points(),width),colorc)

    def end(self):
        self.endpicture()

    def strokepolygons(self,polylines,width,color):
        for polygon in polygons:
            self.strokepolygon(polygon,width,color)
        
    def drawpolygons(self,polygons,color):
        for poly in polygons:
            self.drawpolygon(poly,color)

    def drawcircle(self,circle,color=color.black(),ratio=1.0):
        self.drawpolygon(circle.scale(ratio).polygon(30),color)

    def drawcircles(self,circles,color=color.black(),ratio = 1.0):
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
    def initpicture(self,imagedim,filename,backcolor):
        puts("filename",filename)
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
        
        if fileexists(filename):
            os.remove(filename)
        self.sock.sendall("drawinit " + str(imagedim.width()) + " " + str(imagedim.height()) + " " + filename + " {" + ' '.join([str(i) for i in backcolor]) +"} \n")

    def setviewport(self,viewport):
        self.sock.sendall("focus " + str(viewport.center().x()) + " " + str(viewport.center().y()) + " " + str(viewport.radius()) + " \n")

    def selfinit(self):
        self.openacceptsocket()
        self.initpicture(self.mimagedim,self.mfilename,self.mbackcolor)
        self.setviewport(self.mviewport)

    def openacceptsocket(self):
        host = ''
        port = 45000
        self.s = socket.socket()
        self.s.bind((host, port))
        self.s.listen(1)
        puts("Listening on port ", port)

    def endpicture(self):
        self.sock.sendall("end\n")
        while not fileexists(self.mfilename):
            time.sleep(1)
        self.sock.close()
        self.p.terminate()

    def drawpolygonpicture(self,pointcoords,colorc):
        self.sock.sendall("drawpolygon {" + ' '.join([str(coord) for coord in pointcoords]) + "} {" + ' '.join([str(i) for i in colorc]) + "} \n")

            
class RenderTCLSVG(Render):
    def initpicture(self,imagedim,filename,backcolor):
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
        
        if fileexists(filename):
            os.remove(filename)
        self.sock.sendall("drawinit " + str(imagedim.width()) + " " + str(imagedim.height()) + " " + filename + " {" + ' '.join([str(i) for i in backcolor]) +"} \n")

    def getsock(self):
        return self.sock

    def setviewport(self,viewport):
        self.sock.sendall("focus " + str(viewport.center().x()) + " " + str(viewport.center().y()) + " " + str(viewport.radius()) + " \n")

    def selfinit(self):
        self.openacceptsocket()
        self.initpicture(self.mimagedim,self.mfilename,self.mbackcolor)
        self.setviewport(self.mviewport)

    def openacceptsocket(self):
        host = ''
        port = 45000
        self.s = socket.socket()
        self.s.bind((host, port))
        self.s.listen(1)
        puts("Listening on port ", port)

    def endpicture(self):
        self.sock.sendall("end\n")
        # while not fileexists(self.mfilename):
        time.sleep(10)
        self.sock.close()
        self.p.terminate()

    def drawpolygonpicture(self,pointcoords,colorc):
        self.sock.sendall("drawpolygon {" + ' '.join([str(coord) for coord in pointcoords]) + "} {" + ' '.join([str(i) for i in colorc]) + "} \n")

    def drawcirclepicture(self,circle,colorc=color.black(),ratio=1.0):
        coords = [circle.x(),circle.y(),circle.r() * ratio]
        self.sock.sendall("drawcircle {" + ' '.join([str(coord) for coord in coords]) + "} {" + ' '.join([str(i) for i in colorc]) + "} \n")


class RenderCenter(RenderTCL):
    def __init__(self,imagedim,filename,backcolor=color.white()):
        self.mitems     = []
        self.mimagedim  = imagedim
        self.mfilename  = filename
        self.mbackcolor = backcolor

    def drawpolygon( self, polygon, colorc ):
        if not polygon == None:
            self.mitems.append((polygon,colorc))

    def end(self):
        self.openacceptsocket()
        self.initpicture(self.mimagedim,self.mfilename,self.mbackcolor)
        for item in self.mitems:
            polygon,color = item
            self.drawpolygonpicture(polygon.coords(),color)
        self.endpicture()

    def viewport(self):
        return polygons2bbox([item[0] for item in self.mitems]).resize(1.25).viewport()

class RenderViewport(RenderCenter):
    def __init__(self,viewport,imagedim,filename,backcolor=color.white()):
        self.mitems    = []
        self.mviewport = viewport
        self.mimagedim = imagedim
        self.filename  = filename
        self.backcolor = backcolor

    def viewport(self):
        return self.mviewport

    def end(self):
        self.openacceptsocket()
        self.initpicture(self.mimagedim,self.mfilename,self.mbackcolor)
        self.setviewport(self.viewport())
        for item in self.mitems:
            polygon,color = item
            self.drawpolygonpicture(polygon.coords(),color)
        self.endpicture()


class RenderCenterSVG(RenderTCLSVG):
    def __init__(self,imagesize,filename,backcolor=color.white()):
        self.mitems     = []
        self.width,self.height = imagesize
        self.filename = filename
        self.backcolor = backcolor

    def drawpolygon( self, polygon, colorc = color.black()):
        if not polygon == None:
            self.mitems.append((polygon,colorc,"polygon"))

    def drawcircle( self, circle, colorc = color.black()):
        if not circle == None:
            self.mitems.append((circle,colorc,"circle"))

    def end(self):
        xc,yc,size = self.viewport()
        self.openacceptsocket()
        self.initpicture(self.mimagedim,self.mfilename,self.mbackcolor)
        self.setviewport(self.viewport())
        self.drawpolygonpicture(square(Point(xc,yc),size).coords(),self.backcolor)
        for item in self.mitems:
            polygon,color,itype = item
            if itype == "polygon":
                self.drawpolygonpicture(polygon.coords(),color)
            else:
                self.drawcirclepicture(polygon.coords(),color)
        self.endpicture()

    def viewport(self):
        return polygons2bbox([item[0] for item in self.mitems]).resize(1.25).viewport()


class RenderCenterMulti(RenderCenter):
    def __init__(self,imagedim,nsubs,filename,backcolor=color.white()):
        self.mitems     = []
        self.mimagedim  = imagedim
        self.mfilename  = filename
        self.mbackcolor = backcolor
        self.mnsubs     = nsubs

    def end(self):
        viewport = self.viewport()
        axmin = viewport.xmin()
        aymin = viewport.ymin()
        size = viewport.size() / self.nsubs
        realfilename = self.mfilename
        self.openacceptsocket()
        filelists = []
        
        # TODO : refactor by adding split method on viewport and imagedim
        for i in range(self.nsubs):
            filelist = []
            for j in range(self.nsubs):
                xc = axmin + size * (float(j) + 0.5)
                yc = aymin + size * (float(i) + 0.5)
                self.mfilename = realfilename + "." + str(i) + str(j) + ".ppm"
                filelist.append(self.mfilename)
                self.initpicture(ImageDim(self.mimagedim.width()/self.nsubs,self.mimagedim.height()/self.nsubs),self.mfilename,self.mbackcolor)
                self.setviewport(Viewport(Point(xc,yc),size/2.0))
                for item in self.mitems:
                    polygon,color = item
                    self.drawpolygonpicture(polygon.coords(),color)
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

