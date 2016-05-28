
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
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere0"
	type sphere
	c 0.0 -0.1 0.5
	r 0.075
}

shader {
	name "Sphere1"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1"
	type sphere
	c 0.0 0.1 0.5
	r 0.075
}

shader {
	name "Sphere2"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2"
	type sphere
	c 0.17480526623 1.38777878078e-17 0.5
	r 0.0760405429667
}

shader {
	name "Sphere3"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere3"
	type sphere
	c -0.00475302336178 0.108194098356 0.5
	r 0.0811862598772
}

shader {
	name "Sphere4"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere4"
	type sphere
	c 0.169838162188 -0.196823603436 0.5
	r 0.071624158919
}

shader {
	name "Sphere5"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere5"
	type sphere
	c 0.00117349865131 -0.0979766855808 0.5
	r 0.073485122612
}

shader {
	name "Sphere6"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere6"
	type sphere
	c -0.177040220765 -0.0079592150772 0.5
	r 0.0746522453726
}

shader {
	name "Sphere7"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere7"
	type sphere
	c 0.181007220075 0.200451766771 0.5
	r 0.0743702227924
}

shader {
	name "Sphere8"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere8"
	type sphere
	c 0.342129896071 -0.108576596262 0.5
	r 0.0735584378674
}

shader {
	name "Sphere9"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere9"
	type sphere
	c 0.00377070356817 -0.299946166657 0.5
	r 0.0749862889354
}

shader {
	name "Sphere10"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere10"
	type sphere
	c -0.164612381693 -0.199375408627 0.5
	r 0.0692121641057
}

shader {
	name "Sphere11"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere11"
	type sphere
	c -0.198129982383 0.193643558937 0.5
	r 0.0773749127315
}

shader {
	name "Sphere12"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere12"
	type sphere
	c 0.0201830563157 0.310787769369 0.5
	r 0.0719056309187
}

shader {
	name "Sphere13"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere13"
	type sphere
	c 0.356338386666 0.0969795093226 0.5
	r 0.0783197683575
}

shader {
	name "Sphere14"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere14"
	type sphere
	c 0.331353162029 -0.305577644949 0.5
	r 0.0744132571924
}

shader {
	name "Sphere15"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere15"
	type sphere
	c -0.323534310294 -0.120443415083 0.5
	r 0.0638709750768
}

shader {
	name "Sphere16"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere16"
	type sphere
	c -0.36795925369 0.0702255155531 0.5
	r 0.0800786426094
}

shader {
	name "Sphere17"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere17"
	type sphere
	c 0.190191710357 0.391873138291 0.5
	r 0.0693609644605
}

shader {
	name "Sphere18"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere18"
	type sphere
	c 0.508896371276 -0.215345735575 0.5
	r 0.0749542630325
}

shader {
	name "Sphere19"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere19"
	type sphere
	c -0.319533242276 -0.295702579717 0.5
	r 0.0676076472353
}

shader {
	name "Sphere20"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere20"
	type sphere
	c -0.386469587719 0.280361432421 0.5
	r 0.0781335614504
}

shader {
	name "Sphere21"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere21"
	type sphere
	c 0.0369526860749 0.502371781998 0.5
	r 0.0723317795794
}

shader {
	name "Sphere22"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere22"
	type sphere
	c 0.34468811503 0.29500835716 0.5
	r 0.0674023630258
}

shader {
	name "Sphere23"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere23"
	type sphere
	c 0.500492290427 -0.420231832206 0.5
	r 0.0788395255506
}

shader {
	name "Sphere24"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere24"
	type sphere
	c -0.473892447075 -0.206554741727 0.5
	r 0.066082037791
}

shader {
	name "Sphere25"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere25"
	type sphere
	c -0.562896481914 0.161578152057 0.5
	r 0.0813819648721
}

shader {
	name "Sphere26"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere26"
	type sphere
	c -0.216707226884 0.398770979558 0.5
	r 0.0771002783055
}

shader {
	name "Sphere27"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere27"
	type sphere
	c 0.20851832495 0.572223929647 0.5
	r 0.0665986928616
}

shader {
	name "Sphere28"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere28"
	type sphere
	c 0.686763959306 -0.319973897225 0.5
	r 0.0798147947069
}

shader {
	name "Sphere29"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere29"
	type sphere
	c 0.316115833844 -0.499953134056 0.5
	r 0.0718156007718
}

shader {
	name "Sphere30"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere30"
	type sphere
	c -0.473156418617 -0.379520552046 0.5
	r 0.0636434944627
}

shader {
	name "Sphere31"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere31"
	type sphere
	c -0.569597108972 0.369448712412 0.5
	r 0.0746019314099
}

shader {
	name "Sphere32"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere32"
	type sphere
	c 0.068989738247 0.689681422329 0.5
	r 0.0701904701433
}

shader {
	name "Sphere33"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere33"
	type sphere
	c 0.680836288443 -0.113986097393 0.5
	r 0.074740009217
}

shader {
	name "Sphere34"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere34"
	type sphere
	c 0.682654035368 -0.538330463356 0.5
	r 0.0839816363104
}

shader {
	name "Sphere35"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere35"
	type sphere
	c 0.468979213084 -0.624103842963 0.5
	r 0.0758803498139
}

shader {
	name "Sphere36"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere36"
	type sphere
	c -0.33257383419 -0.465035300572 0.5
	r 0.0597679407188
}

shader {
	name "Sphere37"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere37"
	type sphere
	c -0.627616106752 -0.297015688123 0.5
	r 0.0676918659859
}

shader {
	name "Sphere38"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere38"
	type sphere
	c -0.744667607747 0.268742072782 0.5
	r 0.0768748740059
}

shader {
	name "Sphere39"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere39"
	type sphere
	c -0.40629130459 0.483016063233 0.5
	r 0.074582719329
}

shader {
	name "Sphere40"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere40"
	type sphere
	c -0.116995223629 0.628105289269 0.5
	r 0.0767445145991
}

shader {
	name "Sphere41"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere41"
	type sphere
	c 0.241322355136 0.745506049588 0.5
	r 0.06567119633
}

shader {
	name "Sphere42"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere42"
	type sphere
	c 0.85848329033 -0.205281123718 0.5
	r 0.0750596803692
}

shader {
	name "Sphere43"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere43"
	type sphere
	c 0.871859349395 -0.42716187792 0.5
	r 0.0806038177849
}

shader {
	name "Sphere44"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere44"
	type sphere
	c 0.284346605145 -0.686858838489 0.5
	r 0.0703742450713
}

shader {
	name "Sphere45"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere45"
	type sphere
	c -0.182805596464 -0.401759816767 0.5
	r 0.0621718002756
}

shader {
	name "Sphere46"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere46"
	type sphere
	c -0.473346547162 -0.548181957795 0.5
	r 0.0628526402219
}

shader {
	name "Sphere47"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere47"
	type sphere
	c -0.627928848696 -0.116378936358 0.5
	r 0.067785900885
}

shader {
	name "Sphere48"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere48"
	type sphere
	c -0.750534344419 0.0627725277714 0.5
	r 0.0776649365281
}

shader {
	name "Sphere49"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere49"
	type sphere
	c -0.744709901683 0.477581043057 0.5
	r 0.0797543569128
}

shader {
	name "Sphere50"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere50"
	type sphere
	c -0.0674974892572 0.817414529305 0.5
	r 0.0700104100708
}

shader {
	name "Sphere51"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere51"
	type sphere
	c 0.379250023165 0.630932917879 0.5
	r 0.068809145416
}

shader {
	name "Sphere52"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere52"
	type sphere
	c 0.853028544873 0.00356437983486 0.5
	r 0.081627864489
}

shader {
	name "Sphere53"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere53"
	type sphere
	c 0.878063662753 -0.645380873541 0.5
	r 0.0831265650067
}

shader {
	name "Sphere54"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere54"
	type sphere
	c 0.420722299589 -0.806783986948 0.5
	r 0.0658294951066
}

shader {
	name "Sphere55"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere55"
	type sphere
	c 0.129421639509 -0.566400403903 0.5
	r 0.0768092745055
}

shader {
	name "Sphere56"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere56"
	type sphere
	c -0.207685549874 -0.559775112786 0.5
	r 0.057799710072
}

shader {
	name "Sphere57"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere57"
	type sphere
	c -0.787410674163 -0.207101008661 0.5
	r 0.0698241740356
}

shader {
	name "Sphere58"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere58"
	type sphere
	c -0.918288180521 0.171639178223 0.5
	r 0.0723224950219
}

shader {
	name "Sphere59"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere59"
	type sphere
	c -0.24043375123 0.770220834869 0.5
	r 0.0644346901324
}

shader {
	name "Sphere60"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere60"
	type sphere
	c 0.405007360319 0.808732778224 0.5
	r 0.0659327552688
}

shader {
	name "Sphere61"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere61"
	type sphere
	c 0.654685368801 0.0925863975403 0.5
	r 0.0814258874178
}

shader {
	name "Sphere62"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere62"
	type sphere
	c 1.03184760481 -0.104844334038 0.5
	r 0.0752077080377
}

shader {
	name "Sphere63"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere63"
	type sphere
	c 1.06094405679 -0.527657014154 0.5
	r 0.0799948066615
}

shader {
	name "Sphere64"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere64"
	type sphere
	c 0.686406357742 -0.765772916278 0.5
	r 0.0866234163382
}

shader {
	name "Sphere65"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere65"
	type sphere
	c 0.250887688759 -0.871752502551 0.5
	r 0.0705482723952
}

shader {
	name "Sphere66"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere66"
	type sphere
	c -0.0569892852467 -0.508516092791 0.5
	r 0.0615819420288
}

shader {
	name "Sphere67"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere67"
	type sphere
	c -0.778636893753 -0.384013463383 0.5
	r 0.0630232390756
}

shader {
	name "Sphere68"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere68"
	type sphere
	c -0.93795228675 -0.0289227325885 0.5
	r 0.0788201971349
}

shader {
	name "Sphere69"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere69"
	type sphere
	c -0.19922673849 0.932683923415 0.5
	r 0.0612709325911
}

shader {
	name "Sphere70"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere70"
	type sphere
	c 0.270232938837 0.913212979337 0.5
	r 0.0619642526115
}

shader {
	name "Sphere71"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere71"
	type sphere
	c 0.552887452315 0.700537966394 0.5
	r 0.0714926222638
}

shader {
	name "Sphere72"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere72"
	type sphere
	c 0.827712038654 0.213264839391 0.5
	r 0.0767894787117
}

shader {
	name "Sphere73"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere73"
	type sphere
	c 1.04418943619 0.100607660619 0.5
	r 0.0791590602028
}

shader {
	name "Sphere74"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere74"
	type sphere
	c 1.07700734999 -0.745693515399 0.5
	r 0.0839757523142
}

shader {
	name "Sphere75"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere75"
	type sphere
	c 0.883999335228 -0.859205586014 0.5
	r 0.0773037467428
}

shader {
	name "Sphere76"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere76"
	type sphere
	c 0.398124684365 -0.98452270091 0.5
	r 0.0685476150839
}

shader {
	name "Sphere77"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere77"
	type sphere
	c -0.0953028894094 -0.657952671129 0.5
	r 0.0541205344153
}

shader {
	name "Sphere78"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere78"
	type sphere
	c -0.634159564381 -0.472583545157 0.5
	r 0.0640754486617
}

shader {
	name "Sphere79"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere79"
	type sphere
	c -0.934879397262 -0.312135982166 0.5
	r 0.0659638799227
}

shader {
	name "Sphere80"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere80"
	type sphere
	c -1.10373814654 0.0973927924325 0.5
	r 0.0774978017725
}

shader {
	name "Sphere81"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere81"
	type sphere
	c -0.362863138145 0.892163034197 0.5
	r 0.0651631717365
}

shader {
	name "Sphere82"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere82"
	type sphere
	c -0.0477356389899 0.989860453075 0.5
	r 0.0601705087877
}

shader {
	name "Sphere83"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere83"
	type sphere
	c 0.116452732044 0.85826302466 0.5
	r 0.060512950799
}

shader {
	name "Sphere84"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere84"
	type sphere
	c 0.425462171782 0.983039075723 0.5
	r 0.0656940281804
}

shader {
	name "Sphere85"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere85"
	type sphere
	c 0.523787815151 0.512036340014 0.5
	r 0.0715582577319
}

shader {
	name "Sphere86"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere86"
	type sphere
	c 0.648313392489 0.296389781148 0.5
	r 0.0715013402241
}

shader {
	name "Sphere87"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere87"
	type sphere
	c 1.21201799386 -0.0177697558879 0.5
	r 0.0748735535443
}

shader {
	name "Sphere88"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere88"
	type sphere
	c 1.26302405273 -0.616936423709 0.5
	r 0.0856977247756
}

shader {
	name "Sphere89"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere89"
	type sphere
	c 0.716108422512 -0.987542996834 0.5
	r 0.0811892827366
}

shader {
	name "Sphere90"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere90"
	type sphere
	c 0.234198807106 -1.05025559739 0.5
	r 0.0639128889907
}

shader {
	name "Sphere91"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere91"
	type sphere
	c -0.228479747198 -0.704154262084 0.5
	r 0.0516019685452
}

shader {
	name "Sphere92"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere92"
	type sphere
	c -0.785192257296 -0.554121322939 0.5
	r 0.0646523532628
}

shader {
	name "Sphere93"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere93"
	type sphere
	c -1.12594712725 -0.100910847672 0.5
	r 0.0721597557808
}

shader {
	name "Sphere94"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere94"
	type sphere
	c -1.06549250147 0.288373939503 0.5
	r 0.0685819605005
}

shader {
	name "Sphere95"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere95"
	type sphere
	c -0.412134831726 0.718832666457 0.5
	r 0.0699849057386
}

shader {
	name "Sphere96"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere96"
	type sphere
	c -0.310000716581 1.05038957511 0.5
	r 0.0599544391263
}

shader {
	name "Sphere97"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere97"
	type sphere
	c 0.142591086751 1.02189970993 0.5
	r 0.0637703961257
}

shader {
	name "Sphere98"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere98"
	type sphere
	c 0.70683263466 0.580366695164 0.5
	r 0.0749788515729
}

shader {
	name "Sphere99"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere99"
	type sphere
	c 0.798734047251 0.401751611507 0.5
	r 0.0662364990941
}

shader {
	name "Sphere100"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere100"
	type sphere
	c 1.22972126496 0.175958342917 0.5
	r 0.0710279197751
}

shader {
	name "Sphere101"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere101"
	type sphere
	c 1.20079639515 -0.223432645623 0.5
	r 0.0796030499485
}

shader {
	name "Sphere102"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere102"
	type sphere
	c 1.27890876235 -0.842648220455 0.5
	r 0.0840048187957
}

shader {
	name "Sphere103"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere103"
	type sphere
	c 0.9167186501 -1.06738362031 0.5
	r 0.0807464485606
}

shader {
	name "Sphere104"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere104"
	type sphere
	c 0.363551163826 -1.15129070283 0.5
	r 0.059187964602
}

shader {
	name "Sphere105"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere105"
	type sphere
	c 0.0994655690226 -0.955996230571 0.5
	r 0.0594110906058
}

shader {
	name "Sphere106"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere106"
	type sphere
	c -0.126413373782 -0.793290561536 0.5
	r 0.0500301561006
}

shader {
	name "Sphere107"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere107"
	type sphere
	c -0.336803173501 -0.622854399914 0.5
	r 0.0499770310296
}

shader {
	name "Sphere108"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere108"
	type sphere
	c -0.636557194351 -0.647139968783 0.5
	r 0.0668542182703
}

shader {
	name "Sphere109"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere109"
	type sphere
	c -1.28172648589 0.00994113179124 0.5
	r 0.0712361841362
}

shader {
	name "Sphere110"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere110"
	type sphere
	c -1.23908964212 0.235484270702 0.5
	r 0.0675245140824
}

shader {
	name "Sphere111"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere111"
	type sphere
	c -0.530899988999 0.852782420449 0.5
	r 0.064279128116
}

shader {
	name "Sphere112"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere112"
	type sphere
	c -0.464831215576 1.02124135415 0.5
	r 0.0582082981895
}

shader {
	name "Sphere113"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere113"
	type sphere
	c 0.728260302055 0.773951625588 0.5
	r 0.0710965638709
}

shader {
	name "Sphere114"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere114"
	type sphere
	c 0.973153992589 0.346284305908 0.5
	r 0.0710338668588
}

shader {
	name "Sphere115"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere115"
	type sphere
	c 1.39282296588 0.068616619218 0.5
	r 0.0754131294616
}

shader {
	name "Sphere116"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere116"
	type sphere
	c 1.47630783687 -0.717688841404 0.5
	r 0.0912148949365
}

shader {
	name "Sphere117"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere117"
	type sphere
	c 0.747139811942 -1.20313138047 0.5
	r 0.0821683931978
}

shader {
	name "Sphere118"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere118"
	type sphere
	c 0.523747267554 -1.11037350009 0.5
	r 0.0648163403049
}

shader {
	name "Sphere119"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere119"
	type sphere
	c 0.217067504149 -1.21568264821 0.5
	r 0.0608209065924
}

shader {
	name "Sphere120"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere120"
	type sphere
	c 0.0792648423138 -1.11772376984 0.5
	r 0.0628270982013
}

shader {
	name "Sphere121"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere121"
	type sphere
	c 0.0931345830767 -0.795951413553 0.5
	r 0.0607163998825
}

shader {
	name "Sphere122"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere122"
	type sphere
	c -0.249371930296 -0.834152308983 0.5
	r 0.0471476452544
}

shader {
	name "Sphere123"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere123"
	type sphere
	c -0.790952389302 -0.723201366852 0.5
	r 0.0622312457888
}

shader {
	name "Sphere124"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere124"
	type sphere
	c -1.3060442024 -0.186905865392 0.5
	r 0.077521341876
}

shader {
	name "Sphere125"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere125"
	type sphere
	c -1.20146712774 0.418341738832 0.5
	r 0.0724912808197
}

shader {
	name "Sphere126"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere126"
	type sphere
	c -0.596396010948 0.685504153436 0.5
	r 0.0704534142494
}

shader {
	name "Sphere127"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere127"
	type sphere
	c -0.413678986888 1.1631765686 0.5
	r 0.0549451928081
}

shader {
	name "Sphere128"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere128"
	type sphere
	c 0.874567031495 0.664730046712 0.5
	r 0.0658375241384
}

shader {
	name "Sphere129"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere129"
	type sphere
	c 1.40170636693 0.270549685363 0.5
	r 0.0761831481457
}

shader {
	name "Sphere130"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere130"
	type sphere
	c 1.44797417029 -0.484671116861 0.5
	r 0.0848356144197
}

shader {
	name "Sphere131"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere131"
	type sphere
	c 1.48061352246 -0.961258009153 0.5
	r 0.0914905212493
}

shader {
	name "Sphere132"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere132"
	type sphere
	c 0.95638042512 -1.28758624451 0.5
	r 0.0870630172244
}

shader {
	name "Sphere133"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere133"
	type sphere
	c 0.47119778087 -1.26857400537 0.5
	r 0.0602085661661
}

shader {
	name "Sphere134"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere134"
	type sphere
	c -0.0537298055685 -1.0143061058 0.5
	r 0.0635268457439
}

shader {
	name "Sphere135"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere135"
	type sphere
	c -0.343844423268 -0.757971837429 0.5
	r 0.0438731784522
}

shader {
	name "Sphere136"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere136"
	type sphere
	c -0.653220204449 -0.822036259503 0.5
	r 0.0649119846511
}

shader {
	name "Sphere137"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere137"
	type sphere
	c -0.929750869657 -0.636985150865 0.5
	r 0.0603157570387
}

shader {
	name "Sphere138"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere138"
	type sphere
	c -1.13637112008 -0.294269499249 0.5
	r 0.0730698146192
}

shader {
	name "Sphere139"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere139"
	type sphere
	c -1.45248138651 -0.0608423993374 0.5
	r 0.0673973028188
}

shader {
	name "Sphere140"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere140"
	type sphere
	c -1.37467308731 0.352083156669 0.5
	r 0.0665937959458
}

shader {
	name "Sphere141"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere141"
	type sphere
	c -1.02415276384 0.460532446363 0.5
	r 0.0642072824093
}

shader {
	name "Sphere142"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere142"
	type sphere
	c -0.698768385317 0.83058414835 0.5
	r 0.0627181789172
}

shader {
	name "Sphere143"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere143"
	type sphere
	c -0.555998663712 1.13877526973 0.5
	r 0.0533520902201
}

shader {
	name "Sphere144"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere144"
	type sphere
	c -0.271209485642 1.19899106851 0.5
	r 0.0552314082421
}

shader {
	name "Sphere145"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere145"
	type sphere
	c 0.897661273595 0.836891506853 0.5
	r 0.0644401148159
}

shader {
	name "Sphere146"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere146"
	type sphere
	c 1.22795913334 0.368562531692 0.5
	r 0.0734312673186
}

shader {
	name "Sphere147"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere147"
	type sphere
	c 1.56524873999 0.161195578911 0.5
	r 0.0713676599369
}

shader {
	name "Sphere148"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere148"
	type sphere
	c 1.6641997136 -0.567996981797 0.5
	r 0.0889584749713
}

shader {
	name "Sphere149"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere149"
	type sphere
	c 1.70082739035 -0.835159942587 0.5
	r 0.0988305610683
}

shader {
	name "Sphere150"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere150"
	type sphere
	c 1.26740788432 -1.07317539671 0.5
	r 0.0891055944309
}

shader {
	name "Sphere151"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere151"
	type sphere
	c 0.772772662377 -1.42364669568 0.5
	r 0.0843316866398
}

shader {
	name "Sphere152"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere152"
	type sphere
	c -0.0784485250353 -1.18486898005 0.5
	r 0.0657317087366
}

shader {
	name "Sphere153"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere153"
	type sphere
	c -0.367234383421 -0.876592406456 0.5
	r 0.0468052942856
}

shader {
	name "Sphere154"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere154"
	type sphere
	c -0.496168448296 -0.751326657849 0.5
	r 0.0642647152822
}

shader {
	name "Sphere155"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere155"
	type sphere
	c -0.807461254414 -0.885624924976 0.5
	r 0.060214046523
}

shader {
	name "Sphere156"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere156"
	type sphere
	c -1.31016001304 -0.392360677923 0.5
	r 0.076600683441
}

shader {
	name "Sphere157"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere157"
	type sphere
	c -1.49590280863 -0.239006214979 0.5
	r 0.0701367579458
}

shader {
	name "Sphere158"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere158"
	type sphere
	c -1.42875635375 0.110577806933 0.5
	r 0.0623933648624
}

shader {
	name "Sphere159"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere159"
	type sphere
	c -1.35108994033 0.528377167228 0.5
	r 0.0668045002445
}

shader {
	name "Sphere160"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere160"
	type sphere
	c -1.1362344938 0.582740543677 0.5
	r 0.0601596643539
}

shader {
	name "Sphere161"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere161"
	type sphere
	c -0.77072880589 0.683176288633 0.5
	r 0.0603078379243
}

shader {
	name "Sphere162"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere162"
	type sphere
	c -0.636317124956 0.988153188328 0.5
	r 0.0644022021498
}

shader {
	name "Sphere163"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere163"
	type sphere
	c -0.507566066443 1.27116752923 0.5
	r 0.0523777665175
}

shader {
	name "Sphere164"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere164"
	type sphere
	c -0.170718030912 1.09952024049 0.5
	r 0.0508159876781
}

shader {
	name "Sphere165"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere165"
	type sphere
	c 0.765738543965 0.95843953538 0.5
	r 0.070095607319
}

shader {
	name "Sphere166"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere166"
	type sphere
	c 1.0372702443 0.73243138102 0.5
	r 0.0663324079363
}

shader {
	name "Sphere167"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere167"
	type sphere
	c 1.39440449269 0.467938580105 0.5
	r 0.0719597807723
}

shader {
	name "Sphere168"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere168"
	type sphere
	c 1.58180968915 0.351525508204 0.5
	r 0.0719191423162
}

shader {
	name "Sphere169"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere169"
	type sphere
	c 1.56192829385 -0.028280462419 0.5
	r 0.070761190144
}

shader {
	name "Sphere170"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere170"
	type sphere
	c 1.62217918253 -0.339695620984 0.5
	r 0.0851437090013
}

shader {
	name "Sphere171"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere171"
	type sphere
	c 1.68878388047 -1.08879120732 0.5
	r 0.0916072209637
}

shader {
	name "Sphere172"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere172"
	type sphere
	c 1.46242419294 -1.19218319375 0.5
	r 0.082239807371
}

shader {
	name "Sphere173"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere173"
	type sphere
	c 0.983218924419 -1.52198543982 0.5
	r 0.0898849960168
}

shader {
	name "Sphere174"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere174"
	type sphere
	c 0.0625269460263 -1.28726539687 0.5
	r 0.0649472840666
}

shader {
	name "Sphere175"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere175"
	type sphere
	c -0.209680804602 -1.0758624929 0.5
	r 0.0622182153006
}

shader {
	name "Sphere176"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere176"
	type sphere
	c -0.51393681216 -0.919558824942 0.5
	r 0.0626112061901
}

shader {
	name "Sphere177"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere177"
	type sphere
	c -0.68247985507 -0.986022594954 0.5
	r 0.0600201990336
}

shader {
	name "Sphere178"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere178"
	type sphere
	c -1.13776993192 -0.485497281113 0.5
	r 0.07035485879
}

shader {
	name "Sphere179"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere179"
	type sphere
	c -1.6250571591 -0.109442927175 0.5
	r 0.0670691607817
}

shader {
	name "Sphere180"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere180"
	type sphere
	c -1.51855638954 0.460767476559 0.5
	r 0.0686449222669
}

shader {
	name "Sphere181"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere181"
	type sphere
	c -0.982229626845 0.618584981915 0.5
	r 0.058431256775
}

shader {
	name "Sphere182"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere182"
	type sphere
	c -0.860855312648 0.814926776225 0.5
	r 0.0594128797399
}

shader {
	name "Sphere183"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere183"
	type sphere
	c -0.651710419677 1.25027982266 0.5
	r 0.0568596520069
}

shader {
	name "Sphere184"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere184"
	type sphere
	c -0.134621037253 1.22838934129 0.5
	r 0.0495558655799
}

shader {
	name "Sphere185"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere185"
	type sphere
	c 0.935978152364 1.00020372921 0.5
	r 0.061370155664
}

shader {
	name "Sphere186"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere186"
	type sphere
	c 1.01354401004 0.558383740781 0.5
	r 0.0654106273122
}

shader {
	name "Sphere187"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere187"
	type sphere
	c 1.22772369194 0.561831253058 0.5
	r 0.0715203812619
}

shader {
	name "Sphere188"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere188"
	type sphere
	c 1.73870423813 0.241248903956 0.5
	r 0.071910500946
}

shader {
	name "Sphere189"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere189"
	type sphere
	c 1.39890495025 -0.129252894791 0.5
	r 0.073059093524
}

shader {
	name "Sphere190"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere190"
	type sphere
	c 1.83507406008 -0.413452185764 0.5
	r 0.0838382311603
}

shader {
	name "Sphere191"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere191"
	type sphere
	c 1.92161246098 -0.982644837073 0.5
	r 0.100305161125
}

shader {
	name "Sphere192"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere192"
	type sphere
	c 1.26982184291 -1.3060726646 0.5
	r 0.0855767389048
}

shader {
	name "Sphere193"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere193"
	type sphere
	c 0.783282760163 -1.65759184201 0.5
	r 0.0913041480507
}

shader {
	name "Sphere194"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere194"
	type sphere
	c -0.0992804932291 -1.36362553868 0.5
	r 0.069243035046
}

shader {
	name "Sphere195"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere195"
	type sphere
	c -0.243757540614 -1.24295593842 0.5
	r 0.0656814014045
}

shader {
	name "Sphere196"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere196"
	type sphere
	c -0.833873535895 -1.04691626574 0.5
	r 0.0623656589179
}

shader {
	name "Sphere197"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere197"
	type sphere
	c -1.29674597484 -0.591078490099 0.5
	r 0.0727768474315
}

shader {
	name "Sphere198"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere198"
	type sphere
	c -1.6769746143 -0.284522065297 0.5
	r 0.0698918603241
}

shader {
	name "Sphere199"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere199"
	type sphere
	c -1.53806543054 0.280837270559 0.5
	r 0.0670936443343
}

shader {
	name "Sphere200"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere200"
	type sphere
	c -1.48999325076 0.637686266218 0.5
	r 0.0657623411341
}

shader {
	name "Sphere201"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere201"
	type sphere
	c -1.08801099453 0.734472913551 0.5
	r 0.0592487633086
}

shader {
	name "Sphere202"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere202"
	type sphere
	c -0.591303714573 1.38176953225 0.5
	r 0.0516664461622
}

shader {
	name "Sphere203"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere203"
	type sphere
	c -0.221122055055 1.33449382802 0.5
	r 0.0531163354023
}

shader {
	name "Sphere204"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere204"
	type sphere
	c 0.828203413527 1.11770248658 0.5
	r 0.0582104057843
}

shader {
	name "Sphere205"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere205"
	type sphere
	c 1.39260335893 0.660837481761 0.5
	r 0.0727207019056
}

shader {
	name "Sphere206"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere206"
	type sphere
	c 1.7547655034 0.430828075306 0.5
	r 0.0707832353534
}

shader {
	name "Sphere207"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere207"
	type sphere
	c 1.79477216322 -0.19100362238 0.5
	r 0.0857142047151
}

shader {
	name "Sphere208"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere208"
	type sphere
	c 1.88685553599 -0.632354435906 0.5
	r 0.084869290767
}

shader {
	name "Sphere209"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere209"
	type sphere
	c 1.88528867851 -1.23905471037 0.5
	r 0.093922309037
}

shader {
	name "Sphere210"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere210"
	type sphere
	c 1.46334305469 -1.40513385058 0.5
	r 0.0774746720419
}

shader {
	name "Sphere211"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere211"
	type sphere
	c 1.00530049964 -1.76630074723 0.5
	r 0.0940983742596
}

shader {
	name "Sphere212"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere212"
	type sphere
	c 0.5841813316 -1.54033041363 0.5
	r 0.081995554951
}

shader {
	name "Sphere213"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere213"
	type sphere
	c 0.0557207673993 -1.46863014178 0.5
	r 0.0711720231816
}

shader {
	name "Sphere214"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere214"
	type sphere
	c -0.3620578562 -1.12730033646 0.5
	r 0.05840038775
}

shader {
	name "Sphere215"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere215"
	type sphere
	c -0.702533801354 -1.14642644655 0.5
	r 0.0612192353814
}

shader {
	name "Sphere216"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere216"
	type sphere
	c -0.957143047466 -0.941057470802 0.5
	r 0.059498279694
}

shader {
	name "Sphere217"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere217"
	type sphere
	c -1.1255692079 -0.670621819389 0.5
	r 0.0687897537195
}

shader {
	name "Sphere218"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere218"
	type sphere
	c -1.48322137924 -0.50914567898 0.5
	r 0.0799841091848
}

shader {
	name "Sphere219"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere219"
	type sphere
	c -1.79187132368 -0.151475171933 0.5
	r 0.0619519314661
}

shader {
	name "Sphere220"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere220"
	type sphere
	c -1.68611426418 0.385814108729 0.5
	r 0.0690238011099
}

shader {
	name "Sphere221"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere221"
	type sphere
	c -1.65420210234 0.57727511798 0.5
	r 0.0654642005541
}

shader {
	name "Sphere222"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere222"
	type sphere
	c -1.32192547057 0.710685198909 0.5
	r 0.0716650502012
}

shader {
	name "Sphere223"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere223"
	type sphere
	c -0.731329111178 1.37404449737 0.5
	r 0.0535122977465
}

shader {
	name "Sphere224"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere224"
	type sphere
	c -0.45048483291 1.40260915795 0.5
	r 0.0550979635482
}

shader {
	name "Sphere225"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere225"
	type sphere
	c -0.0874062121556 1.34927994473 0.5
	r 0.0477818196249
}

shader {
	name "Sphere226"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere226"
	type sphere
	c 0.666828139856 1.10600227977 0.5
	r 0.0631387454599
}

shader {
	name "Sphere227"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere227"
	type sphere
	c 0.983819944567 1.15810356533 0.5
	r 0.062371197051
}

shader {
	name "Sphere228"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere228"
	type sphere
	c 1.55586000114 0.564910735346 0.5
	r 0.0692942724666
}

shader {
	name "Sphere229"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere229"
	type sphere
	c 1.92044105518 0.322895607057 0.5
	r 0.077515503568
}

shader {
	name "Sphere230"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere230"
	type sphere
	c 2.00837542635 -0.269725068715 0.5
	r 0.0850214793819
}

shader {
	name "Sphere231"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere231"
	type sphere
	c 2.12309330736 -1.15052836331 0.5
	r 0.0963885551789
}

shader {
	name "Sphere232"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere232"
	type sphere
	c 1.29070334363 -1.52750237569 0.5
	r 0.0812323559939
}

shader {
	name "Sphere233"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere233"
	type sphere
	c 0.802097762124 -1.89210820604 0.5
	r 0.0851482824475
}

shader {
	name "Sphere234"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere234"
	type sphere
	c 0.573713555277 -1.76165553476 0.5
	r 0.0841838383727
}

shader {
	name "Sphere235"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere235"
	type sphere
	c -0.115344583228 -1.54963761754 0.5
	r 0.0707852960692
}

shader {
	name "Sphere236"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere236"
	type sphere
	c -0.40617261945 -1.27722868358 0.5
	r 0.0588124513675
}

shader {
	name "Sphere237"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere237"
	type sphere
	c -0.552372589708 -1.08212421749 0.5
	r 0.0612931352454
}

shader {
	name "Sphere238"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere238"
	type sphere
	c -0.852528678778 -1.21048587937 0.5
	r 0.0611068318723
}

shader {
	name "Sphere239"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere239"
	type sphere
	c -0.98709037747 -1.09490202034 0.5
	r 0.058050883414
}

shader {
	name "Sphere240"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere240"
	type sphere
	c -1.27213378151 -0.774244467582 0.5
	r 0.0658322743617
}

shader {
	name "Sphere241"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere241"
	type sphere
	c -1.44833982379 -0.705788242697 0.5
	r 0.0698001496226
}

shader {
	name "Sphere242"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere242"
	type sphere
	c -1.84635001498 -0.30153278785 0.5
	r 0.0577787410622
}

shader {
	name "Sphere243"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere243"
	type sphere
	c -1.75148501321 0.0123371349263 0.5
	r 0.0645860404944
}

shader {
	name "Sphere244"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere244"
	type sphere
	c -1.69688779184 0.209434634418 0.5
	r 0.0635073486971
}

shader {
	name "Sphere245"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere245"
	type sphere
	c -1.62594671167 0.75268207766 0.5
	r 0.0677869057849
}

shader {
	name "Sphere246"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere246"
	type sphere
	c -0.802791209246 1.2459504141 0.5
	r 0.0564974548494
}

shader {
	name "Sphere247"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere247"
	type sphere
	c -0.665687712769 1.50279120732 0.5
	r 0.054873753185
}

shader {
	name "Sphere248"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere248"
	type sphere
	c -0.160187400245 1.46150850038 0.5
	r 0.0525398973621
}

shader {
	name "Sphere249"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere249"
	type sphere
	c -0.00708173656868 1.25075360452 0.5
	r 0.0475580821187
}

shader {
	name "Sphere250"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere250"
	type sphere
	c 0.593072049796 0.960195996048 0.5
	r 0.0594109635243
}

shader {
	name "Sphere251"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere251"
	type sphere
	c 0.743833006696 1.2549950652 0.5
	r 0.062648127027
}

shader {
	name "Sphere252"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere252"
	type sphere
	c 1.10197272706 1.03466828268 0.5
	r 0.065780846712
}

shader {
	name "Sphere253"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere253"
	type sphere
	c 1.55822068692 0.747030937003 0.5
	r 0.06730735321
}

shader {
	name "Sphere254"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere254"
	type sphere
	c 1.91874863288 0.517206889297 0.5
	r 0.0682234857869
}

shader {
	name "Sphere255"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere255"
	type sphere
	c 1.89136912404 0.126708313463 0.5
	r 0.0712316985345
}

shader {
	name "Sphere256"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere256"
	type sphere
	c 2.17086761716 -0.896472993681 0.5
	r 0.0974926326036
}

shader {
	name "Sphere257"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere257"
	type sphere
	c 2.07411911839 -1.39171730376 0.5
	r 0.0881946214674
}

shader {
	name "Sphere258"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere258"
	type sphere
	c 1.48146995571 -1.60534014396 0.5
	r 0.0732942529806
}

shader {
	name "Sphere259"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere259"
	type sphere
	c 1.00371806439 -2.01365076043 0.5
	r 0.0914179319964
}

shader {
	name "Sphere260"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere260"
	type sphere
	c 0.377588038741 -1.63843528131 0.5
	r 0.0895321730277
}

shader {
	name "Sphere261"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere261"
	type sphere
	c 0.0387879463765 -1.65518850908 0.5
	r 0.0693219054055
}

shader {
	name "Sphere262"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere262"
	type sphere
	c -0.2753193928 -1.43998975021 0.5
	r 0.0746733214521
}

shader {
	name "Sphere263"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere263"
	type sphere
	c -0.720641689707 -1.31205241921 0.5
	r 0.0637404396021
}

shader {
	name "Sphere264"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere264"
	type sphere
	c -1.10847117524 -0.993433706379 0.5
	r 0.0606035653129
}

shader {
	name "Sphere265"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere265"
	type sphere
	c -1.62531140117 -0.649066865943 0.5
	r 0.0695793422396
}

shader {
	name "Sphere266"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere266"
	type sphere
	c -1.76314081213 -0.436572757573 0.5
	r 0.0611845105521
}

shader {
	name "Sphere267"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere267"
	type sphere
	c -1.9527154318 -0.183980160936 0.5
	r 0.0611198496309
}

shader {
	name "Sphere268"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere268"
	type sphere
	c -1.83431268246 0.299345781586 0.5
	r 0.05966086314
}

shader {
	name "Sphere269"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere269"
	type sphere
	c -1.79804309369 0.687201285565 0.5
	r 0.0703127162112
}

shader {
	name "Sphere270"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere270"
	type sphere
	c -0.869617413158 1.37157236733 0.5
	r 0.0502204999307
}

shader {
	name "Sphere271"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere271"
	type sphere
	c -0.804938940669 1.49072342023 0.5
	r 0.0499561160124
}

shader {
	name "Sphere272"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere272"
	type sphere
	c -0.303458604124 1.45298907211 0.5
	r 0.0551033115131
}

shader {
	name "Sphere273"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere273"
	type sphere
	c -0.0265466559235 1.46108655779 0.5
	r 0.0476911604508
}

shader {
	name "Sphere274"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere274"
	type sphere
	c 0.578452719584 1.24680217608 0.5
	r 0.0615391975013
}

shader {
	name "Sphere275"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere275"
	type sphere
	c 1.14162206793 1.19695585562 0.5
	r 0.0595147884533
}

shader {
	name "Sphere276"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere276"
	type sphere
	c 1.41258994528 0.839387197904 0.5
	r 0.0620279490425
}

shader {
	name "Sphere277"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere277"
	type sphere
	c 1.70811796552 0.6565785249 0.5
	r 0.0639979915208
}

shader {
	name "Sphere278"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere278"
	type sphere
	c 2.07329139965 0.433006216737 0.5
	r 0.0637705908243
}

shader {
	name "Sphere279"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere279"
	type sphere
	c 2.06819205119 0.192517169981 0.5
	r 0.0702723602526
}

shader {
	name "Sphere280"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere280"
	type sphere
	c 2.36636001775 -1.06625036004 0.5
	r 0.0967003602127
}

shader {
	name "Sphere281"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere281"
	type sphere
	c 2.29803606903 -1.32248180899 0.5
	r 0.0875877707592
}

shader {
	name "Sphere282"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere282"
	type sphere
	c 1.85119278561 -1.48665518659 0.5
	r 0.09353047363
}

shader {
	name "Sphere283"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere283"
	type sphere
	c 1.33171325451 -1.72660260888 0.5
	r 0.0712275651384
}

shader {
	name "Sphere284"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere284"
	type sphere
	c 0.791923641677 -2.12094323588 0.5
	r 0.086647536131
}

shader {
	name "Sphere285"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere285"
	type sphere
	c 0.377978553913 -1.86862227729 0.5
	r 0.0831083224018
}

shader {
	name "Sphere286"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere286"
	type sphere
	c -0.130295616206 -1.74030025397 0.5
	r 0.0726506584695
}

shader {
	name "Sphere287"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere287"
	type sphere
	c -0.875418645681 -1.37095702536 0.5
	r 0.0604647657378
}

shader {
	name "Sphere288"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere288"
	type sphere
	c -1.13208453255 -1.15027897722 0.5
	r 0.0583560566833
}

shader {
	name "Sphere289"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere289"
	type sphere
	c -1.58470635583 -0.825873854766 0.5
	r 0.0664779363771
}

shader {
	name "Sphere290"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere290"
	type sphere
	c -1.92743997569 -0.439205666135 0.5
	r 0.0620556833264
}

shader {
	name "Sphere291"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere291"
	type sphere
	c -1.8428919801 0.145205702611 0.5
	r 0.0561231261051
}

shader {
	name "Sphere292"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere292"
	type sphere
	c -1.84169177707 0.458344509188 0.5
	r 0.0597165367698
}

shader {
	name "Sphere293"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere293"
	type sphere
	c -1.76450858855 0.867292870983 0.5
	r 0.0670776672676
}

shader {
	name "Sphere294"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere294"
	type sphere
	c -0.940682023979 1.26215421381 0.5
	r 0.0476322596948
}

shader {
	name "Sphere295"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere295"
	type sphere
	c -0.751341225814 1.60924690454 0.5
	r 0.0476030911183
}

shader {
	name "Sphere296"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere296"
	type sphere
	c -0.2355392483 1.57512565296 0.5
	r 0.0497100492471
}

shader {
	name "Sphere297"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere297"
	type sphere
	c -0.086673006037 1.57385537824 0.5
	r 0.0481563302496
}

shader {
	name "Sphere298"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere298"
	type sphere
	c 0.652971667288 1.38704657348 0.5
	r 0.0575705421073
}

shader {
	name "Sphere299"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere299"
	type sphere
	c 1.03478507795 1.30615623576 0.5
	r 0.0550631841944
}

shader {
	name "Sphere300"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere300"
	type sphere
	c 1.25664955376 1.0911273878 0.5
	r 0.0577133235461
}

shader {
	name "Sphere301"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere301"
	type sphere
	c 1.25932366021 0.77984842723 0.5
	r 0.0612904331471
}

shader {
	name "Sphere302"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere302"
	type sphere
	c 1.5600940851 0.924218425828 0.5
	r 0.0655906909703
}

shader {
	name "Sphere303"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere303"
	type sphere
	c 1.71833872503 0.834162117773 0.5
	r 0.069410115299
}

shader {
	name "Sphere304"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere304"
	type sphere
	c 2.07359929815 0.605148818339 0.5
	r 0.065336566895
}

shader {
	name "Sphere305"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere305"
	type sphere
	c 2.03768323001 0.0076867219671 0.5
	r 0.0702262483135
}

shader {
	name "Sphere306"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere306"
	type sphere
	c 2.42011324218 -0.808556834082 0.5
	r 0.100729732182
}

shader {
	name "Sphere307"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere307"
	type sphere
	c 2.24499490625 -1.5449683807 0.5
	r 0.0839535427583
}

shader {
	name "Sphere308"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere308"
	type sphere
	c 1.51177632848 -1.80032514735 0.5
	r 0.0747003943084
}

shader {
	name "Sphere309"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere309"
	type sphere
	c 0.987062013474 -2.25777563849 0.5
	r 0.0921013825637
}

shader {
	name "Sphere310"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere310"
	type sphere
	c 0.608899860709 -1.99623627122 0.5
	r 0.0794559299134
}

shader {
	name "Sphere311"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere311"
	type sphere
	c 0.0307299908556 -1.83992907943 0.5
	r 0.0693652607368
}

shader {
	name "Sphere312"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere312"
	type sphere
	c -0.749007943321 -1.48300152266 0.5
	r 0.0662244986611
}

shader {
	name "Sphere313"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere313"
	type sphere
	c -1.00596661533 -1.27134557926 0.5
	r 0.0626933930384
}

shader {
	name "Sphere314"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere314"
	type sphere
	c -1.26149166838 -1.05370994957 0.5
	r 0.0627446387957
}

shader {
	name "Sphere315"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere315"
	type sphere
	c -1.42132310373 -0.880372909044 0.5
	r 0.0626968739235
}

shader {
	name "Sphere316"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere316"
	type sphere
	c -1.7499258378 -0.774844289154 0.5
	r 0.0632124266228
}

shader {
	name "Sphere317"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere317"
	type sphere
	c -1.84171289932 -0.586284314045 0.5
	r 0.0656234414962
}

shader {
	name "Sphere318"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere318"
	type sphere
	c -1.96384320326 0.224744411788 0.5
	r 0.052447254807
}

shader {
	name "Sphere319"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere319"
	type sphere
	c -1.96914637268 0.372687098868 0.5
	r 0.0554563748027
}

shader {
	name "Sphere320"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere320"
	type sphere
	c -1.93297210712 0.809809126885 0.5
	r 0.0664230446471
}

shader {
	name "Sphere321"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere321"
	type sphere
	c -1.59578103734 0.931710276405 0.5
	r 0.0683769602652
}

shader {
	name "Sphere322"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere322"
	type sphere
	c -0.896211258361 1.14292045325 0.5
	r 0.0478104744034
}

shader {
	name "Sphere323"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere323"
	type sphere
	c -1.00383370773 1.37677444123 0.5
	r 0.050517302592
}

shader {
	name "Sphere324"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere324"
	type sphere
	c -0.874539892815 1.59689727888 0.5
	r 0.0452589783853
}

shader {
	name "Sphere325"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere325"
	type sphere
	c -0.622825234695 1.63738575254 0.5
	r 0.0510672541819
}

shader {
	name "Sphere326"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere326"
	type sphere
	c -0.369017497888 1.57747067392 0.5
	r 0.0504140862446
}

shader {
	name "Sphere327"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere327"
	type sphere
	c 0.0371426711501 1.56677776197 0.5
	r 0.0448570193042
}

shader {
	name "Sphere328"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere328"
	type sphere
	c 0.493711787468 1.38785828238 0.5
	r 0.0618759191541
}

shader {
	name "Sphere329"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere329"
	type sphere
	c 0.800771962116 1.39923560318 0.5
	r 0.0536559993424
}

shader {
	name "Sphere330"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere330"
	type sphere
	c 1.17297072464 1.34241511214 0.5
	r 0.0520844393243
}

shader {
	name "Sphere331"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere331"
	type sphere
	c 1.28817744505 1.23739970267 0.5
	r 0.0545103321196
}

shader {
	name "Sphere332"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere332"
	type sphere
	c 1.40711614136 1.00987557195 0.5
	r 0.0659042190045
}

shader {
	name "Sphere333"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere333"
	type sphere
	c 1.87084600783 0.728915673865 0.5
	r 0.0695632561062
}

shader {
	name "Sphere334"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere334"
	type sphere
	c 2.21374087871 0.516830028733 0.5
	r 0.0589008169726
}

shader {
	name "Sphere335"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere335"
	type sphere
	c 2.21137710917 0.0738874782792 0.5
	r 0.0691852231839
}

shader {
	name "Sphere336"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere336"
	type sphere
	c 2.2123201269 -0.630066203303 0.5
	r 0.104716726217
}

shader {
	name "Sphere337"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere337"
	type sphere
	c 2.61307712204 -0.988708644704 0.5
	r 0.0972613667633
}

shader {
	name "Sphere338"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere338"
	type sphere
	c 2.45262122129 -1.48168116091 0.5
	r 0.0788395832467
}

shader {
	name "Sphere339"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere339"
	type sphere
	c 1.65632798009 -1.67618674073 0.5
	r 0.0682046694225
}

shader {
	name "Sphere340"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere340"
	type sphere
	c 1.35812149291 -1.90724796816 0.5
	r 0.065696516917
}

shader {
	name "Sphere341"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere341"
	type sphere
	c 1.20445756761 -2.14907178663 0.5
	r 0.0901923689257
}

shader {
	name "Sphere342"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere342"
	type sphere
	c 0.76482426695 -2.35446410626 0.5
	r 0.089668472269
}

shader {
	name "Sphere343"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere343"
	type sphere
	c 0.586488381694 -2.20897072706 0.5
	r 0.0809778585794
}

shader {
	name "Sphere344"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere344"
	type sphere
	c -0.134092818813 -1.934840105 0.5
	r 0.0732820211011
}

shader {
	name "Sphere345"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere345"
	type sphere
	c -0.585306149256 -1.41896356881 0.5
	r 0.065611628839
}

shader {
	name "Sphere346"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere346"
	type sphere
	c -0.908730456133 -1.52481840924 0.5
	r 0.0576048693012
}

shader {
	name "Sphere347"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere347"
	type sphere
	c -1.2721044121 -1.21238052623 0.5
	r 0.0565241857254
}

shader {
	name "Sphere348"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere348"
	type sphere
	c -1.54329113041 -0.989223968926 0.5
	r 0.0599109293886
}

shader {
	name "Sphere349"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere349"
	type sphere
	c -1.71301596914 -0.934181565057 0.5
	r 0.0594548961115
}

shader {
	name "Sphere350"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere350"
	type sphere
	c -2.01495490826 -0.583210934984 0.5
	r 0.064328509688
}

shader {
	name "Sphere351"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere351"
	type sphere
	c -1.97323989116 0.0873595574702 0.5
	r 0.0508321185737
}

shader {
	name "Sphere352"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere352"
	type sphere
	c -1.98606898079 0.525158180374 0.5
	r 0.0595991140514
}

shader {
	name "Sphere353"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere353"
	type sphere
	c -1.89936307598 0.984204070662 0.5
	r 0.066779918556
}

shader {
	name "Sphere354"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere354"
	type sphere
	c -0.76971627425 1.10664749742 0.5
	r 0.0508842490407
}

shader {
	name "Sphere355"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere355"
	type sphere
	c -1.02798472194 1.16194787444 0.5
	r 0.0520446068833
}

shader {
	name "Sphere356"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere356"
	type sphere
	c -0.826571589979 1.70802548453 0.5
	r 0.0455202612267
}

shader {
	name "Sphere357"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere357"
	type sphere
	c -0.523208468358 1.53696935984 0.5
	r 0.0550171958224
}

shader {
	name "Sphere358"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere358"
	type sphere
	c -0.299183852574 1.69715627159 0.5
	r 0.0535126977068
}

shader {
	name "Sphere359"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere359"
	type sphere
	c -0.0141435561406 1.67840789421 0.5
	r 0.0472787744348
}

shader {
	name "Sphere360"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere360"
	type sphere
	c 0.0991095726267 1.46182668455 0.5
	r 0.0465526457282
}

shader {
	name "Sphere361"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere361"
	type sphere
	c 0.413597322433 1.24322057459 0.5
	r 0.0621315267406
}

shader {
	name "Sphere362"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere362"
	type sphere
	c 0.579883401231 1.52796829999 0.5
	r 0.0614902219873
}

shader {
	name "Sphere363"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere363"
	type sphere
	c 0.892200468089 1.29199760174 0.5
	r 0.0520359013391
}

shader {
	name "Sphere364"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere364"
	type sphere
	c 1.07762417753 1.43946041758 0.5
	r 0.0499507256262
}

shader {
	name "Sphere365"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere365"
	type sphere
	c 1.55988717675 1.10241100714 0.5
	r 0.0680538351085
}

shader {
	name "Sphere366"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere366"
	type sphere
	c 1.88706410832 0.915898934543 0.5
	r 0.0712007083465
}

shader {
	name "Sphere367"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere367"
	type sphere
	c 2.22437184135 0.673382122285 0.5
	r 0.0587836600887
}

shader {
	name "Sphere368"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere368"
	type sphere
	c 2.22413953188 0.352812878799 0.5
	r 0.0643590247088
}

shader {
	name "Sphere369"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere369"
	type sphere
	c 2.18514056212 -0.114241852537 0.5
	r 0.0732772748708
}

shader {
	name "Sphere370"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere370"
	type sphere
	c 2.48227833256 -0.534438378814 0.5
	r 0.110079546821
}

shader {
	name "Sphere371"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere371"
	type sphere
	c 2.67482917799 -0.735885525279 0.5
	r 0.0979301441905
}

shader {
	name "Sphere372"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere372"
	type sphere
	c 2.55336459028 -1.23240092386 0.5
	r 0.0909146845054
}

shader {
	name "Sphere373"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere373"
	type sphere
	c 2.41147812064 -1.69513775717 0.5
	r 0.0841995721227
}

shader {
	name "Sphere374"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere374"
	type sphere
	c 1.69692081821 -1.85648827287 0.5
	r 0.0704062493844
}

shader {
	name "Sphere375"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere375"
	type sphere
	c 1.51658016764 -1.99194327865 0.5
	r 0.0690583589044
}

shader {
	name "Sphere376"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere376"
	type sphere
	c 1.199541717 -1.84527871072 0.5
	r 0.0619968677432
}

shader {
	name "Sphere377"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere377"
	type sphere
	c 1.19547181854 -2.39699771055 0.5
	r 0.0958741626824
}

shader {
	name "Sphere378"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere378"
	type sphere
	c 0.952866135058 -2.49077317122 0.5
	r 0.0845187739973
}

shader {
	name "Sphere379"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere379"
	type sphere
	c 0.419269072188 -2.08181230757 0.5
	r 0.076578490482
}

shader {
	name "Sphere380"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere380"
	type sphere
	c 0.0330456922942 -2.02423625068 0.5
	r 0.0688760280072
}

shader {
	name "Sphere381"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere381"
	type sphere
	c -0.303397452741 -1.83337619505 0.5
	r 0.0747532062988
}

shader {
	name "Sphere382"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere382"
	type sphere
	c -0.610663927259 -1.5931459853 0.5
	r 0.0664022861711
}

shader {
	name "Sphere383"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere383"
	type sphere
	c -0.804766493783 -1.64024578275 0.5
	r 0.0589036755062
}

shader {
	name "Sphere384"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere384"
	type sphere
	c -1.40624919205 -1.13210630356 0.5
	r 0.0607226040315
}

shader {
	name "Sphere385"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere385"
	type sphere
	c -1.87231358572 -0.892395610366 0.5
	r 0.0640603281311
}

shader {
	name "Sphere386"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere386"
	type sphere
	c -2.08879870057 -0.436311570275 0.5
	r 0.0589828242225
}

shader {
	name "Sphere387"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere387"
	type sphere
	c -2.0842006088 0.16185091143 0.5
	r 0.0494023515682
}

shader {
	name "Sphere388"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere388"
	type sphere
	c -2.1102456239 0.428602811605 0.5
	r 0.0583746651845
}

shader {
	name "Sphere389"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere389"
	type sphere
	c -2.07631604416 0.927363616409 0.5
	r 0.0726135693788
}

shader {
	name "Sphere390"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere390"
	type sphere
	c -0.865843403671 1.02419981876 0.5
	r 0.0440968025381
}

shader {
	name "Sphere391"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere391"
	type sphere
	c -0.951613504218 1.69568944255 0.5
	r 0.0487164501163
}

shader {
	name "Sphere392"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere392"
	type sphere
	c -0.488112272765 1.67893796753 0.5
	r 0.0546645758587
}

shader {
	name "Sphere393"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere393"
	type sphere
	c -0.163664865364 1.68467445051 0.5
	r 0.0485567412081
}

shader {
	name "Sphere394"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere394"
	type sphere
	c 0.110914866479 1.66467472166 0.5
	r 0.0470788835306
}

shader {
	name "Sphere395"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere395"
	type sphere
	c 0.329985394986 1.38442574238 0.5
	r 0.0609458585701
}

shader {
	name "Sphere396"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere396"
	type sphere
	c 0.415533031705 1.53309889131 0.5
	r 0.0618326019283
}

shader {
	name "Sphere397"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere397"
	type sphere
	c 0.939505572863 1.42211210059 0.5
	r 0.0517993051601
}

shader {
	name "Sphere398"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere398"
	type sphere
	c 1.20275263765 1.47086078127 0.5
	r 0.046805420606
}

shader {
	name "Sphere399"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere399"
	type sphere
	c 1.73115213751 1.01732820894 0.5
	r 0.068300179444
}

shader {
	name "Sphere400"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere400"
	type sphere
	c 2.04880419946 0.80540091642 0.5
	r 0.07571062159
}

shader {
	name "Sphere401"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere401"
	type sphere
	c 2.3616949376 0.585582649072 0.5
	r 0.0634603127593
}

shader {
	name "Sphere402"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere402"
	type sphere
	c 2.36890945188 -0.0382883821788 0.5
	r 0.0758576075613
}

shader {
	name "Sphere403"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere403"
	type sphere
	c 2.25978520827 -0.356246544625 0.5
	r 0.103710607471
}

shader {
	name "Sphere404"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere404"
	type sphere
	c 2.85844504319 -0.915591325294 0.5
	r 0.0947614235742
}

shader {
	name "Sphere405"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere405"
	type sphere
	c 2.78133893265 -1.16747827062 0.5
	r 0.0868641923938
}

shader {
	name "Sphere406"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere406"
	type sphere
	c 2.60867235301 -1.61545171398 0.5
	r 0.075315097433
}

shader {
	name "Sphere407"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere407"
	type sphere
	c 2.19294526902 -1.769537921 0.5
	r 0.0889383650317
}

shader {
	name "Sphere408"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere408"
	type sphere
	c 1.83254992331 -1.72821729053 0.5
	r 0.0696022975775
}

shader {
	name "Sphere409"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere409"
	type sphere
	c 1.41865723505 -2.27327926317 0.5
	r 0.0955125301847
}

shader {
	name "Sphere410"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere410"
	type sphere
	c 0.744672728773 -2.59195566527 0.5
	r 0.0890902558092
}

shader {
	name "Sphere411"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere411"
	type sphere
	c 0.39367664018 -2.27965937351 0.5
	r 0.0730430960857
}

shader {
	name "Sphere412"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere412"
	type sphere
	c -0.120464394167 -2.12247193606 0.5
	r 0.06781257081
}

shader {
	name "Sphere413"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere413"
	type sphere
	c -0.30238495493 -2.02740333813 0.5
	r 0.0707691323241
}

shader {
	name "Sphere414"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere414"
	type sphere
	c -0.293560378599 -1.63832643368 0.5
	r 0.0717200414631
}

shader {
	name "Sphere415"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere415"
	type sphere
	c -0.96371819977 -1.67644555992 0.5
	r 0.0633625857667
}

shader {
	name "Sphere416"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere416"
	type sphere
	c -1.40269030685 -1.28913782635 0.5
	r 0.0570812804891
}

shader {
	name "Sphere417"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere417"
	type sphere
	c -1.82266674129 -1.05173784646 0.5
	r 0.0611127561076
}

shader {
	name "Sphere418"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere418"
	type sphere
	c -2.18021457608 -0.566387499188 0.5
	r 0.0602568205582
}

shader {
	name "Sphere419"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere419"
	type sphere
	c -2.09137670064 0.0345606662755 0.5
	r 0.046216921218
}

shader {
	name "Sphere420"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere420"
	type sphere
	c -2.07923880877 0.290521501754 0.5
	r 0.0471723159386
}

shader {
	name "Sphere421"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere421"
	type sphere
	c -2.13143150754 0.581355347929 0.5
	r 0.0572863727597
}

shader {
	name "Sphere422"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere422"
	type sphere
	c -2.09452005105 0.746520967014 0.5
	r 0.0637038559947
}

shader {
	name "Sphere423"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere423"
	type sphere
	c -2.03075105642 1.11530512938 0.5
	r 0.0724259992843
}

shader {
	name "Sphere424"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere424"
	type sphere
	c -0.996785606789 1.57508505655 0.5
	r 0.0478733497335
}

shader {
	name "Sphere425"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere425"
	type sphere
	c -0.895269055688 1.80675031959 0.5
	r 0.0446855498637
}

shader {
	name "Sphere426"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere426"
	type sphere
	c -0.595461637604 1.77171802177 0.5
	r 0.051750948547
}

shader {
	name "Sphere427"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere427"
	type sphere
	c -0.215127645356 1.79949280117 0.5
	r 0.0458112361311
}

shader {
	name "Sphere428"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere428"
	type sphere
	c 0.0602670392809 1.77733697002 0.5
	r 0.0455635276011
}

shader {
	name "Sphere429"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere429"
	type sphere
	c 0.247193983522 1.2418994276 0.5
	r 0.0626749108117
}

shader {
	name "Sphere430"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere430"
	type sphere
	c 0.502367509072 1.66570350139 0.5
	r 0.0570470330115
}

shader {
	name "Sphere431"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere431"
	type sphere
	c 0.853847136046 1.52401354107 0.5
	r 0.0480416440805
}

shader {
	name "Sphere432"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere432"
	type sphere
	c 1.11867762729 1.5572607482 0.5
	r 0.0436109962106
}

shader {
	name "Sphere433"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere433"
	type sphere
	c 1.29407546546 1.38892698633 0.5
	r 0.0452125975706
}

shader {
	name "Sphere434"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere434"
	type sphere
	c 1.89135468498 1.09998603241 0.5
	r 0.0669021106517
}

shader {
	name "Sphere435"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere435"
	type sphere
	c 2.05328584592 0.995782044815 0.5
	r 0.0671147816207
}

shader {
	name "Sphere436"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere436"
	type sphere
	c 2.3625875058 0.749703400691 0.5
	r 0.059632071274
}

shader {
	name "Sphere437"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere437"
	type sphere
	c 2.37852684211 0.157079931681 0.5
	r 0.0708460585263
}

shader {
	name "Sphere438"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere438"
	type sphere
	c 2.52052972382 -0.244964197905 0.5
	r 0.108913351624
}

shader {
	name "Sphere439"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere439"
	type sphere
	c 2.92581419844 -0.669154044909 0.5
	r 0.0968484382187
}

shader {
	name "Sphere440"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere440"
	type sphere
	c 2.72632179188 -1.38788915364 0.5
	r 0.0835160052855
}

shader {
	name "Sphere441"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere441"
	type sphere
	c 2.58786128368 -1.81681322149 0.5
	r 0.0765104636191
}

shader {
	name "Sphere442"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere442"
	type sphere
	c 2.36905762036 -1.90982861427 0.5
	r 0.0799316571422
}

shader {
	name "Sphere443"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere443"
	type sphere
	c 1.87188866883 -1.9041418561 0.5
	r 0.0655996132441
}

shader {
	name "Sphere444"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere444"
	type sphere
	c 1.41578817856 -2.53027102061 0.5
	r 0.097243298825
}

shader {
	name "Sphere445"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere445"
	type sphere
	c 0.943067808134 -2.72130924632 0.5
	r 0.0885393813597
}

shader {
	name "Sphere446"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere446"
	type sphere
	c 0.559375667434 -2.45737686861 0.5
	r 0.08266867428
}

shader {
	name "Sphere447"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere447"
	type sphere
	c 0.227129076441 -2.16244539559 0.5
	r 0.0797015577579
}

shader {
	name "Sphere448"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere448"
	type sphere
	c -0.468209382577 -1.93650250881 0.5
	r 0.0710596187659
}

shader {
	name "Sphere449"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere449"
	type sphere
	c -0.465303940961 -1.7234216656 0.5
	r 0.0720317949106
}

shader {
	name "Sphere450"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere450"
	type sphere
	c -0.847028731143 -1.7949260828 0.5
	r 0.0613587530025
}

shader {
	name "Sphere451"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere451"
	type sphere
	c -1.06116239164 -1.5473273314 0.5
	r 0.0579587816815
}

shader {
	name "Sphere452"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere452"
	type sphere
	c -1.26946568699 -1.36485088447 0.5
	r 0.0578457068108
}

shader {
	name "Sphere453"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere453"
	type sphere
	c -1.53334049252 -1.21821403586 0.5
	r 0.0544133650255
}

shader {
	name "Sphere454"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere454"
	type sphere
	c -1.99046425065 -1.02087024062 0.5
	r 0.066847032288
}

shader {
	name "Sphere455"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere455"
	type sphere
	c -2.1164207348 -0.708642400545 0.5
	r 0.0566713091594
}

shader {
	name "Sphere456"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere456"
	type sphere
	c -2.25258798237 -0.4161972318 0.5
	r 0.06478198272
}

shader {
	name "Sphere457"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere457"
	type sphere
	c -2.19766835527 0.100161813685 0.5
	r 0.0474623312404
}

shader {
	name "Sphere458"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere458"
	type sphere
	c -2.19060410541 0.233312551557 0.5
	r 0.0467278436386
}

shader {
	name "Sphere459"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere459"
	type sphere
	c -2.2592854757 0.487292013887 0.5
	r 0.0617595563667
}

shader {
	name "Sphere460"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere460"
	type sphere
	c -2.23981302618 0.840719088925 0.5
	r 0.0661638683294
}

shader {
	name "Sphere461"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere461"
	type sphere
	c -2.21962014686 1.06186216481 0.5
	r 0.0747875263526
}

shader {
	name "Sphere462"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere462"
	type sphere
	c -1.84408535718 1.16018302608 0.5
	r 0.0715624941667
}

shader {
	name "Sphere463"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere463"
	type sphere
	c -1.08038013492 1.67394498139 0.5
	r 0.0492258163454
}

shader {
	name "Sphere464"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere464"
	type sphere
	c -1.01919827168 1.80592766187 0.5
	r 0.0482634099455
}

shader {
	name "Sphere465"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere465"
	type sphere
	c -0.776292877582 1.81762884403 0.5
	r 0.044918809425
}

shader {
	name "Sphere466"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere466"
	type sphere
	c -0.463914461885 1.82139796875 0.5
	r 0.0537107770787
}

shader {
	name "Sphere467"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere467"
	type sphere
	c -0.0941916133902 1.78868477908 0.5
	r 0.0452522837752
}

shader {
	name "Sphere468"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere468"
	type sphere
	c 0.185498109121 1.76818954689 0.5
	r 0.048610004319
}

shader {
	name "Sphere469"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere469"
	type sphere
	c 0.343730582452 1.68268188473 0.5
	r 0.0626101491529
}

shader {
	name "Sphere470"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere470"
	type sphere
	c 0.65854832889 1.66976754652 0.5
	r 0.0601282322102
}

shader {
	name "Sphere471"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere471"
	type sphere
	c 0.983146198017 1.55238109729 0.5
	r 0.0512391103021
}

shader {
	name "Sphere472"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere472"
	type sphere
	c 1.23196132108 1.58929829817 0.5
	r 0.0446841052167
}

shader {
	name "Sphere473"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere473"
	type sphere
	c 1.32013554626 1.5066805467 0.5
	r 0.0452394819822
}

shader {
	name "Sphere474"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere474"
	type sphere
	c 1.741470354 1.19796589687 0.5
	r 0.0673989268114
}

shader {
	name "Sphere475"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere475"
	type sphere
	c 2.21563328746 0.908167870456 0.5
	r 0.0712453503509
}

shader {
	name "Sphere476"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere476"
	type sphere
	c 2.50682232659 0.672030500226 0.5
	r 0.063232403595
}

shader {
	name "Sphere477"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere477"
	type sphere
	c 2.5465277112 0.0576796102274 0.5
	r 0.0755571610549
}

shader {
	name "Sphere478"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere478"
	type sphere
	c 2.75614939693 -0.421777033771 0.5
	r 0.11202423622
}

shader {
	name "Sphere479"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere479"
	type sphere
	c 3.10422185824 -0.853231727969 0.5
	r 0.0954119610958
}

shader {
	name "Sphere480"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere480"
	type sphere
	c 2.9334245083 -1.32693036314 0.5
	r 0.0783997875671
}

shader {
	name "Sphere481"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere481"
	type sphere
	c 2.76523572158 -1.7318385545 0.5
	r 0.070998321555
}

shader {
	name "Sphere482"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere482"
	type sphere
	c 2.17420497897 -1.99237753168 0.5
	r 0.0787813071576
}

shader {
	name "Sphere483"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere483"
	type sphere
	c 1.75070534469 -2.02776000047 0.5
	r 0.0642323919084
}

shader {
	name "Sphere484"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere484"
	type sphere
	c 1.64987250437 -2.40198585688 0.5
	r 0.102955507581
}

shader {
	name "Sphere485"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere485"
	type sphere
	c 1.19113041401 -2.64944465008 0.5
	r 0.0934890375496
}

shader {
	name "Sphere486"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere486"
	type sphere
	c 0.734091195398 -2.82633541334 0.5
	r 0.0868736105815
}

shader {
	name "Sphere487"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere487"
	type sphere
	c 0.531361794767 -2.67647698031 0.5
	r 0.0829941466958
}

shader {
	name "Sphere488"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere488"
	type sphere
	c 0.221178135552 -2.36266590102 0.5
	r 0.070530134221
}

shader {
	name "Sphere489"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere489"
	type sphere
	c -0.463338653589 -2.12512201459 0.5
	r 0.07045216909
}

shader {
	name "Sphere490"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere490"
	type sphere
	c -0.697295152728 -1.74944603991 0.5
	r 0.0560074498789
}

shader {
	name "Sphere491"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere491"
	type sphere
	c -1.00977531071 -1.84236227171 0.5
	r 0.0657803859906
}

shader {
	name "Sphere492"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere492"
	type sphere
	c -1.12930679328 -1.69100954508 0.5
	r 0.0613082878541
}

shader {
	name "Sphere493"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere493"
	type sphere
	c -1.40178336847 -1.44056409106 0.5
	r 0.0564904549992
}

shader {
	name "Sphere494"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere494"
	type sphere
	c -1.53139549027 -1.36307430447 0.5
	r 0.0542416291389
}

shader {
	name "Sphere495"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere495"
	type sphere
	c -1.92538225053 -1.18029876161 0.5
	r 0.0623035775658
}

shader {
	name "Sphere496"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere496"
	type sphere
	c -1.97226288389 -0.733828409552 0.5
	r 0.0530847810068
}

shader {
	name "Sphere497"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere497"
	type sphere
	c -2.26810573382 -0.696428027742 0.5
	r 0.057460678165
}

shader {
	name "Sphere498"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere498"
	type sphere
	c -2.33988344622 -0.557341530715 0.5
	r 0.0596868638169
}

shader {
	name "Sphere499"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere499"
	type sphere
	c -2.144983544 -0.281645144847 0.5
	r 0.0644336348883
}

shader {
	name "Sphere500"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere500"
	type sphere
	c -2.19771011842 -0.0218854220937 0.5
	r 0.0440731009527
}

shader {
	name "Sphere501"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere501"
	type sphere
	c -2.26616341671 0.640072059114 0.5
	r 0.0529415319643
}

shader {
	name "Sphere502"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere502"
	type sphere
	c -2.1683643931 1.25272985783 0.5
	r 0.0734349957168
}

shader {
	name "Sphere503"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere503"
	type sphere
	c -1.974872811 1.29843038722 0.5
	r 0.0711696015652
}

shader {
	name "Sphere504"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere504"
	type sphere
	c -1.11843811877 1.5547242145 0.5
	r 0.0446351221933
}

shader {
	name "Sphere505"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere505"
	type sphere
	c -0.953334200704 1.90761089081 0.5
	r 0.0425998093817
}

shader {
	name "Sphere506"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere506"
	type sphere
	c -0.574262131288 1.90729863798 0.5
	r 0.051170047566
}

shader {
	name "Sphere507"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere507"
	type sphere
	c -0.144111107985 1.90346464221 0.5
	r 0.0486217529342
}

shader {
	name "Sphere508"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere508"
	type sphere
	c 0.126738926875 1.88122809627 0.5
	r 0.0469388039884
}

shader {
	name "Sphere509"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere509"
	type sphere
	c 0.246778090092 1.54294309606 0.5
	r 0.0649487670136
}

shader {
	name "Sphere510"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere510"
	type sphere
	c 0.445527145302 1.81344046647 0.5
	r 0.0616735792071
}

shader {
	name "Sphere511"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere511"
	type sphere
	c 0.890747158625 1.64530542274 0.5
	r 0.0470438404904
}

shader {
	name "Sphere512"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere512"
	type sphere
	c 1.14656170574 1.66975786145 0.5
	r 0.0433150143126
}

shader {
	name "Sphere513"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere513"
	type sphere
	c 1.40725624002 1.42560315008 0.5
	r 0.0440185833788
}

shader {
	name "Sphere514"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere514"
	type sphere
	c 1.90015388383 1.27588605351 0.5
	r 0.0651878657617
}

shader {
	name "Sphere515"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere515"
	type sphere
	c 2.20145897437 1.08724234512 0.5
	r 0.0634805769131
}

shader {
	name "Sphere516"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere516"
	type sphere
	c 2.49542025058 0.833466163928 0.5
	r 0.0581459634211
}

shader {
	name "Sphere517"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere517"
	type sphere
	c 2.51151190984 0.499721355416 0.5
	r 0.0660473082187
}

shader {
	name "Sphere518"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere518"
	type sphere
	c 2.53918534558 0.24883307588 0.5
	r 0.067913659122
}

shader {
	name "Sphere519"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere519"
	type sphere
	c 2.78129002345 -0.136199107254 0.5
	r 0.102987569988
}

shader {
	name "Sphere520"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere520"
	type sphere
	c 3.1786066762 -0.605345954711 0.5
	r 0.0986924115256
}

shader {
	name "Sphere521"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere521"
	type sphere
	c 3.03727585993 -1.10856188541 0.5
	r 0.102558570785
}

shader {
	name "Sphere522"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere522"
	type sphere
	c 2.88516300043 -1.52234589899 0.5
	r 0.072565366346
}

shader {
	name "Sphere523"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere523"
	type sphere
	c 2.75837133834 -1.92784066032 0.5
	r 0.0760933818078
}

shader {
	name "Sphere524"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere524"
	type sphere
	c 2.34291012427 -2.12333567364 0.5
	r 0.0813949919985
}

shader {
	name "Sphere525"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere525"
	type sphere
	c 1.91304745692 -2.06817780584 0.5
	r 0.0612409726827
}

shader {
	name "Sphere526"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere526"
	type sphere
	c 1.6320909501 -2.66252946206 0.5
	r 0.0929067502772
}

shader {
	name "Sphere527"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere527"
	type sphere
	c 1.39966422376 -2.78169375747 0.5
	r 0.0917111220631
}

shader {
	name "Sphere528"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere528"
	type sphere
	c 0.93220782512 -2.9652605512 0.5
	r 0.0946053028133
}

shader {
	name "Sphere529"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere529"
	type sphere
	c 0.356172092685 -2.54229983188 0.5
	r 0.082507826457
}

shader {
	name "Sphere530"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere530"
	type sphere
	c 0.0488321753645 -2.26967865877 0.5
	r 0.0763430710709
}

shader {
	name "Sphere531"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere531"
	type sphere
	c -0.295519257845 -2.22096244146 0.5
	r 0.0744914908893
}

shader {
	name "Sphere532"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere532"
	type sphere
	c -0.634039284284 -2.0359860257 0.5
	r 0.0739767426
}

shader {
	name "Sphere533"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere533"
	type sphere
	c -0.728378829561 -1.89276589247 0.5
	r 0.053981463182
}

shader {
	name "Sphere534"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere534"
	type sphere
	c -0.880719487799 -1.96082971506 0.5
	r 0.0656086986615
}

shader {
	name "Sphere535"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere535"
	type sphere
	c -1.21316881726 -1.55842884087 0.5
	r 0.0563496750445
}

shader {
	name "Sphere536"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere536"
	type sphere
	c -1.65176611549 -1.29246806753 0.5
	r 0.0504212084005
}

shader {
	name "Sphere537"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere537"
	type sphere
	c -2.088196727 -1.16011386751 0.5
	r 0.0607421083786
}

shader {
	name "Sphere538"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere538"
	type sphere
	c -2.06050986416 -0.84051974759 0.5
	r 0.0507585927152
}

shader {
	name "Sphere539"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere539"
	type sphere
	c -2.42633180354 -0.414506518495 0.5
	r 0.0655320526855
}

shader {
	name "Sphere540"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere540"
	type sphere
	c -2.32192590464 -0.249821755208 0.5
	r 0.0704023636565
}

shader {
	name "Sphere541"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere541"
	type sphere
	c -2.09679690238 -0.0898407655192 0.5
	r 0.0471726704716
}

shader {
	name "Sphere542"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere542"
	type sphere
	c -2.30419190607 0.0346274769684 0.5
	r 0.0463387033599
}

shader {
	name "Sphere543"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere543"
	type sphere
	c -2.39435035318 0.569470859743 0.5
	r 0.0568160931477
}

shader {
	name "Sphere544"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere544"
	type sphere
	c -2.35299262886 1.20181215109 0.5
	r 0.0702055679923
}

shader {
	name "Sphere545"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere545"
	type sphere
	c -1.79059646086 1.34249330513 0.5
	r 0.0709337555425
}

shader {
	name "Sphere546"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere546"
	type sphere
	c -1.20101490055 1.64049945302 0.5
	r 0.0446631308281
}

shader {
	name "Sphere547"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere547"
	type sphere
	c -1.0709307538 1.92067709574 0.5
	r 0.0461403573659
}

shader {
	name "Sphere548"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere548"
	type sphere
	c -0.445084565824 1.9650604459 0.5
	r 0.0549576552446
}

shader {
	name "Sphere549"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere549"
	type sphere
	c -0.269209082976 1.90822722001 0.5
	r 0.0452696968387
}

shader {
	name "Sphere550"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere550"
	type sphere
	c -0.025336224657 1.88224162462 0.5
	r 0.0418703062713
}

shader {
	name "Sphere551"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere551"
	type sphere
	c 0.251037007811 1.87652285457 0.5
	r 0.0463515257668
}

shader {
	name "Sphere552"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere552"
	type sphere
	c 1.0154491606 1.68494709107 0.5
	r 0.0510946014208
}

shader {
	name "Sphere553"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere553"
	type sphere
	c 1.26035172188 1.70772535704 0.5
	r 0.0466527877191
}

shader {
	name "Sphere554"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere554"
	type sphere
	c 1.43695657169 1.542426657 0.5
	r 0.0463862606646
}

shader {
	name "Sphere555"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere555"
	type sphere
	c 1.75984689814 1.36747613386 0.5
	r 0.0604786416753
}

shader {
	name "Sphere556"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere556"
	type sphere
	c 2.05324300906 1.17074933855 0.5
	r 0.0641106926128
}

shader {
	name "Sphere557"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere557"
	type sphere
	c 2.36259516701 1.02028604603 0.5
	r 0.0673896276473
}

shader {
	name "Sphere558"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere558"
	type sphere
	c 2.62977399381 0.768251413153 0.5
	r 0.0538626937069
}

shader {
	name "Sphere559"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere559"
	type sphere
	c 2.66274757304 0.593895563048 0.5
	r 0.0675727372624
}

shader {
	name "Sphere560"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere560"
	type sphere
	c 2.70490558473 0.169546964565 0.5
	r 0.0698690878906
}

shader {
	name "Sphere561"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere561"
	type sphere
	c 3.00875319638 -0.288319734598 0.5
	r 0.102244253618
}

shader {
	name "Sphere562"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere562"
	type sphere
	c 3.35435250505 -0.797746126101 0.5
	r 0.0967461659094
}

shader {
	name "Sphere563"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere563"
	type sphere
	c 3.07962385505 -1.47482815101 0.5
	r 0.0775713719868
}

shader {
	name "Sphere564"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere564"
	type sphere
	c 2.93421266949 -1.8290040332 0.5
	r 0.0751927034292
}

shader {
	name "Sphere565"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere565"
	type sphere
	c 2.57849666354 -2.01864942207 0.5
	r 0.0750295335287
}

shader {
	name "Sphere566"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere566"
	type sphere
	c 2.14711912168 -2.19590554814 0.5
	r 0.0752105096618
}

shader {
	name "Sphere567"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere567"
	type sphere
	c 1.80292992 -2.17991333079 0.5
	r 0.0564175095976
}

shader {
	name "Sphere568"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere568"
	type sphere
	c 1.86832928239 -2.56133427133 0.5
	r 0.0998432734641
}

shader {
	name "Sphere569"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere569"
	type sphere
	c 1.18276238557 -2.89760440167 0.5
	r 0.0927365608357
}

shader {
	name "Sphere570"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere570"
	type sphere
	c 0.70402769224 -3.06192804412 0.5
	r 0.0912536818814
}

shader {
	name "Sphere571"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere571"
	type sphere
	c 0.329976712926 -2.7569133212 0.5
	r 0.0796468700239
}

shader {
	name "Sphere572"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere572"
	type sphere
	c 0.0597627306192 -2.47221229002 0.5
	r 0.0757782085506
}

shader {
	name "Sphere573"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere573"
	type sphere
	c -0.470912495351 -2.32200899312 0.5
	r 0.0773222807786
}

shader {
	name "Sphere574"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere574"
	type sphere
	c -1.05192897702 -2.01816166182 0.5
	r 0.0698065820233
}

shader {
	name "Sphere575"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere575"
	type sphere
	c -1.28091585964 -1.68669588113 0.5
	r 0.0524445281306
}

shader {
	name "Sphere576"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere576"
	type sphere
	c -1.65528507207 -1.4265171606 0.5
	r 0.050150246816
}

shader {
	name "Sphere577"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere577"
	type sphere
	c -1.66113425157 -1.1559624297 0.5
	r 0.0521988311307
}

shader {
	name "Sphere578"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere578"
	type sphere
	c -2.02555009357 -1.30513113194 0.5
	r 0.0577355975882
}

shader {
	name "Sphere579"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere579"
	type sphere
	c -2.15665007422 -1.01762646304 0.5
	r 0.0578160763379
}

shader {
	name "Sphere580"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere580"
	type sphere
	c -2.19085922631 -0.82606778706 0.5
	r 0.0476024572393
}

shader {
	name "Sphere581"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere581"
	type sphere
	c -2.49919690203 -0.565100634113 0.5
	r 0.0599398545609
}

shader {
	name "Sphere582"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere582"
	type sphere
	c -2.20733613507 -0.137881088759 0.5
	r 0.0432226943121
}

shader {
	name "Sphere583"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere583"
	type sphere
	c -2.30739220298 0.156370346898 0.5
	r 0.0449999913809
}

shader {
	name "Sphere584"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere584"
	type sphere
	c -2.40420566026 0.413953806703 0.5
	r 0.0600556655699
}

shader {
	name "Sphere585"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere585"
	type sphere
	c -2.38478470005 0.714199037316 0.5
	r 0.0519668685044
}

shader {
	name "Sphere586"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere586"
	type sphere
	c -2.40585903182 1.02604891113 0.5
	r 0.0674507426434
}

shader {
	name "Sphere587"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere587"
	type sphere
	c -2.31123357404 1.39378796839 0.5
	r 0.0771432523723
}

shader {
	name "Sphere588"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere588"
	type sphere
	c -1.91903211591 1.47357301409 0.5
	r 0.0667021927721
}

shader {
	name "Sphere589"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere589"
	type sphere
	c -1.65158950827 1.2036130345 0.5
	r 0.0764382147263
}

shader {
	name "Sphere590"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere590"
	type sphere
	c -1.23355035678 1.52648917887 0.5
	r 0.0442582131781
}

shader {
	name "Sphere591"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere591"
	type sphere
	c -1.17636158367 1.76264077979 0.5
	r 0.0487902692017
}

shader {
	name "Sphere592"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere592"
	type sphere
	c -0.996722206734 2.01135611708 0.5
	r 0.0417396532762
}

shader {
	name "Sphere593"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere593"
	type sphere
	c -0.560766982911 2.03867684283 0.5
	r 0.0478820743338
}

shader {
	name "Sphere594"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere594"
	type sphere
	c -0.206997219191 2.01529570245 0.5
	r 0.0476031272766
}

shader {
	name "Sphere595"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere595"
	type sphere
	c -0.0588444887525 1.98851341923 0.5
	r 0.0417016996744
}

shader {
	name "Sphere596"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere596"
	type sphere
	c 0.193948134961 1.99117044867 0.5
	r 0.0497047377367
}

shader {
	name "Sphere597"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere597"
	type sphere
	c 0.913848031915 1.77083814158 0.5
	r 0.0486865832986
}

shader {
	name "Sphere598"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere598"
	type sphere
	c 1.16564498744 1.78778923277 0.5
	r 0.0463580677326
}

shader {
	name "Sphere599"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere599"
	type sphere
	c 1.34403491175 1.62242809987 0.5
	r 0.0429667152964
}

shader {
	name "Sphere600"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere600"
	type sphere
	c 1.5191273294 1.45617247101 0.5
	r 0.042960802176
}

shader {
	name "Sphere601"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere601"
	type sphere
	c 1.60359010539 1.30801640114 0.5
	r 0.0649119495419
}

shader {
	name "Sphere602"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere602"
	type sphere
	c 1.90033023616 1.44048861318 0.5
	r 0.0582641248417
}

shader {
	name "Sphere603"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere603"
	type sphere
	c 2.19679471714 1.25060256878 0.5
	r 0.05908952082
}

shader {
	name "Sphere604"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere604"
	type sphere
	c 2.62269901924 0.911839462189 0.5
	r 0.0539589900531
}

shader {
	name "Sphere605"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere605"
	type sphere
	c 2.66420899647 0.419276350762 0.5
	r 0.0633962584773
}

shader {
	name "Sphere606"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere606"
	type sphere
	c 3.02162378266 -0.0246764724119 0.5
	r 0.0957236723176
}

shader {
	name "Sphere607"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere607"
	type sphere
	c 3.43564385172 -0.550551980605 0.5
	r 0.0984170762592
}

shader {
	name "Sphere608"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere608"
	type sphere
	c 2.93508675045 -2.03390115733 0.5
	r 0.0784815379589
}

shader {
	name "Sphere609"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere609"
	type sphere
	c 2.74155568377 -2.12110418826 0.5
	r 0.0694018967364
}

shader {
	name "Sphere610"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere610"
	type sphere
	c 2.30097908479 -2.33461814208 0.5
	r 0.0801573296065
}

shader {
	name "Sphere611"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere611"
	type sphere
	c 1.94306828015 -2.216413453 0.5
	r 0.0521927944032
}

shader {
	name "Sphere612"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere612"
	type sphere
	c 1.65562971127 -2.15600902765 0.5
	r 0.0555029154872
}

shader {
	name "Sphere613"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere613"
	type sphere
	c 1.82526723279 -2.80977324847 0.5
	r 0.0892642338758
}

shader {
	name "Sphere614"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere614"
	type sphere
	c 1.39677011432 -3.03418931236 0.5
	r 0.0976729833222
}

shader {
	name "Sphere615"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere615"
	type sphere
	c 0.901921464091 -3.22331822 0.5
	r 0.100266324297
}

shader {
	name "Sphere616"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere616"
	type sphere
	c 0.52970261271 -2.91437923315 0.5
	r 0.0800353583324
}

shader {
	name "Sphere617"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere617"
	type sphere
	c -0.120103575723 -2.38110890173 0.5
	r 0.0754388208372
}

shader {
	name "Sphere618"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere618"
	type sphere
	c -0.911069031352 -2.13679728077 0.5
	r 0.0683155128319
}

shader {
	name "Sphere619"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere619"
	type sphere
	c -1.17174592457 -1.89122991234 0.5
	r 0.0611060628729
}

shader {
	name "Sphere620"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere620"
	type sphere
	c -1.54343821508 -1.5041863966 0.5
	r 0.051977145063
}

shader {
	name "Sphere621"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere621"
	type sphere
	c -1.77142160411 -1.35676330633 0.5
	r 0.0514555011568
}

shader {
	name "Sphere622"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere622"
	type sphere
	c -2.1797988548 -1.29006515399 0.5
	r 0.0585014920965
}

shader {
	name "Sphere623"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere623"
	type sphere
	c -2.58812225364 -0.437052481284 0.5
	r 0.0569833115582
}

shader {
	name "Sphere624"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere624"
	type sphere
	c -2.41578982822 0.0944507504131 0.5
	r 0.048627172905
}

shader {
	name "Sphere625"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere625"
	type sphere
	c -2.52541811585 0.503837257782 0.5
	r 0.0531210346393
}

shader {
	name "Sphere626"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere626"
	type sphere
	c -2.5093494535 0.656037788657 0.5
	r 0.0511386532455
}

shader {
	name "Sphere627"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere627"
	type sphere
	c -2.53687245744 1.15737265782 0.5
	r 0.0716746498171
}

shader {
	name "Sphere628"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere628"
	type sphere
	c -2.11666175944 1.44104540038 0.5
	r 0.0730281295637
}

shader {
	name "Sphere629"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere629"
	type sphere
	c -1.74197422227 1.5266750194 0.5
	r 0.0719348977703
}

shader {
	name "Sphere630"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere630"
	type sphere
	c -1.15137253491 1.4380728326 0.5
	r 0.0462734809467
}

shader {
	name "Sphere631"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere631"
	type sphere
	c -1.32195082944 1.61277753506 0.5
	r 0.0483912997109
}

shader {
	name "Sphere632"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere632"
	type sphere
	c -1.10240723207 2.02926665332 0.5
	r 0.0386543013334
}

shader {
	name "Sphere633"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere633"
	type sphere
	c -0.885300124203 1.99825586619 0.5
	r 0.0424025156409
}

shader {
	name "Sphere634"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere634"
	type sphere
	c -0.680144189009 1.98894552587 0.5
	r 0.0491092561429
}

shader {
	name "Sphere635"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere635"
	type sphere
	c -0.451137044953 2.09994986266 0.5
	r 0.0463111964929
}

shader {
	name "Sphere636"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere636"
	type sphere
	c 0.0461408950069 1.9634260507 0.5
	r 0.039254214937
}

shader {
	name "Sphere637"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere637"
	type sphere
	c 0.324838658088 1.97977346197 0.5
	r 0.0488345891687
}

shader {
	name "Sphere638"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere638"
	type sphere
	c 0.796576560553 1.72535125298 0.5
	r 0.0456515370671
}

shader {
	name "Sphere639"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere639"
	type sphere
	c 1.03533522951 1.81641876355 0.5
	r 0.0486307425335
}

shader {
	name "Sphere640"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere640"
	type sphere
	c 1.28593484475 1.83466772406 0.5
	r 0.0504681891868
}

shader {
	name "Sphere641"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere641"
	type sphere
	c 1.37865531427 1.73325990351 0.5
	r 0.0441181386995
}

shader {
	name "Sphere642"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere642"
	type sphere
	c 1.55306999369 1.56463673392 0.5
	r 0.0422776160574
}

shader {
	name "Sphere643"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere643"
	type sphere
	c 1.76867825587 1.52860838142 0.5
	r 0.0605519192243
}

shader {
	name "Sphere644"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere644"
	type sphere
	c 2.03292819548 1.36681163407 0.5
	r 0.0555050066801
}

shader {
	name "Sphere645"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere645"
	type sphere
	c 2.74691110968 0.8458656977 0.5
	r 0.0515251998467
}

shader {
	name "Sphere646"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere646"
	type sphere
	c 2.81234258854 0.502327244575 0.5
	r 0.0639735546077
}

shader {
	name "Sphere647"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere647"
	type sphere
	c 3.24474876293 -0.158973533492 0.5
	r 0.0995940363203
}

shader {
	name "Sphere648"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere648"
	type sphere
	c 3.60888954801 -0.746838104707 0.5
	r 0.0979373265688
}

shader {
	name "Sphere649"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere649"
	type sphere
	c 3.10395744679 -1.92649408785 0.5
	r 0.071618910888
}

shader {
	name "Sphere650"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere650"
	type sphere
	c 2.58270997624 -2.20640678355 0.5
	r 0.0658239384616
}

shader {
	name "Sphere651"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere651"
	type sphere
	c 2.10257595147 -2.39035737385 0.5
	r 0.0744057617635
}

shader {
	name "Sphere652"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere652"
	type sphere
	c 1.84640140255 -2.32291380879 0.5
	r 0.0556790332044
}

shader {
	name "Sphere653"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere653"
	type sphere
	c 2.05074994731 -2.73479644255 0.5
	r 0.0889518890925
}

shader {
	name "Sphere654"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere654"
	type sphere
	c 1.61042963748 -2.89904225383 0.5
	r 0.0852202441393
}

shader {
	name "Sphere655"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere655"
	type sphere
	c 1.16117649477 -3.15478208368 0.5
	r 0.100824927656
}

shader {
	name "Sphere656"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere656"
	type sphere
	c 0.65027453912 -3.31047926162 0.5
	r 0.0994692819119
}

shader {
	name "Sphere657"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere657"
	type sphere
	c 0.489020242881 -3.11744595111 0.5
	r 0.0752909764473
}

shader {
	name "Sphere658"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere658"
	type sphere
	c -0.106303148691 -2.57599859955 0.5
	r 0.0710944550194
}

shader {
	name "Sphere659"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere659"
	type sphere
	c -1.08343275897 -2.20161133629 0.5
	r 0.0697947346912
}

shader {
	name "Sphere660"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere660"
	type sphere
	c -1.22631724832 -2.04713252501 0.5
	r 0.0627771699759
}

shader {
	name "Sphere661"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere661"
	type sphere
	c -1.66452080199 -1.55510233846 0.5
	r 0.0465370778635
}

shader {
	name "Sphere662"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere662"
	type sphere
	c -2.11482966772 -1.43263043798 0.5
	r 0.0590018853078
}

shader {
	name "Sphere663"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere663"
	type sphere
	c -2.24137992615 -1.15288743486 0.5
	r 0.0542730603172
}

shader {
	name "Sphere664"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere664"
	type sphere
	c -2.65568323772 -0.574108567487 0.5
	r 0.0576191851463
}

shader {
	name "Sphere665"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere665"
	type sphere
	c -2.53687046217 -0.293161069258 0.5
	r 0.0575765421357
}

shader {
	name "Sphere666"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere666"
	type sphere
	c -2.4097862963 -0.0348779803056 0.5
	r 0.0484738269817
}

shader {
	name "Sphere667"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere667"
	type sphere
	c -2.40706851318 0.214214385668 0.5
	r 0.0414333994164
}

shader {
	name "Sphere668"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere668"
	type sphere
	c -2.54453320691 0.366161186387 0.5
	r 0.0511265031224
}

shader {
	name "Sphere669"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere669"
	type sphere
	c -2.49846993798 0.792597131645 0.5
	r 0.0516053739955
}

shader {
	name "Sphere670"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere670"
	type sphere
	c -2.57861643212 0.976889880731 0.5
	r 0.067260886096
}

shader {
	name "Sphere671"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere671"
	type sphere
	c -2.250758303 1.59280815777 0.5
	r 0.0788608837275
}

shader {
	name "Sphere672"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere672"
	type sphere
	c -1.88148854651 1.6464258726 0.5
	r 0.0659601305967
}

shader {
	name "Sphere673"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere673"
	type sphere
	c -1.61199117283 1.39250289104 0.5
	r 0.068172154723
}

shader {
	name "Sphere674"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere674"
	type sphere
	c -1.27086163521 1.41308170233 0.5
	r 0.0452824497586
}

shader {
	name "Sphere675"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere675"
	type sphere
	c -1.17756336563 1.95856783726 0.5
	r 0.0387330777401
}

shader {
	name "Sphere676"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere676"
	type sphere
	c -1.03901728813 2.10585661083 0.5
	r 0.0359105862028
}

shader {
	name "Sphere677"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere677"
	type sphere
	c -0.930856714492 2.09857659953 0.5
	r 0.0402325526205
}

shader {
	name "Sphere678"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere678"
	type sphere
	c -0.661566533162 2.11671685552 0.5
	r 0.0477268740595
}

shader {
	name "Sphere679"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere679"
	type sphere
	c -0.340378770521 2.04827743268 0.5
	r 0.045352904433
}

shader {
	name "Sphere680"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere680"
	type sphere
	c 0.0169654891849 2.06018903253 0.5
	r 0.0365450720895
}

shader {
	name "Sphere681"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere681"
	type sphere
	c 0.270141224315 2.09579087335 0.5
	r 0.0473639818432
}

shader {
	name "Sphere682"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere682"
	type sphere
	c 0.81079157177 1.85117257271 0.5
	r 0.0493147857031
}

shader {
	name "Sphere683"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere683"
	type sphere
	c 0.935861023715 1.89706737208 0.5
	r 0.0474141171291
}

shader {
	name "Sphere684"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere684"
	type sphere
	c 1.18018957822 1.91316355406 0.5
	r 0.0483032991363
}

shader {
	name "Sphere685"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere685"
	type sphere
	c 1.48239580189 1.64692626637 0.5
	r 0.0390771920511
}

shader {
	name "Sphere686"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere686"
	type sphere
	c 1.62481993668 1.48355339785 0.5
	r 0.0389254686113
}

shader {
	name "Sphere687"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere687"
	type sphere
	c 1.91558683964 1.60008424018 0.5
	r 0.0619782743397
}

shader {
	name "Sphere688"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere688"
	type sphere
	c 2.74099895299 0.978062915732 0.5
	r 0.0477218159987
}

shader {
	name "Sphere689"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere689"
	type sphere
	c 2.82085260316 0.675023382335 0.5
	r 0.0657057100977
}

shader {
	name "Sphere690"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere690"
	type sphere
	c 2.8071435645 0.336431170188 0.5
	r 0.0605095858502
}

shader {
	name "Sphere691"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere691"
	type sphere
	c 3.24413638222 0.102457277148 0.5
	r 0.0964796095786
}

shader {
	name "Sphere692"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere692"
	type sphere
	c 3.69414316587 -0.497852448717 0.5
	r 0.0994452851009
}

shader {
	name "Sphere693"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere693"
	type sphere
	c 3.52355485129 -0.98997281928 0.5
	r 0.0953190606223
}

shader {
	name "Sphere694"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere694"
	type sphere
	c 3.11096075813 -1.72762251017 0.5
	r 0.077627227465
}

shader {
	name "Sphere695"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere695"
	type sphere
	c 3.11422889242 -2.1128136185 0.5
	r 0.0683329180746
}

shader {
	name "Sphere696"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere696"
	type sphere
	c 2.73499819483 -2.30987118303 0.5
	r 0.0722587476655
}

shader {
	name "Sphere697"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere697"
	type sphere
	c 2.24172429767 -2.53258043847 0.5
	r 0.0748228718103
}

shader {
	name "Sphere698"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere698"
	type sphere
	c 2.00294782646 -2.96626691938 0.5
	r 0.0883142631382
}

shader {
	name "Sphere699"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere699"
	type sphere
	c 1.39293907599 -3.30753258494 0.5
	r 0.107354605321
}

shader {
	name "Sphere700"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere700"
	type sphere
	c 0.852506738313 -3.4908123219 0.5
	r 0.103748716061
}

shader {
	name "Sphere701"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere701"
	type sphere
	c 0.332128836552 -2.98686315079 0.5
	r 0.0778023427393
}

shader {
	name "Sphere702"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere702"
	type sphere
	c 0.0597905935456 -2.66864050312 0.5
	r 0.0715429527572
}

shader {
	name "Sphere703"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere703"
	type sphere
	c -0.286209377549 -2.49673378354 0.5
	r 0.0763509713584
}

shader {
	name "Sphere704"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere704"
	type sphere
	c -0.937316994982 -2.32284251677 0.5
	r 0.0726002574219
}

shader {
	name "Sphere705"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere705"
	type sphere
	c -1.33158317901 -1.92044541722 0.5
	r 0.0607579604031
}

shader {
	name "Sphere706"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere706"
	type sphere
	c -1.56906448118 -1.63052299635 0.5
	r 0.0447049297904
}

shader {
	name "Sphere707"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere707"
	type sphere
	c -1.76564881771 -1.48785479619 0.5
	r 0.044547349851
}

shader {
	name "Sphere708"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere708"
	type sphere
	c -1.95266093324 -1.44903149519 0.5
	r 0.0632451080327
}

shader {
	name "Sphere709"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere709"
	type sphere
	c -2.26718033383 -1.41525655868 0.5
	r 0.0560017000455
}

shader {
	name "Sphere710"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere710"
	type sphere
	c -2.32256581755 -1.26590897519 0.5
	r 0.0500956244767
}

shader {
	name "Sphere711"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere711"
	type sphere
	c -2.57255013599 -0.709724211942 0.5
	r 0.0616820199529
}

shader {
	name "Sphere712"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere712"
	type sphere
	c -2.73889011239 -0.446975003711 0.5
	r 0.0563372054386
}

shader {
	name "Sphere713"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere713"
	type sphere
	c -2.52968255057 0.0241486231675 0.5
	r 0.0517550565005
}

shader {
	name "Sphere714"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere714"
	type sphere
	c -2.5147304422 0.171515044914 0.5
	r 0.0454317697994
}

shader {
	name "Sphere715"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere715"
	type sphere
	c -2.31023682202 0.275905699055 0.5
	r 0.0446769044924
}

shader {
	name "Sphere716"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere716"
	type sphere
	c -2.65033883517 0.448402141316 0.5
	r 0.0493802288465
}

shader {
	name "Sphere717"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere717"
	type sphere
	c -2.61916797071 0.73288772593 0.5
	r 0.0493893827128
}

shader {
	name "Sphere718"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere718"
	type sphere
	c -2.71024926616 1.09650860873 0.5
	r 0.0661376211461
}

shader {
	name "Sphere719"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere719"
	type sphere
	c -2.44490531051 1.54080470737 0.5
	r 0.0718824358564
}

shader {
	name "Sphere720"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere720"
	type sphere
	c -1.71113163238 1.71626627674 0.5
	r 0.0721278038377
}

shader {
	name "Sphere721"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere721"
	type sphere
	c -1.56068408304 1.56541842112 0.5
	r 0.0671029774271
}

shader {
	name "Sphere722"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere722"
	type sphere
	c -1.19167269506 1.32636446146 0.5
	r 0.042793126089
}

shader {
	name "Sphere723"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere723"
	type sphere
	c -1.19947233992 2.05730492065 0.5
	r 0.0371208662529
}

shader {
	name "Sphere724"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere724"
	type sphere
	c -0.824876198561 2.089309045 0.5
	r 0.0395561589533
}

shader {
	name "Sphere725"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere725"
	type sphere
	c -0.350990554812 2.16710531003 0.5
	r 0.0441226751993
}

shader {
	name "Sphere726"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere726"
	type sphere
	c -0.0742121966461 2.09023545075 0.5
	r 0.0354555436939
}

shader {
	name "Sphere727"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere727"
	type sphere
	c 0.147386113371 2.10886516521 0.5
	r 0.0452230681875
}

shader {
	name "Sphere728"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere728"
	type sphere
	c 0.397602475006 2.0871568349 0.5
	r 0.048451026581
}

shader {
	name "Sphere729"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere729"
	type sphere
	c 1.29735711735 1.9652991548 0.5
	r 0.0478792024559
}

shader {
	name "Sphere730"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere730"
	type sphere
	c 1.58123697385 1.66564916837 0.5
	r 0.036371929466
}

shader {
	name "Sphere731"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere731"
	type sphere
	c 1.77929092257 1.68920082667 0.5
	r 0.0601551278776
}

shader {
	name "Sphere732"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere732"
	type sphere
	c 2.63091626224 1.05319515628 0.5
	r 0.0522367602199
}

shader {
	name "Sphere733"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere733"
	type sphere
	c 2.85459482602 0.921871242535 0.5
	r 0.047328742441
}

shader {
	name "Sphere734"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere734"
	type sphere
	c 2.95792192707 0.579492290699 0.5
	r 0.0596008393218
}

shader {
	name "Sphere735"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere735"
	type sphere
	c 2.94317201581 0.410817029574 0.5
	r 0.0557694322472
}

shader {
	name "Sphere736"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere736"
	type sphere
	c 3.02735187615 0.221631200831 0.5
	r 0.089057030236
}

shader {
	name "Sphere737"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere737"
	type sphere
	c 3.47013679836 -0.0235861358159 0.5
	r 0.0975996542618
}

shader {
	name "Sphere738"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere738"
	type sphere
	c 3.51786236838 -0.300375694451 0.5
	r 0.0990880704645
}

shader {
	name "Sphere739"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere739"
	type sphere
	c 3.86040632497 -0.695950303613 0.5
	r 0.0945224608809
}

shader {
	name "Sphere740"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere740"
	type sphere
	c 3.76845468975 -0.94298997076 0.5
	r 0.0917053145277
}

shader {
	name "Sphere741"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere741"
	type sphere
	c 3.28148214707 -1.84128028142 0.5
	r 0.0760690431225
}

shader {
	name "Sphere742"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere742"
	type sphere
	c 2.9688045853 -2.23374411056 0.5
	r 0.0735190551869
}

shader {
	name "Sphere743"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere743"
	type sphere
	c 2.56446865476 -2.38206361569 0.5
	r 0.066627141274
}

shader {
	name "Sphere744"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere744"
	type sphere
	c 2.23900034289 -2.89525107912 0.5
	r 0.0965634600883
}

shader {
	name "Sphere745"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere745"
	type sphere
	c 1.63143049709 -3.16126916163 0.5
	r 0.102472752642
}

shader {
	name "Sphere746"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere746"
	type sphere
	c 1.13963604604 -3.42401944143 0.5
	r 0.10174831707
}

shader {
	name "Sphere747"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere747"
	type sphere
	c 0.596284431252 -3.56622693505 0.5
	r 0.0965690175842
}

shader {
	name "Sphere748"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere748"
	type sphere
	c 0.300119951548 -3.19009521727 0.5
	r 0.0765006412923
}

shader {
	name "Sphere749"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere749"
	type sphere
	c -0.107816817875 -2.77265320065 0.5
	r 0.0764008648097
}

shader {
	name "Sphere750"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere750"
	type sphere
	c -0.772359767268 -2.24573734135 0.5
	r 0.0639658564809
}

shader {
	name "Sphere751"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere751"
	type sphere
	c -1.11701376587 -2.38494631399 0.5
	r 0.069994075364
}

shader {
	name "Sphere752"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere752"
	type sphere
	c -1.38711967676 -2.07024456753 0.5
	r 0.059063988794
}

shader {
	name "Sphere753"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere753"
	type sphere
	c -1.45864646219 -1.59639517548 0.5
	r 0.0419739400634
}

shader {
	name "Sphere754"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere754"
	type sphere
	c -1.67787671673 -1.67395825393 0.5
	r 0.0431658979414
}

shader {
	name "Sphere755"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere755"
	type sphere
	c -2.05260840872 -1.57330625 0.5
	r 0.0563645207717
}

shader {
	name "Sphere756"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere756"
	type sphere
	c -2.20934518511 -1.55045067113 0.5
	r 0.0542823571138
}

shader {
	name "Sphere757"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere757"
	type sphere
	c -2.37828402387 -1.14683199851 0.5
	r 0.0485054036643
}

shader {
	name "Sphere758"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere758"
	type sphere
	c -2.73489966183 -0.709580189523 0.5
	r 0.0600801723404
}

shader {
	name "Sphere759"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere759"
	type sphere
	c -2.51549525911 -0.10800433585 0.5
	r 0.0479291807013
}

shader {
	name "Sphere760"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere760"
	type sphere
	c -2.67329420807 0.313592240229 0.5
	r 0.053182534616
}

shader {
	name "Sphere761"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere761"
	type sphere
	c -2.63852905636 0.578298714025 0.5
	r 0.0484440122361
}

shader {
	name "Sphere762"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere762"
	type sphere
	c -2.75196013022 0.920644647742 0.5
	r 0.0694194149583
}

shader {
	name "Sphere763"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere763"
	type sphere
	c -2.68046865633 1.26754176091 0.5
	r 0.064067269025
}

shader {
	name "Sphere764"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere764"
	type sphere
	c -2.50374773104 1.36216704346 0.5
	r 0.0691770836756
}

shader {
	name "Sphere765"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere765"
	type sphere
	c -2.39871652114 1.72241564301 0.5
	r 0.0686619134328
}

shader {
	name "Sphere766"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere766"
	type sphere
	c -1.8605229595 1.81722928193 0.5
	r 0.0631038662028
}

shader {
	name "Sphere767"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere767"
	type sphere
	c -1.44223793756 1.43764599839 0.5
	r 0.063567775929
}

shader {
	name "Sphere768"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere768"
	type sphere
	c -1.30492570042 1.29792632194 0.5
	r 0.0447835328421
}

shader {
	name "Sphere769"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere769"
	type sphere
	c -1.27415459624 1.99113004168 0.5
	r 0.0377160339624
}

shader {
	name "Sphere770"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere770"
	type sphere
	c -0.868489283072 2.19041747522 0.5
	r 0.0430290781542
}

shader {
	name "Sphere771"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere771"
	type sphere
	c -0.456421070833 2.22129411466 0.5
	r 0.0447832379538
}

shader {
	name "Sphere772"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere772"
	type sphere
	c -0.00320367852663 2.15710062121 0.5
	r 0.0376960309645
}

shader {
	name "Sphere773"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere773"
	type sphere
	c 0.217276225853 2.20927502413 0.5
	r 0.0465309876925
}

shader {
	name "Sphere774"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere774"
	type sphere
	c 0.450181875641 1.97378068186 0.5
	r 0.0452802078884
}

shader {
	name "Sphere775"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere775"
	type sphere
	c 1.19374571955 2.04182482701 0.5
	r 0.0487267957809
}

shader {
	name "Sphere776"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere776"
	type sphere
	c 1.39789806791 1.89399563235 0.5
	r 0.0445647249742
}

shader {
	name "Sphere777"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere777"
	type sphere
	c 1.51907891418 1.74299460362 0.5
	r 0.0380481059012
}

shader {
	name "Sphere778"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere778"
	type sphere
	c 1.65566610339 1.59857859856 0.5
	r 0.0387710217693
}

shader {
	name "Sphere779"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere779"
	type sphere
	c 1.92582474538 1.76911270228 0.5
	r 0.0650253972166
}

shader {
	name "Sphere780"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere780"
	type sphere
	c 2.75698130296 1.10889037177 0.5
	r 0.0511282373879
}

shader {
	name "Sphere781"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere781"
	type sphere
	c 2.97251304169 0.733039013025 0.5
	r 0.0560779911388
}

shader {
	name "Sphere782"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere782"
	type sphere
	c 3.23201422446 0.357999699725 0.5
	r 0.0953927255834
}

shader {
	name "Sphere783"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere783"
	type sphere
	c 3.77569871006 -0.246996635486 0.5
	r 0.0983897965285
}

shader {
	name "Sphere784"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere784"
	type sphere
	c 3.96077451607 -0.451747277022 0.5
	r 0.103495850745
}

shader {
	name "Sphere785"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere785"
	type sphere
	c 3.69146709779 -1.17786024643 0.5
	r 0.0936693434967
}

shader {
	name "Sphere786"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere786"
	type sphere
	c 3.29694812401 -1.63709268449 0.5
	r 0.0775103216714
}

shader {
	name "Sphere787"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere787"
	type sphere
	c 3.14704038644 -2.28969156572 0.5
	r 0.0665887307575
}

shader {
	name "Sphere788"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere788"
	type sphere
	c 2.70689392462 -2.50065666009 0.5
	r 0.0723745244328
}

shader {
	name "Sphere789"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere789"
	type sphere
	c 2.17032224791 -3.13213741755 0.5
	r 0.0884173434106
}

shader {
	name "Sphere790"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere790"
	type sphere
	c 1.64245548895 -3.43450087097 0.5
	r 0.10261778482
}

shader {
	name "Sphere791"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere791"
	type sphere
	c 1.35538226929 -3.57671540676 0.5
	r 0.096488034298
}

shader {
	name "Sphere792"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere792"
	type sphere
	c 0.780803083164 -3.75420901605 0.5
	r 0.100987866806
}

shader {
	name "Sphere793"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere793"
	type sphere
	c 0.132463129969 -3.06136525469 0.5
	r 0.082032067832
}

shader {
	name "Sphere794"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere794"
	type sphere
	c -0.780211056124 -2.41742521058 0.5
	r 0.0649346149585
}

shader {
	name "Sphere795"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere795"
	type sphere
	c -0.974267197663 -2.51796963558 0.5
	r 0.0763458716307
}

shader {
	name "Sphere796"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere796"
	type sphere
	c -1.26647092926 -2.26254778917 0.5
	r 0.0748915655489
}

shader {
	name "Sphere797"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere797"
	type sphere
	c -1.48242903462 -1.95202191276 0.5
	r 0.0548285669831
}

shader {
	name "Sphere798"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere798"
	type sphere
	c -1.48033133194 -1.70944749827 0.5
	r 0.044361000489
}

shader {
	name "Sphere799"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere799"
	type sphere
	c -1.77525726872 -1.60738329639 0.5
	r 0.0453061216069
}

shader {
	name "Sphere800"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere800"
	type sphere
	c -2.35572304519 -1.53561659661 0.5
	r 0.0560633352601
}

shader {
	name "Sphere801"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere801"
	type sphere
	c -2.45854464562 -1.25455079778 0.5
	r 0.052243654667
}

shader {
	name "Sphere802"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere802"
	type sphere
	c -2.31224371631 -1.0400095834 0.5
	r 0.045685610817
}

shader {
	name "Sphere803"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere803"
	type sphere
	c -2.65600030573 -0.851448537948 0.5
	r 0.0616689626917
}

shader {
	name "Sphere804"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere804"
	type sphere
	c -2.63791521065 -0.0594901807427 0.5
	r 0.050832657206
}

shader {
	name "Sphere805"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere805"
	type sphere
	c -2.77618844731 0.405567130734 0.5
	r 0.0503245438171
}

shader {
	name "Sphere806"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere806"
	type sphere
	c -2.87419536061 1.04683120835 0.5
	r 0.0623427990477
}

shader {
	name "Sphere807"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere807"
	type sphere
	c -2.62192391503 1.49645527655 0.5
	r 0.0649847728857
}

shader {
	name "Sphere808"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere808"
	type sphere
	c -2.58067985342 1.67650299921 0.5
	r 0.0720877815909
}

shader {
	name "Sphere809"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere809"
	type sphere
	c -2.22291378862 1.79450175662 0.5
	r 0.0738440243432
}

shader {
	name "Sphere810"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere810"
	type sphere
	c -2.00959661698 1.75250525044 0.5
	r 0.0587847613567
}

shader {
	name "Sphere811"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere811"
	type sphere
	c -1.71443366268 1.89269886472 0.5
	r 0.0602198098373
}

shader {
	name "Sphere812"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere812"
	type sphere
	c -1.22123731176 1.21522903214 0.5
	r 0.0434573637229
}

shader {
	name "Sphere813"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere813"
	type sphere
	c -1.25697761205 1.88696467248 0.5
	r 0.0414630574791
}

shader {
	name "Sphere814"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere814"
	type sphere
	c -1.29398633936 2.08994427367 0.5
	r 0.0378724714119
}

shader {
	name "Sphere815"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere815"
	type sphere
	c -0.975905007411 2.19197897541 0.5
	r 0.0375412269618
}

shader {
	name "Sphere816"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere816"
	type sphere
	c -0.353997967027 2.28892428166 0.5
	r 0.0472693914033
}

shader {
	name "Sphere817"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere817"
	type sphere
	c -0.0954975026205 2.1797971036 0.5
	r 0.0335866468523
}

shader {
	name "Sphere818"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere818"
	type sphere
	c 0.338330386531 2.19780660699 0.5
	r 0.0446661578494
}

shader {
	name "Sphere819"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere819"
	type sphere
	c 0.522691570149 2.07166669961 0.5
	r 0.0460823782742
}

shader {
	name "Sphere820"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere820"
	type sphere
	c 1.06965831072 1.98926406775 0.5
	r 0.0523433735363
}

shader {
	name "Sphere821"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere821"
	type sphere
	c 1.30964028798 2.08849791311 0.5
	r 0.0449779771772
}

shader {
	name "Sphere822"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere822"
	type sphere
	c 1.41123824596 2.01185283879 0.5
	r 0.0443926149241
}

shader {
	name "Sphere823"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere823"
	type sphere
	c 1.6174455919 1.75556394891 0.5
	r 0.0363267577713
}

shader {
	name "Sphere824"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere824"
	type sphere
	c 1.7791004082 1.85048518491 0.5
	r 0.0608082251882
}

shader {
	name "Sphere825"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere825"
	type sphere
	c 2.066074725 1.67173848547 0.5
	r 0.0630288281007
}

shader {
	name "Sphere826"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere826"
	type sphere
	c 2.64987143015 1.18430698318 0.5
	r 0.0471194442554
}

shader {
	name "Sphere827"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere827"
	type sphere
	c 3.1001284861 0.648205031093 0.5
	r 0.0588520297596
}

shader {
	name "Sphere828"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere828"
	type sphere
	c 3.45527167607 0.241962623071 0.5
	r 0.0933161169019
}

shader {
	name "Sphere829"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere829"
	type sphere
	c 4.10701303351 -0.667037225757 0.5
	r 0.0916994351364
}

shader {
	name "Sphere830"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere830"
	type sphere
	c 3.92680545282 -1.12226679388 0.5
	r 0.0876923393116
}

shader {
	name "Sphere831"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere831"
	type sphere
	c 3.45031086546 -1.22729881187 0.5
	r 0.0909594227622
}

shader {
	name "Sphere832"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere832"
	type sphere
	c 3.46158156416 -1.75413424614 0.5
	r 0.0739876302372
}

shader {
	name "Sphere833"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere833"
	type sphere
	c 3.28132771048 -2.17563031805 0.5
	r 0.0655540619334
}

shader {
	name "Sphere834"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere834"
	type sphere
	c 3.01944523489 -2.4145453045 0.5
	r 0.0673004045992
}

shader {
	name "Sphere835"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere835"
	type sphere
	c 2.52442949666 -2.56276182704 0.5
	r 0.0721836111751
}

shader {
	name "Sphere836"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere836"
	type sphere
	c 2.40568698226 -3.08324671587 0.5
	r 0.0918743871975
}

shader {
	name "Sphere837"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere837"
	type sphere
	c 1.93867509279 -3.19830408123 0.5
	r 0.0922664077131
}

shader {
	name "Sphere838"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere838"
	type sphere
	c 1.11709524257 -3.69705377428 0.5
	r 0.103724082628
}

shader {
	name "Sphere839"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere839"
	type sphere
	c 0.518929868167 -3.81834886456 0.5
	r 0.101222343758
}

shader {
	name "Sphere840"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere840"
	type sphere
	c 0.106544577044 -3.2811306118 0.5
	r 0.0839342789323
}

shader {
	name "Sphere841"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere841"
	type sphere
	c -1.16883921558 -2.57109044083 0.5
	r 0.0749239227307
}

shader {
	name "Sphere842"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere842"
	type sphere
	c -1.54165709483 -2.08999346635 0.5
	r 0.0577816608094
}

shader {
	name "Sphere843"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere843"
	type sphere
	c -1.78420720198 -1.73019941009 0.5
	r 0.047050216768
}

shader {
	name "Sphere844"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere844"
	type sphere
	c -2.29233504223 -1.66222111278 0.5
	r 0.0501265541758
}

shader {
	name "Sphere845"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere845"
	type sphere
	c -2.50930171281 -1.12672304417 0.5
	r 0.0509085175614
}

shader {
	name "Sphere846"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere846"
	type sphere
	c -2.48755937825 -0.855219941833 0.5
	r 0.0646933947004
}

shader {
	name "Sphere847"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere847"
	type sphere
	c -2.81281327197 -0.843456591792 0.5
	r 0.0560934034941
}

shader {
	name "Sphere848"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere848"
	type sphere
	c -2.65988657428 0.0787234571741 0.5
	r 0.0541291676202
}

shader {
	name "Sphere849"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere849"
	type sphere
	c -2.80602497575 0.274302126847 0.5
	r 0.0506353730656
}

shader {
	name "Sphere850"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere850"
	type sphere
	c -2.92573712928 0.887482038519 0.5
	r 0.0632653233445
}

shader {
	name "Sphere851"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere851"
	type sphere
	c -2.52522772525 1.85902294636 0.5
	r 0.0709804334858
}

shader {
	name "Sphere852"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere852"
	type sphere
	c -1.99281280634 1.90406180728 0.5
	r 0.0555775401223
}

shader {
	name "Sphere853"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere853"
	type sphere
	c -1.85061233272 1.9856746495 0.5
	r 0.0634486331321
}

shader {
	name "Sphere854"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere854"
	type sphere
	c -1.57462258498 1.82188620769 0.5
	r 0.0573211746583
}

shader {
	name "Sphere855"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere855"
	type sphere
	c -1.32937356852 1.18708302608 0.5
	r 0.0403470324718
}

shader {
	name "Sphere856"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere856"
	type sphere
	c -1.3567201428 1.92908918922 0.5
	r 0.0397417092227
}

shader {
	name "Sphere857"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere857"
	type sphere
	c -1.21840997167 2.15262980259 0.5
	r 0.0357699781337
}

shader {
	name "Sphere858"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere858"
	type sphere
	c -0.927891351869 2.2779131635 0.5
	r 0.0362871052515
}

shader {
	name "Sphere859"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere859"
	type sphere
	c -0.463978985546 2.33828564115 0.5
	r 0.0431433131118
}

shader {
	name "Sphere860"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere860"
	type sphere
	c -0.249809361044 2.22643779402 0.5
	r 0.0438481291396
}

shader {
	name "Sphere861"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere861"
	type sphere
	c -0.160708283855 2.11949474522 0.5
	r 0.0330276270208
}

shader {
	name "Sphere862"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere862"
	type sphere
	c -0.0361786819679 2.24372657805 0.5
	r 0.0318213523187
}

shader {
	name "Sphere863"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere863"
	type sphere
	c 0.289498340565 2.30180747844 0.5
	r 0.0415047297004
}

shader {
	name "Sphere864"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere864"
	type sphere
	c 0.476803086381 2.18808164098 0.5
	r 0.0477671434496
}

shader {
	name "Sphere865"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere865"
	type sphere
	c 0.56824928067 1.96081684368 0.5
	r 0.0438025342235
}

shader {
	name "Sphere866"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere866"
	type sphere
	c 1.08968356349 2.12732028194 0.5
	r 0.052282376533
}

shader {
	name "Sphere867"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere867"
	type sphere
	c 1.50597792095 1.94167551972 0.5
	r 0.0440325508857
}

shader {
	name "Sphere868"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere868"
	type sphere
	c 1.55998895736 1.8316434614 0.5
	r 0.0351768320267
}

shader {
	name "Sphere869"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere869"
	type sphere
	c 1.91720401455 1.93802864277 0.5
	r 0.0618264375095
}

shader {
	name "Sphere870"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere870"
	type sphere
	c 2.08441652674 1.84309812317 0.5
	r 0.0662250219657
}

shader {
	name "Sphere871"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere871"
	type sphere
	c 2.5278213429 1.14192702284 0.5
	r 0.0497795248832
}

shader {
	name "Sphere872"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere872"
	type sphere
	c 2.76086694726 1.23707813578 0.5
	r 0.0450567437932
}

shader {
	name "Sphere873"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere873"
	type sphere
	c 3.10533637744 0.801028202198 0.5
	r 0.05583188199
}

shader {
	name "Sphere874"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere874"
	type sphere
	c 3.44158106916 0.482630879346 0.5
	r 0.0874768898524
}

shader {
	name "Sphere875"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere875"
	type sphere
	c 4.23234126444 -0.44386799796 0.5
	r 0.100264921472
}

shader {
	name "Sphere876"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere876"
	type sphere
	c 4.00429055206 -0.901321918663 0.5
	r 0.0879111213574
}

shader {
	name "Sphere877"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere877"
	type sphere
	c 3.86624306862 -1.35654861068 0.5
	r 0.0937949103398
}

shader {
	name "Sphere878"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere878"
	type sphere
	c 3.60977250283 -1.41011087098 0.5
	r 0.0909805338065
}

shader {
	name "Sphere879"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere879"
	type sphere
	c 3.44778841326 -1.94903559715 0.5
	r 0.0725539783503
}

shader {
	name "Sphere880"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere880"
	type sphere
	c 3.31231424546 -2.34608841602 0.5
	r 0.0643846631998
}

shader {
	name "Sphere881"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere881"
	type sphere
	c 2.66946079471 -2.69056330153 0.5
	r 0.0727960530561
}

shader {
	name "Sphere882"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere882"
	type sphere
	c 2.48515267727 -2.85309542837 0.5
	r 0.0907385412854
}

shader {
	name "Sphere883"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere883"
	type sphere
	c 2.32616599343 -3.31421779041 0.5
	r 0.0913333201475
}

shader {
	name "Sphere884"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere884"
	type sphere
	c 1.34306374329 -3.82786634582 0.5
	r 0.0921016099152
}

shader {
	name "Sphere885"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere885"
	type sphere
	c 0.70286467565 -4.00139839957 0.5
	r 0.0934010603838
}

shader {
	name "Sphere886"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere886"
	type sphere
	c 0.33151863826 -3.61621372423 0.5
	r 0.105513335382
}

shader {
	name "Sphere887"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere887"
	type sphere
	c -0.077835963585 -3.14534615466 0.5
	r 0.087803606935
}

shader {
	name "Sphere888"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere888"
	type sphere
	c -1.0296125235 -2.70508165124 0.5
	r 0.0699983508993
}

shader {
	name "Sphere889"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere889"
	type sphere
	c -1.4493810158 -2.21078750096 0.5
	r 0.0562234547665
}

shader {
	name "Sphere890"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere890"
	type sphere
	c -1.63170255407 -1.96530756412 0.5
	r 0.0575691168425
}

shader {
	name "Sphere891"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere891"
	type sphere
	c -1.67939899379 -1.7888925296 0.5
	r 0.0430423693076
}

shader {
	name "Sphere892"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere892"
	type sphere
	c -1.88697272437 -1.65862724798 0.5
	r 0.0468746011817
}

shader {
	name "Sphere893"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere893"
	type sphere
	c -2.15739370175 -1.68262326575 0.5
	r 0.0522296617308
}

shader {
	name "Sphere894"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere894"
	type sphere
	c -2.42373751602 -1.65730950589 0.5
	r 0.0484941225349
}

shader {
	name "Sphere895"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere895"
	type sphere
	c -2.5918722203 -1.2316290498 0.5
	r 0.0492190349987
}

shader {
	name "Sphere896"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere896"
	type sphere
	c -2.57875921436 -0.99169643905 0.5
	r 0.0584145862541
}

shader {
	name "Sphere897"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere897"
	type sphere
	c -2.74845820462 -0.979614728362 0.5
	r 0.056857226104
}

shader {
	name "Sphere898"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere898"
	type sphere
	c -2.89621730957 -0.711606871027 0.5
	r 0.0609176112644
}

shader {
	name "Sphere899"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere899"
	type sphere
	c -2.76777911165 -0.0137296357753 0.5
	r 0.0524351809391
}

shader {
	name "Sphere900"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere900"
	type sphere
	c -2.89902783976 0.364874313408 0.5
	r 0.0467285329922
}

shader {
	name "Sphere901"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere901"
	type sphere
	c -2.81939486097 0.760038008031 0.5
	r 0.0612226104102
}

shader {
	name "Sphere902"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere902"
	type sphere
	c -3.03863732851 1.01331022485 0.5
	r 0.0635250270308
}

shader {
	name "Sphere903"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere903"
	type sphere
	c -2.70335869207 1.81494848341 0.5
	r 0.0666465071499
}

shader {
	name "Sphere904"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere904"
	type sphere
	c -1.69774970136 2.05566643489 0.5
	r 0.062644711956
}

shader {
	name "Sphere905"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere905"
	type sphere
	c -1.25463700607 1.1050969739 0.5
	r 0.0428565576962
}

shader {
	name "Sphere906"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere906"
	type sphere
	c -1.40783872545 1.25674969959 0.5
	r 0.0383501864489
}

shader {
	name "Sphere907"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere907"
	type sphere
	c -1.34339164717 1.82716401523 0.5
	r 0.0373530007936
}

shader {
	name "Sphere908"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere908"
	type sphere
	c -1.3079343617 2.18803032831 0.5
	r 0.0364321351807
}

shader {
	name "Sphere909"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere909"
	type sphere
	c -1.02206487726 2.27599915589 0.5
	r 0.0343576250853
}

shader {
	name "Sphere910"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere910"
	type sphere
	c -0.828058191017 2.292608166 0.5
	r 0.0393945586185
}

shader {
	name "Sphere911"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere911"
	type sphere
	c -0.558044266439 2.27560202322 0.5
	r 0.0416349333724
}

shader {
	name "Sphere912"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere912"
	type sphere
	c -0.371133018409 2.41142977946 0.5
	r 0.0455041442833
}

shader {
	name "Sphere913"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere913"
	type sphere
	c -0.244985999882 2.34383989925 0.5
	r 0.0442777297693
}

shader {
	name "Sphere914"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere914"
	type sphere
	c -0.118599170896 2.26388503358 0.5
	r 0.0318160496744
}

shader {
	name "Sphere915"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere915"
	type sphere
	c 0.0521491118492 2.23613069858 0.5
	r 0.0346689989126
}

shader {
	name "Sphere916"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere916"
	type sphere
	c 0.180427167374 2.32074743877 0.5
	r 0.0415228207977
}

shader {
	name "Sphere917"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere917"
	type sphere
	c 0.401822271391 2.2957275451 0.5
	r 0.0428615399332
}

shader {
	name "Sphere918"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere918"
	type sphere
	c 0.597178407195 2.16593951939 0.5
	r 0.0440289698544
}

shader {
	name "Sphere919"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere919"
	type sphere
	c 0.966377241659 2.07480456632 0.5
	r 0.0482353907129
}

shader {
	name "Sphere920"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere920"
	type sphere
	c 1.51727526728 2.05518313526 0.5
	r 0.041518778509
}

shader {
	name "Sphere921"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere921"
	type sphere
	c 1.77191280501 2.0120099699 0.5
	r 0.0604552432008
}

shader {
	name "Sphere922"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere922"
	type sphere
	c 2.22621462385 1.7369063615 0.5
	r 0.0666401623679
}

shader {
	name "Sphere923"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere923"
	type sphere
	c 2.55570435889 1.2693289689 0.5
	r 0.0480335832519
}

shader {
	name "Sphere924"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere924"
	type sphere
	c 2.86681542791 1.17764128393 0.5
	r 0.0460545820603
}

shader {
	name "Sphere925"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere925"
	type sphere
	c 3.2259710479 0.724238024898 0.5
	r 0.05141931131
}

shader {
	name "Sphere926"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere926"
	type sphere
	c 3.64284334634 0.380779342424 0.5
	r 0.0816979749499
}

shader {
	name "Sphere927"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere927"
	type sphere
	c 4.09412852465 -0.218230790456 0.5
	r 0.0981875598759
}

shader {
	name "Sphere928"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere928"
	type sphere
	c 4.35858476515 -0.67471243255 0.5
	r 0.0970671543034
}

shader {
	name "Sphere929"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere929"
	type sphere
	c 4.15411167978 -1.07822928972 0.5
	r 0.085957236572
}

shader {
	name "Sphere930"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere930"
	type sphere
	c 3.61905056838 -1.86509701799 0.5
	r 0.0704905290638
}

shader {
	name "Sphere931"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere931"
	type sphere
	c 3.44192986767 -2.23604332126 0.5
	r 0.063137685732
}

shader {
	name "Sphere932"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere932"
	type sphere
	c 3.1859129205 -2.45491168166 0.5
	r 0.0607098467865
}

shader {
	name "Sphere933"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere933"
	type sphere
	c 2.84586251324 -2.62613685829 0.5
	r 0.0680529343416
}

shader {
	name "Sphere934"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere934"
	type sphere
	c 2.65229367461 -3.03795472564 0.5
	r 0.0961741480601
}

shader {
	name "Sphere935"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere935"
	type sphere
	c 1.5683496931 -3.71893411479 0.5
	r 0.095578288989
}

shader {
	name "Sphere936"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere936"
	type sphere
	c 1.12939763915 -3.96753808186 0.5
	r 0.0993488701676
}

shader {
	name "Sphere937"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere937"
	type sphere
	c 0.462638021377 -4.0734348034 0.5
	r 0.0946951251335
}

shader {
	name "Sphere938"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere938"
	type sphere
	c 0.25354258821 -3.88427827068 0.5
	r 0.103868162878
}

shader {
	name "Sphere939"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere939"
	type sphere
	c -0.103110299393 -3.38167501973 0.5
	r 0.0904537773223
}

shader {
	name "Sphere940"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere940"
	type sphere
	c -0.84251134765 -2.6675058025 0.5
	r 0.0731294656055
}

shader {
	name "Sphere941"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere941"
	type sphere
	c -1.20246667091 -2.7543311843 0.5
	r 0.0648016525904
}

shader {
	name "Sphere942"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere942"
	type sphere
	c -1.59688088133 -2.23039918555 0.5
	r 0.055375004154
}

shader {
	name "Sphere943"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere943"
	type sphere
	c -1.69428358696 -2.10501137314 0.5
	r 0.0572410142916
}

shader {
	name "Sphere944"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere944"
	type sphere
	c -1.77632262638 -1.84970539675 0.5
	r 0.0427741348925
}

shader {
	name "Sphere945"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere945"
	type sphere
	c -1.90092160508 -1.78779310311 0.5
	r 0.0505630406218
}

shader {
	name "Sphere946"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere946"
	type sphere
	c -2.24618352838 -1.79403997302 0.5
	r 0.0546218250818
}

shader {
	name "Sphere947"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere947"
	type sphere
	c -2.5000503317 -1.54638911206 0.5
	r 0.0524832314961
}

shader {
	name "Sphere948"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere948"
	type sphere
	c -2.54919601884 -1.35868153784 0.5
	r 0.0513022115086
}

shader {
	name "Sphere949"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere949"
	type sphere
	c -2.90245849624 -0.967963750481 0.5
	r 0.0589730689271
}

shader {
	name "Sphere950"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere950"
	type sphere
	c -2.73969030365 -0.147499554343 0.5
	r 0.0500801685931
}

shader {
	name "Sphere951"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere951"
	type sphere
	c -2.79988966933 0.129315833393 0.5
	r 0.0575187433535
}

shader {
	name "Sphere952"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere952"
	type sphere
	c -2.93387814792 0.243467557238 0.5
	r 0.0480037542043
}

shader {
	name "Sphere953"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere953"
	type sphere
	c -2.87761742564 0.490678132065 0.5
	r 0.0489810079354
}

shader {
	name "Sphere954"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere954"
	type sphere
	c -2.97597839824 0.734049062194 0.5
	r 0.0578216211362
}

shader {
	name "Sphere955"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere955"
	type sphere
	c -2.98515470045 1.17921048964 0.5
	r 0.0672059955552
}

shader {
	name "Sphere956"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere956"
	type sphere
	c -2.758901156 1.65139631525 0.5
	r 0.0628980057299
}

shader {
	name "Sphere957"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere957"
	type sphere
	c -2.65684993105 1.9854346644 0.5
	r 0.0658906161464
}

shader {
	name "Sphere958"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere958"
	type sphere
	c -1.8346263378 2.15528442345 0.5
	r 0.0643224627487
}

shader {
	name "Sphere959"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere959"
	type sphere
	c -1.36804034317 1.08143784078 0.5
	r 0.0440272163267
}

shader {
	name "Sphere960"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere960"
	type sphere
	c -1.43154671607 1.86442981674 0.5
	r 0.0344281358374
}

shader {
	name "Sphere961"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere961"
	type sphere
	c -1.38222272321 2.12930452744 0.5
	r 0.034590450616
}

shader {
	name "Sphere962"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere962"
	type sphere
	c -1.2328796425 2.24460381014 0.5
	r 0.0340589668641
}

shader {
	name "Sphere963"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere963"
	type sphere
	c -1.06996980967 2.19965149521 0.5
	r 0.0332416678912
}

shader {
	name "Sphere964"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere964"
	type sphere
	c -0.979222136378 2.35876978734 0.5
	r 0.0355433320307
}

shader {
	name "Sphere965"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere965"
	type sphere
	c -0.762564819436 2.21261997939 0.5
	r 0.0381406855714
}

shader {
	name "Sphere966"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere966"
	type sphere
	c -0.554991114786 2.16759452346 0.5
	r 0.0394030498742
}

shader {
	name "Sphere967"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere967"
	type sphere
	c -0.565618402931 2.3853275847 0.5
	r 0.0408550650637
}

shader {
	name "Sphere968"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere968"
	type sphere
	c -0.060305894951 2.32368131055 0.5
	r 0.0308154653795
}

shader {
	name "Sphere969"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere969"
	type sphere
	c 0.250538013053 2.40083649243 0.5
	r 0.0383082840313
}

shader {
	name "Sphere970"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere970"
	type sphere
	c 0.561107295317 2.2805189312 0.5
	r 0.0460633787741
}

shader {
	name "Sphere971"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere971"
	type sphere
	c 0.643916107482 2.05595824051 0.5
	r 0.0455961692603
}

shader {
	name "Sphere972"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere972"
	type sphere
	c 0.978871542799 2.2029774961 0.5
	r 0.0483499560686
}

shader {
	name "Sphere973"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere973"
	type sphere
	c 1.42916880461 2.12976188483 0.5
	r 0.0450558453177
}

shader {
	name "Sphere974"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere974"
	type sphere
	c 1.60385405835 1.99245645389 0.5
	r 0.0386664416713
}

shader {
	name "Sphere975"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere975"
	type sphere
	c 1.90772367278 2.10313321988 0.5
	r 0.0622059635893
}

shader {
	name "Sphere976"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere976"
	type sphere
	c 2.24996347707 1.91733293357 0.5
	r 0.069846971514
}

shader {
	name "Sphere977"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere977"
	type sphere
	c 2.19793008813 1.56432386392 0.5
	r 0.0645235237453
}

shader {
	name "Sphere978"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere978"
	type sphere
	c 2.43216892102 1.23199295426 0.5
	r 0.04875705472
}

shader {
	name "Sphere979"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere979"
	type sphere
	c 2.8639074837 1.29931426245 0.5
	r 0.0452262102003
}

shader {
	name "Sphere980"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere980"
	type sphere
	c 2.87801165321 1.05053371526 0.5
	r 0.0496452106738
}

shader {
	name "Sphere981"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere981"
	type sphere
	c 3.23255863101 0.857305311926 0.5
	r 0.0485033751009
}

shader {
	name "Sphere982"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere982"
	type sphere
	c 3.23691603856 0.583066745325 0.5
	r 0.0547768829992
}

shader {
	name "Sphere983"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere983"
	type sphere
	c 3.63043610409 0.589899181257 0.5
	r 0.075417710909
}

shader {
	name "Sphere984"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere984"
	type sphere
	c 3.67958134906 0.160761338111 0.5
	r 0.0856001174609
}

shader {
	name "Sphere985"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere985"
	type sphere
	c 4.35584028967 -0.209838794809 0.5
	r 0.0981971489676
}

shader {
	name "Sphere986"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere986"
	type sphere
	c 4.48468880918 -0.460438503726 0.5
	r 0.0894033390811
}

shader {
	name "Sphere987"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere987"
	type sphere
	c 4.22526804061 -0.869341835552 0.5
	r 0.0795485725729
}

shader {
	name "Sphere988"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere988"
	type sphere
	c 3.63952392093 -1.67688188399 0.5
	r 0.0715034966655
}

shader {
	name "Sphere989"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere989"
	type sphere
	c 3.60842223069 -2.05385460665 0.5
	r 0.0713019027619
}

shader {
	name "Sphere990"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere990"
	type sphere
	c 3.47318186216 -2.40165021873 0.5
	r 0.0632597491825
}

shader {
	name "Sphere991"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere991"
	type sphere
	c 3.34179575084 -2.51579833212 0.5
	r 0.0648040391494
}

shader {
	name "Sphere992"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere992"
	type sphere
	c 2.81866459504 -2.80710431237 0.5
	r 0.0691969553964
}

shader {
	name "Sphere993"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere993"
	type sphere
	c 1.53990494222 -3.95766540355 0.5
	r 0.0847366418877
}

shader {
	name "Sphere994"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere994"
	type sphere
	c 0.645636008042 -4.24119839685 0.5
	r 0.0914996616018
}

shader {
	name "Sphere995"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere995"
	type sphere
	c 0.0727116796007 -3.68849376544 0.5
	r 0.0960196978711
}

shader {
	name "Sphere996"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere996"
	type sphere
	c -0.302825605851 -3.23714077215 0.5
	r 0.0944426753238
}

shader {
	name "Sphere997"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere997"
	type sphere
	c -0.909292231463 -2.83989613828 0.5
	r 0.0655254632709
}

shader {
	name "Sphere998"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere998"
	type sphere
	c -1.08102635039 -2.8774078448 0.5
	r 0.0648759626369
}

shader {
	name "Sphere999"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere999"
	type sphere
	c -1.34093851427 -2.64758809548 0.5
	r 0.0663273024839
}

shader {
	name "Sphere1000"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1000"
	type sphere
	c -1.50700261007 -2.35058436382 0.5
	r 0.0571814334944
}

shader {
	name "Sphere1001"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1001"
	type sphere
	c -1.78169309581 -1.98245924564 0.5
	r 0.055656897485
}

shader {
	name "Sphere1002"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1002"
	type sphere
	c -2.00513806476 -1.70625799184 0.5
	r 0.0486782699396
}

shader {
	name "Sphere1003"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1003"
	type sphere
	c -2.10287142109 -1.81306740023 0.5
	r 0.0538054626891
}

shader {
	name "Sphere1004"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1004"
	type sphere
	c -2.55472133621 -1.67216288427 0.5
	r 0.0503733569555
}

shader {
	name "Sphere1005"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1005"
	type sphere
	c -2.68285760856 -1.32992555676 0.5
	r 0.0512377024019
}

shader {
	name "Sphere1006"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1006"
	type sphere
	c -2.83271674738 -1.10706557937 0.5
	r 0.0577314385428
}

shader {
	name "Sphere1007"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1007"
	type sphere
	c -2.86264571783 -0.106562348929 0.5
	r 0.047113259026
}

shader {
	name "Sphere1008"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1008"
	type sphere
	c -2.90659113921 0.023269205948 0.5
	r 0.0553085078414
}

shader {
	name "Sphere1009"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1009"
	type sphere
	c -3.01820389399 0.335111172285 0.5
	r 0.0453987526771
}

shader {
	name "Sphere1010"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1010"
	type sphere
	c -3.08207125482 0.846254429227 0.5
	r 0.057993869912
}

shader {
	name "Sphere1011"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1011"
	type sphere
	c -3.15559189833 1.13746616416 0.5
	r 0.0644001508087
}

shader {
	name "Sphere1012"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1012"
	type sphere
	c -2.86774545707 1.77446996214 0.5
	r 0.0603263424864
}

shader {
	name "Sphere1013"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1013"
	type sphere
	c -2.82995428918 1.94212861174 0.5
	r 0.0679387521268
}

shader {
	name "Sphere1014"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1014"
	type sphere
	c -2.48486524811 2.04269210191 0.5
	r 0.0700584340141
}

shader {
	name "Sphere1015"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1015"
	type sphere
	c -1.99838347206 2.0839375269 0.5
	r 0.0696460522154
}

shader {
	name "Sphere1016"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1016"
	type sphere
	c -1.67764324427 2.22332040423 0.5
	r 0.0639967868327
}

shader {
	name "Sphere1017"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1017"
	type sphere
	c -1.29013713255 0.999071863249 0.5
	r 0.0410013010661
}

shader {
	name "Sphere1018"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1018"
	type sphere
	c -1.42110453414 1.77577568339 0.5
	r 0.0325221025395
}

shader {
	name "Sphere1019"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1019"
	type sphere
	c -1.45299066906 1.95435412262 0.5
	r 0.0349062059278
}

shader {
	name "Sphere1020"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1020"
	type sphere
	c -1.37710071519 2.03315264823 0.5
	r 0.0376257047691
}

shader {
	name "Sphere1021"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1021"
	type sphere
	c -1.39813973942 2.22181365826 0.5
	r 0.0358109059954
}

shader {
	name "Sphere1022"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1022"
	type sphere
	c -1.31520784688 2.28087356306 0.5
	r 0.0334136451298
}

shader {
	name "Sphere1023"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1023"
	type sphere
	c -1.11165189911 2.27727659342 0.5
	r 0.0328394716586
}

shader {
	name "Sphere1024"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1024"
	type sphere
	c -0.723279644789 2.30939247784 0.5
	r 0.0401912095278
}

shader {
	name "Sphere1025"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1025"
	type sphere
	c -0.479426040063 2.44513633039 0.5
	r 0.037827797308
}

shader {
	name "Sphere1026"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1026"
	type sphere
	c -0.137168738489 2.34207821642 0.5
	r 0.0284598908836
}

shader {
	name "Sphere1027"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1027"
	type sphere
	c 0.149333515418 2.42437491036 0.5
	r 0.0396210377702
}

shader {
	name "Sphere1028"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1028"
	type sphere
	c 0.679742422461 2.25204307402 0.5
	r 0.0454402108111
}

shader {
	name "Sphere1029"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1029"
	type sphere
	c 0.860232216357 2.14969211672 0.5
	r 0.0491922120277
}

shader {
	name "Sphere1030"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1030"
	type sphere
	c 1.0955419706 2.26419297876 0.5
	r 0.050466134591
}

shader {
	name "Sphere1031"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1031"
	type sphere
	c 1.53611169411 2.15989276059 0.5
	r 0.0382740193773
}

shader {
	name "Sphere1032"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1032"
	type sphere
	c 1.75605403032 2.17811026391 0.5
	r 0.0646864953522
}

shader {
	name "Sphere1033"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1033"
	type sphere
	c 2.04789559226 2.02787059873 0.5
	r 0.0571186101475
}

shader {
	name "Sphere1034"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1034"
	type sphere
	c 2.38367601847 1.80385117519 0.5
	r 0.0616859090981
}

shader {
	name "Sphere1035"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1035"
	type sphere
	c 2.35718463295 1.62402835983 0.5
	r 0.0630352205399
}

shader {
	name "Sphere1036"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1036"
	type sphere
	c 2.46203357332 1.35959351809 0.5
	r 0.0495295835229
}

shader {
	name "Sphere1037"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1037"
	type sphere
	c 2.75789819555 1.35797086917 0.5
	r 0.0456401408884
}

shader {
	name "Sphere1038"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1038"
	type sphere
	c 2.96688431388 1.24197905453 0.5
	r 0.0431706161725
}

shader {
	name "Sphere1039"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1039"
	type sphere
	c 3.13291342164 0.933226013652 0.5
	r 0.0454507647477
}

shader {
	name "Sphere1040"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1040"
	type sphere
	c 3.34854433232 0.788858379139 0.5
	r 0.0525037377783
}

shader {
	name "Sphere1041"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1041"
	type sphere
	c 3.82269015522 0.504961603012 0.5
	r 0.0822179670368
}

shader {
	name "Sphere1042"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1042"
	type sphere
	c 4.21804907523 0.00186480506943 0.5
	r 0.09124999023
}

shader {
	name "Sphere1043"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1043"
	type sphere
	c 4.60540375521 -0.664188126924 0.5
	r 0.0882152945747
}

shader {
	name "Sphere1044"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1044"
	type sphere
	c 4.37782802197 -1.02867526137 0.5
	r 0.0858968860482
}

shader {
	name "Sphere1045"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1045"
	type sphere
	c 3.78692908606 -1.78946330362 0.5
	r 0.067606560658
}

shader {
	name "Sphere1046"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1046"
	type sphere
	c 3.59880525562 -2.29202755374 0.5
	r 0.0617865649851
}

shader {
	name "Sphere1047"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1047"
	type sphere
	c 3.20387351236 -2.62347551206 0.5
	r 0.0664286431622
}

shader {
	name "Sphere1048"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1048"
	type sphere
	c 2.98954891521 -2.73871426733 0.5
	r 0.0688491968184
}

shader {
	name "Sphere1049"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1049"
	type sphere
	c 1.74198790078 -3.87435637117 0.5
	r 0.0791995601011
}

shader {
	name "Sphere1050"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1050"
	type sphere
	c 0.871750371696 -4.1709487344 0.5
	r 0.0860820950493
}

shader {
	name "Sphere1051"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1051"
	type sphere
	c 0.414458048354 -4.31590379883 0.5
	r 0.0907119796233
}

shader {
	name "Sphere1052"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1052"
	type sphere
	c -0.0132381835914 -3.93504536608 0.5
	r 0.0998079745935
}

shader {
	name "Sphere1053"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1053"
	type sphere
	c -0.322355548716 -3.48336709612 0.5
	r 0.0908070533468
}

shader {
	name "Sphere1054"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1054"
	type sphere
	c -0.262601643181 -2.99042804555 0.5
	r 0.0930350283144
}

shader {
	name "Sphere1055"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1055"
	type sphere
	c -0.738600953587 -2.81731318129 0.5
	r 0.0636085564059
}

shader {
	name "Sphere1056"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1056"
	type sphere
	c -1.24973638563 -2.922283134 0.5
	r 0.0660562259492
}

shader {
	name "Sphere1057"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1057"
	type sphere
	c -1.33145656489 -2.46529260227 0.5
	r 0.0705791409132
}

shader {
	name "Sphere1058"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1058"
	type sphere
	c -1.65589894844 -2.36525997023 0.5
	r 0.0550319338685
}

shader {
	name "Sphere1059"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1059"
	type sphere
	c -1.8402816853 -2.11419236217 0.5
	r 0.0524738483941
}

shader {
	name "Sphere1060"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1060"
	type sphere
	c -2.18921872892 -1.92219820082 0.5
	r 0.0505642236573
}

shader {
	name "Sphere1061"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1061"
	type sphere
	c -2.47442664375 -1.77365423687 0.5
	r 0.046686415415
}

shader {
	name "Sphere1062"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1062"
	type sphere
	c -2.63568797931 -1.56523097408 0.5
	r 0.0502218331667
}

shader {
	name "Sphere1063"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1063"
	type sphere
	c -2.68329285994 -1.11291099685 0.5
	r 0.0544221958625
}

shader {
	name "Sphere1064"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1064"
	type sphere
	c -2.98645506372 -1.09895355935 0.5
	r 0.0577326990231
}

shader {
	name "Sphere1065"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1065"
	type sphere
	c -2.83903684806 -0.228570639951 0.5
	r 0.0460903541986
}

shader {
	name "Sphere1066"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1066"
	type sphere
	c -3.05533186862 0.220945805502 0.5
	r 0.0446394188299
}

shader {
	name "Sphere1067"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1067"
	type sphere
	c -3.12117037138 0.702721673592 0.5
	r 0.0535782860294
}

shader {
	name "Sphere1068"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1068"
	type sphere
	c -3.20615806294 0.97104034261 0.5
	r 0.0660534855317
}

shader {
	name "Sphere1069"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1069"
	type sphere
	c -3.10766475142 1.29561728641 0.5
	r 0.0595401321703
}

shader {
	name "Sphere1070"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1070"
	type sphere
	c -2.91821318886 1.62462323514 0.5
	r 0.0582615210081
}

shader {
	name "Sphere1071"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1071"
	type sphere
	c -2.77899989932 2.11750457686 0.5
	r 0.0690324380207
}

shader {
	name "Sphere1072"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1072"
	type sphere
	c -1.96843533801 2.25580631087 0.5
	r 0.0611978258206
}

shader {
	name "Sphere1073"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1073"
	type sphere
	c -1.53979563054 2.11991264468 0.5
	r 0.0652452738805
}

shader {
	name "Sphere1074"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1074"
	type sphere
	c -1.18270720732 1.01947701155 0.5
	r 0.0410116667386
}

shader {
	name "Sphere1075"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1075"
	type sphere
	c -1.39384225226 0.973681158408 0.5
	r 0.0390748180839
}

shader {
	name "Sphere1076"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1076"
	type sphere
	c -1.34536628361 1.73447817302 0.5
	r 0.0321771549037
}

shader {
	name "Sphere1077"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1077"
	type sphere
	c -1.24172672356 2.33831749325 0.5
	r 0.0365388054121
}

shader {
	name "Sphere1078"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1078"
	type sphere
	c -0.790526262202 2.38727139769 0.5
	r 0.0369795035824
}

shader {
	name "Sphere1079"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1079"
	type sphere
	c -0.568986719818 2.48906175588 0.5
	r 0.0369865668131
}

shader {
	name "Sphere1080"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1080"
	type sphere
	c -0.0865315333983 2.39688277097 0.5
	r 0.0275027035659
}

shader {
	name "Sphere1081"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1081"
	type sphere
	c 0.0731333126252 2.34770829569 0.5
	r 0.0414492120106
}

shader {
	name "Sphere1082"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1082"
	type sphere
	c 0.221191750441 2.49649149096 0.5
	r 0.0367332614899
}

shader {
	name "Sphere1083"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1083"
	type sphere
	c 0.644834453967 2.36452673398 0.5
	r 0.0428916422396
}

shader {
	name "Sphere1084"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1084"
	type sphere
	c 0.848743823953 2.01850771765 0.5
	r 0.0495726499788
}

shader {
	name "Sphere1085"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1085"
	type sphere
	c 0.876202869629 2.27551205447 0.5
	r 0.0459299024273
}

shader {
	name "Sphere1086"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1086"
	type sphere
	c 1.21069592131 2.19311809528 0.5
	r 0.0510254422849
}

shader {
	name "Sphere1087"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1087"
	type sphere
	c 1.46525648725 2.2399733029 0.5
	r 0.0419211263502
}

shader {
	name "Sphere1088"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1088"
	type sphere
	c 1.61114894421 2.09649328331 0.5
	r 0.0354021061625
}

shader {
	name "Sphere1089"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1089"
	type sphere
	c 1.90010425588 2.2711225085 0.5
	r 0.0639155327537
}

shader {
	name "Sphere1090"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1090"
	type sphere
	c 2.05045512216 2.18622056289 0.5
	r 0.0616593763181
}

shader {
	name "Sphere1091"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1091"
	type sphere
	c 2.41403141252 1.95941446748 0.5
	r 0.05718705111
}

shader {
	name "Sphere1092"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1092"
	type sphere
	c 2.33306407822 1.45192764801 0.5
	r 0.0673018677912
}

shader {
	name "Sphere1093"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1093"
	type sphere
	c 2.58965695521 1.39539083506 0.5
	r 0.0498819913745
}

shader {
	name "Sphere1094"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1094"
	type sphere
	c 2.86347629985 1.42249622737 0.5
	r 0.047160829475
}

shader {
	name "Sphere1095"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1095"
	type sphere
	c 2.96728088851 1.35821277497 0.5
	r 0.0440051815528
}

shader {
	name "Sphere1096"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1096"
	type sphere
	c 2.97346181505 1.12865703285 0.5
	r 0.0419639453604
}

shader {
	name "Sphere1097"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1097"
	type sphere
	c 3.01552373169 0.902177082549 0.5
	r 0.045619050113
}

shader {
	name "Sphere1098"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1098"
	type sphere
	c 3.24277585407 0.98059030164 0.5
	r 0.0442773553278
}

shader {
	name "Sphere1099"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1099"
	type sphere
	c 3.78693171692 0.705314684906 0.5
	r 0.070421356617
}

shader {
	name "Sphere1100"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1100"
	type sphere
	c 3.96707666129 0.00898301435527 0.5
	r 0.0970550138812
}

shader {
	name "Sphere1101"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1101"
	type sphere
	c 4.45902384209 0.0187861332602 0.5
	r 0.0899261199649
}

shader {
	name "Sphere1102"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1102"
	type sphere
	c 4.71983382601 -0.460579434845 0.5
	r 0.0869554552193
}

shader {
	name "Sphere1103"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1103"
	type sphere
	c 4.3090509887 -1.2475734907 0.5
	r 0.0861896539486
}

shader {
	name "Sphere1104"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1104"
	type sphere
	c 3.81038688817 -1.61423765701 0.5
	r 0.0649850730778
}

shader {
	name "Sphere1105"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1105"
	type sphere
	c 3.7677567121 -1.9621091969 0.5
	r 0.0626738243523
}

shader {
	name "Sphere1106"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1106"
	type sphere
	c 3.63216212821 -2.45406253579 0.5
	r 0.0622880464398
}

shader {
	name "Sphere1107"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1107"
	type sphere
	c 3.37008057185 -2.69061364987 0.5
	r 0.068012525559
}

shader {
	name "Sphere1108"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1108"
	type sphere
	c 2.96407683963 -2.92150205563 0.5
	r 0.0695663504621
}

shader {
	name "Sphere1109"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1109"
	type sphere
	c 1.7944816942 -3.67192325865 0.5
	r 0.0776468756574
}

shader {
	name "Sphere1110"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1110"
	type sphere
	c 1.71429290415 -4.0755985342 0.5
	r 0.0731546302632
}

shader {
	name "Sphere1111"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1111"
	type sphere
	c 0.823648899931 -4.39155952062 0.5
	r 0.0832633055452
}

shader {
	name "Sphere1112"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1112"
	type sphere
	c 0.594810913314 -4.48242307546 0.5
	r 0.0933909855395
}

shader {
	name "Sphere1113"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1113"
	type sphere
	c 0.226560981856 -4.15798055226 0.5
	r 0.09337453785
}

shader {
	name "Sphere1114"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1114"
	type sphere
	c -0.184716396295 -3.73161042101 0.5
	r 0.0997407332401
}

shader {
	name "Sphere1115"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1115"
	type sphere
	c -0.521734775623 -3.34845236921 0.5
	r 0.0897453173362
}

shader {
	name "Sphere1116"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1116"
	type sphere
	c -0.504344299369 -3.07569258418 0.5
	r 0.0992190321623
}

shader {
	name "Sphere1117"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1117"
	type sphere
	c -0.666693453119 -2.67085852098 0.5
	r 0.0587579283202
}

shader {
	name "Sphere1118"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1118"
	type sphere
	c -0.802845585984 -2.96927741801 0.5
	r 0.0601312205217
}

shader {
	name "Sphere1119"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1119"
	type sphere
	c -1.12270888473 -3.05388736114 0.5
	r 0.0711254344608
}

shader {
	name "Sphere1120"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1120"
	type sphere
	c -1.49430371147 -2.5538937814 0.5
	r 0.0684631770165
}

shader {
	name "Sphere1121"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1121"
	type sphere
	c -1.74225216967 -2.24762143785 0.5
	r 0.0544159213121
}

shader {
	name "Sphere1122"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1122"
	type sphere
	c -1.92348846106 -2.00283752105 0.5
	r 0.0517822706019
}

shader {
	name "Sphere1123"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1123"
	type sphere
	c -2.0548894376 -1.94524045594 0.5
	r 0.0516542116409
}

shader {
	name "Sphere1124"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1124"
	type sphere
	c -2.32516523226 -1.91175560814 0.5
	r 0.0516960128776
}

shader {
	name "Sphere1125"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1125"
	type sphere
	c -2.59984557374 -1.79666637953 0.5
	r 0.0489480450326
}

shader {
	name "Sphere1126"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1126"
	type sphere
	c -2.68342275544 -1.68524963341 0.5
	r 0.0466504367855
}

shader {
	name "Sphere1127"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1127"
	type sphere
	c -2.91669420025 -1.23775755317 0.5
	r 0.0587786043342
}

shader {
	name "Sphere1128"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1128"
	type sphere
	c -3.05922609099 -0.961833760684 0.5
	r 0.0586924793004
}

shader {
	name "Sphere1129"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1129"
	type sphere
	c -2.72344629445 -0.277215481014 0.5
	r 0.0479666331147
}

shader {
	name "Sphere1130"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1130"
	type sphere
	c -2.95988401537 -0.190091843583 0.5
	r 0.0490286175442
}

shader {
	name "Sphere1131"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1131"
	type sphere
	c -3.14068634158 0.31072100393 0.5
	r 0.0482667000357
}

shader {
	name "Sphere1132"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1132"
	type sphere
	c -3.02700060782 0.591578325163 0.5
	r 0.0556768895982
}

shader {
	name "Sphere1133"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1133"
	type sphere
	c -3.22360101217 0.801751358698 0.5
	r 0.0532774088209
}

shader {
	name "Sphere1134"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1134"
	type sphere
	c -3.32551187977 1.10051708465 0.5
	r 0.0660180014751
}

shader {
	name "Sphere1135"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1135"
	type sphere
	c -3.26341906393 1.26313234913 0.5
	r 0.0597892683175
}

shader {
	name "Sphere1136"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1136"
	type sphere
	c -2.95607325505 1.34698958248 0.5
	r 0.0605046123962
}

shader {
	name "Sphere1137"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1137"
	type sphere
	c -2.82141164689 1.49857501686 0.5
	r 0.0609358538413
}

shader {
	name "Sphere1138"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1138"
	type sphere
	c -3.02693838885 1.74170259878 0.5
	r 0.0615713622383
}

shader {
	name "Sphere1139"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1139"
	type sphere
	c -2.94919551749 2.07040131809 0.5
	r 0.0634126895023
}

shader {
	name "Sphere1140"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1140"
	type sphere
	c -2.12581656565 2.20587692328 0.5
	r 0.0626357699402
}

shader {
	name "Sphere1141"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1141"
	type sphere
	c -1.5248268042 2.28612258156 0.5
	r 0.0599166911701
}

shader {
	name "Sphere1142"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1142"
	type sphere
	c -1.14789275622 1.11869291847 0.5
	r 0.0378484070161
}

shader {
	name "Sphere1143"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1143"
	type sphere
	c -1.21833874064 0.913992592368 0.5
	r 0.0424932431894
}

shader {
	name "Sphere1144"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1144"
	type sphere
	c -1.47204666158 1.04277718606 0.5
	r 0.0391922391901
}

shader {
	name "Sphere1145"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1145"
	type sphere
	c -1.41906783728 1.68844110683 0.5
	r 0.0329966388551
}

shader {
	name "Sphere1146"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1146"
	type sphere
	c -1.32945997922 2.36825124895 0.5
	r 0.0329856439314
}

shader {
	name "Sphere1147"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1147"
	type sphere
	c -0.695795929156 2.40652957068 0.5
	r 0.0355215390967
}

shader {
	name "Sphere1148"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1148"
	type sphere
	c -0.48561148126 2.5484189117 0.5
	r 0.0397729281863
}

shader {
	name "Sphere1149"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1149"
	type sphere
	c -0.160056068639 2.41580367076 0.5
	r 0.0294373524047
}

shader {
	name "Sphere1150"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1150"
	type sphere
	c 0.0449220363076 2.45545193777 0.5
	r 0.0420826369564
}

shader {
	name "Sphere1151"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1151"
	type sphere
	c 0.125820475833 2.5250810278 0.5
	r 0.0379399326341
}

shader {
	name "Sphere1152"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1152"
	type sphere
	c 0.315527310608 2.47524981906 0.5
	r 0.0357898636307
}

shader {
	name "Sphere1153"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1153"
	type sphere
	c 0.533336333776 2.39788993607 0.5
	r 0.0443953866295
}

shader {
	name "Sphere1154"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1154"
	type sphere
	c 0.761566965677 2.3427335216 0.5
	r 0.0461704184834
}

shader {
	name "Sphere1155"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1155"
	type sphere
	c 1.21144817306 2.32453423413 0.5
	r 0.047538276604
}

shader {
	name "Sphere1156"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1156"
	type sphere
	c 1.35854464367 2.21811130588 0.5
	r 0.0397750639883
}

shader {
	name "Sphere1157"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1157"
	type sphere
	c 1.57128208759 2.25603398967 0.5
	r 0.0385052228352
}

shader {
	name "Sphere1158"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1158"
	type sphere
	c 1.74569000761 2.35415767995 0.5
	r 0.0675776699958
}

shader {
	name "Sphere1159"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1159"
	type sphere
	c 2.17862996267 2.09914429603 0.5
	r 0.0545569074821
}

shader {
	name "Sphere1160"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1160"
	type sphere
	c 2.53465246755 1.86124656977 0.5
	r 0.0594527189925
}

shader {
	name "Sphere1161"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1161"
	type sphere
	c 2.49328746112 1.5229111096 0.5
	r 0.0641305431194
}

shader {
	name "Sphere1162"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1162"
	type sphere
	c 2.75549511825 1.47677457863 0.5
	r 0.0434808672427
}

shader {
	name "Sphere1163"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1163"
	type sphere
	c 3.06549215147 1.29866594197 0.5
	r 0.0421347835565
}

shader {
	name "Sphere1164"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1164"
	type sphere
	c 3.04607466174 1.02502195389 0.5
	r 0.0493210611679
}

shader {
	name "Sphere1165"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1165"
	type sphere
	c 3.61117205636 0.791312838016 0.5
	r 0.0763318941102
}

shader {
	name "Sphere1166"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1166"
	type sphere
	c 3.96018112209 0.647816081382 0.5
	r 0.0664848640641
}

shader {
	name "Sphere1167"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1167"
	type sphere
	c 4.10639370211 0.221220761742 0.5
	r 0.0933535753282
}

shader {
	name "Sphere1168"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1168"
	type sphere
	c 4.59651452833 -0.169357128231 0.5
	r 0.0848441186398
}

shader {
	name "Sphere1169"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1169"
	type sphere
	c 4.8452937692 -0.663076699238 0.5
	r 0.091704146903
}

shader {
	name "Sphere1170"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1170"
	type sphere
	c 4.54151026455 -1.1999346857 0.5
	r 0.0917782041104
}

shader {
	name "Sphere1171"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1171"
	type sphere
	c 3.95294323359 -1.71894184223 0.5
	r 0.0676722632736
}

shader {
	name "Sphere1172"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1172"
	type sphere
	c 3.9234528873 -1.89854363482 0.5
	r 0.0634553051365
}

shader {
	name "Sphere1173"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1173"
	type sphere
	c 3.75908020521 -2.3427888185 0.5
	r 0.0643043965228
}

shader {
	name "Sphere1174"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1174"
	type sphere
	c 3.50796343688 -2.57424564424 0.5
	r 0.0673062588994
}

shader {
	name "Sphere1175"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1175"
	type sphere
	c 3.22363696827 -2.8079791474 0.5
	r 0.0727406940628
}

shader {
	name "Sphere1176"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1176"
	type sphere
	c 1.94804683865 -3.81759240483 0.5
	r 0.0811013100909
}

shader {
	name "Sphere1177"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1177"
	type sphere
	c 1.546886185 -4.1608537124 0.5
	r 0.0677445125736
}

shader {
	name "Sphere1178"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1178"
	type sphere
	c 1.03628303783 -4.326194228 0.5
	r 0.0835773899414
}

shader {
	name "Sphere1179"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1179"
	type sphere
	c 0.361092755158 -4.54945259913 0.5
	r 0.0889641299721
}

shader {
	name "Sphere1180"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1180"
	type sphere
	c -0.278193000715 -3.98427262282 0.5
	r 0.102308854447
}

shader {
	name "Sphere1181"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1181"
	type sphere
	c -0.541451970936 -3.58982256129 0.5
	r 0.0918853237929
}

shader {
	name "Sphere1182"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1182"
	type sphere
	c -0.448936285286 -2.82282356818 0.5
	r 0.0949321791207
}

shader {
	name "Sphere1183"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1183"
	type sphere
	c -1.30480838664 -3.09315333407 0.5
	r 0.0685882028041
}

shader {
	name "Sphere1184"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1184"
	type sphere
	c -1.49594984416 -2.73439807411 0.5
	r 0.0669206719484
}

shader {
	name "Sphere1185"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1185"
	type sphere
	c -1.7991919817 -2.3789295788 0.5
	r 0.0529257442478
}

shader {
	name "Sphere1186"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1186"
	type sphere
	c -1.98233837373 -2.13239371033 0.5
	r 0.0549396418636
}

shader {
	name "Sphere1187"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1187"
	type sphere
	c -2.14351079341 -2.05018768633 0.5
	r 0.0513655051791
}

shader {
	name "Sphere1188"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1188"
	type sphere
	c -2.51555245455 -1.88681833973 0.5
	r 0.0436175914273
}

shader {
	name "Sphere1189"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1189"
	type sphere
	c -2.76280088371 -1.58921452869 0.5
	r 0.0467949541145
}

shader {
	name "Sphere1190"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1190"
	type sphere
	c -3.06670852649 -1.2247143234 0.5
	r 0.0541566136278
}

shader {
	name "Sphere1191"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1191"
	type sphere
	c -3.13984795575 -1.09392911788 0.5
	r 0.0573736700058
}

shader {
	name "Sphere1192"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1192"
	type sphere
	c -2.92881653308 -0.314370799439 0.5
	r 0.0470488336101
}

shader {
	name "Sphere1193"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1193"
	type sphere
	c -3.17275581496 0.188067959229 0.5
	r 0.0468154961415
}

shader {
	name "Sphere1194"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1194"
	type sphere
	c -3.09720399728 0.431996800098 0.5
	r 0.0483597705262
}

shader {
	name "Sphere1195"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1195"
	type sphere
	c -3.17045879977 0.56911510425 0.5
	r 0.0532277826495
}

shader {
	name "Sphere1196"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1196"
	type sphere
	c -3.38488023839 0.926108134638 0.5
	r 0.0721593652173
}

shader {
	name "Sphere1197"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1197"
	type sphere
	c -3.21375738294 1.41630335224 0.5
	r 0.0609761936233
}

shader {
	name "Sphere1198"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1198"
	type sphere
	c -3.06906432895 1.58762146489 0.5
	r 0.0582306399972
}

shader {
	name "Sphere1199"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1199"
	type sphere
	c -2.99746753326 1.91381954357 0.5
	r 0.0594775960592
}

shader {
	name "Sphere1200"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1200"
	type sphere
	c -2.91238934292 2.24020717968 0.5
	r 0.0668990823351
}

shader {
	name "Sphere1201"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1201"
	type sphere
	c -2.167080191 2.04805952935 0.5
	r 0.0597062581615
}

shader {
	name "Sphere1202"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1202"
	type sphere
	c -2.08795645894 2.36581699753 0.5
	r 0.0606342424528
}

shader {
	name "Sphere1203"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1203"
	type sphere
	c -1.64724177819 2.380283358 0.5
	r 0.0559132216038
}

shader {
	name "Sphere1204"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1204"
	type sphere
	c -1.08068165768 1.04376138266 0.5
	r 0.0376452191387
}

shader {
	name "Sphere1205"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1205"
	type sphere
	c -1.11364749781 0.93938811752 0.5
	r 0.0383022939691
}

shader {
	name "Sphere1206"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1206"
	type sphere
	c -1.45786009668 1.1459412071 0.5
	r 0.0389089230673
}

shader {
	name "Sphere1207"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1207"
	type sphere
	c -1.26374391227 2.43221182208 0.5
	r 0.0357920810871
}

shader {
	name "Sphere1208"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1208"
	type sphere
	c -0.75730290334 2.47592176213 0.5
	r 0.0340240650847
}

shader {
	name "Sphere1209"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1209"
	type sphere
	c -0.581875567682 2.58897859215 0.5
	r 0.0385719655999
}

shader {
	name "Sphere1210"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1210"
	type sphere
	c -0.104417360058 2.46934386898 0.5
	r 0.0284742010959
}

shader {
	name "Sphere1211"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1211"
	type sphere
	c 0.199204883886 2.59100801415 0.5
	r 0.0360468693467
}

shader {
	name "Sphere1212"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1212"
	type sphere
	c 0.620696762364 2.47971875312 0.5
	r 0.0453787041646
}

shader {
	name "Sphere1213"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1213"
	type sphere
	c 1.1075029465 2.39080903816 0.5
	r 0.04491868567
}

shader {
	name "Sphere1214"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1214"
	type sphere
	c 1.38996494752 2.32175156635 0.5
	r 0.0414487209169
}

shader {
	name "Sphere1215"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1215"
	type sphere
	c 1.50927531088 2.33692785726 0.5
	r 0.0379383525774
}

shader {
	name "Sphere1216"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1216"
	type sphere
	c 1.89895573796 2.4437834988 0.5
	r 0.0655830748649
}

shader {
	name "Sphere1217"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1217"
	type sphere
	c 2.19640488486 2.24652319776 0.5
	r 0.0567782837215
}

shader {
	name "Sphere1218"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1218"
	type sphere
	c 2.55814864814 2.01814109077 0.5
	r 0.0595303814416
}

shader {
	name "Sphere1219"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1219"
	type sphere
	c 2.51397201622 1.69704226851 0.5
	r 0.0646733768132
}

shader {
	name "Sphere1220"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1220"
	type sphere
	c 2.85133421955 1.54367611254 0.5
	r 0.0441791782451
}

shader {
	name "Sphere1221"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1221"
	type sphere
	c 3.06947520896 1.41122970778 0.5
	r 0.0423408767942
}

shader {
	name "Sphere1222"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1222"
	type sphere
	c 3.06425719504 1.18938518614 0.5
	r 0.0398310166379
}

shader {
	name "Sphere1223"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1223"
	type sphere
	c 3.77478076559 0.886118483726 0.5
	r 0.0654873750683
}

shader {
	name "Sphere1224"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1224"
	type sphere
	c 4.0143819156 0.484822306778 0.5
	r 0.0623421200063
}

shader {
	name "Sphere1225"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1225"
	type sphere
	c 4.68584205935 0.0321693811332 0.5
	r 0.0804834115791
}

shader {
	name "Sphere1226"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1226"
	type sphere
	c 4.95286567317 -0.448920786651 0.5
	r 0.0880370254759
}

shader {
	name "Sphere1227"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1227"
	type sphere
	c 4.72177837105 -0.861496065742 0.5
	r 0.0835878750309
}

shader {
	name "Sphere1228"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1228"
	type sphere
	c 4.4594235166 -1.42763498021 0.5
	r 0.0897553542162
}

shader {
	name "Sphere1229"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1229"
	type sphere
	c 3.89785691614 -2.06099896898 0.5
	r 0.0598892336599
}

shader {
	name "Sphere1230"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1230"
	type sphere
	c 3.7912276714 -2.51159311013 0.5
	r 0.0645742130527
}

shader {
	name "Sphere1231"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1231"
	type sphere
	c 3.54505893267 -2.75656195466 0.5
	r 0.0722326728746
}

shader {
	name "Sphere1232"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1232"
	type sphere
	c 3.39607097621 -2.86352748679 0.5
	r 0.0631296361041
}

shader {
	name "Sphere1233"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1233"
	type sphere
	c 1.99246119427 -3.61036305268 0.5
	r 0.077850285214
}

shader {
	name "Sphere1234"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1234"
	type sphere
	c 1.69923014273 -4.2691274706 0.5
	r 0.0724310455549
}

shader {
	name "Sphere1235"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1235"
	type sphere
	c 1.3803776535 -4.08645885339 0.5
	r 0.069034774732
}

shader {
	name "Sphere1236"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1236"
	type sphere
	c 0.983665361666 -4.53493956052 0.5
	r 0.0778786999172
}

shader {
	name "Sphere1237"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1237"
	type sphere
	c 0.532385322925 -4.72776936009 0.5
	r 0.0964816335153
}

shader {
	name "Sphere1238"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1238"
	type sphere
	c -0.0991904415305 -4.19162799817 0.5
	r 0.103139361495
}

shader {
	name "Sphere1239"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1239"
	type sphere
	c -0.748008052025 -3.44851722407 0.5
	r 0.0958134902445
}

shader {
	name "Sphere1240"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1240"
	type sphere
	c -1.18369052581 -3.22877547242 0.5
	r 0.0677858475133
}

shader {
	name "Sphere1241"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1241"
	type sphere
	c -1.42093178928 -2.95792807409 0.5
	r 0.0650939389061
}

shader {
	name "Sphere1242"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1242"
	type sphere
	c -1.64779242359 -2.64477438219 0.5
	r 0.0653189721917
}

shader {
	name "Sphere1243"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1243"
	type sphere
	c -1.71845833152 -2.49702946021 0.5
	r 0.0543675274269
}

shader {
	name "Sphere1244"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1244"
	type sphere
	c -1.89042870237 -2.26360664485 0.5
	r 0.0573612859946
}

shader {
	name "Sphere1245"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1245"
	type sphere
	c -2.62424603513 -1.91305997102 0.5
	r 0.0402447433237
}

shader {
	name "Sphere1246"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1246"
	type sphere
	c -2.80711595688 -1.70691813112 0.5
	r 0.0475321607572
}

shader {
	name "Sphere1247"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1247"
	type sphere
	c -2.72481090057 -1.46660913263 0.5
	r 0.0494722189233
}

shader {
	name "Sphere1248"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1248"
	type sphere
	c -3.00945568041 -1.36318280623 0.5
	r 0.0582218435204
}

shader {
	name "Sphere1249"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1249"
	type sphere
	c -3.21018054674 -0.962350056269 0.5
	r 0.0545240246976
}

shader {
	name "Sphere1250"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1250"
	type sphere
	c -3.05076556257 -0.28154367409 0.5
	r 0.0476687312786
}

shader {
	name "Sphere1251"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1251"
	type sphere
	c -3.08177861513 0.100298729019 0.5
	r 0.0479943787231
}

shader {
	name "Sphere1252"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1252"
	type sphere
	c -3.26925233283 0.276734835281 0.5
	r 0.0514699732245
}

shader {
	name "Sphere1253"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1253"
	type sphere
	c -3.23014206567 0.41108991183 0.5
	r 0.0525692429034
}

shader {
	name "Sphere1254"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1254"
	type sphere
	c -3.5079442693 1.07415408699 0.5
	r 0.0722275363251
}

shader {
	name "Sphere1255"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1255"
	type sphere
	c -3.37185290151 1.38126051038 0.5
	r 0.0604733184737
}

shader {
	name "Sphere1256"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1256"
	type sphere
	c -3.17884278393 1.69591204631 0.5
	r 0.0574206226438
}

shader {
	name "Sphere1257"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1257"
	type sphere
	c -3.10746977352 2.02806133173 0.5
	r 0.0594670105922
}

shader {
	name "Sphere1258"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1258"
	type sphere
	c -2.74669074575 2.2905299523 0.5
	r 0.062979625242
}

shader {
	name "Sphere1259"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1259"
	type sphere
	c -2.28969141787 2.16025936211 0.5
	r 0.0649434607608
}

shader {
	name "Sphere1260"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1260"
	type sphere
	c -2.24268470742 2.32070384183 0.5
	r 0.0602438596944
}

shader {
	name "Sphere1261"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1261"
	type sphere
	c -1.93494504584 2.41322079402 0.5
	r 0.0595053930089
}

shader {
	name "Sphere1262"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1262"
	type sphere
	c -1.78559058418 2.33599867447 0.5
	r 0.0530345089294
}

shader {
	name "Sphere1263"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1263"
	type sphere
	c -1.50627304772 2.44586286491 0.5
	r 0.0606939426987
}

shader {
	name "Sphere1264"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1264"
	type sphere
	c -1.35510152389 2.45493854479 0.5
	r 0.0348144227401
}

shader {
	name "Sphere1265"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1265"
	type sphere
	c -1.1731409217 2.40493726734 0.5
	r 0.0351723594491
}

shader {
	name "Sphere1266"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1266"
	type sphere
	c -0.850817875224 2.46469177426 0.5
	r 0.036616071942
}

shader {
	name "Sphere1267"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1267"
	type sphere
	c -0.668140270029 2.49565391507 0.5
	r 0.0344658964719
}

shader {
	name "Sphere1268"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1268"
	type sphere
	c -0.500551064081 2.65156040391 0.5
	r 0.0383904531668
}

shader {
	name "Sphere1269"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1269"
	type sphere
	c -0.176387055961 2.49026770983 0.5
	r 0.0277380074314
}

shader {
	name "Sphere1270"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1270"
	type sphere
	c 0.106899468602 2.62374652404 0.5
	r 0.0374075797537
}

shader {
	name "Sphere1271"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1271"
	type sphere
	c 0.503623217222 2.51520946192 0.5
	r 0.0463724022484
}

shader {
	name "Sphere1272"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1272"
	type sphere
	c 0.990820757189 2.34548707924 0.5
	r 0.0489626621079
}

shader {
	name "Sphere1273"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1273"
	type sphere
	c 1.21108822969 2.44487072625 0.5
	r 0.0427144962269
}

shader {
	name "Sphere1274"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1274"
	type sphere
	c 1.74705218934 2.53295425886 0.5
	r 0.0665236558549
}

shader {
	name "Sphere1275"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1275"
	type sphere
	c 2.04780879032 2.35622984825 0.5
	r 0.063936676595
}

shader {
	name "Sphere1276"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1276"
	type sphere
	c 2.31959171899 2.15383627934 0.5
	r 0.0588430671757
}

shader {
	name "Sphere1277"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1277"
	type sphere
	c 2.69020138338 1.9180492059 0.5
	r 0.0647442118748
}

shader {
	name "Sphere1278"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1278"
	type sphere
	c 2.74492391337 1.59239339342 0.5
	r 0.0435949425306
}

shader {
	name "Sphere1279"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1279"
	type sphere
	c 2.96054003159 1.4973767559 0.5
	r 0.0447821399944
}

shader {
	name "Sphere1280"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1280"
	type sphere
	c 3.16732772685 1.35113485931 0.5
	r 0.0437835080444
}

shader {
	name "Sphere1281"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1281"
	type sphere
	c 3.15475970206 1.24005124962 0.5
	r 0.0379586773697
}

shader {
	name "Sphere1282"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1282"
	type sphere
	c 3.62609268796 0.982245061254 0.5
	r 0.0673038544131
}

shader {
	name "Sphere1283"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1283"
	type sphere
	c 4.12890484041 0.607629415327 0.5
	r 0.0635977902571
}

shader {
	name "Sphere1284"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1284"
	type sphere
	c 3.92741505505 0.342570476768 0.5
	r 0.0627052114787
}

shader {
	name "Sphere1285"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1285"
	type sphere
	c 4.57356247656 0.210519236588 0.5
	r 0.077578755951
}

shader {
	name "Sphere1286"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1286"
	type sphere
	c 4.81168413686 -0.137981682549 0.5
	r 0.0782397193139
}

shader {
	name "Sphere1287"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1287"
	type sphere
	c 5.09444049391 -0.648487412199 0.5
	r 0.0954759868565
}

shader {
	name "Sphere1288"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1288"
	type sphere
	c 4.9422131833 -0.873397381747 0.5
	r 0.0819790166607
}

shader {
	name "Sphere1289"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1289"
	type sphere
	c 4.70009582352 -1.38865566695 0.5
	r 0.0931009615841
}

shader {
	name "Sphere1290"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1290"
	type sphere
	c 4.22125126266 -1.46740381566 0.5
	r 0.0913468692292
}

shader {
	name "Sphere1291"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1291"
	type sphere
	c 4.05036405259 -2.00659216821 0.5
	r 0.0615517859051
}

shader {
	name "Sphere1292"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1292"
	type sphere
	c 3.92790316876 -2.39772231299 0.5
	r 0.0688472877835
}

shader {
	name "Sphere1293"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1293"
	type sphere
	c 3.27551333078 -2.98298547603 0.5
	r 0.0641592119925
}

shader {
	name "Sphere1294"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1294"
	type sphere
	c 2.15693696627 -3.749437692 0.5
	r 0.08369427402
}

shader {
	name "Sphere1295"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1295"
	type sphere
	c 1.86533528626 -4.1856343254 0.5
	r 0.0670004376197
}

shader {
	name "Sphere1296"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1296"
	type sphere
	c 1.52226713975 -4.34585489919 0.5
	r 0.0722295538886
}

shader {
	name "Sphere1297"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1297"
	type sphere
	c 1.18479868983 -4.48233994345 0.5
	r 0.0780443617856
}

shader {
	name "Sphere1298"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1298"
	type sphere
	c 0.766698567655 -4.6526747119 0.5
	r 0.0880578483014
}

shader {
	name "Sphere1299"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1299"
	type sphere
	c 0.286871410051 -4.77837223584 0.5
	r 0.0915242826209
}

shader {
	name "Sphere1300"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1300"
	type sphere
	c -0.368531929721 -4.2417399051 0.5
	r 0.102333319823
}

shader {
	name "Sphere1301"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1301"
	type sphere
	c -0.757357745096 -3.69276874989 0.5
	r 0.0875093161714
}

shader {
	name "Sphere1302"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1302"
	type sphere
	c -1.01259398324 -3.19485685765 0.5
	r 0.0630338026188
}

shader {
	name "Sphere1303"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1303"
	type sphere
	c -1.36150466405 -3.26711869057 0.5
	r 0.0686401010868
}

shader {
	name "Sphere1304"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1304"
	type sphere
	c -1.47792534172 -3.11839596333 0.5
	r 0.0626225137533
}

shader {
	name "Sphere1305"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1305"
	type sphere
	c -1.65029079701 -2.81828627318 0.5
	r 0.0648284355
}

shader {
	name "Sphere1306"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1306"
	type sphere
	c -1.86059151663 -2.50524569789 0.5
	r 0.0524103201776
}

shader {
	name "Sphere1307"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1307"
	type sphere
	c -2.55169759127 -1.99439406501 0.5
	r 0.0414966950457
}

shader {
	name "Sphere1308"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1308"
	type sphere
	c -2.70477789838 -1.84642283343 0.5
	r 0.0381504900898
}

shader {
	name "Sphere1309"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1309"
	type sphere
	c -2.89108280915 -1.60702513593 0.5
	r 0.0503393701239
}

shader {
	name "Sphere1310"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1310"
	type sphere
	c -2.8543627411 -1.38179781535 0.5
	r 0.0589327139807
}

shader {
	name "Sphere1311"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1311"
	type sphere
	c -3.16400602604 -1.34000318302 0.5
	r 0.0589873547106
}

shader {
	name "Sphere1312"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1312"
	type sphere
	c -3.28288984365 -1.08171131474 0.5
	r 0.0502983747845
}

shader {
	name "Sphere1313"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1313"
	type sphere
	c -3.1408509152 -0.827439243085 0.5
	r 0.0592377131324
}

shader {
	name "Sphere1314"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1314"
	type sphere
	c -3.01706447726 -0.40242414587 0.5
	r 0.0464491019404
}

shader {
	name "Sphere1315"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1315"
	type sphere
	c -3.08493036709 -0.15924418964 0.5
	r 0.0475676784735
}

shader {
	name "Sphere1316"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1316"
	type sphere
	c -3.20577069574 0.0651047518156 0.5
	r 0.0486731794208
}

shader {
	name "Sphere1317"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1317"
	type sphere
	c -3.57294666076 0.894831593415 0.5
	r 0.0708276995949
}

shader {
	name "Sphere1318"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1318"
	type sphere
	c -3.32346593103 1.53403517619 0.5
	r 0.0597173053405
}

shader {
	name "Sphere1319"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1319"
	type sphere
	c -3.14574383625 1.84247340198 0.5
	r 0.0552686464234
}

shader {
	name "Sphere1320"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1320"
	type sphere
	c -3.06757925637 2.17651491053 0.5
	r 0.0558226967141
}

shader {
	name "Sphere1321"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1321"
	type sphere
	c -2.86716425815 2.40692184053 0.5
	r 0.0626558717128
}

shader {
	name "Sphere1322"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1322"
	type sphere
	c -2.60750569669 2.18339139956 0.5
	r 0.0687540849218
}

shader {
	name "Sphere1323"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1323"
	type sphere
	c -2.20500966327 2.47752144593 0.5
	r 0.060715981055
}

shader {
	name "Sphere1324"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1324"
	type sphere
	c -2.05046173106 2.52046846488 0.5
	r 0.058714610381
}

shader {
	name "Sphere1325"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1325"
	type sphere
	c -1.75755294128 2.47426156343 0.5
	r 0.0527732834738
}

shader {
	name "Sphere1326"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1326"
	type sphere
	c -1.29211675504 2.51830414697 0.5
	r 0.032193284756
}

shader {
	name "Sphere1327"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1327"
	type sphere
	c -1.19478005653 2.49437789541 0.5
	r 0.0338434462341
}

shader {
	name "Sphere1328"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1328"
	type sphere
	c -0.809843498162 2.54593461348 0.5
	r 0.0316269160175
}

shader {
	name "Sphere1329"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1329"
	type sphere
	c -0.593833833239 2.68903862693 0.5
	r 0.0370070890684
}

shader {
	name "Sphere1330"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1330"
	type sphere
	c -0.40896669388 2.6139590841 0.5
	r 0.0358616533053
}

shader {
	name "Sphere1331"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1331"
	type sphere
	c -0.232245709215 2.44128929856 0.5
	r 0.0279798449746
}

shader {
	name "Sphere1332"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1332"
	type sphere
	c -0.122324006506 2.54564115203 0.5
	r 0.030303617049
}

shader {
	name "Sphere1333"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1333"
	type sphere
	c 0.181645479975 2.68276775807 0.5
	r 0.0340216905677
}

shader {
	name "Sphere1334"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1334"
	type sphere
	c 0.416236950233 2.42790923812 0.5
	r 0.0462691106571
}

shader {
	name "Sphere1335"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1335"
	type sphere
	c 0.593859080298 2.59749593768 0.5
	r 0.0452184596387
}

shader {
	name "Sphere1336"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1336"
	type sphere
	c 1.01474904535 2.47170765881 0.5
	r 0.0473888360413
}

shader {
	name "Sphere1337"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1337"
	type sphere
	c 1.89956106494 2.61634907945 0.5
	r 0.0638419068796
}

shader {
	name "Sphere1338"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1338"
	type sphere
	c 2.33364671834 2.30519553723 0.5
	r 0.0551647482394
}

shader {
	name "Sphere1339"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1339"
	type sphere
	c 2.70227041652 2.08232663806 0.5
	r 0.0587959198927
}

shader {
	name "Sphere1340"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1340"
	type sphere
	c 2.64719053317 1.5250087337 0.5
	r 0.0454389533123
}

shader {
	name "Sphere1341"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1341"
	type sphere
	c 2.84090627252 1.66338565718 0.5
	r 0.0459429799634
}

shader {
	name "Sphere1342"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1342"
	type sphere
	c 3.16964874759 1.46835005494 0.5
	r 0.0441451217503
}

shader {
	name "Sphere1343"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1343"
	type sphere
	c 3.15439904847 1.13954586548 0.5
	r 0.0374208460509
}

shader {
	name "Sphere1344"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1344"
	type sphere
	c 3.45724161636 0.911316814275 0.5
	r 0.0700536866499
}

shader {
	name "Sphere1345"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1345"
	type sphere
	c 3.7832788696 1.05795619028 0.5
	r 0.0635484088443
}

shader {
	name "Sphere1346"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1346"
	type sphere
	c 4.08285208697 0.772025638209 0.5
	r 0.0644458467823
}

shader {
	name "Sphere1347"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1347"
	type sphere
	c 4.17317955679 0.449309221514 0.5
	r 0.0596980451627
}

shader {
	name "Sphere1348"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1348"
	type sphere
	c 4.36102882817 0.226412338974 0.5
	r 0.0822665367579
}

shader {
	name "Sphere1349"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1349"
	type sphere
	c 4.7884418132 0.225998537891 0.5
	r 0.0839983623908
}

shader {
	name "Sphere1350"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1350"
	type sphere
	c 5.1858125211 -0.421763831647 0.5
	r 0.0878563384391
}

shader {
	name "Sphere1351"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1351"
	type sphere
	c 4.82333096697 -1.06945614911 0.5
	r 0.0899854045434
}

shader {
	name "Sphere1352"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1352"
	type sphere
	c 4.60973783155 -1.6215771334 0.5
	r 0.094274461405
}

shader {
	name "Sphere1353"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1353"
	type sphere
	c 4.08584227723 -1.84038459626 0.5
	r 0.0659121679654
}

shader {
	name "Sphere1354"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1354"
	type sphere
	c 4.01744081462 -2.1616684169 0.5
	r 0.0573476575782
}

shader {
	name "Sphere1355"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1355"
	type sphere
	c 3.95491280795 -2.57808241606 0.5
	r 0.0679311796588
}

shader {
	name "Sphere1356"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1356"
	type sphere
	c 3.43859962791 -3.02508266682 0.5
	r 0.0621647327055
}

shader {
	name "Sphere1357"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1357"
	type sphere
	c 2.1839331267 -3.53904953996 0.5
	r 0.0753905509861
}

shader {
	name "Sphere1358"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1358"
	type sphere
	c 2.10546869719 -3.95662762685 0.5
	r 0.0764208928206
}

shader {
	name "Sphere1359"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1359"
	type sphere
	c 1.88518088148 -4.01297590366 0.5
	r 0.063345976847
}

shader {
	name "Sphere1360"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1360"
	type sphere
	c 1.86363724126 -4.37269425653 0.5
	r 0.0733002908874
}

shader {
	name "Sphere1361"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1361"
	type sphere
	c 1.67671824763 -4.46031609383 0.5
	r 0.0719510161092
}

shader {
	name "Sphere1362"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1362"
	type sphere
	c 1.2471689965 -4.28429938999 0.5
	r 0.0776779559248
}

shader {
	name "Sphere1363"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1363"
	type sphere
	c 1.12739609011 -4.67453474297 0.5
	r 0.0723935603665
}

shader {
	name "Sphere1364"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1364"
	type sphere
	c 0.727329616412 -4.89533027387 0.5
	r 0.0963135033067
}

shader {
	name "Sphere1365"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1365"
	type sphere
	c 0.448169876798 -4.97357326862 0.5
	r 0.0983911174854
}

shader {
	name "Sphere1366"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1366"
	type sphere
	c 0.130670302047 -4.59770010052 0.5
	r 0.0876004748113
}

shader {
	name "Sphere1367"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1367"
	type sphere
	c -0.193780021995 -4.43775562604 0.5
	r 0.0946190108624
}

shader {
	name "Sphere1368"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1368"
	type sphere
	c -0.558242066731 -4.03055683094 0.5
	r 0.110577172232
}

shader {
	name "Sphere1369"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1369"
	type sphere
	c -0.951471287514 -3.57360961745 0.5
	r 0.0833178435069
}

shader {
	name "Sphere1370"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1370"
	type sphere
	c -1.06188661649 -3.36162473683 0.5
	r 0.067391368214
}

shader {
	name "Sphere1371"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1371"
	type sphere
	c -1.24009405177 -3.39349130871 0.5
	r 0.0627931468234
}

shader {
	name "Sphere1372"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1372"
	type sphere
	c -1.58886981502 -2.9921220801 0.5
	r 0.063443919048
}

shader {
	name "Sphere1373"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1373"
	type sphere
	c -1.79686781433 -2.73004794064 0.5
	r 0.0634869542663
}

shader {
	name "Sphere1374"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1374"
	type sphere
	c -2.44683033673 -1.97262158859 0.5
	r 0.0388310073072
}

shader {
	name "Sphere1375"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1375"
	type sphere
	c -2.66308439228 -2.01840455246 0.5
	r 0.0439622521592
}

shader {
	name "Sphere1376"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1376"
	type sphere
	c -2.93314034382 -1.73250229692 0.5
	r 0.048914152285
}

shader {
	name "Sphere1377"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1377"
	type sphere
	c -3.10545823367 -1.48324967164 0.5
	r 0.0570747527024
}

shader {
	name "Sphere1378"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1378"
	type sphere
	c -3.34806015703 -0.966564811284 0.5
	r 0.0489339860618
}

shader {
	name "Sphere1379"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1379"
	type sphere
	c -3.29021337205 -0.842800880555 0.5
	r 0.0533750389218
}

shader {
	name "Sphere1380"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1380"
	type sphere
	c -2.89852728955 -0.434093004056 0.5
	r 0.0455718987366
}

shader {
	name "Sphere1381"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1381"
	type sphere
	c -3.13875903299 -0.372909605106 0.5
	r 0.0474677685798
}

shader {
	name "Sphere1382"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1382"
	type sphere
	c -3.16975468557 -0.248726033563 0.5
	r 0.044905117726
}

shader {
	name "Sphere1383"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1383"
	type sphere
	c -3.11338780326 -0.0211162439904 0.5
	r 0.0461021900261
}

shader {
	name "Sphere1384"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1384"
	type sphere
	c -3.45241599939 0.739948445758 0.5
	r 0.076364323759
}

shader {
	name "Sphere1385"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1385"
	type sphere
	c -3.6991004684 1.03999207087 0.5
	r 0.073411062226
}

shader {
	name "Sphere1386"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1386"
	type sphere
	c -3.48188869001 1.50123187792 0.5
	r 0.0616201482911
}

shader {
	name "Sphere1387"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1387"
	type sphere
	c -3.29120369489 1.80129317745 0.5
	r 0.058113845698
}

shader {
	name "Sphere1388"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1388"
	type sphere
	c -3.21177908848 2.14061960737 0.5
	r 0.0556275666635
}

shader {
	name "Sphere1389"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1389"
	type sphere
	c -3.03730847707 2.36959310808 0.5
	r 0.0679873460301
}

shader {
	name "Sphere1390"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1390"
	type sphere
	c -2.70728376762 2.45248129785 0.5
	r 0.0620279580965
}

shader {
	name "Sphere1391"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1391"
	type sphere
	c -2.35630669812 2.43030075235 0.5
	r 0.0581550835293
}

shader {
	name "Sphere1392"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1392"
	type sphere
	c -1.89994388006 2.56831400615 0.5
	r 0.0597398570276
}

shader {
	name "Sphere1393"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1393"
	type sphere
	c -1.37729260704 2.54500167541 0.5
	r 0.0347531276278
}

shader {
	name "Sphere1394"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1394"
	type sphere
	c -1.10797477973 2.46984603394 0.5
	r 0.0338104130243
}

shader {
	name "Sphere1395"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1395"
	type sphere
	c -0.898273506261 2.5470934416 0.5
	r 0.0347012844965
}

shader {
	name "Sphere1396"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1396"
	type sphere
	c -0.674996913468 2.63070021141 0.5
	r 0.0379584642109
}

shader {
	name "Sphere1397"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1397"
	type sphere
	c -0.518193644615 2.74721896458 0.5
	r 0.0345634654647
}

shader {
	name "Sphere1398"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1398"
	type sphere
	c -0.418071142519 2.71304521322 0.5
	r 0.0387659922585
}

shader {
	name "Sphere1399"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1399"
	type sphere
	c -0.391127886701 2.52308835541 0.5
	r 0.0335922033918
}

shader {
	name "Sphere1400"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1400"
	type sphere
	c -0.244260429088 2.51180355101 0.5
	r 0.025668034545
}

shader {
	name "Sphere1401"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1401"
	type sphere
	c -0.046615096556 2.52064988167 0.5
	r 0.0294916711024
}

shader {
	name "Sphere1402"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1402"
	type sphere
	c 0.0993786380498 2.71710315344 0.5
	r 0.0328367297615
}

shader {
	name "Sphere1403"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1403"
	type sphere
	c 0.266855798844 2.65419828851 0.5
	r 0.0333824623531
}

shader {
	name "Sphere1404"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1404"
	type sphere
	c 0.481853681558 2.6319071821 0.5
	r 0.042660750007
}

shader {
	name "Sphere1405"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1405"
	type sphere
	c 0.710135129911 2.56226583798 0.5
	r 0.045903545368
}

shader {
	name "Sphere1406"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1406"
	type sphere
	c 0.89758835253 2.43062157592 0.5
	r 0.0457281090293
}

shader {
	name "Sphere1407"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1407"
	type sphere
	c 1.7546390409 2.70764867245 0.5
	r 0.0646206554277
}

shader {
	name "Sphere1408"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1408"
	type sphere
	c 2.04902424298 2.53186629914 0.5
	r 0.0649236833931
}

shader {
	name "Sphere1409"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1409"
	type sphere
	c 2.21914883568 2.38840054169 0.5
	r 0.0509883078608
}

shader {
	name "Sphere1410"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1410"
	type sphere
	c 2.46153612907 2.22201060508 0.5
	r 0.0592574165759
}

shader {
	name "Sphere1411"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1411"
	type sphere
	c 2.82860909228 1.99798789142 0.5
	r 0.0551312406616
}

shader {
	name "Sphere1412"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1412"
	type sphere
	c 2.73078447218 1.70674075381 0.5
	r 0.0428187368053
}

shader {
	name "Sphere1413"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1413"
	type sphere
	c 3.26916085835 1.40726970428 0.5
	r 0.043426714766
}

shader {
	name "Sphere1414"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1414"
	type sphere
	c 3.24433440684 1.18874249771 0.5
	r 0.0394630338319
}

shader {
	name "Sphere1415"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1415"
	type sphere
	c 3.48463651306 1.09189399267 0.5
	r 0.0669288349298
}

shader {
	name "Sphere1416"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1416"
	type sphere
	c 3.92262680565 0.967455132898 0.5
	r 0.0610696571697
}

shader {
	name "Sphere1417"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1417"
	type sphere
	c 4.25463079077 0.730285903273 0.5
	r 0.0681369473926
}

shader {
	name "Sphere1418"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1418"
	type sphere
	c 4.28476393271 0.560603634518 0.5
	r 0.0585013821418
}

shader {
	name "Sphere1419"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1419"
	type sphere
	c 4.48795966454 0.40867836729 0.5
	r 0.0843151025174
}

shader {
	name "Sphere1420"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1420"
	type sphere
	c 5.04535972262 -0.227524599384 0.5
	r 0.0919183141731
}

shader {
	name "Sphere1421"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1421"
	type sphere
	c 5.33991031647 -0.604695031774 0.5
	r 0.0915331802523
}

shader {
	name "Sphere1422"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1422"
	type sphere
	c 5.06206194942 -1.06743251393 0.5
	r 0.0890692647826
}

shader {
	name "Sphere1423"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1423"
	type sphere
	c 4.86368410328 -1.58438533266 0.5
	r 0.0982170076798
}

shader {
	name "Sphere1424"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1424"
	type sphere
	c 4.21359699062 -1.96057909354 0.5
	r 0.0656438694597
}

shader {
	name "Sphere1425"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1425"
	type sphere
	c 3.87198607778 -2.21840405478 0.5
	r 0.0597484881931
}

shader {
	name "Sphere1426"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1426"
	type sphere
	c 4.08914587329 -2.46696232577 0.5
	r 0.0627630514323
}

shader {
	name "Sphere1427"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1427"
	type sphere
	c 3.81200007444 -2.68338243429 0.5
	r 0.0652062702674
}

shader {
	name "Sphere1428"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1428"
	type sphere
	c 3.32141258156 -3.15317089723 0.5
	r 0.0680405349064
}

shader {
	name "Sphere1429"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1429"
	type sphere
	c 2.02902032438 -3.40636476086 0.5
	r 0.0775859673062
}

shader {
	name "Sphere1430"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1430"
	type sphere
	c 2.34527479532 -3.65590346618 0.5
	r 0.0740194902936
}

shader {
	name "Sphere1431"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1431"
	type sphere
	c 2.29987820118 -3.90458053811 0.5
	r 0.0745210646117
}

shader {
	name "Sphere1432"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1432"
	type sphere
	c 2.02486555086 -4.27227954658 0.5
	r 0.0691556532025
}

shader {
	name "Sphere1433"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1433"
	type sphere
	c 1.50074362332 -4.53695842932 0.5
	r 0.0720042816203
}

shader {
	name "Sphere1434"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1434"
	type sphere
	c 1.32515532815 -4.6369685369 0.5
	r 0.0785781722115
}

shader {
	name "Sphere1435"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1435"
	type sphere
	c 0.947534722035 -4.79582338946 0.5
	r 0.0849196299233
}

shader {
	name "Sphere1436"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1436"
	type sphere
	c 0.187536533259 -5.01255110742 0.5
	r 0.0992577354608
}

shader {
	name "Sphere1437"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1437"
	type sphere
	c -0.440644595025 -4.49550866584 0.5
	r 0.0955285928581
}

shader {
	name "Sphere1438"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1438"
	type sphere
	c -0.635882659758 -4.30569876927 0.5
	r 0.103837777571
}

shader {
	name "Sphere1439"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1439"
	type sphere
	c -0.964069888178 -3.80100829908 0.5
	r 0.0874927179175
}

shader {
	name "Sphere1440"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1440"
	type sphere
	c -1.39799789499 -3.4339838068 0.5
	r 0.0594666674404
}

shader {
	name "Sphere1441"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1441"
	type sphere
	c -1.6383495178 -3.14889106154 0.5
	r 0.0598501376741
}

shader {
	name "Sphere1442"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1442"
	type sphere
	c -1.79829880405 -2.89492688145 0.5
	r 0.0601769086044
}

shader {
	name "Sphere1443"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1443"
	type sphere
	c -2.47727909867 -2.0721215366 0.5
	r 0.0392099678356
}

shader {
	name "Sphere1444"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1444"
	type sphere
	c -2.58495050955 -2.09568159345 0.5
	r 0.0384580890275
}

shader {
	name "Sphere1445"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1445"
	type sphere
	c -2.84715420307 -1.82390505134 0.5
	r 0.0452043631766
}

shader {
	name "Sphere1446"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1446"
	type sphere
	c -3.02215309917 -1.63489489466 0.5
	r 0.0501610339129
}

shader {
	name "Sphere1447"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1447"
	type sphere
	c -3.25647655614 -1.46411856313 0.5
	r 0.0570942003055
}

shader {
	name "Sphere1448"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1448"
	type sphere
	c -3.41727635406 -1.07964628835 0.5
	r 0.0505034067671
}

shader {
	name "Sphere1449"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1449"
	type sphere
	c -3.23597109468 -0.710935359382 0.5
	r 0.0535643898928
}

shader {
	name "Sphere1450"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1450"
	type sphere
	c -2.98251158292 -0.515101035384 0.5
	r 0.0419427300629
}

shader {
	name "Sphere1451"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1451"
	type sphere
	c -3.10223721529 -0.493743597984 0.5
	r 0.0472067637103
}

shader {
	name "Sphere1452"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1452"
	type sphere
	c -3.20491242376 -0.135236794724 0.5
	r 0.0442025646657
}

shader {
	name "Sphere1453"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1453"
	type sphere
	c -3.64362319587 0.724457958449 0.5
	r 0.0675109096603
}

shader {
	name "Sphere1454"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1454"
	type sphere
	c -3.63056360308 1.2171211497 0.5
	r 0.0690336885274
}

shader {
	name "Sphere1455"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1455"
	type sphere
	c -3.42879163152 1.65633349438 0.5
	r 0.0613336747087
}

shader {
	name "Sphere1456"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1456"
	type sphere
	c -3.24934669007 1.94450509588 0.5
	r 0.0537887240657
}

shader {
	name "Sphere1457"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1457"
	type sphere
	c -2.97691669121 2.5333028345 0.5
	r 0.0628829095939
}

shader {
	name "Sphere1458"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1458"
	type sphere
	c -2.32540398458 2.58569820596 0.5
	r 0.0606751831929
}

shader {
	name "Sphere1459"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1459"
	type sphere
	c -2.01544178372 2.66666483831 0.5
	r 0.0540345544816
}

shader {
	name "Sphere1460"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1460"
	type sphere
	c -1.30970294572 2.60045932494 0.5
	r 0.0308189790946
}

shader {
	name "Sphere1461"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1461"
	type sphere
	c -1.12916484833 2.56054323383 0.5
	r 0.0360443513404
}

shader {
	name "Sphere1462"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1462"
	type sphere
	c -1.08605035208 2.38514126906 0.5
	r 0.0318117057154
}

shader {
	name "Sphere1463"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1463"
	type sphere
	c -0.942211222241 2.46971997965 0.5
	r 0.0320325990918
}

shader {
	name "Sphere1464"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1464"
	type sphere
	c -0.848930257445 2.62346565954 0.5
	r 0.0334929449589
}

shader {
	name "Sphere1465"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1465"
	type sphere
	c -0.683899959067 2.73088790205 0.5
	r 0.0374784043378
}

shader {
	name "Sphere1466"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1466"
	type sphere
	c -0.601306412282 2.78215383848 0.5
	r 0.0330538391234
}

shader {
	name "Sphere1467"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1467"
	type sphere
	c -0.330009049353 2.66737412634 0.5
	r 0.0356345385963
}

shader {
	name "Sphere1468"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1468"
	type sphere
	c -0.195378584077 2.55683168457 0.5
	r 0.0241771684922
}

shader {
	name "Sphere1469"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1469"
	type sphere
	c -0.0611454078646 2.60027435442 0.5
	r 0.0312128795271
}

shader {
	name "Sphere1470"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1470"
	type sphere
	c 0.0283853072966 2.67015778257 0.5
	r 0.0309966900308
}

shader {
	name "Sphere1471"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1471"
	type sphere
	c 0.167222338502 2.76786808564 0.5
	r 0.0307137493307
}

shader {
	name "Sphere1472"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1472"
	type sphere
	c 0.397153407533 2.56052949668 0.5
	r 0.0404130852098
}

shader {
	name "Sphere1473"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1473"
	type sphere
	c 0.563031345932 2.70782783189 0.5
	r 0.0406998463195
}

shader {
	name "Sphere1474"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1474"
	type sphere
	c 0.679999458551 2.67532382423 0.5
	r 0.0418505152532
}

shader {
	name "Sphere1475"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1475"
	type sphere
	c 0.919656437376 2.54874657554 0.5
	r 0.0443984142439
}

shader {
	name "Sphere1476"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1476"
	type sphere
	c 1.5985675204 2.62946857001 0.5
	r 0.0662977426696
}

shader {
	name "Sphere1477"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1477"
	type sphere
	c 1.90316607999 2.78086296115 0.5
	r 0.0595731247854
}

shader {
	name "Sphere1478"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1478"
	type sphere
	c 2.04345122694 2.69930795122 0.5
	r 0.0607270946178
}

shader {
	name "Sphere1479"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1479"
	type sphere
	c 2.34160446243 2.44576503931 0.5
	r 0.0504311783676
}

shader {
	name "Sphere1480"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1480"
	type sphere
	c 2.84236738092 2.14660549778 0.5
	r 0.0568085731997
}

shader {
	name "Sphere1481"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1481"
	type sphere
	c 2.83554465638 1.85083679829 0.5
	r 0.0553545945027
}

shader {
	name "Sphere1482"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1482"
	type sphere
	c 3.27512881987 1.52671247487 0.5
	r 0.0462671144877
}

shader {
	name "Sphere1483"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1483"
	type sphere
	c 3.9298217971 1.12523543173 0.5
	r 0.0573885410009
}

shader {
	name "Sphere1484"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1484"
	type sphere
	c 4.19878347241 0.895011161833 0.5
	r 0.0623141938396
}

shader {
	name "Sphere1485"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1485"
	type sphere
	c 5.27732905139 -0.214092550078 0.5
	r 0.08235010396
}

shader {
	name "Sphere1486"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1486"
	type sphere
	c 5.26083927964 -0.841100443744 0.5
	r 0.095425660317
}

shader {
	name "Sphere1487"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1487"
	type sphere
	c 4.945690311 -1.27671801724 0.5
	r 0.090528379469
}

shader {
	name "Sphere1488"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1488"
	type sphere
	c 4.76502919356 -1.83388886782 0.5
	r 0.103007873895
}

shader {
	name "Sphere1489"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1489"
	type sphere
	c 4.26005482167 -1.78375127079 0.5
	r 0.071477810233
}

shader {
	name "Sphere1490"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1490"
	type sphere
	c 4.12090058022 -2.63136189462 0.5
	r 0.0628156631334
}

shader {
	name "Sphere1491"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1491"
	type sphere
	c 3.96746484184 -2.7506556878 0.5
	r 0.0618406848447
}

shader {
	name "Sphere1492"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1492"
	type sphere
	c 3.49507505135 -3.18385572133 0.5
	r 0.0642238562307
}

shader {
	name "Sphere1493"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1493"
	type sphere
	c 3.1546548242 -3.10163462126 0.5
	r 0.0628643056287
}

shader {
	name "Sphere1494"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1494"
	type sphere
	c 2.251139583 -4.10169382773 0.5
	r 0.0777660648188
}

shader {
	name "Sphere1495"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1495"
	type sphere
	c 2.03581643801 -4.45905720501 0.5
	r 0.0711681554901
}

shader {
	name "Sphere1496"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1496"
	type sphere
	c 1.65589957588 -4.65268048115 0.5
	r 0.0731647289447
}

shader {
	name "Sphere1497"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1497"
	type sphere
	c 1.2513587532 -4.83283615885 0.5
	r 0.0784032236195
}

shader {
	name "Sphere1498"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1498"
	type sphere
	c 0.931378632519 -5.01826706238 0.5
	r 0.0823525774269
}

shader {
	name "Sphere1499"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1499"
	type sphere
	c 0.351730605615 -5.21195022747 0.5
	r 0.0944684440845
}

shader {
	name "Sphere1500"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1500"
	type sphere
	c -0.264787506071 -4.68530059274 0.5
	r 0.0985268472298
}

shader {
	name "Sphere1501"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1501"
	type sphere
	c -0.846684771285 -4.10728955191 0.5
	r 0.113278799669
}

shader {
	name "Sphere1502"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1502"
	type sphere
	c -1.1593816467 -3.67045643051 0.5
	r 0.0887021778353
}

shader {
	name "Sphere1503"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1503"
	type sphere
	c -1.51743023095 -3.33238288635 0.5
	r 0.0581347433694
}

shader {
	name "Sphere1504"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1504"
	type sphere
	c -1.94387048746 -2.81571298402 0.5
	r 0.0641195135588
}

shader {
	name "Sphere1505"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1505"
	type sphere
	c -2.3721201886 -2.04934802124 0.5
	r 0.0414874857776
}

shader {
	name "Sphere1506"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1506"
	type sphere
	c -2.68313718951 -2.12695295153 0.5
	r 0.0388265705166
}

shader {
	name "Sphere1507"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1507"
	type sphere
	c -2.96570211275 -1.85606212108 0.5
	r 0.0469195873649
}

shader {
	name "Sphere1508"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1508"
	type sphere
	c -3.05775538245 -1.75893734021 0.5
	r 0.0466268972371
}

shader {
	name "Sphere1509"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1509"
	type sphere
	c -3.19751050938 -1.60447950562 0.5
	r 0.0570886846913
}

shader {
	name "Sphere1510"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1510"
	type sphere
	c -3.31367734159 -1.32802522082 0.5
	r 0.053625024852
}

shader {
	name "Sphere1511"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1511"
	type sphere
	c -3.47644524417 -0.963309586194 0.5
	r 0.047385775609
}

shader {
	name "Sphere1512"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1512"
	type sphere
	c -3.37343091111 -0.731746747135 0.5
	r 0.0507053429377
}

shader {
	name "Sphere1513"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1513"
	type sphere
	c -3.09003067904 -0.678917553078 0.5
	r 0.0584941058597
}

shader {
	name "Sphere1514"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1514"
	type sphere
	c -2.87528358478 -0.549093420061 0.5
	r 0.0424225220513
}

shader {
	name "Sphere1515"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1515"
	type sphere
	c -3.23126478044 -0.467185483835 0.5
	r 0.0515925954661
}

shader {
	name "Sphere1516"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1516"
	type sphere
	c -3.28843089366 -0.222300601345 0.5
	r 0.0462818853606
}

shader {
	name "Sphere1517"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1517"
	type sphere
	c -3.54678712178 0.579897687826 0.5
	r 0.0629867133528
}

shader {
	name "Sphere1518"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1518"
	type sphere
	c -3.81186660884 1.1915781423 0.5
	r 0.0682864270158
}

shader {
	name "Sphere1519"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1519"
	type sphere
	c -3.5865510098 1.62409805327 0.5
	r 0.0594306375576
}

shader {
	name "Sphere1520"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1520"
	type sphere
	c -3.38603216634 1.9125007929 0.5
	r 0.0514980134336
}

shader {
	name "Sphere1521"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1521"
	type sphere
	c -3.14181135887 2.50821329361 0.5
	r 0.0622114618747
}

shader {
	name "Sphere1522"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1522"
	type sphere
	c -2.47629133362 2.53150224967 0.5
	r 0.0595687729967
}

shader {
	name "Sphere1523"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1523"
	type sphere
	c -2.17279057946 2.63454421864 0.5
	r 0.059504645448
}

shader {
	name "Sphere1524"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1524"
	type sphere
	c -1.8772289538 2.72384502828 0.5
	r 0.0581458928784
}

shader {
	name "Sphere1525"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1525"
	type sphere
	c -1.38641615225 2.63317412709 0.5
	r 0.0317292867833
}

shader {
	name "Sphere1526"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1526"
	type sphere
	c -1.22822706518 2.57685269213 0.5
	r 0.0328011484209
}

shader {
	name "Sphere1527"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1527"
	type sphere
	c -1.03609403082 2.53130902505 0.5
	r 0.0371212759722
}

shader {
	name "Sphere1528"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1528"
	type sphere
	c -0.935580788735 2.62717004987 0.5
	r 0.0315543136909
}

shader {
	name "Sphere1529"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1529"
	type sphere
	c -0.762571189852 2.67402965171 0.5
	r 0.0353219256149
}

shader {
	name "Sphere1530"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1530"
	type sphere
	c -0.532729416706 2.83398117055 0.5
	r 0.0314150923703
}

shader {
	name "Sphere1531"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1531"
	type sphere
	c -0.333432213554 2.75985747892 0.5
	r 0.033775473751
}

shader {
	name "Sphere1532"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1532"
	type sphere
	c -0.258513975912 2.57932642652 0.5
	r 0.0260901295617
}

shader {
	name "Sphere1533"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1533"
	type sphere
	c -0.142022787668 2.6273911908 0.5
	r 0.0327638058799
}

shader {
	name "Sphere1534"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1534"
	type sphere
	c 0.016218115868 2.57090204758 0.5
	r 0.0308509107023
}

shader {
	name "Sphere1535"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1535"
	type sphere
	c 0.021729966264 2.75296919057 0.5
	r 0.0313121204051
}

shader {
	name "Sphere1536"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1536"
	type sphere
	c 0.0913198100619 2.80334039356 0.5
	r 0.0321229965266
}

shader {
	name "Sphere1537"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1537"
	type sphere
	c 0.248513439815 2.74240256439 0.5
	r 0.0331761086905
}

shader {
	name "Sphere1538"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1538"
	type sphere
	c 0.374070531336 2.66913947446 0.5
	r 0.0428637565659
}

shader {
	name "Sphere1539"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1539"
	type sphere
	c 0.792213762396 2.65031375003 0.5
	r 0.044375200239
}

shader {
	name "Sphere1540"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1540"
	type sphere
	c 1.0296618162 2.59357437423 0.5
	r 0.0446929834024
}

shader {
	name "Sphere1541"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1541"
	type sphere
	c 1.59178347018 2.45709336646 0.5
	r 0.0630837444176
}

shader {
	name "Sphere1542"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1542"
	type sphere
	c 1.61250834827 2.80141397308 0.5
	r 0.0630844708652
}

shader {
	name "Sphere1543"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1543"
	type sphere
	c 1.77165625582 2.87559718846 0.5
	r 0.0619856750529
}

shader {
	name "Sphere1544"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1544"
	type sphere
	c 2.18586733886 2.62568543393 0.5
	r 0.0595131897779
}

shader {
	name "Sphere1545"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1545"
	type sphere
	c 2.46120197009 2.37486861512 0.5
	r 0.0538427401182
}

shader {
	name "Sphere1546"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1546"
	type sphere
	c 2.72128345972 2.23185795964 0.5
	r 0.0542555085326
}

shader {
	name "Sphere1547"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1547"
	type sphere
	c 2.97005151694 2.05751338164 0.5
	r 0.0599619800656
}

shader {
	name "Sphere1548"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1548"
	type sphere
	c 3.17212931972 1.58275077144 0.5
	r 0.0416755832737
}

shader {
	name "Sphere1549"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1549"
	type sphere
	c 3.37602556858 1.45798998468 0.5
	r 0.0452910674984
}

shader {
	name "Sphere1550"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1550"
	type sphere
	c 3.80863524783 1.21486274694 0.5
	r 0.0556582187412
}

shader {
	name "Sphere1551"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1551"
	type sphere
	c 4.05844010992 1.04510633491 0.5
	r 0.0562639124862
}

shader {
	name "Sphere1552"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1552"
	type sphere
	c 4.36715280382 0.868480554548 0.5
	r 0.0655208913134
}

shader {
	name "Sphere1553"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1553"
	type sphere
	c 5.16247039322 -0.0199381375728 0.5
	r 0.0868384050454
}

shader {
	name "Sphere1554"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1554"
	type sphere
	c 5.49927564154 -0.784099447887 0.5
	r 0.0884406480883
}

shader {
	name "Sphere1555"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1555"
	type sphere
	c 5.17953793999 -1.26758427368 0.5
	r 0.084991072745
}

shader {
	name "Sphere1556"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1556"
	type sphere
	c 5.03472176622 -1.78935409803 0.5
	r 0.1020007944
}

shader {
	name "Sphere1557"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1557"
	type sphere
	c 4.5077861226 -1.84529267948 0.5
	r 0.0901139141479
}

shader {
	name "Sphere1558"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1558"
	type sphere
	c 4.25648618336 -2.51983128553 0.5
	r 0.068856940527
}

shader {
	name "Sphere1559"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1559"
	type sphere
	c 3.83643345936 -2.85136348078 0.5
	r 0.0621052572178
}

shader {
	name "Sphere1560"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1560"
	type sphere
	c 3.59825146846 -3.0548931692 0.5
	r 0.0596436173209
}

shader {
	name "Sphere1561"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1561"
	type sphere
	c 3.38698723631 -3.31778004417 0.5
	r 0.0648517756895
}

shader {
	name "Sphere1562"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1562"
	type sphere
	c 3.19043704347 -3.25929969456 0.5
	r 0.0583915661403
}

shader {
	name "Sphere1563"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1563"
	type sphere
	c 2.44875546054 -4.04148740926 0.5
	r 0.0771717515247
}

shader {
	name "Sphere1564"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1564"
	type sphere
	c 2.1879973382 -4.35378574093 0.5
	r 0.0676144910731
}

shader {
	name "Sphere1565"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1565"
	type sphere
	c 1.87630570807 -4.56867094447 0.5
	r 0.0739890014946
}

shader {
	name "Sphere1566"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1566"
	type sphere
	c 1.46026643771 -4.79996191167 0.5
	r 0.080205617362
}

shader {
	name "Sphere1567"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1567"
	type sphere
	c 0.741005307978 -5.13898022152 0.5
	r 0.0867115792907
}

shader {
	name "Sphere1568"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1568"
	type sphere
	c 0.102676282453 -5.25794373357 0.5
	r 0.0954807475437
}

shader {
	name "Sphere1569"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1569"
	type sphere
	c -0.512490652637 -4.7331763746 0.5
	r 0.0906887133369
}

shader {
	name "Sphere1570"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1570"
	type sphere
	c -0.900699869685 -4.39397718894 0.5
	r 0.105520036122
}

shader {
	name "Sphere1571"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1571"
	type sphere
	c -1.17863572089 -3.91363846767 0.5
	r 0.0942551264631
}

shader {
	name "Sphere1572"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1572"
	type sphere
	c -1.54269005429 -3.48043230853 0.5
	r 0.0545068926736
}

shader {
	name "Sphere1573"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1573"
	type sphere
	c -1.93347174872 -2.98076976862 0.5
	r 0.0599185056041
}

shader {
	name "Sphere1574"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1574"
	type sphere
	c -2.40855136123 -2.14928192525 0.5
	r 0.0382880350528
}

shader {
	name "Sphere1575"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1575"
	type sphere
	c -2.60787282472 -2.19193143748 0.5
	r 0.0357482049583
}

shader {
	name "Sphere1576"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1576"
	type sphere
	c -2.767306971 -2.06219273989 0.5
	r 0.0408234193409
}

shader {
	name "Sphere1577"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1577"
	type sphere
	c -2.87590503965 -1.94366725129 0.5
	r 0.047169319586
}

shader {
	name "Sphere1578"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1578"
	type sphere
	c -3.34394731855 -1.5834394169 0.5
	r 0.0538667736344
}

shader {
	name "Sphere1579"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1579"
	type sphere
	c -3.40392436211 -1.44103017291 0.5
	r 0.0548391959778
}

shader {
	name "Sphere1580"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1580"
	type sphere
	c -3.23601237838 -1.21434602337 0.5
	r 0.0496323168885
}

shader {
	name "Sphere1581"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1581"
	type sphere
	c -3.55270315357 -1.07053376825 0.5
	r 0.05129636743
}

shader {
	name "Sphere1582"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1582"
	type sphere
	c -3.32668470101 -0.601785592628 0.5
	r 0.0528791601732
}

shader {
	name "Sphere1583"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1583"
	type sphere
	c -3.31914515444 -0.105442989666 0.5
	r 0.0443380644988
}

shader {
	name "Sphere1584"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1584"
	type sphere
	c -3.3793062513 0.569296926028 0.5
	r 0.0628753051336
}

shader {
	name "Sphere1585"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1585"
	type sphere
	c -3.72018375425 0.561054845598 0.5
	r 0.0678263698231
}

shader {
	name "Sphere1586"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1586"
	type sphere
	c -3.88664810939 1.02653227539 0.5
	r 0.0676114434331
}

shader {
	name "Sphere1587"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1587"
	type sphere
	c -3.74401491345 1.35911157904 0.5
	r 0.067277613424
}

shader {
	name "Sphere1588"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1588"
	type sphere
	c -3.53816777875 1.77675910828 0.5
	r 0.0606779104494
}

shader {
	name "Sphere1589"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1589"
	type sphere
	c -3.34829456628 2.0458420337 0.5
	r 0.052435894832
}

shader {
	name "Sphere1590"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1590"
	type sphere
	c -3.20715938914 2.35948639889 0.5
	r 0.0596261576409
}

shader {
	name "Sphere1591"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1591"
	type sphere
	c -3.08137077687 2.65956070331 0.5
	r 0.0600157653923
}

shader {
	name "Sphere1592"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1592"
	type sphere
	c -2.50185949689 2.3765534179 0.5
	r 0.0582143547687
}

shader {
	name "Sphere1593"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1593"
	type sphere
	c -2.44944928818 2.68952918944 0.5
	r 0.0606490194323
}

shader {
	name "Sphere1594"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1594"
	type sphere
	c -2.29012596849 2.7434503634 0.5
	r 0.0605612939822
}

shader {
	name "Sphere1595"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1595"
	type sphere
	c -1.99727041728 2.80475677672 0.5
	r 0.0504272322204
}

shader {
	name "Sphere1596"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1596"
	type sphere
	c -1.75216610067 2.62832061189 0.5
	r 0.05988235645
}

shader {
	name "Sphere1597"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1597"
	type sphere
	c -1.4548758595 2.58544047755 0.5
	r 0.030864190984
}

shader {
	name "Sphere1598"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1598"
	type sphere
	c -1.31704684954 2.68631905145 0.5
	r 0.0338109433624
}

shader {
	name "Sphere1599"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1599"
	type sphere
	c -1.05813329929 2.62878608085 0.5
	r 0.0378318559939
}

shader {
	name "Sphere1600"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1600"
	type sphere
	c -0.891633545882 2.70030578046 0.5
	r 0.0324387314349
}

shader {
	name "Sphere1601"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1601"
	type sphere
	c -0.776085723468 2.7705813556 0.5
	r 0.0377977824345
}

shader {
	name "Sphere1602"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1602"
	type sphere
	c -0.609674646507 2.86810482108 0.5
	r 0.0317142031422
}

shader {
	name "Sphere1603"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1603"
	type sphere
	c -0.453411611486 2.80682883494 0.5
	r 0.0314623041975
}

shader {
	name "Sphere1604"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1604"
	type sphere
	c -0.248363560578 2.71926073213 0.5
	r 0.0369188259345
}

shader {
	name "Sphere1605"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1605"
	type sphere
	c -0.309142922854 2.53280246239 0.5
	r 0.0254789536905
}

shader {
	name "Sphere1606"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1606"
	type sphere
	c -0.0757127389297 2.68440539174 0.5
	r 0.0328242909104
}

shader {
	name "Sphere1607"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1607"
	type sphere
	c 0.160620422157 2.84835694521 0.5
	r 0.0298556201658
}

shader {
	name "Sphere1608"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1608"
	type sphere
	c 0.753284376509 2.75465423645 0.5
	r 0.0391494621886
}

shader {
	name "Sphere1609"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1609"
	type sphere
	c 0.933568419156 2.67091617471 0.5
	r 0.0478209532194
}

shader {
	name "Sphere1610"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1610"
	type sphere
	c 1.45147987706 2.54476996782 0.5
	r 0.0610005419589
}

shader {
	name "Sphere1611"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1611"
	type sphere
	c 1.46252900385 2.73121551566 0.5
	r 0.061111605107
}

shader {
	name "Sphere1612"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1612"
	type sphere
	c 1.91712819004 2.93362957536 0.5
	r 0.0554793660652
}

shader {
	name "Sphere1613"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1613"
	type sphere
	c 2.1789525461 2.78337831406 0.5
	r 0.0588701201826
}

shader {
	name "Sphere1614"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1614"
	type sphere
	c 2.46055151446 2.51921130095 0.5
	r 0.0544153734425
}

shader {
	name "Sphere1615"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1615"
	type sphere
	c 2.85142641624 2.29391087772 0.5
	r 0.0538791829295
}

shader {
	name "Sphere1616"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1616"
	type sphere
	c 2.97989499605 2.21501147482 0.5
	r 0.0583920679527
}

shader {
	name "Sphere1617"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1617"
	type sphere
	c 3.26609231676 1.64545537453 0.5
	r 0.0430475719734
}

shader {
	name "Sphere1618"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1618"
	type sphere
	c 3.38957912303 1.58390678191 0.5
	r 0.0496920388848
}

shader {
	name "Sphere1619"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1619"
	type sphere
	c 3.36155020577 1.3450291318 0.5
	r 0.0401223439576
}

shader {
	name "Sphere1620"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1620"
	type sphere
	c 3.66150297023 1.1688266887 0.5
	r 0.0599664520455
}

shader {
	name "Sphere1621"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1621"
	type sphere
	c 3.9443718513 1.27550817141 0.5
	r 0.0558430809346
}

shader {
	name "Sphere1622"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1622"
	type sphere
	c 4.06107614602 1.18990305244 0.5
	r 0.0523516201441
}

shader {
	name "Sphere1623"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1623"
	type sphere
	c 4.30240251008 1.03326983831 0.5
	r 0.0672695867981
}

shader {
	name "Sphere1624"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1624"
	type sphere
	c 4.43209554011 0.705175557349 0.5
	r 0.0662873808947
}

shader {
	name "Sphere1625"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1625"
	type sphere
	c 5.38630004144 -0.0253844571987 0.5
	r 0.0810835195902
}

shader {
	name "Sphere1626"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1626"
	type sphere
	c 5.57241884703 -0.564019374023 0.5
	r 0.085496572408
}

shader {
	name "Sphere1627"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1627"
	type sphere
	c 5.43894391205 -1.01859977759 0.5
	r 0.093162094855
}

shader {
	name "Sphere1628"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1628"
	type sphere
	c 5.11520409852 -1.54200865769 0.5
	r 0.0930816487531
}

shader {
	name "Sphere1629"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1629"
	type sphere
	c 4.9420866817 -2.05863665398 0.5
	r 0.111577233552
}

shader {
	name "Sphere1630"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1630"
	type sphere
	c 4.62919403879 -2.05456051957 0.5
	r 0.0913379043651
}

shader {
	name "Sphere1631"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1631"
	type sphere
	c 4.20974895001 -2.35005934303 0.5
	r 0.063208841613
}

shader {
	name "Sphere1632"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1632"
	type sphere
	c 4.28115162986 -2.70090371915 0.5
	r 0.0682015538754
}

shader {
	name "Sphere1633"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1633"
	type sphere
	c 3.99164955515 -2.91712933238 0.5
	r 0.0643252208807
}

shader {
	name "Sphere1634"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1634"
	type sphere
	c 3.65724114199 -3.20026825551 0.5
	r 0.0580220307361
}

shader {
	name "Sphere1635"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1635"
	type sphere
	c 3.55831219412 -3.34439196175 0.5
	r 0.0651828153583
}

shader {
	name "Sphere1636"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1636"
	type sphere
	c 3.04347586 -3.2156710692 0.5
	r 0.0565838164411
}

shader {
	name "Sphere1637"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1637"
	type sphere
	c 2.49188182156 -3.83991398313 0.5
	r 0.0774296638638
}

shader {
	name "Sphere1638"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1638"
	type sphere
	c 2.40403279461 -4.24634997112 0.5
	r 0.0800937633886
}

shader {
	name "Sphere1639"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1639"
	type sphere
	c 2.20496446095 -4.53274814994 0.5
	r 0.0672092002365
}

shader {
	name "Sphere1640"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1640"
	type sphere
	c 2.0538355825 -4.64951738352 0.5
	r 0.0723148405638
}

shader {
	name "Sphere1641"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1641"
	type sphere
	c 1.38169735607 -4.99625902208 0.5
	r 0.0783722234031
}

shader {
	name "Sphere1642"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1642"
	type sphere
	c 0.948290496722 -5.24435522867 0.5
	r 0.0876872765026
}

shader {
	name "Sphere1643"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1643"
	type sphere
	c 0.27064658181 -5.4624446769 0.5
	r 0.102999716797
}

shader {
	name "Sphere1644"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1644"
	type sphere
	c -0.0553377098316 -5.07100595783 0.5
	r 0.0880995114366
}

shader {
	name "Sphere1645"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1645"
	type sphere
	c -0.358510024257 -4.91893180568 0.5
	r 0.0902698500868
}

shader {
	name "Sphere1646"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1646"
	type sphere
	c -1.12905003701 -4.21321694395 0.5
	r 0.112906522725
}

shader {
	name "Sphere1647"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1647"
	type sphere
	c -1.36446832699 -3.76952469052 0.5
	r 0.0821185613923
}

shader {
	name "Sphere1648"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1648"
	type sphere
	c -1.43596547225 -3.58616011243 0.5
	r 0.0581642394909
}

shader {
	name "Sphere1649"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1649"
	type sphere
	c -1.66261333634 -3.38880174369 0.5
	r 0.0586853624482
}

shader {
	name "Sphere1650"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1650"
	type sphere
	c -1.79088030748 -3.05660418205 0.5
	r 0.0612086477274
}

shader {
	name "Sphere1651"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1651"
	type sphere
	c -2.07752155123 -2.91249388981 0.5
	r 0.0596399192005
}

shader {
	name "Sphere1652"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1652"
	type sphere
	c -2.30915316737 -2.13329893181 0.5
	r 0.0372182201522
}

shader {
	name "Sphere1653"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1653"
	type sphere
	c -2.50928992559 -2.17147566033 0.5
	r 0.0390777285482
}

shader {
	name "Sphere1654"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1654"
	type sphere
	c -2.69854176704 -2.22714825192 0.5
	r 0.0372028617243
}

shader {
	name "Sphere1655"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1655"
	type sphere
	c -2.75418802422 -1.95775145616 0.5
	r 0.0381230801888
}

shader {
	name "Sphere1656"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1656"
	type sphere
	c -3.00030120122 -1.98085853764 0.5
	r 0.0502082866534
}

shader {
	name "Sphere1657"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1657"
	type sphere
	c -3.29216738377 -1.71404466052 0.5
	r 0.0515045998997
}

shader {
	name "Sphere1658"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1658"
	type sphere
	c -3.45502605645 -1.30561934805 0.5
	r 0.0537101222704
}

shader {
	name "Sphere1659"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1659"
	type sphere
	c -3.6073639848 -0.944370123102 0.5
	r 0.0518254193244
}

shader {
	name "Sphere1660"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1660"
	type sphere
	c -3.46887017428 -0.627219172045 0.5
	r 0.0554525589637
}

shader {
	name "Sphere1661"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1661"
	type sphere
	c -3.3993866459 -0.186440999363 0.5
	r 0.0411730351943
}

shader {
	name "Sphere1662"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1662"
	type sphere
	c -3.47251892244 0.422508354642 0.5
	r 0.0675373526032
}

shader {
	name "Sphere1663"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1663"
	type sphere
	c -3.81833588757 0.707132636461 0.5
	r 0.0641663052401
}

shader {
	name "Sphere1664"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1664"
	type sphere
	c -3.789399826 0.88304211556 0.5
	r 0.0623933380415
}

shader {
	name "Sphere1665"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1665"
	type sphere
	c -3.9984033236 1.17561410903 0.5
	r 0.0721275072136
}

shader {
	name "Sphere1666"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1666"
	type sphere
	c -3.70282204622 1.74312407948 0.5
	r 0.0653630270044
}

shader {
	name "Sphere1667"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1667"
	type sphere
	c -3.48713042338 2.01178914814 0.5
	r 0.0547773704625
}

shader {
	name "Sphere1668"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1668"
	type sphere
	c -3.31021250453 2.48959911368 0.5
	r 0.0648586226235
}

shader {
	name "Sphere1669"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1669"
	type sphere
	c -2.9251509301 2.68732786377 0.5
	r 0.0589855217594
}

shader {
	name "Sphere1670"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1670"
	type sphere
	c -2.60303920406 2.63283880585 0.5
	r 0.0621396599788
}

shader {
	name "Sphere1671"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1671"
	type sphere
	c -1.87680817687 2.8721863061 0.5
	r 0.0531105130639
}

shader {
	name "Sphere1672"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1672"
	type sphere
	c -1.73562273561 2.78336050256 0.5
	r 0.0570576537166
}

shader {
	name "Sphere1673"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1673"
	type sphere
	c -1.46310146351 2.66817400517 0.5
	r 0.0314918804828
}

shader {
	name "Sphere1674"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1674"
	type sphere
	c -1.15455525835 2.65461514888 0.5
	r 0.0370342805854
}

shader {
	name "Sphere1675"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1675"
	type sphere
	c -0.980052663117 2.70224851077 0.5
	r 0.0338916115664
}

shader {
	name "Sphere1676"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1676"
	type sphere
	c -0.539608395333 2.92125778595 0.5
	r 0.0342453749397
}

shader {
	name "Sphere1677"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1677"
	type sphere
	c -0.260551891673 2.81265505254 0.5
	r 0.0337208807225
}

shader {
	name "Sphere1678"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1678"
	type sphere
	c 0.090160542759 2.88645646366 0.5
	r 0.0302201191115
}

shader {
	name "Sphere1679"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1679"
	type sphere
	c 0.654594695182 2.776983107 0.5
	r 0.0367386482698
}

shader {
	name "Sphere1680"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1680"
	type sphere
	c 1.05226318931 2.71333742068 0.5
	r 0.046714785775
}

shader {
	name "Sphere1681"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1681"
	type sphere
	c 1.47440420764 2.89495793035 0.5
	r 0.0620177449422
}

shader {
	name "Sphere1682"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1682"
	type sphere
	c 1.8026727066 3.03244565499 0.5
	r 0.0579286576633
}

shader {
	name "Sphere1683"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1683"
	type sphere
	c 2.32496106927 2.71166950923 0.5
	r 0.0631303341569
}

shader {
	name "Sphere1684"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1684"
	type sphere
	c 2.59136561031 2.44683921565 0.5
	r 0.0577091158697
}

shader {
	name "Sphere1685"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1685"
	type sphere
	c 2.73350210424 2.37489089704 0.5
	r 0.0534099014426
}

shader {
	name "Sphere1686"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1686"
	type sphere
	c 3.11034108629 2.12988615183 0.5
	r 0.0584311231489
}

shader {
	name "Sphere1687"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1687"
	type sphere
	c 3.1656490099 1.69102464628 0.5
	r 0.0396751379459
}

shader {
	name "Sphere1688"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1688"
	type sphere
	c 3.4821543666 1.50471360959 0.5
	r 0.0416779535863
}

shader {
	name "Sphere1689"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1689"
	type sphere
	c 3.45945951241 1.38326747846 0.5
	r 0.0387111955921
}

shader {
	name "Sphere1690"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1690"
	type sphere
	c 3.7028351073 1.31325149976 0.5
	r 0.052700602932
}

shader {
	name "Sphere1691"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1691"
	type sphere
	c 4.48405269672 1.00694900821 0.5
	r 0.0703908168353
}

shader {
	name "Sphere1692"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1692"
	type sphere
	c 5.28708171176 0.176633799199 0.5
	r 0.0877175607836
}

shader {
	name "Sphere1693"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1693"
	type sphere
	c 5.50330087243 -0.216749805844 0.5
	r 0.0871404791511
}

shader {
	name "Sphere1694"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1694"
	type sphere
	c 5.7249981342 -0.732829744398 0.5
	r 0.0851632537424
}

shader {
	name "Sphere1695"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1695"
	type sphere
	c 5.29215694966 -1.72386730076 0.5
	r 0.0972246665463
}

shader {
	name "Sphere1696"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1696"
	type sphere
	c 5.21607198132 -1.98921528718 0.5
	r 0.100405288608
}

shader {
	name "Sphere1697"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1697"
	type sphere
	c 4.36994654625 -2.38978869473 0.5
	r 0.0605790871875
}

shader {
	name "Sphere1698"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1698"
	type sphere
	c 4.43376508099 -2.58881467594 0.5
	r 0.0738137119519
}

shader {
	name "Sphere1699"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1699"
	type sphere
	c 4.13472156311 -2.80097962817 0.5
	r 0.0648192546828
}

shader {
	name "Sphere1700"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1700"
	type sphere
	c 3.8553179432 -3.01534595588 0.5
	r 0.0616944506839
}

shader {
	name "Sphere1701"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1701"
	type sphere
	c 3.44795200888 -3.48709896998 0.5
	r 0.0701182254154
}

shader {
	name "Sphere1702"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1702"
	type sphere
	c 3.07513635157 -3.36960566755 0.5
	r 0.0612837537545
}

shader {
	name "Sphere1703"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1703"
	type sphere
	c 2.64766863 -3.979000474 0.5
	r 0.0792011190812
}

shader {
	name "Sphere1704"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1704"
	type sphere
	c 1.89861236483 -4.76032582892 0.5
	r 0.0707224862691
}

shader {
	name "Sphere1705"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1705"
	type sphere
	c 1.58593076602 -4.96671727706 0.5
	r 0.0763969603714
}

shader {
	name "Sphere1706"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1706"
	type sphere
	c 1.17028097935 -5.03124177493 0.5
	r 0.0823461047545
}

shader {
	name "Sphere1707"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1707"
	type sphere
	c 0.75142177502 -5.37216488805 0.5
	r 0.0883513242948
}

shader {
	name "Sphere1708"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1708"
	type sphere
	c 0.00321502191463 -5.49789172834 0.5
	r 0.0993281721232
}

shader {
	name "Sphere1709"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1709"
	type sphere
	c -0.138246788215 -5.28881019645 0.5
	r 0.0866884699089
}

shader {
	name "Sphere1710"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1710"
	type sphere
	c 0.00295144173091 -4.84155238379 0.5
	r 0.089456661095
}

shader {
	name "Sphere1711"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1711"
	type sphere
	c -0.588607946988 -4.9536720234 0.5
	r 0.08425941518
}

shader {
	name "Sphere1712"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1712"
	type sphere
	c -1.15862655769 -4.50067130759 0.5
	r 0.103822431806
}

shader {
	name "Sphere1713"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1713"
	type sphere
	c -1.40354038346 -3.98615310163 0.5
	r 0.0829743001347
}

shader {
	name "Sphere1714"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1714"
	type sphere
	c -1.57949662512 -3.61765011067 0.5
	r 0.0520444564331
}

shader {
	name "Sphere1715"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1715"
	type sphere
	c -1.93324421672 -3.14849243482 0.5
	r 0.0658736098002
}

shader {
	name "Sphere1716"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1716"
	type sphere
	c -2.09918886682 -2.75207243498 0.5
	r 0.0617686476344
}

shader {
	name "Sphere1717"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1717"
	type sphere
	c -2.26988143481 -2.04499946482 0.5
	r 0.0352609077208
}

shader {
	name "Sphere1718"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1718"
	type sphere
	c -2.34387519178 -2.22557052428 0.5
	r 0.0367230537669
}

shader {
	name "Sphere1719"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1719"
	type sphere
	c -2.62190433627 -2.28490059505 0.5
	r 0.0347683392795
}

shader {
	name "Sphere1720"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1720"
	type sphere
	c -2.77629628567 -2.1660717894 0.5
	r 0.0369527579937
}

shader {
	name "Sphere1721"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1721"
	type sphere
	c -2.90283076855 -2.0663370184 0.5
	r 0.04702323577
}

shader {
	name "Sphere1722"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1722"
	type sphere
	c -3.08560518411 -1.88559812023 0.5
	r 0.0456959134653
}

shader {
	name "Sphere1723"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1723"
	type sphere
	c -3.43521370842 -1.69869736625 0.5
	r 0.0563958501499
}

shader {
	name "Sphere1724"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1724"
	type sphere
	c -3.5465283856 -1.41589712879 0.5
	r 0.0537621958125
}

shader {
	name "Sphere1725"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1725"
	type sphere
	c -3.69113675664 -1.05636780197 0.5
	r 0.0530710225739
}

shader {
	name "Sphere1726"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1726"
	type sphere
	c -3.52028853382 -0.844829219304 0.5
	r 0.0473633940681
}

shader {
	name "Sphere1727"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1727"
	type sphere
	c -3.41636654063 -0.491134147306 0.5
	r 0.0539440501988
}

shader {
	name "Sphere1728"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1728"
	type sphere
	c -3.37940982338 -0.29297965165 0.5
	r 0.0401234979496
}

shader {
	name "Sphere1729"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1729"
	type sphere
	c -3.42986985759 -0.0817865522672 0.5
	r 0.0405796465007
}

shader {
	name "Sphere1730"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1730"
	type sphere
	c -3.89118499193 0.557802393118 0.5
	r 0.0604477545237
}

shader {
	name "Sphere1731"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1731"
	type sphere
	c -3.96096996664 0.862917698108 0.5
	r 0.0671664329178
}

shader {
	name "Sphere1732"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1732"
	type sphere
	c -3.73526918208 1.58463719429 0.5
	r 0.0559676638326
}

shader {
	name "Sphere1733"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1733"
	type sphere
	c -3.64256510083 1.89832247666 0.5
	r 0.0595011435962
}

shader {
	name "Sphere1734"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1734"
	type sphere
	c -3.44365687534 2.14751554591 0.5
	r 0.0521117192167
}

shader {
	name "Sphere1735"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1735"
	type sphere
	c -3.36749681381 2.32942725027 0.5
	r 0.0627219061722
}

shader {
	name "Sphere1736"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1736"
	type sphere
	c -3.23779300849 2.63615031753 0.5
	r 0.0577424960558
}

shader {
	name "Sphere1737"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1737"
	type sphere
	c -3.02472021014 2.80171222819 0.5
	r 0.0547522301007
}

shader {
	name "Sphere1738"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1738"
	type sphere
	c -2.82041243963 2.57176486116 0.5
	r 0.0579879342621
}

shader {
	name "Sphere1739"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1739"
	type sphere
	c -2.57265829416 2.79259908749 0.5
	r 0.0598278370984
}

shader {
	name "Sphere1740"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1740"
	type sphere
	c -1.99814989794 2.94035535501 0.5
	r 0.0512738405669
}

shader {
	name "Sphere1741"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1741"
	type sphere
	c -1.61605926236 2.69584517554 0.5
	r 0.0540698657685
}

shader {
	name "Sphere1742"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1742"
	type sphere
	c -1.52731714217 2.61920111727 0.5
	r 0.0290772815455
}

shader {
	name "Sphere1743"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1743"
	type sphere
	c -1.08568191652 2.72284836854 0.5
	r 0.0356782464133
}

shader {
	name "Sphere1744"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1744"
	type sphere
	c -0.932229932553 2.77765308264 0.5
	r 0.0330765558515
}

shader {
	name "Sphere1745"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1745"
	type sphere
	c -0.620651421769 2.94997936659 0.5
	r 0.0302411119957
}

shader {
	name "Sphere1746"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1746"
	type sphere
	c -0.344865103047 2.85246750917 0.5
	r 0.0362093272697
}

shader {
	name "Sphere1747"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1747"
	type sphere
	c -0.178492356481 2.78000117124 0.5
	r 0.0325175095431
}

shader {
	name "Sphere1748"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1748"
	type sphere
	c 0.0214173136209 2.84639897057 0.5
	r 0.0294519580821
}

shader {
	name "Sphere1749"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1749"
	type sphere
	c 0.159986482929 2.93033841463 0.5
	r 0.0316323201472
}

shader {
	name "Sphere1750"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1750"
	type sphere
	c 0.72053622931 2.85400042052 0.5
	r 0.0393039271997
}

shader {
	name "Sphere1751"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1751"
	type sphere
	c 0.956556324635 2.79833672822 0.5
	r 0.0492872246381
}

shader {
	name "Sphere1752"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1752"
	type sphere
	c 1.14834185085 2.63036443599 0.5
	r 0.0484957140825
}

shader {
	name "Sphere1753"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1753"
	type sphere
	c 1.31897544773 2.82266801338 0.5
	r 0.0665453192312
}

shader {
	name "Sphere1754"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1754"
	type sphere
	c 1.62551334558 2.97192056586 0.5
	r 0.0651669066222
}

shader {
	name "Sphere1755"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1755"
	type sphere
	c 1.95042243479 3.08278178272 0.5
	r 0.0591379289997
}

shader {
	name "Sphere1756"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1756"
	type sphere
	c 2.30799867998 2.87436501947 0.5
	r 0.0595526835417
}

shader {
	name "Sphere1757"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1757"
	type sphere
	c 2.58645449912 2.6016378768 0.5
	r 0.0584482936441
}

shader {
	name "Sphere1758"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1758"
	type sphere
	c 2.86403733249 2.43975534741 0.5
	r 0.055912324293
}

shader {
	name "Sphere1759"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1759"
	type sphere
	c 3.12340124333 2.2925098199 0.5
	r 0.0639293141988
}

shader {
	name "Sphere1760"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1760"
	type sphere
	c 3.1067887325 1.96917737194 0.5
	r 0.0621299040242
}

shader {
	name "Sphere1761"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1761"
	type sphere
	c 3.07762248224 1.6340413304 0.5
	r 0.0389703922577
}

shader {
	name "Sphere1762"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1762"
	type sphere
	c 3.25180061824 1.75845358875 0.5
	r 0.0423762396783
}

shader {
	name "Sphere1763"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1763"
	type sphere
	c 3.50759646362 1.61249714045 0.5
	r 0.0413812528668
}

shader {
	name "Sphere1764"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1764"
	type sphere
	c 3.44496969275 1.28102835488 0.5
	r 0.0387344060318
}

shader {
	name "Sphere1765"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1765"
	type sphere
	c 4.41096490273 1.1705191372 0.5
	r 0.0639764770264
}

shader {
	name "Sphere1766"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1766"
	type sphere
	c 5.04810504252 0.188920044926 0.5
	r 0.0917516570619
}

shader {
	name "Sphere1767"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1767"
	type sphere
	c 5.51227463714 0.152135462242 0.5
	r 0.0821736175137
}

shader {
	name "Sphere1768"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1768"
	type sphere
	c 5.79823262541 -0.513885527183 0.5
	r 0.0879874661137
}

shader {
	name "Sphere1769"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1769"
	type sphere
	c 5.36339496243 -1.46959485599 0.5
	r 0.100822672441
}

shader {
	name "Sphere1770"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1770"
	type sphere
	c 5.14753358579 -2.23727507219 0.5
	r 0.0926103385733
}

shader {
	name "Sphere1771"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1771"
	type sphere
	c 4.32880535771 -2.22774775127 0.5
	r 0.0648075106697
}

shader {
	name "Sphere1772"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1772"
	type sphere
	c 4.44906163107 -2.78228692288 0.5
	r 0.0717432899894
}

shader {
	name "Sphere1773"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1773"
	type sphere
	c 4.29110477407 -2.88064292353 0.5
	r 0.0668093762466
}

shader {
	name "Sphere1774"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1774"
	type sphere
	c 4.00211214766 -3.08118784279 0.5
	r 0.0589686217561
}

shader {
	name "Sphere1775"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1775"
	type sphere
	c 3.63290277614 -3.50767216172 0.5
	r 0.069450391836
}

shader {
	name "Sphere1776"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1776"
	type sphere
	c 3.27622901546 -3.44611842238 0.5
	r 0.0622906408315
}

shader {
	name "Sphere1777"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1777"
	type sphere
	c 2.92315433378 -3.31418329426 0.5
	r 0.0600452304991
}

shader {
	name "Sphere1778"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1778"
	type sphere
	c 2.68929297052 -3.77202365606 0.5
	r 0.0791394750518
}

shader {
	name "Sphere1779"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1779"
	type sphere
	c 2.07036966364 -4.84045502377 0.5
	r 0.0714242948337
}

shader {
	name "Sphere1780"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1780"
	type sphere
	c 1.51147512032 -5.15458612563 0.5
	r 0.0751667900281
}

shader {
	name "Sphere1781"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1781"
	type sphere
	c 1.31069948519 -5.1916341534 0.5
	r 0.0775342502565
}

shader {
	name "Sphere1782"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1782"
	type sphere
	c 0.957187432031 -5.47200409542 0.5
	r 0.0831797145151
}

shader {
	name "Sphere1783"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1783"
	type sphere
	c 0.16418200416 -5.72449029944 0.5
	r 0.10913578402
}

shader {
	name "Sphere1784"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1784"
	type sphere
	c -0.452745022785 -5.125641938 0.5
	r 0.080112775161
}

shader {
	name "Sphere1785"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1785"
	type sphere
	c -0.741583591978 -4.78645495101 0.5
	r 0.0857162954576
}

shader {
	name "Sphere1786"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1786"
	type sphere
	c -1.39470050088 -4.34334156244 0.5
	r 0.108949746571
}

shader {
	name "Sphere1787"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1787"
	type sphere
	c -1.5615875758 -3.84469503767 0.5
	r 0.076105807399
}

shader {
	name "Sphere1788"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1788"
	type sphere
	c -2.23310295396 -2.85479449224 0.5
	r 0.0648121650006
}

shader {
	name "Sphere1789"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1789"
	type sphere
	c -1.96801076771 -2.64485511662 0.5
	r 0.0652965972667
}

shader {
	name "Sphere1790"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1790"
	type sphere
	c -2.24327734543 -2.21148613132 0.5
	r 0.0394612094348
}

shader {
	name "Sphere1791"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1791"
	type sphere
	c -2.43893811933 -2.24327668417 0.5
	r 0.0358003108404
}

shader {
	name "Sphere1792"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1792"
	type sphere
	c -2.70619667485 -2.32230597045 0.5
	r 0.0343959777751
}

shader {
	name "Sphere1793"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1793"
	type sphere
	c -2.78993088388 -2.26292627002 0.5
	r 0.0364043455084
}

shader {
	name "Sphere1794"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1794"
	type sphere
	c -3.02412510993 -2.11289671434 0.5
	r 0.0504194085244
}

shader {
	name "Sphere1795"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1795"
	type sphere
	c -3.12826464078 -2.00162547952 0.5
	r 0.0470199145205
}

shader {
	name "Sphere1796"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1796"
	type sphere
	c -3.36989792683 -1.82221684377 0.5
	r 0.0483982676059
}

shader {
	name "Sphere1797"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1797"
	type sphere
	c -3.4982098884 -1.55065101156 0.5
	r 0.0536038762366
}

shader {
	name "Sphere1798"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1798"
	type sphere
	c -3.59441730576 -1.28297200402 0.5
	r 0.0522041718531
}

shader {
	name "Sphere1799"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1799"
	type sphere
	c -3.73940336622 -0.930955328579 0.5
	r 0.0477138928235
}

shader {
	name "Sphere1800"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1800"
	type sphere
	c -3.64201667443 -0.818580527776 0.5
	r 0.0460311340842
}

shader {
	name "Sphere1801"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1801"
	type sphere
	c -3.56575644637 -0.509428796164 0.5
	r 0.0589354051437
}

shader {
	name "Sphere1802"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1802"
	type sphere
	c -3.28335567492 -0.335403672802 0.5
	r 0.0386307769626
}

shader {
	name "Sphere1803"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1803"
	type sphere
	c -3.47647923908 -0.257405807581 0.5
	r 0.0374134805696
}

shader {
	name "Sphere1804"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1804"
	type sphere
	c -3.35935847405 0.00082992796129 0.5
	r 0.0408820170761
}

shader {
	name "Sphere1805"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1805"
	type sphere
	c -3.81234638693 0.423347586654 0.5
	r 0.0564503275759
}

shader {
	name "Sphere1806"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1806"
	type sphere
	c -3.84499437901 1.67779404822 0.5
	r 0.051984977544
}

shader {
	name "Sphere1807"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1807"
	type sphere
	c -3.79422562178 1.8758270517 0.5
	r 0.0554886982946
}

shader {
	name "Sphere1808"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1808"
	type sphere
	c -3.57786293614 2.11931425549 0.5
	r 0.0507410930409
}

shader {
	name "Sphere1809"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1809"
	type sphere
	c -3.48327762683 2.45806136922 0.5
	r 0.0670777950476
}

shader {
	name "Sphere1810"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1810"
	type sphere
	c -3.39252196423 2.63177074729 0.5
	r 0.0583506974961
}

shader {
	name "Sphere1811"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1811"
	type sphere
	c -3.17656993139 2.78756627085 0.5
	r 0.0596281696558
}

shader {
	name "Sphere1812"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1812"
	type sphere
	c -2.87947114609 2.8351136667 0.5
	r 0.0570278330626
}

shader {
	name "Sphere1813"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1813"
	type sphere
	c -2.77483672875 2.71656218556 0.5
	r 0.0558624871216
}

shader {
	name "Sphere1814"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1814"
	type sphere
	c -2.42129660698 2.85008501068 0.5
	r 0.0616049955174
}

shader {
	name "Sphere1815"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1815"
	type sphere
	c -2.1123881936 2.87070315329 0.5
	r 0.0490744144623
}

shader {
	name "Sphere1816"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1816"
	type sphere
	c -1.88131999792 3.01118666644 0.5
	r 0.0511946612895
}

shader {
	name "Sphere1817"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1817"
	type sphere
	c -1.6009252725 2.8354691236 0.5
	r 0.0512614450761
}

shader {
	name "Sphere1818"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1818"
	type sphere
	c -1.62038023288 2.55072739464 0.5
	r 0.0548167065433
}

shader {
	name "Sphere1819"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1819"
	type sphere
	c -1.1746328574 2.74621841881 0.5
	r 0.0332990425098
}

shader {
	name "Sphere1820"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1820"
	type sphere
	c -1.01756988274 2.7801480306 0.5
	r 0.0309557537497
}

shader {
	name "Sphere1821"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1821"
	type sphere
	c -0.687597064254 2.90133967057 0.5
	r 0.0318212818588
}

shader {
	name "Sphere1822"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1822"
	type sphere
	c -0.561551400996 3.00333860487 0.5
	r 0.0294770735088
}

shader {
	name "Sphere1823"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1823"
	type sphere
	c -0.266475610954 2.9017168495 0.5
	r 0.0332230543762
}

shader {
	name "Sphere1824"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1824"
	type sphere
	c 0.0199977841599 2.92580566674 0.5
	r 0.0301125794726
}

shader {
	name "Sphere1825"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1825"
	type sphere
	c 0.0878520892688 2.96424528471 0.5
	r 0.0281471805638
}

shader {
	name "Sphere1826"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1826"
	type sphere
	c 0.233306519527 2.88749254069 0.5
	r 0.0320585201105
}

shader {
	name "Sphere1827"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1827"
	type sphere
	c 0.618326337839 2.87025341627 0.5
	r 0.0383166226188
}

shader {
	name "Sphere1828"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1828"
	type sphere
	c 0.819041895723 2.83119151451 0.5
	r 0.0365299836605
}

shader {
	name "Sphere1829"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1829"
	type sphere
	c 1.08287695344 2.83890442529 0.5
	r 0.0502189792407
}

shader {
	name "Sphere1830"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1830"
	type sphere
	c 1.31744513416 2.6483477994 0.5
	r 0.0641998789956
}

shader {
	name "Sphere1831"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1831"
	type sphere
	c 1.33791823015 2.99980054569 0.5
	r 0.0670615825092
}

shader {
	name "Sphere1832"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1832"
	type sphere
	c 1.82990680719 3.18938845651 0.5
	r 0.0615375124024
}

shader {
	name "Sphere1833"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1833"
	type sphere
	c 2.06107257774 2.97481353946 0.5
	r 0.0568107021896
}

shader {
	name "Sphere1834"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1834"
	type sphere
	c 2.46214216063 2.81313667221 0.5
	r 0.0648413748529
}

shader {
	name "Sphere1835"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1835"
	type sphere
	c 2.72184678746 2.52747634785 0.5
	r 0.0573314101723
}

shader {
	name "Sphere1836"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1836"
	type sphere
	c 3.26011509207 2.19221596979 0.5
	r 0.0632383397175
}

shader {
	name "Sphere1837"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1837"
	type sphere
	c 3.07418523518 1.73417354518 0.5
	r 0.0361730023019
}

shader {
	name "Sphere1838"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1838"
	type sphere
	c 3.35855263044 1.71546754995 0.5
	r 0.0439350156519
}

shader {
	name "Sphere1839"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1839"
	type sphere
	c 3.59283984998 1.535902403 0.5
	r 0.0445688411285
}

shader {
	name "Sphere1840"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1840"
	type sphere
	c 3.53636340639 1.32025204387 0.5
	r 0.0358568878776
}

shader {
	name "Sphere1841"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1841"
	type sphere
	c 3.35268242815 1.24420549403 0.5
	r 0.0357873024635
}

shader {
	name "Sphere1842"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1842"
	type sphere
	c 4.23856396931 1.20099677091 0.5
	r 0.0673291568986
}

shader {
	name "Sphere1843"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1843"
	type sphere
	c 4.58357291144 1.15880076551 0.5
	r 0.0657775219913
}

shader {
	name "Sphere1844"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1844"
	type sphere
	c 5.18395179698 0.394325939599 0.5
	r 0.0929462889856
}

shader {
	name "Sphere1845"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1845"
	type sphere
	c 5.42724542224 0.351323899784 0.5
	r 0.0802598321916
}

shader {
	name "Sphere1846"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1846"
	type sphere
	c 5.95777351531 -0.69306430587 0.5
	r 0.0919474131733
}

shader {
	name "Sphere1847"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1847"
	type sphere
	c 5.55092487088 -1.66430447221 0.5
	r 0.101926204083
}

shader {
	name "Sphere1848"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1848"
	type sphere
	c 5.38444367818 -2.17966751617 0.5
	r 0.0902497858143
}

shader {
	name "Sphere1849"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1849"
	type sphere
	c 4.92445774739 -2.32193765051 0.5
	r 0.0863406387646
}

shader {
	name "Sphere1850"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1850"
	type sphere
	c 4.49674331643 -2.27734706941 0.5
	r 0.0665244287634
}

shader {
	name "Sphere1851"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1851"
	type sphere
	c 4.61137921026 -2.67490937534 0.5
	r 0.0742216904136
}

shader {
	name "Sphere1852"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1852"
	type sphere
	c 4.14222620251 -2.99715746028 0.5
	r 0.0635664451554
}

shader {
	name "Sphere1853"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1853"
	type sphere
	c 3.87764258291 -3.17069574751 0.5
	r 0.0560148112933
}

shader {
	name "Sphere1854"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1854"
	type sphere
	c 3.73568304909 -3.35574900534 0.5
	r 0.0681177434582
}

shader {
	name "Sphere1855"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1855"
	type sphere
	c 3.52426824971 -3.65043845308 0.5
	r 0.065098174793
}

shader {
	name "Sphere1856"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1856"
	type sphere
	c 3.31738505767 -3.60966206047 0.5
	r 0.0641913421597
}

shader {
	name "Sphere1857"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1857"
	type sphere
	c 2.94749738805 -3.47855059064 0.5
	r 0.0645748751398
}

shader {
	name "Sphere1858"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1858"
	type sphere
	c 2.89957205241 -3.15522402673 0.5
	r 0.0604790291369
}

shader {
	name "Sphere1859"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1859"
	type sphere
	c 2.85871762686 -3.91368217303 0.5
	r 0.0864931467491
}

shader {
	name "Sphere1860"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1860"
	type sphere
	c 2.22063270545 -4.73241304339 0.5
	r 0.0673805279659
}

shader {
	name "Sphere1861"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1861"
	type sphere
	c 1.91028911179 -4.95713471674 0.5
	r 0.0771437460794
}

shader {
	name "Sphere1862"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1862"
	type sphere
	c 1.71311512371 -5.12759438909 0.5
	r 0.0774121246552
}

shader {
	name "Sphere1863"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1863"
	type sphere
	c 1.14241281233 -5.35660764073 0.5
	r 0.0804935593673
}

shader {
	name "Sphere1864"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1864"
	type sphere
	c 0.776573777491 -5.59772216773 0.5
	r 0.081865153098
}

shader {
	name "Sphere1865"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1865"
	type sphere
	c 0.444846614042 -5.6771102847 0.5
	r 0.104341000628
}

shader {
	name "Sphere1866"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1866"
	type sphere
	c -0.10645553119 -5.73102370204 0.5
	r 0.0939015044284
}

shader {
	name "Sphere1867"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1867"
	type sphere
	c -0.665910953558 -5.16143599522 0.5
	r 0.0819999088684
}

shader {
	name "Sphere1868"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1868"
	type sphere
	c -0.679079619091 -4.56507529156 0.5
	r 0.0868093008734
}

shader {
	name "Sphere1869"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1869"
	type sphere
	c -1.39845225877 -4.61647180038 0.5
	r 0.09591725649
}

shader {
	name "Sphere1870"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1870"
	type sphere
	c -1.60661290562 -4.04070396467 0.5
	r 0.074729578474
}

shader {
	name "Sphere1871"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1871"
	type sphere
	c -2.19805820455 -3.01850278844 0.5
	r 0.0607507839423
}

shader {
	name "Sphere1872"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1872"
	type sphere
	c -2.25463715329 -2.68124288723 0.5
	r 0.066349693998
}

shader {
	name "Sphere1873"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1873"
	type sphere
	c -2.28566831219 -2.2999704539 0.5
	r 0.0341247202055
}

shader {
	name "Sphere1874"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1874"
	type sphere
	c -2.63127353496 -2.37871367633 0.5
	r 0.0359414924858
}

shader {
	name "Sphere1875"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1875"
	type sphere
	c -2.86303673453 -2.20395976822 0.5
	r 0.0340378398274
}

shader {
	name "Sphere1876"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1876"
	type sphere
	c -3.20609077808 -1.90528453393 0.5
	r 0.0458665649197
}

shader {
	name "Sphere1877"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1877"
	type sphere
	c -3.49491014205 -1.82054664873 0.5
	r 0.0453692612758
}

shader {
	name "Sphere1878"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1878"
	type sphere
	c -3.64627714286 -1.52793840414 0.5
	r 0.0587454588214
}

shader {
	name "Sphere1879"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1879"
	type sphere
	c -3.67997957365 -1.3867680846 0.5
	r 0.0486827550401
}

shader {
	name "Sphere1880"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1880"
	type sphere
	c -3.82367315097 -1.02786412661 0.5
	r 0.048604072087
}

shader {
	name "Sphere1881"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1881"
	type sphere
	c -3.61948021819 -0.658515527662 0.5
	r 0.0599179379167
}

shader {
	name "Sphere1882"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1882"
	type sphere
	c -3.49968052717 -0.37740453448 0.5
	r 0.0517917073166
}

shader {
	name "Sphere1883"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1883"
	type sphere
	c -3.50181430553 -0.159824338221 0.5
	r 0.0381990509606
}

shader {
	name "Sphere1884"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1884"
	type sphere
	c -3.4669549509 0.0207300052798 0.5
	r 0.041183937406
}

shader {
	name "Sphere1885"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1885"
	type sphere
	c -3.65768368698 0.401491238717 0.5
	r 0.0606992179614
}

shader {
	name "Sphere1886"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1886"
	type sphere
	c -3.95943077803 0.421508094088 0.5
	r 0.0538715924325
}

shader {
	name "Sphere1887"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1887"
	type sphere
	c -3.86952922884 1.54551717544 0.5
	r 0.0489147775821
}

shader {
	name "Sphere1888"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1888"
	type sphere
	c -3.74349394256 2.01942883858 0.5
	r 0.0587360221754
}

shader {
	name "Sphere1889"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1889"
	type sphere
	c -3.53693731483 2.24911107543 0.5
	r 0.051330906218
}

shader {
	name "Sphere1890"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1890"
	type sphere
	c -3.10621840257 2.92318923513 0.5
	r 0.0549597699431
}

shader {
	name "Sphere1891"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1891"
	type sphere
	c -2.54942902828 2.95272975526 0.5
	r 0.0615272374687
}

shader {
	name "Sphere1892"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1892"
	type sphere
	c -2.11774558244 3.00238791658 0.5
	r 0.0497708580876
}

shader {
	name "Sphere1893"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1893"
	type sphere
	c -2.00119395281 3.07734628449 0.5
	r 0.0514947189698
}

shader {
	name "Sphere1894"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1894"
	type sphere
	c -1.75458086564 2.94835025668 0.5
	r 0.0549011086486
}

shader {
	name "Sphere1895"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1895"
	type sphere
	c -1.11416200253 2.80729710457 0.5
	r 0.0311631417947
}

shader {
	name "Sphere1896"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1896"
	type sphere
	c -0.975569942105 2.84878889381 0.5
	r 0.029397408992
}

shader {
	name "Sphere1897"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1897"
	type sphere
	c -0.694388319787 2.98465245159 0.5
	r 0.030870556578
}

shader {
	name "Sphere1898"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1898"
	type sphere
	c -0.483992509573 2.98649305104 0.5
	r 0.0300483354052
}

shader {
	name "Sphere1899"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1899"
	type sphere
	c -0.346079728155 2.94906017424 0.5
	r 0.0362408988924
}

shader {
	name "Sphere1900"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1900"
	type sphere
	c -0.0466515693936 2.88403050646 0.5
	r 0.0288819664143
}

shader {
	name "Sphere1901"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1901"
	type sphere
	c 0.148267777348 3.0097778712 0.5
	r 0.0285920508963
}

shader {
	name "Sphere1902"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1902"
	type sphere
	c 0.234741745675 2.97526653296 0.5
	r 0.0337807739742
}

shader {
	name "Sphere1903"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1903"
	type sphere
	c 0.681799745963 2.94809674454 0.5
	r 0.0370143619012
}

shader {
	name "Sphere1904"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1904"
	type sphere
	c 0.791786238172 2.92193252072 0.5
	r 0.0345295027314
}

shader {
	name "Sphere1905"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1905"
	type sphere
	c 0.985215746918 2.92213964262 0.5
	r 0.0460204078278
}

shader {
	name "Sphere1906"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1906"
	type sphere
	c 1.98617416572 3.23974171888 0.5
	r 0.0615971814759
}

shader {
	name "Sphere1907"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1907"
	type sphere
	c 2.10123207836 3.12221867289 0.5
	r 0.0577726543844
}

shader {
	name "Sphere1908"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1908"
	type sphere
	c 2.4309811945 2.97828108034 0.5
	r 0.0612025490722
}

shader {
	name "Sphere1909"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1909"
	type sphere
	c 2.72030306145 2.68220554532 0.5
	r 0.0587212634158
}

shader {
	name "Sphere1910"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1910"
	type sphere
	c 3.27800765181 2.35839285057 0.5
	r 0.0621146854225
}

shader {
	name "Sphere1911"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1911"
	type sphere
	c 2.99554411719 1.6848756974 0.5
	r 0.0334385669181
}

shader {
	name "Sphere1912"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1912"
	type sphere
	c 3.34029785049 1.82972517327 0.5
	r 0.04284501276
}

shader {
	name "Sphere1913"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1913"
	type sphere
	c 3.6140029405 1.65159497435 0.5
	r 0.0436403658718
}

shader {
	name "Sphere1914"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1914"
	type sphere
	c 3.55623720945 1.41686826284 0.5
	r 0.038122398222
}

shader {
	name "Sphere1915"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1915"
	type sphere
	c 3.26786687699 1.29658653995 0.5
	r 0.0389777734454
}

shader {
	name "Sphere1916"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1916"
	type sphere
	c 4.35578057945 1.33537815226 0.5
	r 0.0664109838938
}

shader {
	name "Sphere1917"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1917"
	type sphere
	c 4.66301616537 1.0053229125 0.5
	r 0.06383732516
}

shader {
	name "Sphere1918"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1918"
	type sphere
	c 4.94615370511 0.402132081149 0.5
	r 0.0854983479285
}

shader {
	name "Sphere1919"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1919"
	type sphere
	c 5.64051170172 0.327385419097 0.5
	r 0.080694356046
}

shader {
	name "Sphere1920"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1920"
	type sphere
	c 6.02021508 -0.470104214337 0.5
	r 0.0817065823816
}

shader {
	name "Sphere1921"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1921"
	type sphere
	c 5.86686345954 -0.915775803158 0.5
	r 0.0884662509758
}

shader {
	name "Sphere1922"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1922"
	type sphere
	c 5.63190062569 -1.39654398297 0.5
	r 0.107876496711
}

shader {
	name "Sphere1923"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1923"
	type sphere
	c 5.46645393675 -1.95499925393 0.5
	r 0.0891264938196
}

shader {
	name "Sphere1924"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1924"
	type sphere
	c 5.31953568524 -2.41524615112 0.5
	r 0.0930179601081
}

shader {
	name "Sphere1925"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1925"
	type sphere
	c 4.59966525716 -2.47153284898 0.5
	r 0.0785635047029
}

shader {
	name "Sphere1926"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1926"
	type sphere
	c 4.62098126588 -2.87181308802 0.5
	r 0.0736315822594
}

shader {
	name "Sphere1927"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1927"
	type sphere
	c 4.13687772105 -3.15863228689 0.5
	r 0.0576060901381
}

shader {
	name "Sphere1928"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1928"
	type sphere
	c 3.82127362193 -3.52218258658 0.5
	r 0.0722462806243
}

shader {
	name "Sphere1929"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1929"
	type sphere
	c 3.68983857485 -3.67060815862 0.5
	r 0.0599975751082
}

shader {
	name "Sphere1930"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1930"
	type sphere
	c 3.14783153102 -3.56267339712 0.5
	r 0.0677667468224
}

shader {
	name "Sphere1931"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1931"
	type sphere
	c 2.79027714025 -3.41168213006 0.5
	r 0.0635623501405
}

shader {
	name "Sphere1932"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1932"
	type sphere
	c 2.88370977383 -3.69687948121 0.5
	r 0.0771856796364
}

shader {
	name "Sphere1933"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1933"
	type sphere
	c 2.79833886682 -4.12406770324 0.5
	r 0.0776655024777
}

shader {
	name "Sphere1934"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1934"
	type sphere
	c 2.23963726484 -4.90838951101 0.5
	r 0.0653692399048
}

shader {
	name "Sphere1935"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1935"
	type sphere
	c 2.09631231857 -5.03135887471 0.5
	r 0.0730695880035
}

shader {
	name "Sphere1936"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1936"
	type sphere
	c 1.63202086313 -5.31047278684 0.5
	r 0.0726268467723
}

shader {
	name "Sphere1937"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1937"
	type sphere
	c 1.15650645909 -5.57862246353 0.5
	r 0.0863527231433
}

shader {
	name "Sphere1938"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1938"
	type sphere
	c 0.350131192515 -5.93368571857 0.5
	r 0.100783607696
}

shader {
	name "Sphere1939"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1939"
	type sphere
	c 0.0150738704573 -5.94017091598 0.5
	r 0.0875178256244
}

shader {
	name "Sphere1940"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1940"
	type sphere
	c -0.260230700314 -5.52442811962 0.5
	r 0.0992559501021
}

shader {
	name "Sphere1941"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1941"
	type sphere
	c -0.527087898882 -5.32077264454 0.5
	r 0.0764969512997
}

shader {
	name "Sphere1942"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1942"
	type sphere
	c -1.19473908358 -4.75502832968 0.5
	r 0.0888584058101
}

shader {
	name "Sphere1943"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1943"
	type sphere
	c -1.61178666786 -4.49317929562 0.5
	r 0.0888822136241
}

shader {
	name "Sphere1944"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1944"
	type sphere
	c -1.76275440655 -3.90361452814 0.5
	r 0.081107503374
}

shader {
	name "Sphere1945"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1945"
	type sphere
	c -2.36200032685 -2.97370375586 0.5
	r 0.0667138569975
}

shader {
	name "Sphere1946"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1946"
	type sphere
	c -2.39014197119 -2.78819505604 0.5
	r 0.0631210794345
}

shader {
	name "Sphere1947"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1947"
	type sphere
	c -2.19042243755 -2.29914967378 0.5
	r 0.0373123381221
}

shader {
	name "Sphere1948"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1948"
	type sphere
	c -2.54335768049 -2.33852075494 0.5
	r 0.0365593762927
}

shader {
	name "Sphere1949"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1949"
	type sphere
	c -2.7172341017 -2.41160358977 0.5
	r 0.033086893419
}

shader {
	name "Sphere1950"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1950"
	type sphere
	c -2.87675079179 -2.29096567361 0.5
	r 0.0320222305893
}

shader {
	name "Sphere1951"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1951"
	type sphere
	c -3.2514709828 -2.01957368313 0.5
	r 0.0463601778927
}

shader {
	name "Sphere1952"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1952"
	type sphere
	c -3.43802146097 -1.93275285513 0.5
	r 0.0489834656005
}

shader {
	name "Sphere1953"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1953"
	type sphere
	c -3.57127984441 -1.72338221191 0.5
	r 0.0473195099511
}

shader {
	name "Sphere1954"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1954"
	type sphere
	c -3.72714965378 -1.26666363341 0.5
	r 0.0480936822057
}

shader {
	name "Sphere1955"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1955"
	type sphere
	c -3.78630736268 -1.14932973034 0.5
	r 0.0467081960203
}

shader {
	name "Sphere1956"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1956"
	type sphere
	c -3.86766847368 -0.902897402152 0.5
	r 0.0507596649404
}

shader {
	name "Sphere1957"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1957"
	type sphere
	c -3.72590755762 -0.534510882517 0.5
	r 0.0626420921115
}

shader {
	name "Sphere1958"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1958"
	type sphere
	c -3.63993226651 -0.379294961517 0.5
	r 0.0534066520176
}

shader {
	name "Sphere1959"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1959"
	type sphere
	c -3.56997622774 -0.23065030545 0.5
	r 0.0355239472609
}

shader {
	name "Sphere1960"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1960"
	type sphere
	c -3.39625793335 0.100004270924 0.5
	r 0.0384803179705
}

shader {
	name "Sphere1961"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1961"
	type sphere
	c -3.76043553786 0.274202939118 0.5
	r 0.0619899947541
}

shader {
	name "Sphere1962"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1962"
	type sphere
	c -4.04407081475 0.539498866506 0.5
	r 0.0550354274633
}

shader {
	name "Sphere1963"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1963"
	type sphere
	c -3.96780662509 1.62812314058 0.5
	r 0.047372464826
}

shader {
	name "Sphere1964"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1964"
	type sphere
	c -3.89030206146 1.98605701895 0.5
	r 0.0541789677204
}

shader {
	name "Sphere1965"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1965"
	type sphere
	c -3.6681002447 2.21830305671 0.5
	r 0.0497184733297
}

shader {
	name "Sphere1966"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1966"
	type sphere
	c -3.25750241582 2.922692626 0.5
	r 0.0585038513069
}

shader {
	name "Sphere1967"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1967"
	type sphere
	c -2.70541914243 2.89125168355 0.5
	r 0.0642235630081
}

shader {
	name "Sphere1968"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1968"
	type sphere
	c -2.39526650646 3.01404310353 0.5
	r 0.0629036389951
}

shader {
	name "Sphere1969"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1969"
	type sphere
	c -2.22630844724 2.93110730909 0.5
	r 0.0476333851299
}

shader {
	name "Sphere1970"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1970"
	type sphere
	c -1.88037858785 3.15370834327 0.5
	r 0.0556989281944
}

shader {
	name "Sphere1971"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1971"
	type sphere
	c -1.19393688282 2.82973453342 0.5
	r 0.0309895068043
}

shader {
	name "Sphere1972"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1972"
	type sphere
	c -0.893868938011 2.85561820754 0.5
	r 0.0320920425236
}

shader {
	name "Sphere1973"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1973"
	type sphere
	c -0.765214048215 2.93824391491 0.5
	r 0.0326364926178
}

shader {
	name "Sphere1974"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1974"
	type sphere
	c -0.509495531916 3.05952243356 0.5
	r 0.0279674241657
}

shader {
	name "Sphere1975"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1975"
	type sphere
	c -0.456328295221 2.91351775644 0.5
	r 0.0284838786949
}

shader {
	name "Sphere1976"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1976"
	type sphere
	c -0.265061566862 2.98724869173 0.5
	r 0.0309345932656
}

shader {
	name "Sphere1977"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1977"
	type sphere
	c -0.0446425603657 2.80881358028 0.5
	r 0.0275508470184
}

shader {
	name "Sphere1978"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1978"
	type sphere
	c -0.0503602038408 2.96094540455 0.5
	r 0.0288712259521
}

shader {
	name "Sphere1979"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1979"
	type sphere
	c 0.0771373464349 3.04030590845 0.5
	r 0.0294615306813
}

shader {
	name "Sphere1980"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1980"
	type sphere
	c 0.31129212224 2.92778952371 0.5
	r 0.033777644742
}

shader {
	name "Sphere1981"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1981"
	type sphere
	c 0.582699527779 2.9663703819 0.5
	r 0.0385638308858
}

shader {
	name "Sphere1982"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1982"
	type sphere
	c 0.879421847217 2.90147603478 0.5
	r 0.0329641127582
}

shader {
	name "Sphere1983"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1983"
	type sphere
	c 1.10007943762 2.96646861248 0.5
	r 0.0463201727341
}

shader {
	name "Sphere1984"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1984"
	type sphere
	c 1.86338431031 3.35288823655 0.5
	r 0.0636314463098
}

shader {
	name "Sphere1985"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1985"
	type sphere
	c 2.21166503128 3.01160437609 0.5
	r 0.0594553919939
}

shader {
	name "Sphere1986"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1986"
	type sphere
	c 2.5808648806 2.92578738794 0.5
	r 0.0579051658132
}

shader {
	name "Sphere1987"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1987"
	type sphere
	c 2.85222464623 2.60432576092 0.5
	r 0.0561746373325
}

shader {
	name "Sphere1988"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1988"
	type sphere
	c 3.14838617056 2.45418920946 0.5
	r 0.0587695662912
}

shader {
	name "Sphere1989"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1989"
	type sphere
	c 3.40769190682 2.26184222024 0.5
	r 0.0591444049423
}

shader {
	name "Sphere1990"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1990"
	type sphere
	c 2.99134731344 1.77233415441 0.5
	r 0.032230753249
}

shader {
	name "Sphere1991"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1991"
	type sphere
	c 3.23555257568 1.86823154408 0.5
	r 0.040854157891
}

shader {
	name "Sphere1992"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1992"
	type sphere
	c 3.44324086473 1.78900254361 0.5
	r 0.0401837363001
}

shader {
	name "Sphere1993"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1993"
	type sphere
	c 3.52582452921 1.71880674196 0.5
	r 0.0395144916629
}

shader {
	name "Sphere1994"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1994"
	type sphere
	c 3.70748827628 1.57600528688 0.5
	r 0.0465260704135
}

shader {
	name "Sphere1995"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1995"
	type sphere
	c 4.18368812329 1.3687786966 0.5
	r 0.0650668394464
}

shader {
	name "Sphere1996"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1996"
	type sphere
	c 4.75527068968 1.14749687906 0.5
	r 0.0632745857266
}

shader {
	name "Sphere1997"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1997"
	type sphere
	c 4.58063075507 0.858371758092 0.5
	r 0.0625148558881
}

shader {
	name "Sphere1998"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1998"
	type sphere
	c 5.06188830082 0.60238818011 0.5
	r 0.0879722937392
}

shader {
	name "Sphere1999"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere1999"
	type sphere
	c 5.55475746445 0.530696739599 0.5
	r 0.0847980041027
}

shader {
	name "Sphere2000"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2000"
	type sphere
	c 5.73828075047 0.123853457801 0.5
	r 0.0886529969502
}

shader {
	name "Sphere2001"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2001"
	type sphere
	c 5.87922765716 -0.296296983539 0.5
	r 0.0861433621171
}

shader {
	name "Sphere2002"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2002"
	type sphere
	c 6.17130799324 -0.619223613338 0.5
	r 0.0775084789973
}

shader {
	name "Sphere2003"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2003"
	type sphere
	c 6.092968758 -0.882970850983 0.5
	r 0.0828882678435
}

shader {
	name "Sphere2004"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2004"
	type sphere
	c 5.82700293368 -1.61012482803 0.5
	r 0.109081908234
}

shader {
	name "Sphere2005"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2005"
	type sphere
	c 5.61852541176 -2.13622967219 0.5
	r 0.0883086672499
}

shader {
	name "Sphere2006"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2006"
	type sphere
	c 4.78230456819 -2.56884725089 0.5
	r 0.0766470170049
}

shader {
	name "Sphere2007"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2007"
	type sphere
	c 4.27888736553 -3.0904583921 0.5
	r 0.0605383583913
}

shader {
	name "Sphere2008"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2008"
	type sphere
	c 3.92272740074 -3.35850577774 0.5
	r 0.0721807560713
}

shader {
	name "Sphere2009"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2009"
	type sphere
	c 3.59601703501 -3.80850239844 0.5
	r 0.0650913243826
}

shader {
	name "Sphere2010"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2010"
	type sphere
	c 3.19828638887 -3.72723544163 0.5
	r 0.0613255729904
}

shader {
	name "Sphere2011"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2011"
	type sphere
	c 2.99402992861 -4.07794969695 0.5
	r 0.0731234144551
}

shader {
	name "Sphere2012"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2012"
	type sphere
	c 2.37913082644 -4.80695923206 0.5
	r 0.0639846827656
}

shader {
	name "Sphere2013"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2013"
	type sphere
	c 1.94134051904 -5.164694479 0.5
	r 0.0802584464066
}

shader {
	name "Sphere2014"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2014"
	type sphere
	c 1.33969369392 -5.44775444411 0.5
	r 0.0824955840745
}

shader {
	name "Sphere2015"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2015"
	type sphere
	c 0.628849856206 -5.89604858883 0.5
	r 0.110152671667
}

shader {
	name "Sphere2016"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2016"
	type sphere
	c -0.211171643598 -5.94113412015 0.5
	r 0.0821678476683
}

shader {
	name "Sphere2017"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2017"
	type sphere
	c -0.730523888463 -5.36765646944 0.5
	r 0.0800794386119
}

shader {
	name "Sphere2018"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2018"
	type sphere
	c -0.976457488103 -4.67528843808 0.5
	r 0.0854344058462
}

shader {
	name "Sphere2019"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2019"
	type sphere
	c -1.40821731843 -4.86654208398 0.5
	r 0.0917783961214
}

shader {
	name "Sphere2020"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2020"
	type sphere
	c -1.61522202682 -4.72717611059 0.5
	r 0.0866343098059
}

shader {
	name "Sphere2021"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2021"
	type sphere
	c -1.79139613296 -4.10612551424 0.5
	r 0.0722872960449
}

shader {
	name "Sphere2022"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2022"
	type sphere
	c -2.30894393868 -3.13060649477 0.5
	r 0.0575089891841
}

shader {
	name "Sphere2023"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2023"
	type sphere
	c -2.42105428406 -2.61681024652 0.5
	r 0.0674916391701
}

shader {
	name "Sphere2024"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2024"
	type sphere
	c -2.14351176241 -2.21431539366 0.5
	r 0.0353930600303
}

shader {
	name "Sphere2025"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2025"
	type sphere
	c -2.24154816974 -2.38076255198 0.5
	r 0.0349158252815
}

shader {
	name "Sphere2026"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2026"
	type sphere
	c -2.5513339296 -2.4393871167 0.5
	r 0.0393265542851
}

shader {
	name "Sphere2027"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2027"
	type sphere
	c -2.65068984318 -2.46698398395 0.5
	r 0.0318439051353
}

shader {
	name "Sphere2028"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2028"
	type sphere
	c -2.78570504329 -2.35950821106 0.5
	r 0.0314401284985
}

shader {
	name "Sphere2029"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2029"
	type sphere
	c -2.94319523553 -2.23856411814 0.5
	r 0.0314438450366
}

shader {
	name "Sphere2030"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2030"
	type sphere
	c -3.17566137055 -2.114079815 0.5
	r 0.0445059862003
}

shader {
	name "Sphere2031"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2031"
	type sphere
	c -3.56350348214 -1.92053687704 0.5
	r 0.0455729692048
}

shader {
	name "Sphere2032"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2032"
	type sphere
	c -3.81409958538 -1.36924562958 0.5
	r 0.0527620962853
}

shader {
	name "Sphere2033"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2033"
	type sphere
	c -3.9057561699 -1.1221705991 0.5
	r 0.0451649242363
}

shader {
	name "Sphere2034"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2034"
	type sphere
	c -3.77546167811 -0.807496253073 0.5
	r 0.0487488935993
}

shader {
	name "Sphere2035"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2035"
	type sphere
	c -3.59533493834 -0.142731330014 0.5
	r 0.033103349606
}

shader {
	name "Sphere2036"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2036"
	type sphere
	c -3.49969680691 0.126022455306 0.5
	r 0.04151535314
}

shader {
	name "Sphere2037"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2037"
	type sphere
	c -3.5932675788 0.246654541569 0.5
	r 0.0650770069361
}

shader {
	name "Sphere2038"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2038"
	type sphere
	c -4.10735139222 0.402780326535 0.5
	r 0.0579544824589
}

shader {
	name "Sphere2039"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2039"
	type sphere
	c -3.98925450875 0.671513512569 0.5
	r 0.0521718039874
}

shader {
	name "Sphere2040"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2040"
	type sphere
	c -3.99475907775 1.49958848757 0.5
	r 0.0511251003609
}

shader {
	name "Sphere2041"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2041"
	type sphere
	c -3.95176597546 1.74957647694 0.5
	r 0.0445085513639
}

shader {
	name "Sphere2042"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2042"
	type sphere
	c -3.8510580703 2.12600250517 0.5
	r 0.0548289074538
}

shader {
	name "Sphere2043"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2043"
	type sphere
	c -3.6315979237 2.34802999158 0.5
	r 0.0513549757181
}

shader {
	name "Sphere2044"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2044"
	type sphere
	c -3.33771815305 2.78462802755 0.5
	r 0.0612530849782
}

shader {
	name "Sphere2045"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2045"
	type sphere
	c -3.17764844237 3.05037952268 0.5
	r 0.0544467479433
}

shader {
	name "Sphere2046"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2046"
	type sphere
	c -2.67481901414 3.0516935474 0.5
	r 0.0582768542725
}

shader {
	name "Sphere2047"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2047"
	type sphere
	c -2.52547357145 3.11211111556 0.5
	r 0.059351456195
}

shader {
	name "Sphere2048"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2048"
	type sphere
	c -2.23327223896 3.05500762264 0.5
	r 0.0454385087328
}

shader {
	name "Sphere2049"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2049"
	type sphere
	c -2.01321474097 3.21944496131 0.5
	r 0.0554599442422
}

shader {
	name "Sphere2050"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2050"
	type sphere
	c -1.2549702804 2.77472451115 0.5
	r 0.030634658266
}

shader {
	name "Sphere2051"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2051"
	type sphere
	c -1.13573396513 2.88446088075 0.5
	r 0.0289286532577
}

shader {
	name "Sphere2052"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2052"
	type sphere
	c -0.944434171862 2.92444007508 0.5
	r 0.0319585385294
}

shader {
	name "Sphere2053"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2053"
	type sphere
	c -0.767064632828 3.02253516231 0.5
	r 0.0305971769477
}

shader {
	name "Sphere2054"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2054"
	type sphere
	c -0.582093548919 3.07729275612 0.5
	r 0.0280885232952
}

shader {
	name "Sphere2055"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2055"
	type sphere
	c -0.435906399199 3.04714102395 0.5
	r 0.0280001656863
}

shader {
	name "Sphere2056"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2056"
	type sphere
	c -0.330095734313 3.03588608725 0.5
	r 0.0299727916533
}

shader {
	name "Sphere2057"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2057"
	type sphere
	c -0.193821335793 2.9462794659 0.5
	r 0.0307008429165
}

shader {
	name "Sphere2058"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2058"
	type sphere
	c -0.109608957094 2.84296090078 0.5
	r 0.0274946170389
}

shader {
	name "Sphere2059"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2059"
	type sphere
	c -0.116349011077 2.91923127478 0.5
	r 0.0296796716305
}

shader {
	name "Sphere2060"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2060"
	type sphere
	c 0.139775145884 3.08521621273 0.5
	r 0.0283441049408
}

shader {
	name "Sphere2061"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2061"
	type sphere
	c 0.313216956141 3.01633744535 0.5
	r 0.032648985228
}

shader {
	name "Sphere2062"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2062"
	type sphere
	c 0.305235455176 2.83889781519 0.5
	r 0.0330457098633
}

shader {
	name "Sphere2063"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2063"
	type sphere
	c 0.51816066939 2.88743804847 0.5
	r 0.0379051977802
}

shader {
	name "Sphere2064"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2064"
	type sphere
	c 0.649841655436 3.04137317797 0.5
	r 0.0369350774354
}

shader {
	name "Sphere2065"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2065"
	type sphere
	c 0.85430532633 2.98300944972 0.5
	r 0.0310216456006
}

shader {
	name "Sphere2066"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2066"
	type sphere
	c 1.00257175316 3.04700876138 0.5
	r 0.0485317437682
}

shader {
	name "Sphere2067"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2067"
	type sphere
	c 1.71037067714 3.29627930557 0.5
	r 0.058730641116
}

shader {
	name "Sphere2068"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2068"
	type sphere
	c 2.02031759171 3.39612626969 0.5
	r 0.0584541386512
}

shader {
	name "Sphere2069"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2069"
	type sphere
	c 2.2509950446 3.16448213343 0.5
	r 0.0589364699885
}

shader {
	name "Sphere2070"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2070"
	type sphere
	c 2.55283014948 3.07321391299 0.5
	r 0.0546461385854
}

shader {
	name "Sphere2071"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2071"
	type sphere
	c 2.85223724988 2.74865229917 0.5
	r 0.0520702667657
}

shader {
	name "Sphere2072"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2072"
	type sphere
	c 3.28789853402 2.51455059937 0.5
	r 0.0552383206517
}

shader {
	name "Sphere2073"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2073"
	type sphere
	c 3.42843529545 2.41851012825 0.5
	r 0.0593819882506
}

shader {
	name "Sphere2074"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2074"
	type sphere
	c 3.3961616855 2.10742317714 0.5
	r 0.0569922822755
}

shader {
	name "Sphere2075"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2075"
	type sphere
	c 2.92214882336 1.72672454712 0.5
	r 0.0299273142901
}

shader {
	name "Sphere2076"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2076"
	type sphere
	c 3.05868177707 1.82134392141 0.5
	r 0.0302307275194
}

shader {
	name "Sphere2077"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2077"
	type sphere
	c 3.31796478997 1.93823792672 0.5
	r 0.0402453180906
}

shader {
	name "Sphere2078"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2078"
	type sphere
	c 3.42941841795 1.89506285742 0.5
	r 0.0400341902415
}

shader {
	name "Sphere2079"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2079"
	type sphere
	c 3.62387967764 1.76510172619 0.5
	r 0.0418113726437
}

shader {
	name "Sphere2080"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2080"
	type sphere
	c 3.72339321437 1.69741411802 0.5
	r 0.0453085778749
}

shader {
	name "Sphere2081"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2081"
	type sphere
	c 3.68306731604 1.45386780389 0.5
	r 0.0468901796592
}

shader {
	name "Sphere2082"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2082"
	type sphere
	c 4.2967085787 1.50041772853 0.5
	r 0.0650586102775
}

shader {
	name "Sphere2083"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2083"
	type sphere
	c 4.68273586362 1.30396951978 0.5
	r 0.0660759299693
}

shader {
	name "Sphere2084"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2084"
	type sphere
	c 4.83805376657 0.99368575319 0.5
	r 0.0677306866719
}

shader {
	name "Sphere2085"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2085"
	type sphere
	c 4.8234810147 0.602700284019 0.5
	r 0.0908333240653
}

shader {
	name "Sphere2086"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2086"
	type sphere
	c 5.29838844439 0.608945832319 0.5
	r 0.0894709870577
}

shader {
	name "Sphere2087"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2087"
	type sphere
	c 5.76796706983 0.495141721129 0.5
	r 0.0773173977876
}

shader {
	name "Sphere2088"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2088"
	type sphere
	c 6.11065031264 -0.260529226513 0.5
	r 0.0894844405685
}

shader {
	name "Sphere2089"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2089"
	type sphere
	c 6.01570863998 -1.09422964791 0.5
	r 0.0858190686221
}

shader {
	name "Sphere2090"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2090"
	type sphere
	c 5.72407701336 -1.86344851797 0.5
	r 0.0959942563666
}

shader {
	name "Sphere2091"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2091"
	type sphere
	c 4.26405453195 -3.25066951208 0.5
	r 0.0601338585951
}

shader {
	name "Sphere2092"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2092"
	type sphere
	c 4.01594240429 -3.52946147103 0.5
	r 0.0738573326175
}

shader {
	name "Sphere2093"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2093"
	type sphere
	c 3.76308020972 -3.81324112228 0.5
	r 0.0602564514898
}

shader {
	name "Sphere2094"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2094"
	type sphere
	c 3.41696981832 -3.79447017406 0.5
	r 0.0696058549907
}

shader {
	name "Sphere2095"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2095"
	type sphere
	c 3.06970463022 -3.8997288918 0.5
	r 0.0720927697895
}

shader {
	name "Sphere2096"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2096"
	type sphere
	c 2.94331920556 -4.27402171958 0.5
	r 0.078769298385
}

shader {
	name "Sphere2097"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2097"
	type sphere
	c 2.36650761495 -4.6384303352 0.5
	r 0.0627660595671
}

shader {
	name "Sphere2098"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2098"
	type sphere
	c 2.40355609232 -4.98391787563 0.5
	r 0.0699925999001
}

shader {
	name "Sphere2099"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2099"
	type sphere
	c 2.13644454213 -5.22048734645 0.5
	r 0.071935060139
}

shader {
	name "Sphere2100"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2100"
	type sphere
	c 1.36389252901 -5.66652248489 0.5
	r 0.0825811695791
}

shader {
	name "Sphere2101"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2101"
	type sphere
	c 0.50882416721 -6.14885224829 0.5
	r 0.0997346055619
}

shader {
	name "Sphere2102"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2102"
	type sphere
	c -0.104413524683 -6.13933906033 0.5
	r 0.0866779489149
}

shader {
	name "Sphere2103"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2103"
	type sphere
	c -0.337263079431 -5.76391936608 0.5
	r 0.0809534785829
}

shader {
	name "Sphere2104"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2104"
	type sphere
	c -0.585044919197 -5.51336559618 0.5
	r 0.0743464175953
}

shader {
	name "Sphere2105"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2105"
	type sphere
	c -0.886770457536 -5.20825629985 0.5
	r 0.087325877857
}

shader {
	name "Sphere2106"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2106"
	type sphere
	c -1.01148688456 -4.90461960649 0.5
	r 0.0885588754208
}

shader {
	name "Sphere2107"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2107"
	type sphere
	c -1.80846404264 -4.61022782291 0.5
	r 0.0827717128207
}

shader {
	name "Sphere2108"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2108"
	type sphere
	c -1.64362744793 -4.2398275031 0.5
	r 0.0771713635658
}

shader {
	name "Sphere2109"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2109"
	type sphere
	c -1.94893077111 -3.99219558727 0.5
	r 0.0735239505771
}

shader {
	name "Sphere2110"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2110"
	type sphere
	c -2.15648168709 -3.1767450535 0.5
	r 0.0619589832128
}

shader {
	name "Sphere2111"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2111"
	type sphere
	c -2.45998897135 -3.10670229131 0.5
	r 0.0571846558895
}

shader {
	name "Sphere2112"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2112"
	type sphere
	c -2.54558447621 -2.73345426736 0.5
	r 0.0604786618726
}

shader {
	name "Sphere2113"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2113"
	type sphere
	c -2.09600511973 -2.29315702041 0.5
	r 0.0336431392001
}

shader {
	name "Sphere2114"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2114"
	type sphere
	c -2.14979701753 -2.3850780471 0.5
	r 0.033973613704
}

shader {
	name "Sphere2115"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2115"
	type sphere
	c -2.33049914452 -2.37573898329 0.5
	r 0.0319037121943
}

shader {
	name "Sphere2116"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2116"
	type sphere
	c -2.45901889251 -2.39221397075 0.5
	r 0.0384255943782
}

shader {
	name "Sphere2117"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2117"
	type sphere
	c -2.73215091739 -2.4998504535 0.5
	r 0.0340371443444
}

shader {
	name "Sphere2118"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2118"
	type sphere
	c -2.95815861471 -2.32457310747 0.5
	r 0.0340318377851
}

shader {
	name "Sphere2119"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2119"
	type sphere
	c -3.29511963822 -2.13545312687 0.5
	r 0.046510449667
}

shader {
	name "Sphere2120"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2120"
	type sphere
	c -3.51587378718 -2.03490431651 0.5
	r 0.0473438253881
}

shader {
	name "Sphere2121"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2121"
	type sphere
	c -3.87253625757 -1.24276477352 0.5
	r 0.0486496059905
}

shader {
	name "Sphere2122"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2122"
	type sphere
	c -3.94527803398 -1.01075577091 0.5
	r 0.0434977705401
}

shader {
	name "Sphere2123"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2123"
	type sphere
	c -3.90294452458 -0.772791576193 0.5
	r 0.0503427990004
}

shader {
	name "Sphere2124"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2124"
	type sphere
	c -3.65413878311 -0.204128814862 0.5
	r 0.0306578698717
}

shader {
	name "Sphere2125"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2125"
	type sphere
	c -3.54116137125 -0.0748446604714 0.5
	r 0.0320361053451
}

shader {
	name "Sphere2126"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2126"
	type sphere
	c -3.57095498212 0.0456772154619 0.5
	r 0.0390287985298
}

shader {
	name "Sphere2127"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2127"
	type sphere
	c -3.42057227334 0.204903458627 0.5
	r 0.0422798363407
}

shader {
	name "Sphere2128"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2128"
	type sphere
	c -3.70569673387 0.111366525895 0.5
	r 0.0668530073844
}

shader {
	name "Sphere2129"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2129"
	type sphere
	c -4.0113854753 0.282313181143 0.5
	r 0.0575596165091
}

shader {
	name "Sphere2130"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2130"
	type sphere
	c -4.19763243088 0.532003402886 0.5
	r 0.0602729003216
}

shader {
	name "Sphere2131"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2131"
	type sphere
	c -3.89189898415 1.42103017787 0.5
	r 0.0459458987582
}

shader {
	name "Sphere2132"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2132"
	type sphere
	c -4.08766460094 1.59114318461 0.5
	r 0.0467023271215
}

shader {
	name "Sphere2133"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2133"
	type sphere
	c -3.99396924686 2.0896925509 0.5
	r 0.0557599014559
}

shader {
	name "Sphere2134"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2134"
	type sphere
	c -3.76031295054 2.3120188726 0.5
	r 0.0488882377156
}

shader {
	name "Sphere2135"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2135"
	type sphere
	c -3.40869468419 2.92226339378 0.5
	r 0.0548908069437
}

shader {
	name "Sphere2136"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2136"
	type sphere
	c -3.32365638181 3.05918941004 0.5
	r 0.0552583660128
}

shader {
	name "Sphere2137"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2137"
	type sphere
	c -3.03712971555 3.04639997156 0.5
	r 0.0509845521748
}

shader {
	name "Sphere2138"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2138"
	type sphere
	c -2.82053431682 3.00411714955 0.5
	r 0.0566873161316
}

shader {
	name "Sphere2139"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2139"
	type sphere
	c -2.38319781726 3.17313132473 0.5
	r 0.0567553656934
}

shader {
	name "Sphere2140"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2140"
	type sphere
	c -2.13698423113 3.12677947155 0.5
	r 0.0446320222168
}

shader {
	name "Sphere2141"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2141"
	type sphere
	c -1.88812066654 3.30588299557 0.5
	r 0.0585796736033
}

shader {
	name "Sphere2142"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2142"
	type sphere
	c -1.27341621871 2.8558358989 0.5
	r 0.0317521335907
}

shader {
	name "Sphere2143"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2143"
	type sphere
	c -1.20971638815 2.90880943878 0.5
	r 0.0294859536224
}

shader {
	name "Sphere2144"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2144"
	type sphere
	c -1.05763713789 2.86783687984 0.5
	r 0.0309562605771
}

shader {
	name "Sphere2145"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2145"
	type sphere
	c -0.858113930493 2.93510027783 0.5
	r 0.0332734589549
}

shader {
	name "Sphere2146"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2146"
	type sphere
	c -0.699822358157 3.06364207558 0.5
	r 0.0285116825798
}

shader {
	name "Sphere2147"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2147"
	type sphere
	c -0.529857418286 3.13282435152 0.5
	r 0.0290906593637
}

shader {
	name "Sphere2148"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2148"
	type sphere
	c -0.254240462986 3.0717450348 0.5
	r 0.0329552311045
}

shader {
	name "Sphere2149"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2149"
	type sphere
	c -0.189795482777 2.86451219058 0.5
	r 0.0306988991683
}

shader {
	name "Sphere2150"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2150"
	type sphere
	c -0.118881977539 2.99832099429 0.5
	r 0.0296680309694
}

shader {
	name "Sphere2151"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2151"
	type sphere
	c 0.0703945559347 3.11842335646 0.5
	r 0.0293444044776
}

shader {
	name "Sphere2152"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2152"
	type sphere
	c 0.239926580482 3.06410961765 0.5
	r 0.032964912164
}

shader {
	name "Sphere2153"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2153"
	type sphere
	c 0.387691194308 2.97191024503 0.5
	r 0.0323902791175
}

shader {
	name "Sphere2154"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2154"
	type sphere
	c 0.385695463851 2.87708469516 0.5
	r 0.0337508362563
}

shader {
	name "Sphere2155"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2155"
	type sphere
	c 0.552929912388 3.06348361774 0.5
	r 0.0376164221246
}

shader {
	name "Sphere2156"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2156"
	type sphere
	c 0.745473576325 3.0221360026 0.5
	r 0.0362256185013
}

shader {
	name "Sphere2157"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2157"
	type sphere
	c 1.12610870579 3.0925104482 0.5
	r 0.0502059261918
}

shader {
	name "Sphere2158"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2158"
	type sphere
	c 1.67627310388 3.14341309982 0.5
	r 0.0587365064907
}

shader {
	name "Sphere2159"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2159"
	type sphere
	c 1.73403994173 3.44916797444 0.5
	r 0.057301846895
}

shader {
	name "Sphere2160"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2160"
	type sphere
	c 1.91341500724 3.502324549 0.5
	r 0.0545602779774
}

shader {
	name "Sphere2161"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2161"
	type sphere
	c 2.13782085305 3.29280143073 0.5
	r 0.058898787646
}

shader {
	name "Sphere2162"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2162"
	type sphere
	c 2.41772901924 3.13503937782 0.5
	r 0.0567855477314
}

shader {
	name "Sphere2163"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2163"
	type sphere
	c 2.68474206321 3.0261121085 0.5
	r 0.0504056333913
}

shader {
	name "Sphere2164"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2164"
	type sphere
	c 2.73674247221 2.83348628985 0.5
	r 0.0554072444789
}

shader {
	name "Sphere2165"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2165"
	type sphere
	c 2.97940982403 2.6820254382 0.5
	r 0.0556063381591
}

shader {
	name "Sphere2166"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2166"
	type sphere
	c 3.17303395039 2.59997786527 0.5
	r 0.0521235711541
}

shader {
	name "Sphere2167"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2167"
	type sphere
	c 3.55053144975 2.32232299896 0.5
	r 0.05719280336
}

shader {
	name "Sphere2168"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2168"
	type sphere
	c 2.9860270247 1.85482942535 0.5
	r 0.0297692350576
}

shader {
	name "Sphere2169"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2169"
	type sphere
	c 3.13371274388 1.79724730303 0.5
	r 0.0288733316609
}

shader {
	name "Sphere2170"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2170"
	type sphere
	c 3.53325907519 1.8548746733 0.5
	r 0.0434754462394
}

shader {
	name "Sphere2171"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2171"
	type sphere
	c 3.8235567186 1.62421578577 0.5
	r 0.0477359379545
}

shader {
	name "Sphere2172"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2172"
	type sphere
	c 3.80362407519 1.49377689332 0.5
	r 0.0483529330753
}

shader {
	name "Sphere2173"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2173"
	type sphere
	c 4.12332629987 1.53495501461 0.5
	r 0.0675329026264
}

shader {
	name "Sphere2174"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2174"
	type sphere
	c 4.47648976357 1.47367033631 0.5
	r 0.0712613893538
}

shader {
	name "Sphere2175"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2175"
	type sphere
	c 4.86075796573 1.287221625 0.5
	r 0.0680301957737
}

shader {
	name "Sphere2176"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2176"
	type sphere
	c 4.94667382984 0.802641858647 0.5
	r 0.0853019092611
}

shader {
	name "Sphere2177"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2177"
	type sphere
	c 5.17284868554 0.79937051106 0.5
	r 0.0815911551455
}

shader {
	name "Sphere2178"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2178"
	type sphere
	c 5.69950474471 0.68391479309 0.5
	r 0.0732858192944
}

shader {
	name "Sphere2179"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2179"
	type sphere
	c 5.96055246236 -0.0844651735645 0.5
	r 0.0840363144231
}

shader {
	name "Sphere2180"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2180"
	type sphere
	c 6.2314771856 -1.04934165704 0.5
	r 0.0794721465545
}

shader {
	name "Sphere2181"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2181"
	type sphere
	c 5.79382863298 -1.13248247048 0.5
	r 0.0830459187737
}

shader {
	name "Sphere2182"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2182"
	type sphere
	c 5.98513630298 -1.84059892907 0.5
	r 0.100548758596
}

shader {
	name "Sphere2183"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2183"
	type sphere
	c 4.40614742035 -3.18356262038 0.5
	r 0.0577229174685
}

shader {
	name "Sphere2184"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2184"
	type sphere
	c 4.12081228616 -3.30911283058 0.5
	r 0.0558956802364
}

shader {
	name "Sphere2185"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2185"
	type sphere
	c 3.91048778598 -3.68729164298 0.5
	r 0.0685064964685
}

shader {
	name "Sphere2186"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2186"
	type sphere
	c 3.681865205 -3.95021372403 0.5
	r 0.0591735320804
}

shader {
	name "Sphere2187"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2187"
	type sphere
	c 3.50051947372 -3.95347029244 0.5
	r 0.0651054667019
}

shader {
	name "Sphere2188"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2188"
	type sphere
	c 3.19098060712 -4.05487703172 0.5
	r 0.0755997467417
}

shader {
	name "Sphere2189"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2189"
	type sphere
	c 2.73391012758 -4.32930385155 0.5
	r 0.0836680904181
}

shader {
	name "Sphere2190"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2190"
	type sphere
	c 2.51478437267 -4.71046408422 0.5
	r 0.0608699285486
}

shader {
	name "Sphere2191"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2191"
	type sphere
	c 2.00429503052 -5.35172610128 0.5
	r 0.0677484968942
}

shader {
	name "Sphere2192"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2192"
	type sphere
	c 1.53717377213 -5.53651977796 0.5
	r 0.0798887963393
}

shader {
	name "Sphere2193"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2193"
	type sphere
	c 1.18948953182 -5.80218595297 0.5
	r 0.0831348597496
}

shader {
	name "Sphere2194"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2194"
	type sphere
	c 0.773391020311 -6.13450830186 0.5
	r 0.0989819509055
}

shader {
	name "Sphere2195"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2195"
	type sphere
	c 0.246506825755 -6.17793666517 0.5
	r 0.0982089814777
}

shader {
	name "Sphere2196"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2196"
	type sphere
	c -0.333443671186 -6.12798063094 0.5
	r 0.0853057707595
}

shader {
	name "Sphere2197"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2197"
	type sphere
	c -0.778865843364 -5.5722283022 0.5
	r 0.0775750915877
}

shader {
	name "Sphere2198"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2198"
	type sphere
	c -1.81732453648 -4.83306232724 0.5
	r 0.0844862320687
}

shader {
	name "Sphere2199"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2199"
	type sphere
	c -1.81949234453 -4.38398381859 0.5
	r 0.0871127619674
}

shader {
	name "Sphere2200"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2200"
	type sphere
	c -1.9690935997 -4.18880293291 0.5
	r 0.0747049459257
}

shader {
	name "Sphere2201"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2201"
	type sphere
	c -1.9390376288 -3.79604473398 0.5
	r 0.0737761859686
}

shader {
	name "Sphere2202"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2202"
	type sphere
	c -2.27777368944 -3.2822825298 0.5
	r 0.0586253178623
}

shader {
	name "Sphere2203"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2203"
	type sphere
	c -2.53432075523 -2.96521584422 0.5
	r 0.0626831513125
}

shader {
	name "Sphere2204"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2204"
	type sphere
	c -2.58455285496 -2.58011248284 0.5
	r 0.0581831835147
}

shader {
	name "Sphere2205"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2205"
	type sphere
	c -2.19812385174 -2.46155462888 0.5
	r 0.0338761072679
}

shader {
	name "Sphere2206"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2206"
	type sphere
	c -2.29413433296 -2.45241486748 0.5
	r 0.0317429278513
}

shader {
	name "Sphere2207"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2207"
	type sphere
	c -2.88452292408 -2.38028548903 0.5
	r 0.0352207612363
}

shader {
	name "Sphere2208"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2208"
	type sphere
	c -3.02442869885 -2.26523819067 0.5
	r 0.0326817326257
}

shader {
	name "Sphere2209"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2209"
	type sphere
	c -3.21493601432 -2.22429189462 0.5
	r 0.0432446552652
}

shader {
	name "Sphere2210"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2210"
	type sphere
	c -3.63698291041 -2.01573288206 0.5
	r 0.0446190314666
}

shader {
	name "Sphere2211"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2211"
	type sphere
	c -3.98692315006 -1.20484877912 0.5
	r 0.0417307895107
}

shader {
	name "Sphere2212"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2212"
	type sphere
	c -4.01663719705 -1.09653756557 0.5
	r 0.0401890780548
}

shader {
	name "Sphere2213"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2213"
	type sphere
	c -3.99853345336 -0.867966661673 0.5
	r 0.0508253351286
}

shader {
	name "Sphere2214"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2214"
	type sphere
	c -3.80732466922 -0.681090771543 0.5
	r 0.049020721975
}

shader {
	name "Sphere2215"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2215"
	type sphere
	c -3.67754567081 -0.12720862101 0.5
	r 0.0296441758667
}

shader {
	name "Sphere2216"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2216"
	type sphere
	c -3.6235047729 -0.0629343100802 0.5
	r 0.0303641301193
}

shader {
	name "Sphere2217"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2217"
	type sphere
	c -3.87683715532 0.151323773297 0.5
	r 0.0649542925968
}

shader {
	name "Sphere2218"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2218"
	type sphere
	c -4.1621418114 0.260008769217 0.5
	r 0.0567384141491
}

shader {
	name "Sphere2219"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2219"
	type sphere
	c -4.25556707509 0.391786660097 0.5
	r 0.0535126495161
}

shader {
	name "Sphere2220"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2220"
	type sphere
	c -4.00698856362 1.36541733023 0.5
	r 0.0499204147779
}

shader {
	name "Sphere2221"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2221"
	type sphere
	c -4.1257807544 1.46803955281 0.5
	r 0.0499497899821
}

shader {
	name "Sphere2222"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2222"
	type sphere
	c -4.03076013399 1.94623231486 0.5
	r 0.0553171208935
}

shader {
	name "Sphere2223"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2223"
	type sphere
	c -3.95253623004 2.23102628855 0.5
	r 0.054701427335
}

shader {
	name "Sphere2224"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2224"
	type sphere
	c -3.72971032096 2.43862823243 0.5
	r 0.0488032596085
}

shader {
	name "Sphere2225"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2225"
	type sphere
	c -3.49538515194 2.79994191487 0.5
	r 0.0575536328358
}

shader {
	name "Sphere2226"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2226"
	type sphere
	c -3.24190811402 3.1816824866 0.5
	r 0.0551912825275
}

shader {
	name "Sphere2227"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2227"
	type sphere
	c -2.79037934355 3.15192630983 0.5
	r 0.0564530371
}

shader {
	name "Sphere2228"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2228"
	type sphere
	c -2.5059785048 3.27207563817 0.5
	r 0.0615096094623
}

shader {
	name "Sphere2229"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2229"
	type sphere
	c -2.2430541697 3.17033207685 0.5
	r 0.0413654165755
}

shader {
	name "Sphere2230"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2230"
	type sphere
	c -2.03040583689 3.37063903436 0.5
	r 0.0586662560599
}

shader {
	name "Sphere2231"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2231"
	type sphere
	c -1.75336921122 3.23263157356 0.5
	r 0.0564511727548
}

shader {
	name "Sphere2232"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2232"
	type sphere
	c -1.33775952767 2.7969617595 0.5
	r 0.0336581252053
}

shader {
	name "Sphere2233"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2233"
	type sphere
	c -1.15041114312 2.96201557906 0.5
	r 0.0302698248991
}

shader {
	name "Sphere2234"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2234"
	type sphere
	c -0.912519269553 3.00624214873 0.5
	r 0.0338970146645
}

shader {
	name "Sphere2235"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2235"
	type sphere
	c -0.810791312664 2.86435779403 0.5
	r 0.0305599974711
}

shader {
	name "Sphere2236"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2236"
	type sphere
	c -0.76679889897 3.10300004521 0.5
	r 0.0297518143171
}

shader {
	name "Sphere2237"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2237"
	type sphere
	c -0.604472018318 3.14885686005 0.5
	r 0.0281475592985
}

shader {
	name "Sphere2238"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2238"
	type sphere
	c -0.324070318926 3.1125522351 0.5
	r 0.0277041289495
}

shader {
	name "Sphere2239"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2239"
	type sphere
	c -0.0528235446211 3.03578500246 0.5
	r 0.0272888695166
}

shader {
	name "Sphere2240"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2240"
	type sphere
	c 0.134149072446 3.15952460388 0.5
	r 0.0275466966731
}

shader {
	name "Sphere2241"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2241"
	type sphere
	c 0.31949721855 3.1052900794 0.5
	r 0.0342315590271
}

shader {
	name "Sphere2242"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2242"
	type sphere
	c 0.377333776866 2.78866956222 0.5
	r 0.0328563995898
}

shader {
	name "Sphere2243"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2243"
	type sphere
	c 0.620297025799 3.13140586069 0.5
	r 0.0341321978604
}

shader {
	name "Sphere2244"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2244"
	type sphere
	c 0.715591711675 3.11603971938 0.5
	r 0.037682053938
}

shader {
	name "Sphere2245"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2245"
	type sphere
	c 1.02523233288 3.16975898741 0.5
	r 0.045086523272
}

shader {
	name "Sphere2246"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2246"
	type sphere
	c 1.55796627867 3.25004609817 0.5
	r 0.060716389834
}

shader {
	name "Sphere2247"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2247"
	type sphere
	c 2.0556251295 3.54597224913 0.5
	r 0.0570079649849
}

shader {
	name "Sphere2248"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2248"
	type sphere
	c 2.54176074174 3.22066140085 0.5
	r 0.0562506718922
}

shader {
	name "Sphere2249"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2249"
	type sphere
	c 2.87045808638 2.88705584615 0.5
	r 0.0526280696304
}

shader {
	name "Sphere2250"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2250"
	type sphere
	c 3.29842380838 2.65540494467 0.5
	r 0.0506969638097
}

shader {
	name "Sphere2251"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2251"
	type sphere
	c 3.57893540185 2.47908458214 0.5
	r 0.0622927622161
}

shader {
	name "Sphere2252"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2252"
	type sphere
	c 3.53205286059 2.1735553602 0.5
	r 0.0552403482787
}

shader {
	name "Sphere2253"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2253"
	type sphere
	c 3.5121681983 1.96744137106 0.5
	r 0.0424186669132
}

shader {
	name "Sphere2254"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2254"
	type sphere
	c 3.83702507901 1.75344946798 0.5
	r 0.0497142647609
}

shader {
	name "Sphere2255"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2255"
	type sphere
	c 4.24474764832 1.67452384281 0.5
	r 0.0712122357966
}

shader {
	name "Sphere2256"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2256"
	type sphere
	c 4.78355509632 1.44876418672 0.5
	r 0.0662518163874
}

shader {
	name "Sphere2257"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2257"
	type sphere
	c 5.39090088679 0.81889865548 0.5
	r 0.0826025182331
}

shader {
	name "Sphere2258"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2258"
	type sphere
	c 5.89622740848 0.654200928734 0.5
	r 0.0759297298272
}

shader {
	name "Sphere2259"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2259"
	type sphere
	c 6.17329468527 -0.0460417987612 0.5
	r 0.0781018369813
}

shader {
	name "Sphere2260"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2260"
	type sphere
	c 6.30755426521 -0.851040979415 0.5
	r 0.0798227700068
}

shader {
	name "Sphere2261"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2261"
	type sphere
	c 6.16762449598 -1.24401506265 0.5
	r 0.0741861812839
}

shader {
	name "Sphere2262"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2262"
	type sphere
	c 5.93245910046 -1.29478111326 0.5
	r 0.0770386884811
}

shader {
	name "Sphere2263"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2263"
	type sphere
	c 6.11132337957 -1.59829974443 0.5
	r 0.104342776514
}

shader {
	name "Sphere2264"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2264"
	type sphere
	c 5.86740096019 -2.06466219041 0.5
	r 0.0892856436183
}

shader {
	name "Sphere2265"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2265"
	type sphere
	c 4.42996086503 -3.02406569412 0.5
	r 0.0632257148905
}

shader {
	name "Sphere2266"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2266"
	type sphere
	c 4.39483348838 -3.33618625255 0.5
	r 0.0570588873247
}

shader {
	name "Sphere2267"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2267"
	type sphere
	c 4.23957074637 -3.41081406657 0.5
	r 0.0613701554342
}

shader {
	name "Sphere2268"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2268"
	type sphere
	c 4.09843564845 -3.70743025301 0.5
	r 0.0732612853938
}

shader {
	name "Sphere2269"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2269"
	type sphere
	c 3.84095946233 -3.953666729 0.5
	r 0.0601752618081
}

shader {
	name "Sphere2270"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2270"
	type sphere
	c 2.88935565717 -4.46952151158 0.5
	r 0.0733388249685
}

shader {
	name "Sphere2271"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2271"
	type sphere
	c 2.50337324137 -4.55098326384 0.5
	r 0.0590464782435
}

shader {
	name "Sphere2272"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2272"
	type sphere
	c 2.52949771002 -4.86785437192 0.5
	r 0.0576874585649
}

shader {
	name "Sphere2273"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2273"
	type sphere
	c 2.17496397259 -5.39907890562 0.5
	r 0.0650887114657
}

shader {
	name "Sphere2274"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2274"
	type sphere
	c 1.82880446367 -5.3232835905 0.5
	r 0.0655868977102
}

shader {
	name "Sphere2275"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2275"
	type sphere
	c 1.56611169709 -5.74958916789 0.5
	r 0.0813803335001
}

shader {
	name "Sphere2276"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2276"
	type sphere
	c 1.38822066872 -5.87657908854 0.5
	r 0.0760143686805
}

shader {
	name "Sphere2277"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2277"
	type sphere
	c 0.984817718181 -5.72242390644 0.5
	r 0.0816135883253
}

shader {
	name "Sphere2278"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2278"
	type sphere
	c 0.653928236252 -6.36024698645 0.5
	r 0.0925682700621
}

shader {
	name "Sphere2279"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2279"
	type sphere
	c -0.230384359859 -6.32822893026 0.5
	r 0.0836034924723
}

shader {
	name "Sphere2280"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2280"
	type sphere
	c -0.626912481485 -5.709234364 0.5
	r 0.0758736715197
}

shader {
	name "Sphere2281"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2281"
	type sphere
	c -0.934268612574 -5.43096289096 0.5
	r 0.079935510003
}

shader {
	name "Sphere2282"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2282"
	type sphere
	c -1.99875316036 -4.71202915446 0.5
	r 0.079084924142
}

shader {
	name "Sphere2283"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2283"
	type sphere
	c -2.12141231067 -4.07231501094 0.5
	r 0.0691121755976
}

shader {
	name "Sphere2284"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2284"
	type sphere
	c -1.7706913975 -3.70035099433 0.5
	r 0.0714563234368
}

shader {
	name "Sphere2285"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2285"
	type sphere
	c -2.12986523617 -3.33653148999 0.5
	r 0.0595320830028
}

shader {
	name "Sphere2286"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2286"
	type sphere
	c -2.60879919669 -3.10251671167 0.5
	r 0.0544671522532
}

shader {
	name "Sphere2287"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2287"
	type sphere
	c -2.69202593284 -2.68600474921 0.5
	r 0.054973983433
}

shader {
	name "Sphere2288"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2288"
	type sphere
	c -2.1064390704 -2.46614038764 0.5
	r 0.0349734364903
}

shader {
	name "Sphere2289"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2289"
	type sphere
	c -2.37876398909 -2.44582826989 0.5
	r 0.0319212583546
}

shader {
	name "Sphere2290"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2290"
	type sphere
	c -2.97012246656 -2.41430622586 0.5
	r 0.0338635305177
}

shader {
	name "Sphere2291"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2291"
	type sphere
	c -3.04532355958 -2.35250107884 0.5
	r 0.0346154913678
}

shader {
	name "Sphere2292"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2292"
	type sphere
	c -3.32634675333 -2.24995361674 0.5
	r 0.0425012960734
}

shader {
	name "Sphere2293"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2293"
	type sphere
	c -3.59613960842 -2.12702752409 0.5
	r 0.0442952720625
}

shader {
	name "Sphere2294"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2294"
	type sphere
	c -3.68018035704 -1.90799278381 0.5
	r 0.0424389712866
}

shader {
	name "Sphere2295"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2295"
	type sphere
	c -3.97040026355 -1.31764496639 0.5
	r 0.0437691632601
}

shader {
	name "Sphere2296"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2296"
	type sphere
	c -4.05980955847 -0.99389242586 0.5
	r 0.0433269748463
}

shader {
	name "Sphere2297"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2297"
	type sphere
	c -4.03269870354 -0.73715122757 0.5
	r 0.0505771670216
}

shader {
	name "Sphere2298"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2298"
	type sphere
	c -3.92958947153 -0.646846602991 0.5
	r 0.0462066718861
}

shader {
	name "Sphere2299"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2299"
	type sphere
	c -3.73135799693 -0.184215868212 0.5
	r 0.0291511970849
}

shader {
	name "Sphere2300"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2300"
	type sphere
	c -3.82977343258 -0.0221151709834 0.5
	r 0.069828994693
}

shader {
	name "Sphere2301"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2301"
	type sphere
	c -4.06884439066 0.142657605158 0.5
	r 0.0557008305042
}

shader {
	name "Sphere2302"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2302"
	type sphere
	c -4.34014675204 0.499706333591 0.5
	r 0.0493232024269
}

shader {
	name "Sphere2303"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2303"
	type sphere
	c -4.21095859413 1.56636507912 0.5
	r 0.0476170337677
}

shader {
	name "Sphere2304"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2304"
	type sphere
	c -4.13934815295 2.0499087407 0.5
	r 0.0572832321842
}

shader {
	name "Sphere2305"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2305"
	type sphere
	c -4.09260958844 2.19679666852 0.5
	r 0.0534448606278
}

shader {
	name "Sphere2306"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2306"
	type sphere
	c -3.86100724795 2.40348242971 0.5
	r 0.0531363654088
}

shader {
	name "Sphere2307"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2307"
	type sphere
	c -3.55907185994 2.94140879535 0.5
	r 0.0588024680571
}

shader {
	name "Sphere2308"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2308"
	type sphere
	c -3.3937321485 3.19459193566 0.5
	r 0.0590876311788
}

shader {
	name "Sphere2309"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2309"
	type sphere
	c -2.36046335735 3.31743260338 0.5
	r 0.0528055283894
}

shader {
	name "Sphere2310"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2310"
	type sphere
	c -2.15616289608 3.24252619092 0.5
	r 0.0433616274462
}

shader {
	name "Sphere2311"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2311"
	type sphere
	c -1.90293649328 3.46174573532 0.5
	r 0.0588443234317
}

shader {
	name "Sphere2312"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2312"
	type sphere
	c -1.75478887002 3.3846437096 0.5
	r 0.0575629010464
}

shader {
	name "Sphere2313"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2313"
	type sphere
	c -1.3561334016 2.88548767451 0.5
	r 0.0341513191253
}

shader {
	name "Sphere2314"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2314"
	type sphere
	c -1.22748102116 2.98668594093 0.5
	r 0.0304217806255
}

shader {
	name "Sphere2315"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2315"
	type sphere
	c -0.997877413799 2.98971137083 0.5
	r 0.0313110727673
}

shader {
	name "Sphere2316"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2316"
	type sphere
	c -0.832553688357 3.06406268422 0.5
	r 0.0275621748524
}

shader {
	name "Sphere2317"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2317"
	type sphere
	c -0.697816498312 3.1404593159 0.5
	r 0.0291208857738
}

shader {
	name "Sphere2318"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2318"
	type sphere
	c -0.554023670039 3.20815402967 0.5
	r 0.0302426750739
}

shader {
	name "Sphere2319"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2319"
	type sphere
	c -0.262802363918 3.15018125302 0.5
	r 0.0262213680923
}

shader {
	name "Sphere2320"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2320"
	type sphere
	c -0.11506100053 3.07491358205 0.5
	r 0.0278478468873
}

shader {
	name "Sphere2321"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2321"
	type sphere
	c 0.0107009771174 3.00246749826 0.5
	r 0.0265098226901
}

shader {
	name "Sphere2322"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2322"
	type sphere
	c 0.0708825228881 3.19187763169 0.5
	r 0.0257475175474
}

shader {
	name "Sphere2323"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2323"
	type sphere
	c 0.242722856386 3.15250980228 0.5
	r 0.0333683874584
}

shader {
	name "Sphere2324"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2324"
	type sphere
	c 0.531008357861 3.15914928678 0.5
	r 0.0359924568702
}

shader {
	name "Sphere2325"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2325"
	type sphere
	c 0.81419956098 3.09364112921 0.5
	r 0.0381577620697
}

shader {
	name "Sphere2326"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2326"
	type sphere
	c 1.13303481708 3.21673736991 0.5
	r 0.0431089613733
}

shader {
	name "Sphere2327"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2327"
	type sphere
	c 1.94199001181 3.65125619009 0.5
	r 0.0591758424475
}

shader {
	name "Sphere2328"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2328"
	type sphere
	c 2.40667684495 3.28494548064 0.5
	r 0.0559491829352
}

shader {
	name "Sphere2329"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2329"
	type sphere
	c 3.19034436706 2.73500149366 0.5
	r 0.0499729752955
}

shader {
	name "Sphere2330"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2330"
	type sphere
	c 3.41731396734 2.58184086676 0.5
	r 0.0541597512529
}

shader {
	name "Sphere2331"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2331"
	type sphere
	c 3.69590311009 2.37015100645 0.5
	r 0.0575852273594
}

shader {
	name "Sphere2332"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2332"
	type sphere
	c 3.62328051374 1.93147128865 0.5
	r 0.0451734778668
}

shader {
	name "Sphere2333"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2333"
	type sphere
	c 3.94239263457 1.6744891262 0.5
	r 0.0490384301467
}

shader {
	name "Sphere2334"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2334"
	type sphere
	c 4.95931150773 1.43614454674 0.5
	r 0.06590484803
}

shader {
	name "Sphere2335"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2335"
	type sphere
	c 5.26311666102 1.00315160903 0.5
	r 0.0855680858437
}

shader {
	name "Sphere2336"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2336"
	type sphere
	c 5.8207942633 0.844985824676 0.5
	r 0.0779373644482
}

shader {
	name "Sphere2337"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2337"
	type sphere
	c 5.97599065677 0.461081453824 0.5
	r 0.0807777537012
}

shader {
	name "Sphere2338"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2338"
	type sphere
	c 6.04073335023 0.125160523035 0.5
	r 0.084291336138
}

shader {
	name "Sphere2339"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2339"
	type sphere
	c 6.32338777312 -0.190970389267 0.5
	r 0.0783810059894
}

shader {
	name "Sphere2340"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2340"
	type sphere
	c 6.43996289079 -1.01608081081 0.5
	r 0.0788694853771
}

shader {
	name "Sphere2341"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2341"
	type sphere
	c 6.35880694225 -1.20609817082 0.5
	r 0.0719934526483
}

shader {
	name "Sphere2342"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2342"
	type sphere
	c 6.25262300212 -1.83153588617 0.5
	r 0.100181386227
}

shader {
	name "Sphere2343"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2343"
	type sphere
	c 6.10248220854 -2.06148365947 0.5
	r 0.0870414082396
}

shader {
	name "Sphere2344"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2344"
	type sphere
	c 4.5476125076 -3.13028029107 0.5
	r 0.055652123256
}

shader {
	name "Sphere2345"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2345"
	type sphere
	c 3.75719580411 -4.08591848513 0.5
	r 0.0572347827369
}

shader {
	name "Sphere2346"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2346"
	type sphere
	c 3.07889251004 -4.42399501213 0.5
	r 0.0728570895517
}

shader {
	name "Sphere2347"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2347"
	type sphere
	c 2.7052729877 -4.53726615092 0.5
	r 0.0737754775755
}

shader {
	name "Sphere2348"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2348"
	type sphere
	c 2.36720758278 -4.47984288214 0.5
	r 0.0561756887857
}

shader {
	name "Sphere2349"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2349"
	type sphere
	c 2.65129331596 -4.78117321595 0.5
	r 0.0544313767822
}

shader {
	name "Sphere2350"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2350"
	type sphere
	c 2.30064906297 -5.28734970346 0.5
	r 0.0610365757042
}

shader {
	name "Sphere2351"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2351"
	type sphere
	c 2.05308816941 -5.52010079453 0.5
	r 0.0637280384578
}

shader {
	name "Sphere2352"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2352"
	type sphere
	c 1.74573394386 -5.61460618477 0.5
	r 0.0871354327153
}

shader {
	name "Sphere2353"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2353"
	type sphere
	c 1.23241995095 -6.01756240527 0.5
	r 0.0815751759636
}

shader {
	name "Sphere2354"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2354"
	type sphere
	c 1.01993921883 -5.92941429457 0.5
	r 0.0758480866362
}

shader {
	name "Sphere2355"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2355"
	type sphere
	c 0.909547837075 -6.36088885951 0.5
	r 0.0991470349692
}

shader {
	name "Sphere2356"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2356"
	type sphere
	c 0.405782425531 -6.38657461977 0.5
	r 0.0945856420153
}

shader {
	name "Sphere2357"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2357"
	type sphere
	c -0.0104388101372 -6.34328975983 0.5
	r 0.0817419528967
}

shader {
	name "Sphere2358"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2358"
	type sphere
	c -0.450813161454 -6.31754424714 0.5
	r 0.0819122113206
}

shader {
	name "Sphere2359"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2359"
	type sphere
	c -0.821082376523 -5.77523389393 0.5
	r 0.0779364741979
}

shader {
	name "Sphere2360"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2360"
	type sphere
	c -2.01293003618 -4.91731898723 0.5
	r 0.0752491480094
}

shader {
	name "Sphere2361"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2361"
	type sphere
	c -2.15105090971 -4.25670552474 0.5
	r 0.0709558376189
}

shader {
	name "Sphere2362"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2362"
	type sphere
	c -2.10632450614 -3.89253834455 0.5
	r 0.066194333995
}

shader {
	name "Sphere2363"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2363"
	type sphere
	c -1.93234176197 -3.60579508871 0.5
	r 0.0689993939183
}

shader {
	name "Sphere2364"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2364"
	type sphere
	c -2.25201397149 -3.43729266552 0.5
	r 0.0592266409654
}

shader {
	name "Sphere2365"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2365"
	type sphere
	c -2.54180306089 -3.23665530711 0.5
	r 0.0579869508771
}

shader {
	name "Sphere2366"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2366"
	type sphere
	c -2.68772304884 -2.98273585229 0.5
	r 0.0531164949781
}

shader {
	name "Sphere2367"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2367"
	type sphere
	c -2.6630930474 -2.82403136305 0.5
	r 0.0507958497835
}

shader {
	name "Sphere2368"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2368"
	type sphere
	c -2.06021905518 -2.38780718937 0.5
	r 0.0332410312812
}

shader {
	name "Sphere2369"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2369"
	type sphere
	c -2.15794600007 -2.54679993432 0.5
	r 0.0368032730281
}

shader {
	name "Sphere2370"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2370"
	type sphere
	c -2.90047881193 -2.46961652193 0.5
	r 0.0328378597136
}

shader {
	name "Sphere2371"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2371"
	type sphere
	c -3.10595925372 -2.2892991974 0.5
	r 0.031073399917
}

shader {
	name "Sphere2372"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2372"
	type sphere
	c -3.24881785264 -2.33637324118 0.5
	r 0.0445732902711
}

shader {
	name "Sphere2373"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2373"
	type sphere
	c -3.4122603068 -2.17059928229 0.5
	r 0.0452142390341
}

shader {
	name "Sphere2374"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2374"
	type sphere
	c -3.71502872175 -2.10798399261 0.5
	r 0.046008208022
}

shader {
	name "Sphere2375"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2375"
	type sphere
	c -3.74825845165 -1.99480240008 0.5
	r 0.0403011444337
}

shader {
	name "Sphere2376"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2376"
	type sphere
	c -4.07021697757 -1.27204687957 0.5
	r 0.0385347921757
}

shader {
	name "Sphere2377"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2377"
	type sphere
	c -4.12341390079 -1.08550667483 0.5
	r 0.0403196579226
}

shader {
	name "Sphere2378"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2378"
	type sphere
	c -4.13425898754 -0.833191097417 0.5
	r 0.0542570267641
}

shader {
	name "Sphere2379"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2379"
	type sphere
	c -3.71245790976 -0.262387841579 0.5
	r 0.0311670404325
}

shader {
	name "Sphere2380"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2380"
	type sphere
	c -4.21880702793 0.117394794103 0.5
	r 0.0583559042267
}

shader {
	name "Sphere2381"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2381"
	type sphere
	c -4.3910021241 0.379639682655 0.5
	r 0.0484713608814
}

shader {
	name "Sphere2382"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2382"
	type sphere
	c -4.30962644957 0.631262651964 0.5
	r 0.0519644399291
}

shader {
	name "Sphere2383"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2383"
	type sphere
	c -4.25593129573 1.44547834597 0.5
	r 0.0491188551448
}

shader {
	name "Sphere2384"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2384"
	type sphere
	c -4.1696244478 1.68603091048 0.5
	r 0.0473355220271
}

shader {
	name "Sphere2385"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2385"
	type sphere
	c -4.17239327949 1.90281490755 0.5
	r 0.0557867641794
}

shader {
	name "Sphere2386"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2386"
	type sphere
	c -4.05347852411 2.33338687733 0.5
	r 0.0531188316083
}

shader {
	name "Sphere2387"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2387"
	type sphere
	c -3.82019276104 2.5361762061 0.5
	r 0.0509853019174
}

shader {
	name "Sphere2388"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2388"
	type sphere
	c -3.64949813432 2.81379994083 0.5
	r 0.058497462051
}

shader {
	name "Sphere2389"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2389"
	type sphere
	c -3.46740112961 3.06510978102 0.5
	r 0.0526415962885
}

shader {
	name "Sphere2390"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2390"
	type sphere
	c -3.30135989759 3.32006475591 0.5
	r 0.0577681967253
}

shader {
	name "Sphere2391"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2391"
	type sphere
	c -2.46147873975 3.42457346635 0.5
	r 0.0576337784627
}

shader {
	name "Sphere2392"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2392"
	type sphere
	c -2.04737341888 3.52869008725 0.5
	r 0.0605531602059
}

shader {
	name "Sphere2393"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2393"
	type sphere
	c -1.61542254665 3.30839068764 0.5
	r 0.0615844497007
}

shader {
	name "Sphere2394"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2394"
	type sphere
	c -1.42683427504 2.82394989835 0.5
	r 0.036146975038
}

shader {
	name "Sphere2395"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2395"
	type sphere
	c -1.16665560434 3.0433042897 0.5
	r 0.0319021306867
}

shader {
	name "Sphere2396"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2396"
	type sphere
	c -0.972621138293 3.07002173575 0.5
	r 0.0318299932544
}

shader {
	name "Sphere2397"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2397"
	type sphere
	c -0.837075386963 3.1408141812 0.5
	r 0.0301012572447
}

shader {
	name "Sphere2398"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2398"
	type sphere
	c -0.763968323045 3.18179491937 0.5
	r 0.0293824604255
}

shader {
	name "Sphere2399"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2399"
	type sphere
	c -0.632435640225 3.22008540719 0.5
	r 0.0292432232245
}

shader {
	name "Sphere2400"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2400"
	type sphere
	c -0.474954084811 3.19034186018 0.5
	r 0.0305456123515
}

shader {
	name "Sphere2401"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2401"
	type sphere
	c -0.324479911642 3.18570367908 0.5
	r 0.0271603140521
}

shader {
	name "Sphere2402"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2402"
	type sphere
	c -0.197171574393 3.12617334487 0.5
	r 0.0261916680297
}

shader {
	name "Sphere2403"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2403"
	type sphere
	c -0.0496511062433 3.10849897787 0.5
	r 0.0272984912429
}

shader {
	name "Sphere2404"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2404"
	type sphere
	c 0.00650216258862 3.16041172178 0.5
	r 0.0279963242571
}

shader {
	name "Sphere2405"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2405"
	type sphere
	c 0.127532610613 3.2297638574 0.5
	r 0.0253659511045
}

shader {
	name "Sphere2406"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2406"
	type sphere
	c 0.322081791229 3.19775630645 0.5
	r 0.0351451970102
}

shader {
	name "Sphere2407"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2407"
	type sphere
	c 0.45499389589 3.09368144082 0.5
	r 0.0392480473241
}

shader {
	name "Sphere2408"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2408"
	type sphere
	c 0.600371495511 3.21687491383 0.5
	r 0.0316885208615
}

shader {
	name "Sphere2409"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2409"
	type sphere
	c 0.783635392129 3.19019962335 0.5
	r 0.0378025075055
}

shader {
	name "Sphere2410"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2410"
	type sphere
	c 1.04222849497 3.28436397356 0.5
	r 0.0418072881421
}

shader {
	name "Sphere2411"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2411"
	type sphere
	c 1.23834464165 3.15810111006 0.5
	r 0.0472913051784
}

shader {
	name "Sphere2412"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2412"
	type sphere
	c 1.80128884189 3.59490919526 0.5
	r 0.0544975458763
}

shader {
	name "Sphere2413"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2413"
	type sphere
	c 2.0955290071 3.69863587724 0.5
	r 0.0613364806889
}

shader {
	name "Sphere2414"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2414"
	type sphere
	c 2.52950988181 3.36992510579 0.5
	r 0.0560735337074
}

shader {
	name "Sphere2415"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2415"
	type sphere
	c 3.31062214456 2.78673771298 0.5
	r 0.0482265732514
}

shader {
	name "Sphere2416"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2416"
	type sphere
	c 3.73100412343 2.51626537369 0.5
	r 0.0551183121394
}

shader {
	name "Sphere2417"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2417"
	type sphere
	c 3.59540140959 2.04688855212 0.5
	r 0.0438790004842
}

shader {
	name "Sphere2418"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2418"
	type sphere
	c 3.95743213211 1.80286152634 0.5
	r 0.0478993515826
}

shader {
	name "Sphere2419"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2419"
	type sphere
	c 3.9232510979 1.54982014566 0.5
	r 0.0455589991988
}

shader {
	name "Sphere2420"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2420"
	type sphere
	c 4.88263675139 1.59210766978 0.5
	r 0.0644388385451
}

shader {
	name "Sphere2421"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2421"
	type sphere
	c 5.03809616051 1.28028529122 0.5
	r 0.0650751507728
}

shader {
	name "Sphere2422"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2422"
	type sphere
	c 5.49584993749 1.0231504183 0.5
	r 0.0896251241317
}

shader {
	name "Sphere2423"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2423"
	type sphere
	c 6.02156264157 0.81122362834 0.5
	r 0.0747531821936
}

shader {
	name "Sphere2424"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2424"
	type sphere
	c 6.25834137818 0.146391074364 0.5
	r 0.0796895909603
}

shader {
	name "Sphere2425"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2425"
	type sphere
	c 6.28935116002 -0.400263392463 0.5
	r 0.0806509227952
}

shader {
	name "Sphere2426"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2426"
	type sphere
	c 6.51874559321 -0.818880635623 0.5
	r 0.0803967244845
}

shader {
	name "Sphere2427"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2427"
	type sphere
	c 6.29908592421 -1.39083632177 0.5
	r 0.0736201326779
}

shader {
	name "Sphere2428"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2428"
	type sphere
	c 5.99039777347 -2.25481725513 0.5
	r 0.0805643789102
}

shader {
	name "Sphere2429"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2429"
	type sphere
	c 3.9059406803 -4.09194725721 0.5
	r 0.0544154687696
}

shader {
	name "Sphere2430"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2430"
	type sphere
	c 3.60731441802 -4.08323810937 0.5
	r 0.0551942306433
}

shader {
	name "Sphere2431"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2431"
	type sphere
	c 3.02282644012 -4.60520399896 0.5
	r 0.0694060710752
}

shader {
	name "Sphere2432"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2432"
	type sphere
	c 2.67027994965 -4.92917706679 0.5
	r 0.0574811697358
}

shader {
	name "Sphere2433"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2433"
	type sphere
	c 2.28492697327 -5.12740568805 0.5
	r 0.0594995831694
}

shader {
	name "Sphere2434"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2434"
	type sphere
	c 2.33216261076 -5.44161194554 0.5
	r 0.0570495917883
}

shader {
	name "Sphere2435"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2435"
	type sphere
	c 2.21213785819 -5.56086888235 0.5
	r 0.0594155678431
}

shader {
	name "Sphere2436"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2436"
	type sphere
	c 1.89344709678 -5.48042830257 0.5
	r 0.0596445193188
}

shader {
	name "Sphere2437"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2437"
	type sphere
	c 1.76595648568 -5.84123626059 0.5
	r 0.0835124654142
}

shader {
	name "Sphere2438"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2438"
	type sphere
	c 1.43229545823 -6.07117730013 0.5
	r 0.073630932618
}

shader {
	name "Sphere2439"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2439"
	type sphere
	c 0.772571334071 -6.57679824527 0.5
	r 0.0926234703084
}

shader {
	name "Sphere2440"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2440"
	type sphere
	c -0.131537889747 -6.53595284235 0.5
	r 0.0889288658673
}

shader {
	name "Sphere2441"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2441"
	type sphere
	c -0.557121051242 -6.1258914728 0.5
	r 0.0824595814392
}

shader {
	name "Sphere2442"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2442"
	type sphere
	c -0.666288158368 -5.90368887784 0.5
	r 0.07292716369
}

shader {
	name "Sphere2443"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2443"
	type sphere
	c -1.85386478536 -5.04844760163 0.5
	r 0.0793608872019
}

shader {
	name "Sphere2444"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2444"
	type sphere
	c -2.19133040485 -4.80715192595 0.5
	r 0.0820068646699
}

shader {
	name "Sphere2445"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2445"
	type sphere
	c -2.29148977991 -4.13711158218 0.5
	r 0.0673897636484
}

shader {
	name "Sphere2446"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2446"
	type sphere
	c -2.09655139618 -3.68898917986 0.5
	r 0.0690618576398
}

shader {
	name "Sphere2447"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2447"
	type sphere
	c -2.10430417805 -3.49257501133 0.5
	r 0.059060321419
}

shader {
	name "Sphere2448"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2448"
	type sphere
	c -2.40667359437 -3.3825020881 0.5
	r 0.0638318961502
}

shader {
	name "Sphere2449"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2449"
	type sphere
	c -2.69298177633 -3.22313388946 0.5
	r 0.0558496904756
}

shader {
	name "Sphere2450"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2450"
	type sphere
	c -2.79346848678 -2.78492081398 0.5
	r 0.0512906674965
}

shader {
	name "Sphere2451"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2451"
	type sphere
	c -2.0179249331 -2.46298740146 0.5
	r 0.031454270651
}

shader {
	name "Sphere2452"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2452"
	type sphere
	c -2.25460656994 -2.53590284467 0.5
	r 0.036151383686
}

shader {
	name "Sphere2453"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2453"
	type sphere
	c -2.81603523512 -2.4418272592 0.5
	r 0.0338360890452
}

shader {
	name "Sphere2454"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2454"
	type sphere
	c -2.98165538433 -2.50251124373 0.5
	r 0.0328533153362
}

shader {
	name "Sphere2455"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2455"
	type sphere
	c -3.13460227027 -2.37083289191 0.5
	r 0.0337405123809
}

shader {
	name "Sphere2456"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2456"
	type sphere
	c -3.08855092253 -2.20581959778 0.5
	r 0.0328831487696
}

shader {
	name "Sphere2457"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2457"
	type sphere
	c -3.36413732119 -2.35813514303 0.5
	r 0.0434428452527
}

shader {
	name "Sphere2458"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2458"
	type sphere
	c -3.38522483124 -2.05385695782 0.5
	r 0.0446596953614
}

shader {
	name "Sphere2459"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2459"
	type sphere
	c -3.66994616465 -2.22170201958 0.5
	r 0.0457380587617
}

shader {
	name "Sphere2460"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2460"
	type sphere
	c -3.78667189698 -1.89804381382 0.5
	r 0.0377774822737
}

shader {
	name "Sphere2461"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2461"
	type sphere
	c -4.06326770594 -1.3728814431 0.5
	r 0.0372705152725
}

shader {
	name "Sphere2462"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2462"
	type sphere
	c -4.16974689316 -0.990179943296 0.5
	r 0.0391730254441
}

shader {
	name "Sphere2463"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2463"
	type sphere
	c -4.16589501308 -0.690685445641 0.5
	r 0.0552242188039
}

shader {
	name "Sphere2464"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2464"
	type sphere
	c -3.78878874856 -0.23674964075 0.5
	r 0.0292240954233
}

shader {
	name "Sphere2465"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2465"
	type sphere
	c -4.12004566251 0.00915053506122 0.5
	r 0.0515405362953
}

shader {
	name "Sphere2466"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2466"
	type sphere
	c -4.3118195075 0.239217683033 0.5
	r 0.0565976838575
}

shader {
	name "Sphere2467"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2467"
	type sphere
	c -4.47363100368 0.484175533765 0.5
	r 0.0514653325717
}

shader {
	name "Sphere2468"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2468"
	type sphere
	c -4.1818251241 0.678473395124 0.5
	r 0.0502174743059
}

shader {
	name "Sphere2469"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2469"
	type sphere
	c -4.17238817222 1.34372981759 0.5
	r 0.0496200520217
}

shader {
	name "Sphere2470"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2470"
	type sphere
	c -4.33509559979 1.54583891443 0.5
	r 0.0467498951915
}

shader {
	name "Sphere2471"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2471"
	type sphere
	c -4.28862227908 1.66054503407 0.5
	r 0.0439367778911
}

shader {
	name "Sphere2472"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2472"
	type sphere
	c -4.28216264356 2.00270695447 0.5
	r 0.0555263103391
}

shader {
	name "Sphere2473"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2473"
	type sphere
	c -4.18698940421 2.29817554708 0.5
	r 0.0504381985581
}

shader {
	name "Sphere2474"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2474"
	type sphere
	c -3.95339891889 2.50750057608 0.5
	r 0.0512080045606
}

shader {
	name "Sphere2475"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2475"
	type sphere
	c -3.68616162636 2.5657109334 0.5
	r 0.0519496917098
}

shader {
	name "Sphere2476"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2476"
	type sphere
	c -3.72066151269 2.95955361873 0.5
	r 0.0631514306161
}

shader {
	name "Sphere2477"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2477"
	type sphere
	c -3.54261399183 3.18397804345 0.5
	r 0.05285714366
}

shader {
	name "Sphere2478"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2478"
	type sphere
	c -3.45064374627 3.3353445673 0.5
	r 0.0547796433887
}

shader {
	name "Sphere2479"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2479"
	type sphere
	c -3.1559017924 3.29698037467 0.5
	r 0.0526906590723
}

shader {
	name "Sphere2480"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2480"
	type sphere
	c -2.61300083711 3.39139090284 0.5
	r 0.0587009370662
}

shader {
	name "Sphere2481"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2481"
	type sphere
	c -2.31655667983 3.45135767341 0.5
	r 0.0528985060682
}

shader {
	name "Sphere2482"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2482"
	type sphere
	c -1.91662804913 3.616178143 0.5
	r 0.0574342873458
}

shader {
	name "Sphere2483"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2483"
	type sphere
	c -1.62490496482 3.46756973764 0.5
	r 0.0580114783071
}

shader {
	name "Sphere2484"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2484"
	type sphere
	c -1.62619329193 3.15054835596 0.5
	r 0.0570725917035
}

shader {
	name "Sphere2485"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2485"
	type sphere
	c -1.40111998777 2.73743629881 0.5
	r 0.0315437034509
}

shader {
	name "Sphere2486"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2486"
	type sphere
	c -1.43944488591 2.91368191498 0.5
	r 0.0318133814344
}

shader {
	name "Sphere2487"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2487"
	type sphere
	c -1.24648322231 3.06523026584 0.5
	r 0.0301858981421
}

shader {
	name "Sphere2488"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2488"
	type sphere
	c -1.09179132113 3.01387284533 0.5
	r 0.0284291616486
}

shader {
	name "Sphere2489"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2489"
	type sphere
	c -0.58382615498 3.2850557843 0.5
	r 0.0316133127943
}

shader {
	name "Sphere2490"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2490"
	type sphere
	c -0.499130244026 3.26929392349 0.5
	r 0.0313823875663
}

shader {
	name "Sphere2491"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2491"
	type sphere
	c -0.388152705469 3.14949990568 0.5
	r 0.027773988152
}

shader {
	name "Sphere2492"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2492"
	type sphere
	c -0.262457736284 3.21961693577 0.5
	r 0.0258560353935
}

shader {
	name "Sphere2493"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2493"
	type sphere
	c -0.111757534605 3.15061222846 0.5
	r 0.0289801730482
}

shader {
	name "Sphere2494"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2494"
	type sphere
	c 0.0149892839671 3.23130259072 0.5
	r 0.0255515041096
}

shader {
	name "Sphere2495"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2495"
	type sphere
	c 0.242577979079 3.24032210622 0.5
	r 0.0324909301286
}

shader {
	name "Sphere2496"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2496"
	type sphere
	c 0.481274645657 2.99792951809 0.5
	r 0.0352217354044
}

shader {
	name "Sphere2497"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2497"
	type sphere
	c 0.441225653885 3.19303848977 0.5
	r 0.0359818042046
}

shader {
	name "Sphere2498"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2498"
	type sphere
	c 0.52052844676 3.25120323084 0.5
	r 0.0334939691413
}

shader {
	name "Sphere2499"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2499"
	type sphere
	c 0.884419307669 3.16949061326 0.5
	r 0.0393646594821
}

shader {
	name "Sphere2500"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2500"
	type sphere
	c 1.14223944045 3.32668513129 0.5
	r 0.0396403278695
}

shader {
	name "Sphere2501"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2501"
	type sphere
	c 1.8212904699 3.73301328805 0.5
	r 0.0501612002107
}

shader {
	name "Sphere2502"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2502"
	type sphere
	c 1.97744672483 3.79947074391 0.5
	r 0.0551216291363
}

shader {
	name "Sphere2503"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2503"
	type sphere
	c 2.20758648872 3.58178757378 0.5
	r 0.0600857286947
}

shader {
	name "Sphere2504"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2504"
	type sphere
	c 2.39191660909 3.43724559748 0.5
	r 0.0588110865872
}

shader {
	name "Sphere2505"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2505"
	type sphere
	c 2.66151709619 3.30585740236 0.5
	r 0.0539762213573
}

shader {
	name "Sphere2506"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2506"
	type sphere
	c 3.20556340434 2.87142638078 0.5
	r 0.0529803880206
}

shader {
	name "Sphere2507"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2507"
	type sphere
	c 3.6318784497 2.63268846441 0.5
	r 0.059561164344
}

shader {
	name "Sphere2508"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2508"
	type sphere
	c 3.84560292686 2.41494252477 0.5
	r 0.0596076791236
}

shader {
	name "Sphere2509"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2509"
	type sphere
	c 3.70321428931 2.01355553112 0.5
	r 0.0407571198727
}

shader {
	name "Sphere2510"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2510"
	type sphere
	c 3.85492342219 1.88782422816 0.5
	r 0.051956878445
}

shader {
	name "Sphere2511"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2511"
	type sphere
	c 4.06575196463 1.72667983622 0.5
	r 0.0514206880077
}

shader {
	name "Sphere2512"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2512"
	type sphere
	c 4.71156972005 1.60735372071 0.5
	r 0.0643699687875
}

shader {
	name "Sphere2513"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2513"
	type sphere
	c 5.05099134591 1.58017283569 0.5
	r 0.0621439870696
}

shader {
	name "Sphere2514"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2514"
	type sphere
	c 5.13098723054 1.42386459494 0.5
	r 0.0631809178297
}

shader {
	name "Sphere2515"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2515"
	type sphere
	c 5.35618595189 1.21976826939 0.5
	r 0.0912549249016
}

shader {
	name "Sphere2516"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2516"
	type sphere
	c 5.95403818993 0.998236857517 0.5
	r 0.0743695640407
}

shader {
	name "Sphere2517"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2517"
	type sphere
	c 6.13772434026 0.318475726963 0.5
	r 0.0779203661879
}

shader {
	name "Sphere2518"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2518"
	type sphere
	c 6.49322435882 -0.322872906276 0.5
	r 0.0828999326179
}

shader {
	name "Sphere2519"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2519"
	type sphere
	c 6.65247288583 -0.988865549258 0.5
	r 0.081814699453
}

shader {
	name "Sphere2520"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2520"
	type sphere
	c 6.49242896514 -1.34900716238 0.5
	r 0.074741943524
}

shader {
	name "Sphere2521"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2521"
	type sphere
	c 6.21468804611 -2.26591562959 0.5
	r 0.0878591391271
}

shader {
	name "Sphere2522"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2522"
	type sphere
	c 3.98649258714 -3.97766410229 0.5
	r 0.0504485034601
}

shader {
	name "Sphere2523"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2523"
	type sphere
	c 3.83000444083 -4.22327965062 0.5
	r 0.059363535833
}

shader {
	name "Sphere2524"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2524"
	type sphere
	c 3.67730827716 -4.21149857197 0.5
	r 0.0543927722541
}

shader {
	name "Sphere2525"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2525"
	type sphere
	c 3.20299260749 -4.56640766894 0.5
	r 0.0688159034318
}

shader {
	name "Sphere2526"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2526"
	type sphere
	c 2.78751508182 -4.83483930548 0.5
	r 0.0553774821303
}

shader {
	name "Sphere2527"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2527"
	type sphere
	c 2.43506534581 -5.19128848548 0.5
	r 0.06287353593
}

shader {
	name "Sphere2528"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2528"
	type sphere
	c 2.10387938746 -5.67519659432 0.5
	r 0.0586724554388
}

shader {
	name "Sphere2529"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2529"
	type sphere
	c 1.29868071325 -6.20886875404 0.5
	r 0.0702671495908
}

shader {
	name "Sphere2530"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2530"
	type sphere
	c 1.0235468544 -6.59492881582 0.5
	r 0.0960986906386
}

shader {
	name "Sphere2531"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2531"
	type sphere
	c 0.101962314569 -6.53695458655 0.5
	r 0.0861978989641
}

shader {
	name "Sphere2532"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2532"
	type sphere
	c -0.66535926932 -6.31205915206 0.5
	r 0.0790499480556
}

shader {
	name "Sphere2533"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2533"
	type sphere
	c -0.447211411966 -5.94402462631 0.5
	r 0.0769144103038
}

shader {
	name "Sphere2534"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2534"
	type sphere
	c -0.849058307267 -5.97685075688 0.5
	r 0.0747249381531
}

shader {
	name "Sphere2535"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2535"
	type sphere
	c -1.66387440974 -4.97644228939 0.5
	r 0.0730222586719
}

shader {
	name "Sphere2536"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2536"
	type sphere
	c -2.04508606024 -5.11008180742 0.5
	r 0.0713207228268
}

shader {
	name "Sphere2537"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2537"
	type sphere
	c -2.17004000515 -4.59927706079 0.5
	r 0.0747148564991
}

shader {
	name "Sphere2538"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2538"
	type sphere
	c -2.33225224597 -4.31970176433 0.5
	r 0.0729238982213
}

shader {
	name "Sphere2539"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2539"
	type sphere
	c -1.97449030788 -3.39185883242 0.5
	r 0.0641667317779
}

shader {
	name "Sphere2540"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2540"
	type sphere
	c -2.37123451052 -3.54661605843 0.5
	r 0.0620906781015
}

shader {
	name "Sphere2541"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2541"
	type sphere
	c -2.63197014102 -3.36084025073 0.5
	r 0.057113011941
}

shader {
	name "Sphere2542"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2542"
	type sphere
	c -2.82981708294 -2.65308085531 0.5
	r 0.0512785031656
}

shader {
	name "Sphere2543"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2543"
	type sphere
	c -1.97248346207 -2.39068054632 0.5
	r 0.032595942713
}

shader {
	name "Sphere2544"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2544"
	type sphere
	c -2.05529441531 -2.53443536964 0.5
	r 0.0290186640056
}

shader {
	name "Sphere2545"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2545"
	type sphere
	c -2.83448874 -2.53233926596 0.5
	r 0.0354444082571
}

shader {
	name "Sphere2546"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2546"
	type sphere
	c -3.05379609478 -2.44959875497 0.5
	r 0.0342455492889
}

shader {
	name "Sphere2547"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2547"
	type sphere
	c -3.28937221641 -2.44593756561 0.5
	r 0.043048403131
}

shader {
	name "Sphere2548"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2548"
	type sphere
	c -3.54998307366 -2.23667978552 0.5
	r 0.0449328055131
}

shader {
	name "Sphere2549"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2549"
	type sphere
	c -3.79108558899 -2.20431961986 0.5
	r 0.0460470746827
}

shader {
	name "Sphere2550"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2550"
	type sphere
	c -3.85506345274 -1.9774956872 0.5
	r 0.0408474365395
}

shader {
	name "Sphere2551"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2551"
	type sphere
	c -3.73123415229 -1.81549380128 0.5
	r 0.0368007622779
}

shader {
	name "Sphere2552"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2552"
	type sphere
	c -3.97857931117 -1.42593583726 0.5
	r 0.03768031717
}

shader {
	name "Sphere2553"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2553"
	type sphere
	c -4.14941090995 -1.32978582725 0.5
	r 0.0349708134915
}

shader {
	name "Sphere2554"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2554"
	type sphere
	c -4.22911398164 -1.07626885587 0.5
	r 0.0392575842369
}

shader {
	name "Sphere2555"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2555"
	type sphere
	c -4.26948775614 -0.789738464746 0.5
	r 0.052271889581
}

shader {
	name "Sphere2556"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2556"
	type sphere
	c -4.05443049892 -0.603743898946 0.5
	r 0.0507971629224
}

shader {
	name "Sphere2557"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2557"
	type sphere
	c -3.77532715454 -0.314967213126 0.5
	r 0.0303015441563
}

shader {
	name "Sphere2558"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2558"
	type sphere
	c -3.80438086214 -0.161903743128 0.5
	r 0.0281154642027
}

shader {
	name "Sphere2559"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2559"
	type sphere
	c -4.24955904383 -0.0213922900696 0.5
	r 0.048259019371
}

shader {
	name "Sphere2560"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2560"
	type sphere
	c -4.3680460135 0.102732339176 0.5
	r 0.0541122472623
}

shader {
	name "Sphere2561"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2561"
	type sphere
	c -4.52101589026 0.356678531354 0.5
	r 0.0505479379824
}

shader {
	name "Sphere2562"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2562"
	type sphere
	c -4.28590463841 0.770547271572 0.5
	r 0.0540032338725
}

shader {
	name "Sphere2563"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2563"
	type sphere
	c -4.30134731359 1.32387134703 0.5
	r 0.0482393403975
}

shader {
	name "Sphere2564"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2564"
	type sphere
	c -4.38371505838 1.43008635778 0.5
	r 0.0474117195706
}

shader {
	name "Sphere2565"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2565"
	type sphere
	c -4.25456208857 1.77109413679 0.5
	r 0.0428210770158
}

shader {
	name "Sphere2566"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2566"
	type sphere
	c -4.25129601797 2.14183733342 0.5
	r 0.0513585863613
}

shader {
	name "Sphere2567"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2567"
	type sphere
	c -4.15355504677 2.42830539597 0.5
	r 0.0503290780205
}

shader {
	name "Sphere2568"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2568"
	type sphere
	c -3.91093368048 2.63535882454 0.5
	r 0.0498363092185
}

shader {
	name "Sphere2569"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2569"
	type sphere
	c -3.80968735121 2.81888249432 0.5
	r 0.0617049084592
}

shader {
	name "Sphere2570"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2570"
	type sphere
	c -3.36720726839 3.45142841561 0.5
	r 0.0524391606758
}

shader {
	name "Sphere2571"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2571"
	type sphere
	c -3.20196621935 3.43333734763 0.5
	r 0.0552550447403
}

shader {
	name "Sphere2572"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2572"
	type sphere
	c -2.56537675246 3.54325879815 0.5
	r 0.060669075813
}

shader {
	name "Sphere2573"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2573"
	type sphere
	c -2.40522819438 3.5593603524 0.5
	r 0.0519063558922
}

shader {
	name "Sphere2574"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2574"
	type sphere
	c -2.05291075781 3.6857771597 0.5
	r 0.0573353183605
}

shader {
	name "Sphere2575"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2575"
	type sphere
	c -1.77993016432 3.55232248077 0.5
	r 0.0557234332787
}

shader {
	name "Sphere2576"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2576"
	type sphere
	c -1.49056012872 3.40026910287 0.5
	r 0.0546831294449
}

shader {
	name "Sphere2577"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2577"
	type sphere
	c -1.48540726286 3.21422641268 0.5
	r 0.0588153951565
}

shader {
	name "Sphere2578"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2578"
	type sphere
	c -1.48413620752 2.75362165198 0.5
	r 0.0318907733649
}

shader {
	name "Sphere2579"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2579"
	type sphere
	c -1.3758465099 2.97431051526 0.5
	r 0.034086744434
}

shader {
	name "Sphere2580"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2580"
	type sphere
	c -1.18991789035 3.12348557095 0.5
	r 0.0307135354439
}

shader {
	name "Sphere2581"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2581"
	type sphere
	c -1.10194939488 3.08612173108 0.5
	r 0.0262904598257
}

shader {
	name "Sphere2582"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2582"
	type sphere
	c -1.07760221214 2.94228460731 0.5
	r 0.0263064869989
}

shader {
	name "Sphere2583"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2583"
	type sphere
	c -0.667124991917 3.29271689942 0.5
	r 0.0311244849638
}

shader {
	name "Sphere2584"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2584"
	type sphere
	c -0.421376488943 3.24879716518 0.5
	r 0.0289250911252
}

shader {
	name "Sphere2585"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2585"
	type sphere
	c -0.319898144299 3.25448581257 0.5
	r 0.024540610937
}

shader {
	name "Sphere2586"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2586"
	type sphere
	c -0.0506852821838 3.20651452727 0.5
	r 0.0270961279375
}

shader {
	name "Sphere2587"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2587"
	type sphere
	c 0.315641538205 3.288690559 0.5
	r 0.0332263231574
}

shader {
	name "Sphere2588"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2588"
	type sphere
	c 0.591187219363 3.29960809232 0.5
	r 0.0307425249835
}

shader {
	name "Sphere2589"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2589"
	type sphere
	c 0.850353409305 3.26985387976 0.5
	r 0.040125684371
}

shader {
	name "Sphere2590"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2590"
	type sphere
	c 1.05860695501 3.39234777297 0.5
	r 0.0401068414307
}

shader {
	name "Sphere2591"
	type diffuse
	diff { "sRGB nonlinear" 1 1 1 }
}

object {
	shader "Sphere2591"
	type sphere
	c 1.69258135826 3.68699729685 0.5
	r 0.0523545186394
}
				
}