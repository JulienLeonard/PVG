
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

shader {
	name "Sphere0"
	type diffuse
	diff { "sRGB nonlinear" 1.0 0.0 0.0 }
}

object {
	shader "Sphere0"
	type sphere
	c 0.0 0.0 0.0
	r 1.0
}
				
