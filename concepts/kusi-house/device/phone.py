import bpy, bmesh, math, sys, os
from mathutils import Vector
args = sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else []
SCREEN = os.path.abspath(args[0]); OUT = os.path.abspath(args[1]); SAMPLES=int(args[2]) if len(args)>2 else 64
MODE = args[3] if len(args)>3 else 'flat'
bpy.ops.wm.read_factory_settings(use_empty=True)
sc=bpy.context.scene
def rrect(name,w,h,r,depth,segs=16):
    bm=bmesh.new()
    pts=[]
    for cx,cy,a0 in [(w/2-r,h/2-r,0),(-w/2+r,h/2-r,90),(-w/2+r,-h/2+r,180),(w/2-r,-h/2+r,270)]:
        for i in range(segs+1):
            a=math.radians(a0+90*i/segs); pts.append((cx+r*math.cos(a),cy+r*math.sin(a)))
    vs=[bm.verts.new((x,y,0)) for x,y in pts]; f=bm.faces.new(vs)
    if depth:
        ex=bmesh.ops.extrude_face_region(bm,geom=[f]); 
        for v in [e for e in ex['geom'] if isinstance(e,bmesh.types.BMVert)]: v.co.z+=depth
    bmesh.ops.recalc_face_normals(bm,faces=bm.faces)
    me=bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    ob=bpy.data.objects.new(name,me); sc.collection.objects.link(ob); return ob
def mat(name,col,metal=0,rough=.5,emit=None,coat=0):
    m=bpy.data.materials.new(name); m.use_nodes=True; b=m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value=(*col,1); b.inputs['Metallic'].default_value=metal; b.inputs['Roughness'].default_value=rough
    if coat: b.inputs['Coat Weight'].default_value=coat
    return m
def srgb(h): 
    c=[int(h[i:i+2],16)/255 for i in (1,3,5)]; return tuple(((x+0.055)/1.055)**2.4 if x>0.04045 else x/12.92 for x in c)
W,H,T,R=7.15,14.66,0.825,1.05
body=rrect('Body',W,H,R,T,24)
bev=body.modifiers.new('b','BEVEL'); bev.width=0.12; bev.segments=6; bev.limit_method='ANGLE'
for p in body.data.polygons: p.use_smooth=True
body.data.materials.append(mat('Titanium',srgb('#8E877C'),metal=1,rough=.32))
glass=rrect('Glass',W-0.06,H-0.06,R-0.03,0.01,24); glass.location.z=T+0.001
glass.data.materials.append(mat('BlackGlass',srgb('#050505'),rough=.08,coat=1))
# screen with UI
scr=rrect('Screen',W-0.42,H-0.42,R-0.2,0,24); scr.location.z=T+0.013
me=scr.data; me.uv_layers.new(name='UV')
for poly in me.polygons:
    for li in poly.loop_indices:
        v=me.vertices[me.loops[li].vertex_index].co; me.uv_layers['UV'].data[li].uv=((v.x+(W-0.42)/2)/(W-0.42),(v.y+(H-0.42)/2)/(H-0.42))
m=bpy.data.materials.new('UI'); m.use_nodes=True; nt=m.node_tree; nt.nodes.clear()
tex=nt.nodes.new('ShaderNodeTexImage'); tex.image=bpy.data.images.load(SCREEN); tex.interpolation='Cubic'
em=nt.nodes.new('ShaderNodeEmission'); em.inputs['Strength'].default_value=2.4
gl=nt.nodes.new('ShaderNodeBsdfGlossy'); gl.inputs['Roughness'].default_value=0.05
mix=nt.nodes.new('ShaderNodeMixShader'); mix.inputs[0].default_value=0.04
out=nt.nodes.new('ShaderNodeOutputMaterial')
nt.links.new(tex.outputs[0],em.inputs[0]); nt.links.new(em.outputs[0],mix.inputs[1]); nt.links.new(gl.outputs[0],mix.inputs[2]); nt.links.new(mix.outputs[0],out.inputs[0])
scr.data.materials.append(m)
isl=rrect('Island',1.25,0.37,0.185,0.002,12); isl.location=(0,(H-0.42)/2-0.3,T+0.016)
isl.data.materials.append(mat('Isl',(0,0,0),rough=.2))
# side buttons
for y,l in [(2.6,1.6),(4.4,0.9)]:
    bt=rrect('Btn',0.08,l,0.04,0.45); bt.location=(-W/2-0.03,y,0.18); bt.data.materials.append(body.data.materials[0])
bt=rrect('Pwr',0.08,2.4,0.04,0.45); bt.location=(W/2+0.03,2.4,0.18); bt.data.materials.append(body.data.materials[0])
phone=[body,glass,scr,isl]+[o for o in sc.objects if o.name.startswith(('Btn','Pwr'))]
root=bpy.data.objects.new('Phone',None); sc.collection.objects.link(root)
for o in phone: o.parent=root
# ground: lime plaster
g=rrect('Ground',200,200,1,0); g.location.z=-0.0
gm=bpy.data.materials.new('Plaster'); gm.use_nodes=True; n=gm.node_tree.nodes; b=n['Principled BSDF']
b.inputs['Base Color'].default_value=(*srgb('#EFE8DC'),1); b.inputs['Roughness'].default_value=.9
noise=n.new('ShaderNodeTexNoise'); noise.inputs['Scale'].default_value=1.6; noise.inputs['Detail'].default_value=12
bmp=n.new('ShaderNodeBump'); bmp.inputs['Strength'].default_value=0.12
gm.node_tree.links.new(noise.outputs['Fac'],bmp.inputs['Height']); gm.node_tree.links.new(bmp.outputs['Normal'],b.inputs['Normal'])
g.data.materials.append(gm)
if MODE=='flat':
    root.rotation_euler=(0,0,math.radians(-14)); root.location=(0,0,0)
# lights: window key with blinds-like gobo via strips
kl=bpy.data.lights.new('Key','AREA'); kl.energy=26000; kl.size=30; kl.color=(1,.95,.88)
k=bpy.data.objects.new('Key',kl); sc.collection.objects.link(k); k.location=(-45,25,40); k.rotation_euler=(math.radians(45),math.radians(-35),math.radians(-30))
k.rotation_mode='XYZ'; d=Vector((0,0,0))-k.location; k.rotation_euler=d.to_track_quat('-Z','Y').to_euler()
fl=bpy.data.lights.new('Fill','AREA'); fl.energy=2600; fl.size=60; f=bpy.data.objects.new('Fill',fl); sc.collection.objects.link(f); f.location=(40,-30,50)
f.rotation_euler=(Vector((0,0,0))-f.location).to_track_quat('-Z','Y').to_euler()
# blinds: thin slats between key and scene
for i in range(9):
    s=rrect('Slat',40,1.1,0.05,0.1); s.location=(-28,10+i*2.4-10,26); s.rotation_euler=(0,math.radians(-35),0)
    s.data.materials.append(mat('SlatM',(.2,.2,.2),rough=.9))
w=bpy.data.worlds.new('W'); sc.world=w; w.use_nodes=True; w.node_tree.nodes['Background'].inputs[0].default_value=(*srgb('#E9E3D8'),1); w.node_tree.nodes['Background'].inputs[1].default_value=0.6
cam=bpy.data.cameras.new('C'); cam.lens=70; cam.dof.use_dof=True; cam.dof.aperture_fstop=4.0
c=bpy.data.objects.new('Cam',cam); sc.collection.objects.link(c); sc.camera=c
c.location=(9,-27,27); tgt=Vector((0,0.6,0.4)); c.rotation_euler=(tgt-c.location).to_track_quat('-Z','Y').to_euler()
cam.dof.focus_distance=(tgt-c.location).length
sc.render.engine='CYCLES'; sc.cycles.samples=SAMPLES; sc.cycles.use_denoising=True; sc.cycles.device='CPU'
sc.render.resolution_x=1080; sc.render.resolution_y=1350; sc.render.resolution_percentage=100
sc.view_settings.view_transform='AgX'; sc.view_settings.look='AgX - Base Contrast'
sc.render.filepath=OUT; bpy.ops.render.render(write_still=True)
