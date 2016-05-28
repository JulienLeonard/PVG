from utils import *
from Render3D import *
from sphere import *
from circle import *

sunflowtemplate = """
%photons {
%  caustics 10000000 kd 64 0.5
%}

%% common settings
image {
   resolution 1526 640
	aa 0 2
}

gi {
   type ambocc
   bright { "sRGB nonlinear" 1 1 1 } 
   dark { "sRGB nonlinear" 0 0 0 }
   samples 64 
   maxdist 3.0 
}

accel bih
filter mitchell
bucket 32 spiral

%% camera
camera {
   type pinhole
   eye    -1.35131 2.91408 -3.65447
   target 4.45034 -7.05377 9.91002
   up     0.455546 0.79908 0.392363
   fov    69.1469
   aspect 2.38437
}


%% common shaders
shader {
	name "floor"
	type amb-occ
	bright   1 1 1
	dark     0 0 0
	samples  4
	dist     6
}

%% scene background - comment out if not needed
background {
   color  { "sRGB nonlinear" 0 0 0 }
}


%% geometry
object {
   shader none
   transform col 0.001 0 0 0  0 0.001 0 0  0 0 0.001 0  0 0 0 1
   type generic-mesh
   name "Box"
   points 8
       1  1  1
       1  0  1
       0  0  1
       0  1  1
       0  1  0
       0  0  0
       1  0  0
       1  1  0

   triangles 12
      0 3 2
      0 2 1
      2 3 4
      2 4 5
      3 0 7
      3 7 4
      0 1 6
      0 6 7
      1 2 5
      1 5 6
      5 4 7
      5 7 6
   normals none
   uvs none
}
		
shader {
	name "shaderBox0"
	type amb-occ
	bright  { "sRGB nonlinear"   1 1 1 }
	dark     0 0 0
	samples  16
	dist     6
}

instance {
	name "Box0"
	geometry "Box"
	transform col 50 0 0 0 0 0.00999999 0 0 0 0 50 0 -24.5 -0.685 -24.5 1
	shader "shaderBox0"
}

%SPHERES%				
"""

spheretemplate = """shader {
	name "%NAME%"
	type diffuse
	diff { "sRGB nonlinear" %CR% %CG% %CB% }
}

object {
	shader "%NAME%"
	type sphere
	c %X% %Z% %Y%
	r %R%
}
"""



#
# dump everythin as a huge circles array for animation
#
class RenderSunflow(RenderCenter3D):
    def __init__(self,imagedim,backcolor=Color.white()):
        self.mdrawings  = []
        self.mimagedim  = imagedim
        self.mbackcolor = backcolor
        self.mmargin    = 1.0
        self.msunflownspheres = 0.0
        
    def margin(self, v = None):
        if v == None:
            return self.mmargin
        else:
            self.mmargin = v
            return self

    def initpicture(self,imagedim,backcolor):
        self.mimagedim = imagedim
        self.mcontent  = []

    def drawcirclepicture(self,circle,style):
        # puts("RenderJS drawcirclepicture style sizeratio",style.sizeratio())
        if style == None:
            style = Style()
        colorc = style.color()
        self.msunflownspheres += 1.0
        circle = circle.scale(style.sizeratio())
        if circle.r() > 0.0:
            # self.mcontent.append("[" + ",".join([f2d(circle.x()),f2d(circle.y()),f2d(circle.r() * style.sizeratio()),f2d(colorc.r()), f2d(colorc.g()),f2d(colorc.b()),f2d(colorc.a())]) + "]")
            self.mcontent.append(spheretemplate.replace("%NAME%","Sphere"+str(len(self.mcontent))).replace("%X%",str(circle.x())).replace("%Z%",str(0.0+self.msunflownspheres*0.0000)).replace("%Y%",str(circle.y())).replace("%R%",str(circle.r())).replace("%CR%",str(colorc.r())).replace("%CG%",str(colorc.g())).replace("%CB%",str(colorc.b())))

    def drawspherepicture(self,sphere,style):
        # puts("RenderJS drawcirclepicture style sizeratio",style.sizeratio())
        if style == None:
            style = Style()
        colorc = style.color()
        sphere = sphere.scale(style.sizeratio())
        self.msunflownspheres += 1.0
        if sphere.r() > 0.0:
            # self.mcontent.append("[" + ",".join([f2d(circle.x()),f2d(circle.y()),f2d(circle.r() * style.sizeratio()),f2d(colorc.r()), f2d(colorc.g()),f2d(colorc.b()),f2d(colorc.a())]) + "]")
            self.mcontent.append(spheretemplate.replace("%NAME%","Sphere"+str(len(self.mcontent))).replace("%X%",str(sphere.x())).replace("%Z%",str(sphere.z())).replace("%Y%",str(sphere.y())).replace("%R%",str(sphere.r())).replace("%CR%",str(colorc.r())).replace("%CG%",str(colorc.g())).replace("%CB%",str(colorc.b())))

        
    def end(self):
        mnspheres = 0
        puts("RenderSunflow end start")
        self.initpicture(self.mimagedim,self.mbackcolor)
        # self.setviewport(self.viewport())
        puts("RenderCenter(RenderSunflow start drawing")
        for drawing in self.mdrawings:
            shape = drawing.shape()
            if isinstance(shape,Polygon):
                self.drawpolygonpicture(shape,drawing.style())
            if isinstance(shape,Circle):
                self.drawcirclepicture(shape,drawing.style())
                mnspheres+=1
            if isinstance(shape,Sphere):
                self.drawspherepicture(shape,drawing.style())
                mnspheres+=1

        puts("N spheres to draw",mnspheres)
        self.endpicture()

    def endpicture(self):
        outputfilepath = self.outputfilepath().replace(".ppm",".sc")
        puts("RenderSunflow output",outputfilepath)
        filecontent = sunflowtemplate.replace("%SPHERES%","\n".join(self.mcontent))
        fput(outputfilepath,filecontent)
        fput(self.outputfilepath(),filecontent)

