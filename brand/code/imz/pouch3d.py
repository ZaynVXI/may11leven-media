import sys,math,bpy,bmesh
from mathutils import Vector,noise
OUT=sys.argv[1];W,H,SAMP=int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]);SHOT=sys.argv[5] if len(sys.argv)>5 else 'trio'
bpy.ops.wm.read_factory_settings(use_empty=True);sc=bpy.context.scene
def lin(h):
    c=[int(h[i:i+2],16)/255 for i in (0,2,4)];return tuple((x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4) for x in c)+(1,)
def bag_mat(name,tex):
    m=bpy.data.materials.new(name);m.use_nodes=True;nt=m.node_tree;p=nt.nodes["Principled BSDF"]
    tc=nt.nodes.new("ShaderNodeTexCoord");mp=nt.nodes.new("ShaderNodeMapping")
    sp=nt.nodes.new("ShaderNodeSeparateXYZ");cb=nt.nodes.new("ShaderNodeCombineXYZ")
    nt.links.new(tc.outputs["Generated"],sp.inputs[0]);nt.links.new(sp.outputs["X"],cb.inputs["X"]);nt.links.new(sp.outputs["Z"],cb.inputs["Y"])
    im=nt.nodes.new("ShaderNodeTexImage");im.image=bpy.data.images.load(tex);im.extension='EXTEND'
    nt.links.new(cb.outputs[0],im.inputs["Vector"]);nt.links.new(im.outputs["Color"],p.inputs["Base Color"])
    p.inputs["Roughness"].default_value=.62;p.inputs["Specular IOR Level"].default_value=.25
    nz=nt.nodes.new("ShaderNodeTexNoise");nz.inputs["Scale"].default_value=60;nz.inputs["Detail"].default_value=6
    b=nt.nodes.new("ShaderNodeBump");b.inputs["Strength"].default_value=.12;b.inputs["Distance"].default_value=.002
    nt.links.new(nz.outputs["Fac"],b.inputs["Height"]);nt.links.new(b.outputs["Normal"],p.inputs["Normal"])
    return m
def pouch(name,tex,loc,rz,seed):
    Wb,D,Hb=.13,.075,.21
    bpy.ops.mesh.primitive_cube_add(size=1);o=bpy.context.object;o.name=name
    o.scale=(Wb,D,Hb);bpy.ops.object.transform_apply(scale=True)
    md=o.modifiers.new("s","SUBSURF");md.levels=4;md.subdivision_type='SIMPLE';bpy.ops.object.modifier_apply(modifier="s")
    for v in o.data.vertices:
        x,y,z=v.co;t=(z+Hb/2)/Hb
        depth=1-max(0,(t-.55)/.45)**1.6*0.97          # flattens to the seal
        bulge=1+.06*math.sin(math.pi*min(1,t/.85))
        y*=depth*bulge;x*=1+.02*math.sin(math.pi*t)
        if t>.92: y=max(-.0015,min(.0015,y))
        n=noise.noise(Vector((x*40+seed,y*40,z*40)))*.0018*(t>.3)
        v.co=(x+n*.3,y+n,z)
    o.data.update()
    md=o.modifiers.new("bv","BEVEL");md.width=.008;md.segments=5;md.limit_method="ANGLE"
    for p in o.data.polygons: p.use_smooth=True
    o.data.materials.append(bag_mat(name+"_m",tex));o.location=loc;o.rotation_euler=(0,0,rz)
    return o
if SHOT=='trio':
    pouch("A","/home/claude/imz/tex/nyam.png",(-.15,.06,.105),math.radians(14),1)
    pouch("B","/home/claude/imz/tex/huye.png",(0,-.02,.105),math.radians(-6),2)
    pouch("C","/home/claude/imz/tex/gak.png",(.155,.07,.105),math.radians(-18),3)
else:
    pouch("B","/home/claude/imz/tex/"+SHOT+".png",(0,0,.105),math.radians(-8),2)
# cyclorama
me=bpy.data.meshes.new("cyc");bm=bmesh.new();prof=[(-4+i*(4.6/29),0) for i in range(30)];R=.9
for i in range(1,25):
    a=i/24*math.pi/2;prof.append((.6+math.sin(a)*R,R-math.cos(a)*R))
for i in range(1,10): prof.append((.6+R,R+i*.4))
rows=[[bm.verts.new((x,y,z)) for y,z in prof] for x in (-5,5)]
for i in range(len(prof)-1): bm.faces.new((rows[0][i],rows[0][i+1],rows[1][i+1],rows[1][i]))
bm.to_mesh(me);cyc=bpy.data.objects.new("cyc",me);sc.collection.objects.link(cyc)
for p in me.polygons: p.use_smooth=True
cm=bpy.data.materials.new("set");cm.use_nodes=True;cp=cm.node_tree.nodes["Principled BSDF"];cp.inputs["Base Color"].default_value=lin("E6E0D6");cp.inputs["Roughness"].default_value=.9
cyc.data.materials.append(cm)
def area(name,loc,size,power,col=(1,1,1),target=(0,0,.11)):
    l=bpy.data.lights.new(name,"AREA");l.size=size;l.energy=power;l.color=col
    o=bpy.data.objects.new(name,l);sc.collection.objects.link(o);o.location=loc
    o.rotation_euler=(Vector(target)-Vector(loc)).to_track_quat("-Z","Y").to_euler()
area("key",(-1.0,-.8,.9),1.4,48,(1,.96,.9));area("fill",(1.1,-1.0,.4),1.6,12,(.94,.96,1));area("rim",(.4,.9,.7),.6,22)
w=bpy.data.worlds.new("w");sc.world=w;w.use_nodes=True;w.node_tree.nodes["Background"].inputs["Strength"].default_value=0
cam=bpy.data.cameras.new("cam");cam.lens=70;co=bpy.data.objects.new("cam",cam);sc.collection.objects.link(co);sc.camera=co
tgt=Vector((0,0,.11));az,el,dist=math.radians(-12),math.radians(12),(1.25 if SHOT=='trio' else .8)
co.location=tgt+Vector((math.sin(az)*math.cos(el)*dist,-math.cos(az)*math.cos(el)*dist,math.sin(el)*dist))
co.rotation_euler=(tgt-co.location).to_track_quat("-Z","Y").to_euler()
cam.dof.use_dof=True;cam.dof.focus_distance=(tgt-co.location).length;cam.dof.aperture_fstop=5.6
sc.render.engine="CYCLES";sc.cycles.device="CPU";sc.cycles.samples=SAMP;sc.cycles.use_denoising=True
sc.render.resolution_x,sc.render.resolution_y=W,H
sc.view_settings.view_transform="AgX";sc.view_settings.look="AgX - Medium High Contrast"
sc.render.filepath=OUT;bpy.ops.render.render(write_still=True);print("done")
