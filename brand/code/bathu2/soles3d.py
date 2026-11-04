import sys,math,bpy,bmesh
sys.path.insert(0,'/home/claude/bathu2')
from sole import outline
from mathutils import Vector
OUT=sys.argv[1];W,H,SAMP=int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
AZ=float(sys.argv[5]) if len(sys.argv)>5 else 0
bpy.ops.wm.read_factory_settings(use_empty=True);sc=bpy.context.scene
def srgb(h):
    c=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    return tuple((x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4) for x in c)+(1,)
def rubber(name,hexc,rough,tex,sss=0):
    m=bpy.data.materials.new(name);m.use_nodes=True;nt=m.node_tree;p=nt.nodes["Principled BSDF"]
    p.inputs["Base Color"].default_value=srgb(hexc);p.inputs["Roughness"].default_value=rough
    if sss:
        p.inputs["Subsurface Weight"].default_value=sss;p.inputs["Subsurface Radius"].default_value=(.004,.002,.001)
    tc=nt.nodes.new("ShaderNodeTexCoord");im=nt.nodes.new("ShaderNodeTexImage");im.image=bpy.data.images.load(tex);im.extension='EXTEND'
    im.image.colorspace_settings.name='Non-Color'
    nt.links.new(tc.outputs["Generated"],im.inputs["Vector"])
    nz=nt.nodes.new("ShaderNodeTexNoise");nz.inputs["Scale"].default_value=1800
    mx=nt.nodes.new("ShaderNodeMath");mx.operation='MULTIPLY_ADD';mx.inputs[1].default_value=1.0
    nt.links.new(im.outputs["Color"],mx.inputs[0]);nt.links.new(nz.outputs["Fac"],mx.inputs[2])
    mx.inputs[1].default_value=1.0
    b=nt.nodes.new("ShaderNodeBump");b.inputs["Strength"].default_value=.9;b.inputs["Distance"].default_value=.0018
    nt.links.new(im.outputs["Color"],b.inputs["Height"]);nt.links.new(b.outputs["Normal"],p.inputs["Normal"])
    g=nt.nodes.new("ShaderNodeNewGeometry");sp=nt.nodes.new("ShaderNodeSeparateXYZ");gt=nt.nodes.new("ShaderNodeMath");gt.operation='GREATER_THAN';gt.inputs[1].default_value=.8
    mu=nt.nodes.new("ShaderNodeMath");mu.operation='MULTIPLY';mu.inputs[1].default_value=.9
    nt.links.new(g.outputs["Normal"],sp.inputs[0]);nt.links.new(sp.outputs["Z"],gt.inputs[0]);nt.links.new(gt.outputs[0],mu.inputs[0]);nt.links.new(mu.outputs[0],b.inputs["Strength"])
    return m
def sole(name,mirror,mat,loc,rz,th=.026):
    me=bpy.data.meshes.new(name);bm=bmesh.new()
    vs=[bm.verts.new((x,y,0)) for x,y in outline(mirror=mirror)]
    f=bm.faces.new(vs);r=bmesh.ops.extrude_face_region(bm,geom=[f])
    for v in [e for e in r['geom'] if isinstance(e,bmesh.types.BMVert)]: v.co.z+=th
    bmesh.ops.recalc_face_normals(bm,faces=bm.faces);bm.to_mesh(me)
    o=bpy.data.objects.new(name,me);sc.collection.objects.link(o)
    md=o.modifiers.new("bv","BEVEL");md.width=.0035;md.segments=4;md.limit_method='ANGLE';md.harden_normals=True
    o.data.materials.append(mat);o.location=loc;o.rotation_euler=(0,0,rz)
    for p in me.polygons: p.use_smooth=True
    return o
black=rubber("black","1B1A19",.62,'/home/claude/bathu2/tread_l.png')
gum=rubber("gum","A8723F",.38,'/home/claude/bathu2/tread_r.png',sss=.35)
sole("L",-1,black,(-.058,-.075,0),math.radians(92))
sole("R",1,gum,(.058,.085,0),math.radians(86))
# concrete floor
fl=bpy.data.materials.new("conc");fl.use_nodes=True;nt=fl.node_tree;p=nt.nodes["Principled BSDF"]
n1=nt.nodes.new("ShaderNodeTexNoise");n1.inputs["Scale"].default_value=6;n1.inputs["Detail"].default_value=10
ramp=nt.nodes.new("ShaderNodeValToRGB");ramp.color_ramp.elements[0].color=srgb("BDBAB4");ramp.color_ramp.elements[1].color=srgb("D3D1CC")
nt.links.new(n1.outputs["Fac"],ramp.inputs["Fac"]);nt.links.new(ramp.outputs["Color"],p.inputs["Base Color"])
p.inputs["Roughness"].default_value=.85
vo=nt.nodes.new("ShaderNodeTexVoronoi");vo.inputs["Scale"].default_value=900
n2=nt.nodes.new("ShaderNodeTexNoise");n2.inputs["Scale"].default_value=400;n2.inputs["Detail"].default_value=8
add=nt.nodes.new("ShaderNodeMath");add.operation='ADD';nt.links.new(vo.outputs["Distance"],add.inputs[0]);nt.links.new(n2.outputs["Fac"],add.inputs[1])
b=nt.nodes.new("ShaderNodeBump");b.inputs["Strength"].default_value=.35;b.inputs["Distance"].default_value=.0006
nt.links.new(add.outputs["Value"],b.inputs["Height"]);nt.links.new(b.outputs["Normal"],p.inputs["Normal"])
bpy.ops.mesh.primitive_plane_add(size=6);bpy.context.object.data.materials.append(fl)
# low hard sun from the left + soft sky fill
s=bpy.data.lights.new("sun","SUN");s.energy=3.2;s.angle=math.radians(1.2);s.color=(1,.96,.9)
so=bpy.data.objects.new("sun",s);sc.collection.objects.link(so);so.rotation_euler=(math.radians(66),0,math.radians(-58))
w=bpy.data.worlds.new("w");sc.world=w;w.use_nodes=True
w.node_tree.nodes["Background"].inputs["Color"].default_value=srgb("C8CDD3");w.node_tree.nodes["Background"].inputs["Strength"].default_value=.35
cam=bpy.data.cameras.new("cam");cam.lens=70
co=bpy.data.objects.new("cam",cam);sc.collection.objects.link(co);sc.camera=co
tgt=Vector((0,.005,0));az,el,dist=math.radians(AZ),math.radians(64),1.22
co.location=tgt+Vector((math.sin(az)*math.cos(el)*dist,-math.cos(az)*math.cos(el)*dist,math.sin(el)*dist))
co.rotation_euler=(tgt-co.location).to_track_quat("-Z","Y").to_euler()
cam.dof.use_dof=True;cam.dof.focus_distance=(tgt-co.location).length;cam.dof.aperture_fstop=8
sc.render.engine="CYCLES";sc.cycles.device="CPU";sc.cycles.samples=SAMP;sc.cycles.use_denoising=True
sc.render.resolution_x,sc.render.resolution_y=W,H
try: sc.view_settings.view_transform="AgX";sc.view_settings.look="AgX - Medium High Contrast"
except Exception: pass
sc.render.filepath=OUT;bpy.ops.render.render(write_still=True);print("done")
