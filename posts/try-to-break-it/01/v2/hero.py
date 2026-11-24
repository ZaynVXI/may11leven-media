"""Try to break it No. 01, hero: Kusi House night desk. A thermal audit slip curls out of the receipt printer on a
black-walnut counter, stamped REFUSED; the Kusi phone lies cropped at the edge showing the guest's chat; a Lamu wooden
lantern glows behind on coral stone. CC0 Poly Haven assets (walnut veneer, coral stone wall, wooden lantern, HDRI).
usage: python3 hero.py OUT W H SAMPLES [variant]   variant: hero | top | morning"""
import sys, math, bpy, bmesh
from mathutils import Vector
sys.path.insert(0, "/home/claude/r3d"); import real as R
OUT, W, H, SAMP = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
VAR = sys.argv[5] if len(sys.argv) > 5 else "hero"
D = "/home/claude/may11leven-media/posts/try-to-break-it/01/v2/"
sc = R.reset()

def mat(name, col, rough=.5, metal=0., coat=0.):
    m = bpy.data.materials.new(name); m.use_nodes = True; p = m.node_tree.nodes["Principled BSDF"]
    p.inputs["Base Color"].default_value = R.lin(col); p.inputs["Roughness"].default_value = rough
    p.inputs["Metallic"].default_value = metal; p.inputs["Coat Weight"].default_value = coat; return m, p
def box(sx, sy, sz, loc, m, bev=.002, seg=4, rotz=0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc); o = bpy.context.object; o.scale = (sx, sy, sz)
    bpy.ops.object.transform_apply(scale=True); o.rotation_euler[2] = math.radians(rotz)
    b = o.modifiers.new("b", "BEVEL"); b.width = bev; b.segments = seg; o.data.materials.append(m); bpy.ops.object.shade_smooth(); return o
def cyl(r, d, loc, m, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=d, location=loc, rotation=rot, vertices=48); o = bpy.context.object
    o.data.materials.append(m); bpy.ops.object.shade_smooth(); b = o.modifiers.new("b", "BEVEL"); b.width = min(r, d) * .2; b.segments = 3; return o

# --- set: black walnut counter, coral stone wall behind
counter = box(1.8, .9, .05, (0, .1, -.025), R.pbr("black_walnut_veneer_01", scale=2.2, tint="5A3F2E", rough_mul=.7), .004)
bpy.context.view_layer.objects.active = counter; bpy.ops.object.mode_set(mode="EDIT"); bpy.ops.uv.cube_project(cube_size=1.0); bpy.ops.object.mode_set(mode="OBJECT")
bpy.ops.mesh.primitive_plane_add(size=3, location=(0, .55, .6), rotation=(math.radians(90), 0, 0)); wall = bpy.context.object
wall.data.materials.append(R.pbr("coral_stone_wall", scale=2.0, tint="E8DCC8"))

# --- receipt printer: graphite body, black lid, paper slot, green power LED
PX, PY = .03, .07
body = box(.105, .15, .07, (PX, PY, .035), mat("printer", "2A2A29", .5)[0], .008, 5)
box(.104, .006, .003, (PX, PY - .0195, .0786), mat("cutter", "8E8C88", .3, 1.)[0], .001, 2)
box(.002, .12, .0006, (PX - .05, PY + .005, .0700), mat("seam", "101010", .8)[0], .0002, 1)
cyl(.0065, .003, (PX - .03, PY - .066, .0712), mat("btn", "3A3937", .35)[0])
box(.10, .085, .012, (PX, PY + .03, .075), mat("lid", "1A1A1B", .3)[0], .006, 5)
box(.088, .004, .004, (PX, PY - .016, .0805), mat("slot", "050505", .9)[0], .001, 2)
lm, lp = mat("led", "2E6B45", .3); lp.inputs["Emission Color"].default_value = R.lin("59D98A"); lp.inputs["Emission Strength"].default_value = 8
cyl(.0022, .002, (PX + .04, PY - .066, .071), lm)

# --- the slip: rises out of the slot and curls toward the camera; REFUSED sits low, near the slot
img = bpy.data.images.load(D + "slip_cousin.png"); iw, ih = img.size
PWd = .08; PL0 = PWd * ih / iw; PL = PL0 * 1.55
bm = bmesh.new(); n = 140; pos = Vector((PX, PY - .016, .081)); ang = 0.0; pts = []
for i in range(n + 1):
    s = i / n; pts.append(pos.copy())
    k = 0 if s < .5 else (s - .5) / .5; ang = math.radians(96) * k ** 1.4
    pos += Vector((0, -math.sin(ang), math.cos(ang))) * (PL / n)
for i, p in enumerate(pts):
    for sx in (-1, 1):
        bm.verts.new((p.x + sx * PWd / 2, p.y + sx * .0012 * (i / n), p.z + .0004 * math.sin(i * .25 + sx)))
bm.verts.ensure_lookup_table(); bm.verts.index_update()
for i in range(n): bm.faces.new((bm.verts[2 * i], bm.verts[2 * i + 1], bm.verts[2 * i + 3], bm.verts[2 * i + 2]))
uv = bm.loops.layers.uv.new()
for f in bm.faces:
    for lo in f.loops: idx = lo.vert.index; lo[uv].uv = (idx % 2, (idx // 2) / n * PL / PL0)
me = bpy.data.meshes.new("slip"); bm.to_mesh(me); slip = bpy.data.objects.new("slip", me); sc.collection.objects.link(slip)
sm, sp = mat("paper", "FFFFFF", .62); nt = sm.node_tree
it = nt.nodes.new("ShaderNodeTexImage"); it.image = img; it.extension = "EXTEND"
nt.links.new(it.outputs["Color"], sp.inputs["Base Color"])
fib = nt.nodes.new("ShaderNodeTexNoise"); fib.inputs["Scale"].default_value = 900; fb = nt.nodes.new("ShaderNodeBump"); fb.inputs["Strength"].default_value = .05
nt.links.new(fib.outputs["Fac"], fb.inputs["Height"]); nt.links.new(fb.outputs["Normal"], sp.inputs["Normal"])
tr = nt.nodes.new("ShaderNodeBsdfTranslucent"); tr.inputs["Color"].default_value = R.lin("F2E6CF")
mx = nt.nodes.new("ShaderNodeMixShader"); mx.inputs["Fac"].default_value = .15
nt.links.new(sp.outputs["BSDF"], mx.inputs[1]); nt.links.new(tr.outputs["BSDF"], mx.inputs[2]); nt.links.new(mx.outputs[0], nt.nodes["Material Output"].inputs["Surface"])
slip.data.materials.append(sm); slip.modifiers.new("s", "SOLIDIFY").thickness = .00012
bpy.context.view_layer.objects.active = slip; slip.select_set(True); bpy.ops.object.shade_smooth()

# --- the Kusi phone lying on the counter, screen live (emission + glossy coat), cropped by the frame
PW, PH, PT = .0715, .147, .0078
root = bpy.data.objects.new("phone", None); sc.collection.objects.link(root)
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, PT / 2)); pb = bpy.context.object; pb.scale = (PW, PH, PT); bpy.ops.object.transform_apply(scale=True)
bv = pb.modifiers.new("bv", "BEVEL"); bv.width = .0095; bv.segments = 14; bv.limit_method = "ANGLE"
pb.data.materials.append(mat("ti", "1A1A1C", .3, 1.0)[0]); bpy.ops.object.shade_smooth(); pb.parent = root
bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 0, PT + .0001)); bz = bpy.context.object; bz.scale = (PW - .0014, PH - .0014, 1); bpy.ops.object.transform_apply(scale=True)
b2 = bz.modifiers.new("bv", "BEVEL"); b2.width = .0092; b2.segments = 10; b2.affect = "VERTICES"; bz.data.materials.append(mat("bezel", "040405", .05, coat=1.)[0]); bz.parent = root
bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 0, PT + .0002)); sc_ = bpy.context.object; sc_.scale = (PW - .0046, PH - .0046, 1); bpy.ops.object.transform_apply(scale=True)
b3 = sc_.modifiers.new("bv", "BEVEL"); b3.width = .0086; b3.segments = 10; b3.affect = "VERTICES"
gm, gp = mat("glass", "FFFFFF", .03, coat=1.); gt = gm.node_tree.nodes.new("ShaderNodeTexImage"); gt.image = bpy.data.images.load(D + "scr_chat.png"); gt.interpolation = "Cubic"
gm.node_tree.links.new(gt.outputs["Color"], gp.inputs["Base Color"]); gm.node_tree.links.new(gt.outputs["Color"], gp.inputs["Emission Color"]); gp.inputs["Emission Strength"].default_value = (.22 if VAR != "morning" else .1)
gp.inputs["Coat Roughness"].default_value = .03; sc_.data.materials.append(gm); sc_.parent = root
root.location = (-.07, -.05, 0)
if VAR == "hero": root.location = (5, 5, 0)   # the phone gets its own slide; the hero stays one object; root.rotation_euler = (0, 0, math.radians(18))

# --- props from the house: a room key on a carved fob, a Lamu wooden lantern glowing behind
fob = mat("fob", "6B4A2E", .5)[0]; brass = mat("brass", "C39A52", .24, 1.)[0]
cyl(.011, .07, (.115, -.075, .011), fob, rot=(0, math.radians(90), math.radians(24)))
bpy.ops.mesh.primitive_torus_add(major_radius=.012, minor_radius=.0016, location=(.075, -.094, .0018)); bpy.context.object.data.materials.append(brass)
box(.045, .008, .0025, (.046, -.107, .0013), brass, .001, 2, rotz=24)
fl = bpy.data.lights.new("glow", "POINT"); fl.energy = 2.2; fl.color = (1, .62, .3); fl.shadow_soft_size = .05
fo = bpy.data.objects.new("glow", fl); sc.collection.objects.link(fo); fo.location = (-.22, .40, .16)   # a lamp off-frame warming the coral wall

# --- light
if VAR == "morning":
    R.world_hdri("brown_photostudio_02", strength=.5, rot=120)
    R.area((-.9, -.2, .7), size=1.4, energy=55, color=(1, .97, .92)); fl.energy = 0
else:
    R.world_hdri("courtyard_night", strength=.12, rot=200)
    R.area((-.45, -.12, .34), target=(PX, PY - .02, .08), size=.16, energy=10, color=(1, .70, .43))   # desk lamp, out of frame left
    R.area((.6, .2, .28), target=(0, 0, .05), size=.7, energy=3.5, color=(.45, .6, .95))               # night spill from the door
    R.area((PX, .36, .22), target=(PX, PY, .12), size=.25, energy=1.2, color=(1, .82, .62))             # bounce off the wall onto the slip back

# --- camera
if VAR == "top":
    R.camera((0, .02, .62), (0, .02, 0), lens=50, fstop=8)
else:
    R.camera((.12, -.42, .10), (.0, .03, .095), lens=60, fstop=3.2, focus=(PX, PY - .04, .09))
sc.view_settings.exposure = -0.2 if VAR != "morning" else 0
R.render(OUT, W, H, SAMP)
R.finish(OUT, grain=.012, vignette=.18, warm=.02)
