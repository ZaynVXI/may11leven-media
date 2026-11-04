"""ata v2: photoreal glass bottle of Lagos pepper oil on a basalt slab, scotch bonnet prop.
Built with the blender-skills rules (lookdev: one change per pass; lighting: strip lights for glass edges + backlight through liquid; rendering: AgX, sample test first).
usage: python3 bottle2.py OUT.png W H SAMPLES SHOT(wide|close)"""
import sys,math,bpy,bmesh
from mathutils import Vector,noise
OUT=sys.argv[1];W,H,SAMP,SHOT=int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),sys.argv[5]
D='/home/claude/ata2'
bpy.ops.wm.read_factory_settings(use_empty=True);sc=bpy.context.scene
def lin(h):
    c=[int(h[i:i+2],16)/255 for i in (0,2,4)];return tuple((x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4) for x in c)+(1,)
def mat(name):
    m=bpy.data.materials.new(name);m.use_nodes=True;return m,m.node_tree,m.node_tree.nodes["Principled BSDF"]
def lathe(name,prof,segs=160):
    me=bpy.data.meshes.new(name);bm=bmesh.new();rings=[]
    for r,z in prof: rings.append([bm.verts.new((r*math.cos(2*math.pi*i/segs),r*math.sin(2*math.pi*i/segs),z)) for i in range(segs)])
    for a,b in zip(rings,rings[1:]):
        for i in range(segs): bm.faces.new((a[i],a[(i+1)%segs],b[(i+1)%segs],b[i]))
    bm.to_mesh(me);o=bpy.data.objects.new(name,me);sc.collection.objects.link(o)
    for p in me.polygons: p.use_smooth=True
    return o
# ---- bottle profile: round shoulder, short neck, screw thread, thick base
R=.034
prof=[(0,.0),(R-.006,0),(R-.002,.001),(R,.005)]+[(R,.005+i*.0105) for i in range(1,11)]
for i in range(1,17):
    a=i/16*math.pi/2;prof.append((.0135+(R-.0135)*math.cos(a),.11+.03*math.sin(a)))
prof+=[(.0135,.146),(.0142,.148),(.0142,.150),(.0135,.151),(.0135,.158)]
gm,gt,gp=mat("glass");gp.inputs["Base Color"].default_value=(.97,.99,.975,1);gp.inputs["Transmission Weight"].default_value=1
gp.inputs["Roughness"].default_value=.004;gp.inputs["IOR"].default_value=1.5
nz=gt.nodes.new("ShaderNodeTexNoise");nz.inputs["Scale"].default_value=180;bb=gt.nodes.new("ShaderNodeBump");bb.inputs["Strength"].default_value=.015
gt.links.new(nz.outputs["Fac"],bb.inputs["Height"]);gt.links.new(bb.outputs["Normal"],gp.inputs["Normal"])
bot=lathe("bottle",prof);bot.data.materials.append(gm)
so=bot.modifiers.new("sol","SOLIDIFY");so.thickness=.0028;so.offset=-1;so.use_even_offset=True
bv=bot.modifiers.new("ws","WEIGHTED_NORMAL")
# ---- oil: fills to the shoulder with a meniscus, small gap to the glass
ri=R-.0034;top=.104
lp=[(0,.0045),(ri-.001,.0045),(ri,.006)]+[(ri,.006+i*(top-.006)/10) for i in range(1,11)]+[(ri-.0008,top+.0012),(ri-.003,top+.0004),(0,top)]
om,ot,op=mat("oil");op.inputs["Base Color"].default_value=(1,.22,.05,1);op.inputs["Transmission Weight"].default_value=1
op.inputs["Roughness"].default_value=0;op.inputs["IOR"].default_value=1.47
va=ot.nodes.new("ShaderNodeVolumeAbsorption");va.inputs["Color"].default_value=(.95,.12,.02,1);va.inputs["Density"].default_value=140
ot.links.new(va.outputs["Volume"],ot.nodes["Material Output"].inputs["Volume"])
oil=lathe("oil",lp);oil.data.materials.append(om)
# ---- cap: black, knurled ridges
bpy.ops.mesh.primitive_cylinder_add(radius=.0162,depth=.026,location=(0,0,.165),vertices=180);cap=bpy.context.object
for v in cap.data.vertices:
    a=math.atan2(v.co.y,v.co.x);r=math.hypot(v.co.x,v.co.y)
    if r>.016 and abs(v.co.z)<.0115:
        k=1+.018*(1 if math.sin(a*60)>0 else -1);v.co.x*=k;v.co.y*=k
md=cap.modifiers.new("bv","BEVEL");md.width=.0012;md.segments=3;md.limit_method='ANGLE'
cm,ct,cp=mat("cap");cp.inputs["Base Color"].default_value=lin("0D0C0C");cp.inputs["Roughness"].default_value=.42;cp.inputs["Coat Weight"].default_value=.25
cap.data.materials.append(cm);bpy.ops.object.shade_smooth()
# ---- paper label wrap with fibre bump
bpy.ops.mesh.primitive_cylinder_add(radius=R+.0004,depth=.064,location=(0,0,.056),vertices=180,end_fill_type="NOTHING");lab=bpy.context.object;bpy.ops.object.shade_smooth()
sol2=lab.modifiers.new("t","SOLIDIFY");sol2.thickness=.0003
lm,lt,lpb=mat("label");tx=lt.nodes.new("ShaderNodeTexImage");tx.image=bpy.data.images.load(f"{D}/ata_label.png");tx.interpolation="Cubic"
lt.links.new(tx.outputs["Color"],lpb.inputs["Base Color"]);lt.links.new(tx.outputs["Alpha"],lpb.inputs["Alpha"])
lpb.inputs["Roughness"].default_value=.85;lpb.inputs["Specular IOR Level"].default_value=.3
fz=lt.nodes.new("ShaderNodeTexNoise");fz.inputs["Scale"].default_value=900;fz.inputs["Detail"].default_value=10
fb=lt.nodes.new("ShaderNodeBump");fb.inputs["Strength"].default_value=.08;lt.links.new(fz.outputs["Fac"],fb.inputs["Height"]);lt.links.new(fb.outputs["Normal"],lpb.inputs["Normal"])
lab.data.materials.append(lm);lab.rotation_euler=(0,0,math.radians(-14))
# ---- scotch bonnet: lobed, wrinkled, glossy skin with subsurface, curved stem + calyx
bpy.ops.mesh.primitive_uv_sphere_add(radius=.024,segments=96,ring_count=72,location=(.074,-.03,.0));pep=bpy.context.object
for v in pep.data.vertices:
    p=v.co.copy();ang=math.atan2(p.y,p.x);zn=p.z/.024
    lobes=1+.2*math.cos(3*ang+.4)*(1-zn)*.6+.05*math.cos(9*ang)
    wr=.03*noise.noise(Vector((p.x*120,p.y*120,p.z*60)))+.012*noise.noise(Vector((p.x*420,p.y*420,p.z*300)))
    sq=.66 if zn>0 else .82
    dent=-.25*max(0,zn)**3
    v.co=Vector((p.x*lobes*(1+wr),p.y*lobes*(1+wr),p.z*sq+dent*.024))
bpy.ops.object.shade_smooth()
pm,pt,pp=mat("pepper");pp.inputs["Base Color"].default_value=lin("D2260E");pp.inputs["Roughness"].default_value=.22
pp.inputs["Subsurface Weight"].default_value=.35;pp.inputs["Subsurface Radius"].default_value=(.01,.002,.001);pp.inputs["Coat Weight"].default_value=.45;pp.inputs["Coat Roughness"].default_value=.08
cz=pt.nodes.new("ShaderNodeTexNoise");cz.inputs["Scale"].default_value=6;ramp=pt.nodes.new("ShaderNodeValToRGB")
ramp.color_ramp.elements[0].color=lin("B81A08");ramp.color_ramp.elements[1].color=lin("E0461A")
pt.links.new(cz.outputs["Fac"],ramp.inputs["Fac"]);pt.links.new(ramp.outputs["Color"],pp.inputs["Base Color"])
pep.data.materials.append(pm);pep.rotation_euler=(math.radians(8),math.radians(-14),math.radians(30))
pep.location.z=.017
cu=bpy.data.curves.new("stem","CURVE");cu.dimensions="3D";cu.bevel_depth=.0024;cu.bevel_resolution=4
sp=cu.splines.new("BEZIER");sp.bezier_points.add(2)
for b,c in zip(sp.bezier_points,[(.073,-.03,.03),(.071,-.028,.040),(.064,-.022,.046)]): b.co=c;b.handle_left_type=b.handle_right_type="AUTO"
stem=bpy.data.objects.new("stem",cu);sc.collection.objects.link(stem)
sm,st,spb=mat("stem");spb.inputs["Base Color"].default_value=lin("5B7330");spb.inputs["Roughness"].default_value=.55;stem.data.materials.append(sm)
bpy.ops.mesh.primitive_cone_add(radius1=.008,radius2=.002,depth=.004,location=(.073,-.03,.029),vertices=48);cal=bpy.context.object;cal.data.materials.append(sm);bpy.ops.object.shade_smooth()
# ---- basalt slab plinth + dark seamless set
bpy.ops.mesh.primitive_cube_add(size=1,location=(.02,.0,-.02));slab=bpy.context.object;slab.scale=(.34,.22,.04);bpy.ops.object.transform_apply(scale=True)
mb=slab.modifiers.new("bv","BEVEL");mb.width=.003;mb.segments=3
bm_,bt,bp=mat("basalt");bn=bt.nodes.new("ShaderNodeTexNoise");bn.inputs["Scale"].default_value=140;bn.inputs["Detail"].default_value=12
br=bt.nodes.new("ShaderNodeValToRGB");br.color_ramp.elements[0].color=lin("0B0A0A");br.color_ramp.elements[1].color=lin("1C1A19")
bt.links.new(bn.outputs["Fac"],br.inputs["Fac"]);bt.links.new(br.outputs["Color"],bp.inputs["Base Color"]);bp.inputs["Roughness"].default_value=.9
vo=bt.nodes.new("ShaderNodeTexVoronoi");vo.inputs["Scale"].default_value=500;bbp=bt.nodes.new("ShaderNodeBump");bbp.inputs["Strength"].default_value=.3
bt.links.new(vo.outputs["Distance"],bbp.inputs["Height"]);bt.links.new(bbp.outputs["Normal"],bp.inputs["Normal"])
slab.data.materials.append(bm_);bpy.ops.object.shade_smooth()
me=bpy.data.meshes.new("cyc");bmx=bmesh.new();prof2=[(-3+i*(3.4/29),-.04) for i in range(30)];Rc=.8
for i in range(1,25):
    a=i/24*math.pi/2;prof2.append((.4+math.sin(a)*Rc,Rc-math.cos(a)*Rc-.04))
for i in range(1,10): prof2.append((.4+Rc,Rc-.04+i*.4))
rows=[[bmx.verts.new((x,y,z)) for y,z in prof2] for x in (-4,4)]
for i in range(len(prof2)-1): bmx.faces.new((rows[0][i],rows[0][i+1],rows[1][i+1],rows[1][i]))
bmx.to_mesh(me);cyc=bpy.data.objects.new("cyc",me);sc.collection.objects.link(cyc)
for p in me.polygons: p.use_smooth=True
yc,ytc,ypc=mat("set");ypc.inputs["Base Color"].default_value=lin("0E0D0D");ypc.inputs["Roughness"].default_value=.7;cyc.data.materials.append(yc)
# ---- lights: two tall strips for the glass edges, soft front key, backlight through the oil, top
def area(name,loc,sx,sy,power,col=(1,1,1),tgt=(0,0,.08)):
    l=bpy.data.lights.new(name,"AREA");l.shape="RECTANGLE";l.size=sx;l.size_y=sy;l.energy=power;l.color=col
    o=bpy.data.objects.new(name,l);sc.collection.objects.link(o);o.location=loc
    o.rotation_euler=(Vector(tgt)-Vector(loc)).to_track_quat("-Z","Y").to_euler()
area("strip_L",(-.42,.10,.16),.06,.9,26,(1,.97,.93))
area("strip_R",(.40,.14,.16),.06,.9,22,(1,.96,.9))
area("key",(-.25,-.6,.35),.6,.6,5,(1,.97,.94))
area("back",(.0,.45,.12),.18,.14,22,(1,.85,.7),(0,0,.06))
area("top",(0,.05,.75),.4,.4,1.5)
w=bpy.data.worlds.new("w");sc.world=w;w.use_nodes=True;w.node_tree.nodes["Background"].inputs["Strength"].default_value=0
cam=bpy.data.cameras.new("cam");co=bpy.data.objects.new("cam",cam);sc.collection.objects.link(co);sc.camera=co
if SHOT=="wide": cam.lens=75;tgt=Vector((.02,0,.08));az,el,dist=math.radians(-12),math.radians(7),.66
else: cam.lens=110;tgt=Vector((.0,-.004,.085));az,el,dist=math.radians(-16),math.radians(8),.62
co.location=tgt+Vector((math.sin(az)*math.cos(el)*dist,-math.cos(az)*math.cos(el)*dist,math.sin(el)*dist))
co.rotation_euler=(tgt-co.location).to_track_quat("-Z","Y").to_euler()
cam.dof.use_dof=True;cam.dof.focus_distance=(Vector((-.01,-.033,.06))-co.location).length;cam.dof.aperture_fstop=5.6 if SHOT=="wide" else 4.5
sc.render.engine="CYCLES";sc.cycles.device="CPU";sc.cycles.samples=SAMP;sc.cycles.use_denoising=True
sc.cycles.max_bounces=24;sc.cycles.transmission_bounces=24;sc.cycles.transparent_max_bounces=24;sc.cycles.volume_bounces=4
sc.cycles.caustics_reflective=False;sc.cycles.caustics_refractive=True;sc.cycles.blur_glossy=.6
sc.render.resolution_x,sc.render.resolution_y=W,H
sc.view_settings.view_transform="AgX";sc.view_settings.look="AgX - Medium High Contrast"
sc.render.filepath=OUT;bpy.ops.render.render(write_still=True);print("done")
