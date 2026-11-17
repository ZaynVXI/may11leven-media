"""ata v3: apothecary bottle of Lagos pepper oil on a travertine plinth, late sun through blinds.
Brief: one object, real material, hard window light (stripes on plaster), the oil glowing where the sun passes,
a red pool of light on the stone, one pepper and one drip as the human trace.
usage: python3 ata3.py OUT.png W H SAMPLES"""
import sys, math, bpy, bmesh
from mathutils import Vector
OUT=sys.argv[1]; W,H,SAMP=int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]); LABROT=float(sys.argv[5]) if len(sys.argv)>5 else -13; CARD=float(sys.argv[6]) if len(sys.argv)>6 else 3
D='/home/claude/may11leven-media/concepts/ata3'
bpy.ops.wm.read_factory_settings(use_empty=True); sc=bpy.context.scene

def lin(h):
    c=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    return tuple((x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4) for x in c)+(1,)
def mat(name):
    m=bpy.data.materials.new(name); m.use_nodes=True; return m,m.node_tree,m.node_tree.nodes["Principled BSDF"]
def link(t,a,b): t.links.new(a,b)
def lathe(name,prof,segs=192):
    me=bpy.data.meshes.new(name); bm=bmesh.new(); rings=[]
    for r,z in prof: rings.append([bm.verts.new((r*math.cos(2*math.pi*i/segs),r*math.sin(2*math.pi*i/segs),z)) for i in range(segs)])
    for a,b in zip(rings,rings[1:]):
        for i in range(segs): bm.faces.new((a[i],a[(i+1)%segs],b[(i+1)%segs],b[i]))
    bm.to_mesh(me); o=bpy.data.objects.new(name,me); sc.collection.objects.link(o)
    for p in me.polygons: p.use_smooth=True
    return o
def smooth_profile(pts,n=3):
    for _ in range(n):
        out=[pts[0]]
        for a,b in zip(pts,pts[1:]):
            out+=[(a[0]*.75+b[0]*.25,a[1]*.75+b[1]*.25),(a[0]*.25+b[0]*.75,a[1]*.25+b[1]*.75)]
        out.append(pts[-1]); pts=out
    return pts

# ---------- bottle: tall apothecary, heavy base, long shoulder, short neck with lip
R=.029
base=[(0,0),(R-.004,0),(R-.001,.0015),(R,.006)]
body=[(R,.006+i*.012) for i in range(1,10)]                       # to z=.114
shoulder=[(R-(R-.011)*(1-math.cos(a*math.pi/2))**1.0*1.0 if False else .011+(R-.011)*math.cos(a*math.pi/2),.114+.034*math.sin(a*math.pi/2)) for a in [i/14 for i in range(1,15)]]
neck=[(.0108,.152),(.0108,.163),(.0124,.1645),(.0126,.1665),(.0118,.168),(.0108,.168)]
prof=smooth_profile(base,1)+body+shoulder+neck
gm,gt,gp=mat("glass")
gp.inputs["Base Color"].default_value=(.94,.975,.955,1); gp.inputs["Transmission Weight"].default_value=1
gp.inputs["Roughness"].default_value=.002; gp.inputs["IOR"].default_value=1.52
nz=gt.nodes.new("ShaderNodeTexNoise"); nz.inputs["Scale"].default_value=60; nz.inputs["Detail"].default_value=4
bb=gt.nodes.new("ShaderNodeBump"); bb.inputs["Strength"].default_value=.006
link(gt,nz.outputs["Fac"],bb.inputs["Height"]); link(gt,bb.outputs["Normal"],gp.inputs["Normal"])
bot=lathe("bottle",prof); bot.data.materials.append(gm)
so=bot.modifiers.new("sol","SOLIDIFY"); so.thickness=.0026; so.offset=-1; so.use_even_offset=True
# thick glass punt in the base
bpy.ops.mesh.primitive_cylinder_add(radius=R-.0026,depth=.009,location=(0,0,.0075),vertices=192); punt=bpy.context.object
pb=punt.modifiers.new("bv","BEVEL"); pb.width=.003; pb.segments=6; punt.data.materials.append(gm); bpy.ops.object.shade_smooth()

# ---------- oil: to just under the shoulder, meniscus
ri=R-.0029; top=.118
lp=[(0,.0122),(ri-.002,.0122),(ri,.0135)]+[(ri,.0135+i*(top-.0135)/10) for i in range(1,11)]+[(ri-.0007,top+.0013),(ri-.0025,top+.0005),(0,top)]
om,ot,op=mat("oil")
op.inputs["Base Color"].default_value=(1,.92,.88,1); op.inputs["Transmission Weight"].default_value=1
op.inputs["Roughness"].default_value=0; op.inputs["IOR"].default_value=1.47
va=ot.nodes.new("ShaderNodeVolumeAbsorption"); va.inputs["Color"].default_value=(.88,.12,.03,1); va.inputs["Density"].default_value=170
link(ot,va.outputs["Volume"],ot.nodes["Material Output"].inputs["Volume"])
oil=lathe("oil",lp); oil.data.materials.append(om)

# ---------- stopper: oak cork top with a paper seal strip (human trace: hand-closed)
bpy.ops.mesh.primitive_cylinder_add(radius=.0145,depth=.022,location=(0,0,.179),vertices=160); cap=bpy.context.object
cb=cap.modifiers.new("bv","BEVEL"); cb.width=.0022; cb.segments=5
km,kt,kp=mat("oak")
wv=kt.nodes.new("ShaderNodeTexWave"); wv.inputs["Scale"].default_value=6; wv.inputs["Distortion"].default_value=4; wv.inputs["Detail"].default_value=6
wv.bands_direction='Z'
kr=kt.nodes.new("ShaderNodeValToRGB"); kr.color_ramp.elements[0].color=lin("6E4A2E"); kr.color_ramp.elements[1].color=lin("9A7148")
link(kt,wv.outputs["Fac"],kr.inputs["Fac"]); link(kt,kr.outputs["Color"],kp.inputs["Base Color"]); kp.inputs["Roughness"].default_value=.62
kb=kt.nodes.new("ShaderNodeBump"); kb.inputs["Strength"].default_value=.15; link(kt,wv.outputs["Fac"],kb.inputs["Height"]); link(kt,kb.outputs["Normal"],kp.inputs["Normal"])
cap.data.materials.append(km); bpy.ops.object.shade_smooth()
# seal strip: thin paper band over the top, down both sides
pm_,ptt,pp=mat("seal"); pp.inputs["Base Color"].default_value=lin("C42612"); pp.inputs["Roughness"].default_value=.8
sb=ptt.nodes.new("ShaderNodeTexNoise"); sb.inputs["Scale"].default_value=700; sbb=ptt.nodes.new("ShaderNodeBump"); sbb.inputs["Strength"].default_value=.1
link(ptt,sb.outputs["Fac"],sbb.inputs["Height"]); link(ptt,sbb.outputs["Normal"],pp.inputs["Normal"])
curve=bpy.data.curves.new("seal","CURVE"); curve.dimensions='3D'; curve.extrude=.003; curve.bevel_depth=0
spn=curve.splines.new('POLY'); pts=[(-.0152,0,.150),(-.0152,0,.188),(-.012,0,.1905),(.012,0,.1905),(.0152,0,.188),(.0152,0,.150)]
spn.points.add(len(pts)-1)
for p,c in zip(spn.points,pts): p.co=(c[0],c[1],c[2],1)
seal=bpy.data.objects.new("seal",curve); sc.collection.objects.link(seal); seal.data.materials.append(pm_)
seal.rotation_euler=(0,0,math.radians(165))
sm=seal.modifiers.new("sol","SOLIDIFY"); sm.thickness=.0003

# ---------- label: cotton paper, letterpress ink bump, wrapped
bpy.ops.mesh.primitive_cylinder_add(radius=R+.0003,depth=.060,location=(0,0,.060),vertices=192,end_fill_type="NOTHING"); lab=bpy.context.object
bpy.ops.object.shade_smooth()
lab.modifiers.new("t","SOLIDIFY").thickness=.00025
lm,lt,lpb=mat("label")
tx=lt.nodes.new("ShaderNodeTexImage"); tx.image=bpy.data.images.load(f"{D}/label.png"); tx.interpolation="Cubic"
ti=lt.nodes.new("ShaderNodeTexImage"); ti.image=bpy.data.images.load(f"{D}/label_ink.png"); ti.image.colorspace_settings.name="Non-Color"
link(lt,tx.outputs["Color"],lpb.inputs["Base Color"]); lpb.inputs["Roughness"].default_value=.88; lpb.inputs["Specular IOR Level"].default_value=.25
fz=lt.nodes.new("ShaderNodeTexNoise"); fz.inputs["Scale"].default_value=1100; fz.inputs["Detail"].default_value=12
mix=lt.nodes.new("ShaderNodeMath"); mix.operation='SUBTRACT'
link(lt,fz.outputs["Fac"],mix.inputs[0]); link(lt,ti.outputs["Color"],mix.inputs[1])
fb=lt.nodes.new("ShaderNodeBump"); fb.inputs["Strength"].default_value=.12; fb.inputs["Distance"].default_value=.0004
link(lt,mix.outputs["Value"],fb.inputs["Height"]); link(lt,fb.outputs["Normal"],lpb.inputs["Normal"])
lab.data.materials.append(lm)
lab.rotation_euler=(0,0,math.radians(LABROT))   # front panel toward camera

# ---------- a single oil drip running down from the lip (human trace)
bpy.ops.mesh.primitive_uv_sphere_add(radius=.0016,location=(0,0,0),segments=24,ring_count=16); drip=bpy.context.object
drip.scale=(1,.55,7); bpy.ops.object.transform_apply(scale=True)
ang=math.radians(-128); r=.0110
drip.location=(r*math.cos(ang)*1.02,r*math.sin(ang)*1.02,.158); drip.rotation_euler=(0,0,ang)
dm,dt,dp=mat("drip"); dp.inputs["Base Color"].default_value=(1,.25,.06,1); dp.inputs["Transmission Weight"].default_value=1; dp.inputs["Roughness"].default_value=0
dva=dt.nodes.new("ShaderNodeVolumeAbsorption"); dva.inputs["Color"].default_value=(.96,.16,.03,1); dva.inputs["Density"].default_value=300
link(dt,dva.outputs["Volume"],dt.nodes["Material Output"].inputs["Volume"])
drip.data.materials.append(dm); bpy.ops.object.shade_smooth()

# ---------- travertine plinth and plaster wall
bpy.ops.mesh.primitive_cube_add(size=1,location=(0,.02,-.06)); pl=bpy.context.object
pl.scale=(.30,.22,.12); bpy.ops.object.transform_apply(scale=True)
plb=pl.modifiers.new("bv","BEVEL"); plb.width=.002; plb.segments=3
tm,tt,tp=mat("travertine")
tco=tt.nodes.new("ShaderNodeTexCoord"); mp=tt.nodes.new("ShaderNodeMapping"); mp.inputs["Scale"].default_value=(1,1,4.5)
link(tt,tco.outputs["Object"],mp.inputs["Vector"])
n1=tt.nodes.new("ShaderNodeTexNoise"); n1.inputs["Scale"].default_value=14; n1.inputs["Detail"].default_value=10; n1.inputs["Roughness"].default_value=.6
link(tt,mp.outputs["Vector"],n1.inputs["Vector"])
r1=tt.nodes.new("ShaderNodeValToRGB"); r1.color_ramp.elements[0].color=lin("B59F80"); r1.color_ramp.elements[1].color=lin("DCCBB0")
link(tt,n1.outputs["Fac"],r1.inputs["Fac"]); link(tt,r1.outputs["Color"],tp.inputs["Base Color"]); tp.inputs["Roughness"].default_value=.55
vo=tt.nodes.new("ShaderNodeTexVoronoi"); vo.inputs["Scale"].default_value=90; link(tt,mp.outputs["Vector"],vo.inputs["Vector"])
pr=tt.nodes.new("ShaderNodeMath"); pr.operation='POWER'; pr.inputs[1].default_value=.25; link(tt,vo.outputs["Distance"],pr.inputs[0])
tb=tt.nodes.new("ShaderNodeBump"); tb.inputs["Strength"].default_value=.6; tb.inputs["Distance"].default_value=.0015
link(tt,pr.outputs["Value"],tb.inputs["Height"]); link(tt,tb.outputs["Normal"],tp.inputs["Normal"])
pl.data.materials.append(tm); bpy.ops.object.shade_smooth()
# oil drop pooled on the stone
bpy.ops.mesh.primitive_uv_sphere_add(radius=.006,location=(-.036,-.026,0),segments=48,ring_count=24); pool=bpy.context.object
pool.scale=(1.1,.8,.10); pool.data.materials.append(dm); bpy.ops.object.shade_smooth()
# floor and wall (warm plaster)
bpy.ops.mesh.primitive_plane_add(size=6,location=(0,0,-.12)); fl=bpy.context.object
wm,wt,wp=mat("plaster"); wn=wt.nodes.new("ShaderNodeTexNoise"); wn.inputs["Scale"].default_value=35; wn.inputs["Detail"].default_value=12
wr=wt.nodes.new("ShaderNodeValToRGB"); wr.color_ramp.elements[0].color=lin("B9A88F"); wr.color_ramp.elements[1].color=lin("CDBDA4")
link(wt,wn.outputs["Fac"],wr.inputs["Fac"]); link(wt,wr.outputs["Color"],wp.inputs["Base Color"]); wp.inputs["Roughness"].default_value=.92
wb=wt.nodes.new("ShaderNodeBump"); wb.inputs["Strength"].default_value=.25; link(wt,wn.outputs["Fac"],wb.inputs["Height"]); link(wt,wb.outputs["Normal"],wp.inputs["Normal"])
fl.data.materials.append(wm)
bpy.ops.mesh.primitive_plane_add(size=6,location=(0,.30,1)); wall=bpy.context.object; wall.rotation_euler=(math.radians(90),0,0); wall.data.materials.append(wm)

# ---------- scotch bonnet, satin skin, beside the bottle
from mathutils import noise
bpy.ops.mesh.primitive_uv_sphere_add(radius=.019,segments=96,ring_count=72,location=(.062,-.020,0)); pep=bpy.context.object
for v in pep.data.vertices:
    p=v.co.copy(); a=math.atan2(p.y,p.x); zn=p.z/.019
    lobes=1+.16*math.cos(4*a+.3)*(1-zn)*.7+.04*math.cos(11*a)
    wr_=.035*noise.noise(Vector((p.x*90,p.y*90,p.z*50)))+.01*noise.noise(Vector((p.x*380,p.y*380,p.z*300)))
    sq=.62 if zn>0 else .78
    v.co=Vector((p.x*lobes*(1+wr_),p.y*lobes*(1+wr_),p.z*sq-.22*max(0,zn)**3*.019))
bpy.ops.object.shade_smooth(); pep.location.z=.0142
pepm,pept,pepp=mat("pepper")
pc=pept.nodes.new("ShaderNodeTexNoise"); pc.inputs["Scale"].default_value=9; pc.inputs["Detail"].default_value=6
prr=pept.nodes.new("ShaderNodeValToRGB"); prr.color_ramp.elements[0].color=lin("A9180A"); prr.color_ramp.elements[1].color=lin("D8401A")
link(pept,pc.outputs["Fac"],prr.inputs["Fac"]); link(pept,prr.outputs["Color"],pepp.inputs["Base Color"])
pepp.inputs["Roughness"].default_value=.34; pepp.inputs["Subsurface Weight"].default_value=.25; pepp.inputs["Subsurface Radius"].default_value=(.006,.0015,.0008)
pepp.inputs["Coat Weight"].default_value=.15; pepp.inputs["Coat Roughness"].default_value=.25
mk=pept.nodes.new("ShaderNodeTexNoise"); mk.inputs["Scale"].default_value=260; mk.inputs["Detail"].default_value=8
mkb=pept.nodes.new("ShaderNodeBump"); mkb.inputs["Strength"].default_value=.06; link(pept,mk.outputs["Fac"],mkb.inputs["Height"]); link(pept,mkb.outputs["Normal"],pepp.inputs["Normal"])
pep.data.materials.append(pepm); pep.rotation_euler=(math.radians(10),math.radians(-18),math.radians(35))
cu=bpy.data.curves.new("stem","CURVE"); cu.dimensions="3D"; cu.bevel_depth=.0019; cu.bevel_resolution=4
spb=cu.splines.new("BEZIER"); spb.bezier_points.add(2)
for b,c in zip(spb.bezier_points,[(.062,-.020,.025),(.060,-.018,.034),(.053,-.013,.039)]): b.co=c; b.handle_left_type=b.handle_right_type="AUTO"
stem=bpy.data.objects.new("stem",cu); sc.collection.objects.link(stem)
stm,stt,stp=mat("stem"); stp.inputs["Base Color"].default_value=lin("55692C"); stp.inputs["Roughness"].default_value=.6; stem.data.materials.append(stm)
bpy.ops.mesh.primitive_cone_add(radius1=.0065,radius2=.0018,depth=.0035,location=(.062,-.020,.0235),vertices=48); cal=bpy.context.object
cal.data.materials.append(stm); bpy.ops.object.shade_smooth()

# ---------- light: late sun through blinds (left, low), warm bounce, cool sky fill, rim for glass edges
sun=bpy.data.lights.new("sun","SUN"); sun.energy=8; sun.angle=math.radians(.8); sun.color=(1,.86,.68)
so_=bpy.data.objects.new("sun",sun); sc.collection.objects.link(so_)
sdir=Vector((.78,.42,-.42)).normalized()   # light travels toward +x,+y,down (from front-left, low)
so_.rotation_euler=sdir.to_track_quat('-Z','Y').to_euler()
# blinds: slats on a plane between sun and set
from mathutils import Matrix
src=Vector((0,.05,.10))-sdir*.9
u=sdir.cross(Vector((0,0,1))).normalized(); v=u.cross(sdir).normalized()
rot=Matrix((u,sdir,v)).transposed().to_euler()
for i in range(-16,17):
    bpy.ops.mesh.primitive_cube_add(size=1); s=bpy.context.object
    s.scale=(1.2,.006,.0155)          # long along u, thin along the ray, slat height along v
    s.rotation_euler=rot
    s.location=src+v*(i*.028)
    s.visible_camera=False; s.visible_glossy=False; s.visible_transmission=False
def area(name,loc,sx,sy,power,col=(1,1,1),tgt=(0,0,.09)):
    l=bpy.data.lights.new(name,"AREA"); l.shape="RECTANGLE"; l.size=sx; l.size_y=sy; l.energy=power; l.color=col
    o=bpy.data.objects.new(name,l); sc.collection.objects.link(o); o.location=loc
    o.rotation_euler=(Vector(tgt)-Vector(loc)).to_track_quat("-Z","Y").to_euler(); o.visible_camera=False; return o
area("strip_R",(.36,.10,.14),.05,.7,6,(1,.95,.9))
area("fill",(-.1,-.9,.3),1.2,.8,3,(.86,.92,1))
w=bpy.data.worlds.new("w"); sc.world=w; w.use_nodes=True
w.node_tree.nodes["Background"].inputs["Color"].default_value=lin("C9BEAD"); w.node_tree.nodes["Background"].inputs["Strength"].default_value=.25

# photographer's trick: a glowing card hidden behind the bottle, seen only through the oil
bpy.ops.mesh.primitive_plane_add(size=1,location=(0,.045,.062)); card=bpy.context.object
card.scale=(.036,.088,1); card.rotation_euler=(math.radians(90),0,0)
cm2=bpy.data.materials.new("card"); cm2.use_nodes=True; nt=cm2.node_tree; nt.nodes.remove(nt.nodes["Principled BSDF"])
em=nt.nodes.new("ShaderNodeEmission"); em.inputs["Color"].default_value=(1,.93,.82,1); em.inputs["Strength"].default_value=CARD
nt.links.new(em.outputs["Emission"],nt.nodes["Material Output"].inputs["Surface"]); card.data.materials.append(cm2)
card.visible_glossy=False; card.visible_diffuse=False

# ---------- camera: 90mm, slightly low, bottle left of centre
cam=bpy.data.cameras.new("cam"); co=bpy.data.objects.new("cam",cam); sc.collection.objects.link(co); sc.camera=co
cam.lens=90; tgt=Vector((.022,0,.085)); az,el,dist=math.radians(-6),math.radians(9),.78
co.location=tgt+Vector((math.sin(az)*math.cos(el)*dist,-math.cos(az)*math.cos(el)*dist,math.sin(el)*dist))
co.rotation_euler=(tgt-co.location).to_track_quat("-Z","Y").to_euler()
cam.dof.use_dof=True; cam.dof.focus_distance=(Vector((0,-.03,.07))-co.location).length; cam.dof.aperture_fstop=6.3
sc.render.engine="CYCLES"; sc.cycles.device="CPU"; sc.cycles.samples=SAMP; sc.cycles.use_denoising=True
sc.cycles.max_bounces=24; sc.cycles.transmission_bounces=24; sc.cycles.transparent_max_bounces=24; sc.cycles.volume_bounces=4
sc.cycles.caustics_reflective=False; sc.cycles.caustics_refractive=True; sc.cycles.blur_glossy=.5
sc.render.resolution_x,sc.render.resolution_y=W,H
sc.view_settings.view_transform="AgX"; sc.view_settings.look="AgX - Medium High Contrast"
sc.render.film_transparent=False
sc.render.filepath=OUT; bpy.ops.render.render(write_still=True); print("done")
