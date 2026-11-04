"""Photoreal 3D product render (Blender/Cycles via bpy): two Bathu concept shoe boxes, stacked.
usage: python3 boxes.py TEXDIR OUT.png [W H SAMPLES]"""
import sys, math, bpy
from mathutils import Vector
TEX, OUT = sys.argv[1], sys.argv[2]
W, H, SAMP = (int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])) if len(sys.argv) > 5 else (1080, 1350, 128)

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene

def srgb(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return tuple((x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4) for x in c) + (1,)

def mat_paper(name, hexcol, rough=.62, bump=.06):
    m = bpy.data.materials.new(name); m.use_nodes = True
    nt = m.node_tree; p = nt.nodes["Principled BSDF"]
    p.inputs["Base Color"].default_value = srgb(hexcol); p.inputs["Roughness"].default_value = rough
    n = nt.nodes.new("ShaderNodeTexNoise"); n.inputs["Scale"].default_value = 900; n.inputs["Detail"].default_value = 8
    b = nt.nodes.new("ShaderNodeBump"); b.inputs["Strength"].default_value = bump; b.inputs["Distance"].default_value = .0004
    nt.links.new(n.outputs["Fac"], b.inputs["Height"]); nt.links.new(b.outputs["Normal"], p.inputs["Normal"])
    return m

def mat_decal(name, img):
    m = bpy.data.materials.new(name); m.use_nodes = True
    nt = m.node_tree; p = nt.nodes["Principled BSDF"]
    t = nt.nodes.new("ShaderNodeTexImage"); t.image = bpy.data.images.load(f"{TEX}/{img}.png")
    t.interpolation = "Cubic"
    nt.links.new(t.outputs["Color"], p.inputs["Base Color"]); nt.links.new(t.outputs["Alpha"], p.inputs["Alpha"])
    p.inputs["Roughness"].default_value = .85; p.inputs["Specular IOR Level"].default_value = .05
    try: m.blend_method = "HASHED"
    except Exception: pass
    return m

def cube(name, size, loc, mat, bevel=.0025):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc); o = bpy.context.object; o.name = name
    o.scale = size; bpy.ops.object.transform_apply(scale=True)
    md = o.modifiers.new("bv", "BEVEL"); md.width = bevel; md.segments = 4
    o.data.materials.append(mat); bpy.ops.object.shade_smooth()
    return o

def decal(name, w, h, loc, rot, mat):
    bpy.ops.mesh.primitive_plane_add(size=1, location=loc, rotation=rot); o = bpy.context.object; o.name = name
    o.scale = (w, h, 1); bpy.ops.object.transform_apply(scale=True); o.data.materials.append(mat)
    return o

def shoebox(prefix, col, lidtex, fronttex, origin, rz):
    L, Wd, Hb = .33, .21, .118
    root = bpy.data.objects.new(prefix, None); sc.collection.objects.link(root)
    paper = mat_paper(prefix + "_paper", col)
    parts = [
        cube(prefix + "_body", (L, Wd, Hb - .004), (0, 0, (Hb - .004) / 2), paper),
        cube(prefix + "_lid", (L + .006, Wd + .006, .042), (0, 0, Hb - .021), paper, .003),
        decal(prefix + "_top", L * .98, Wd * .98, (0, 0, Hb + .0003), (0, 0, 0), mat_decal(prefix + "_tm", lidtex)),
        decal(prefix + "_front", L * .98, .074, (0, -Wd / 2 - .0004, (Hb - .042) / 2), (math.pi / 2, 0, 0),
              mat_decal(prefix + "_fm", fronttex)),
    ]
    for p in parts: p.parent = root
    root.location = origin; root.rotation_euler = (0, 0, rz)
    return root

shoebox("black", "141414", "lid_black", "front_black", (0, 0, 0), math.radians(-4))
orng = shoebox("orange", "C4C0B8", "lid_orange", "front_orange", (.018, .012, .1185), math.radians(13))
bpy.context.view_layer.update()
# a white shoelace draped over the top box, aglets on both ends
pts = [(-.2,-.29,-.1155),(-.13,-.25,-.1155),(-.09,-.18,-.085),(-.08,-.135,.0),(-.075,-.117,.095),(-.06,-.10,.1215),(-.02,-.03,.1215),(.04,.05,.1215),(.09,.09,.1215),(.115,.115,.1),(.14,.13,.03),(.19,.14,-.04)]
cu = bpy.data.curves.new("lace","CURVE"); cu.dimensions="3D"; cu.bevel_depth=.0024; cu.bevel_resolution=4
sp = cu.splines.new("BEZIER"); sp.bezier_points.add(len(pts)-1)
for bp,p in zip(sp.bezier_points,pts):
    bp.co = orng.matrix_world @ Vector(p); bp.handle_left_type = bp.handle_right_type = "AUTO"
lace = bpy.data.objects.new("lace",cu); sc.collection.objects.link(lace)
lace.data.materials.append(mat_paper("cotton","F2F0EA",.85,.15))
aglet = bpy.data.materials.new("aglet"); aglet.use_nodes=True
ap = aglet.node_tree.nodes["Principled BSDF"]; ap.inputs["Base Color"].default_value=(.02,.02,.02,1); ap.inputs["Roughness"].default_value=.25
for i,j in ((0,1),(-1,-2)):
    a = orng.matrix_world @ Vector(pts[i]); b = orng.matrix_world @ Vector(pts[j]); d=(b-a).normalized()
    bpy.ops.mesh.primitive_cylinder_add(radius=.0028, depth=.022, location=a+d*.011)
    c=bpy.context.object; c.rotation_euler=d.to_track_quat("Z","Y").to_euler(); c.data.materials.append(aglet); bpy.ops.object.shade_smooth()


# cyclorama: floor curving up into a wall, bone coloured
import bmesh
me = bpy.data.meshes.new("cyc"); bm = bmesh.new(); prof = []
for i in range(30): prof.append((-4 + i * (4.6 / 29), 0))
R = .9
for i in range(1, 25):
    a = i / 24 * math.pi / 2; prof.append((.6 + math.sin(a) * R, R - math.cos(a) * R))
for i in range(1, 10): prof.append((.6 + R, R + i * .4))
rows = []
for x in (-5, 5):
    rows.append([bm.verts.new((x, y, z)) for y, z in prof])
for i in range(len(prof) - 1):
    bm.faces.new((rows[0][i], rows[0][i + 1], rows[1][i + 1], rows[1][i]))
bm.to_mesh(me); cyc = bpy.data.objects.new("cyc", me); sc.collection.objects.link(cyc)
for p in me.polygons: p.use_smooth = True
cyc.data.materials.append(mat_paper("set", "D6D4CF", .8, .0))
cyc.rotation_euler = (0, 0, math.radians(-30))

def area(name, loc, size, power, col=(1, 1, 1), target=(0, 0, .14)):
    l = bpy.data.lights.new(name, "AREA"); l.size = size; l.energy = power; l.color = col
    o = bpy.data.objects.new(name, l); sc.collection.objects.link(o); o.location = loc
    d = Vector(target) - Vector(loc); o.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()

area("key", (-.9, -.7, 1.2), .25, 22, (1, .96, .9))
area("fill", (1.2, -1.2, .35), 1.6, 9, (.93, .96, 1))
area("rim", (.7, .9, .6), .5, 45)
area("top", (0, .2, 1.4), .6, 7)

w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs["Color"].default_value = srgb("E9E6E0")
w.node_tree.nodes["Background"].inputs["Strength"].default_value = .0

cam = bpy.data.cameras.new("cam"); cam.lens = 85
co = bpy.data.objects.new("cam", cam); sc.collection.objects.link(co); sc.camera = co
tgt = Vector((.0, 0, .13))
az, el, dist = math.radians(-28), math.radians(21), 1.3
co.location = tgt + Vector((math.sin(az) * math.cos(el) * dist, -math.cos(az) * math.cos(el) * dist, math.sin(el) * dist))
co.rotation_euler = (tgt - co.location).to_track_quat("-Z", "Y").to_euler()
cam.dof.use_dof = True; cam.dof.focus_distance = (tgt - co.location).length; cam.dof.aperture_fstop = 5.6

sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"; sc.cycles.samples = SAMP
sc.cycles.use_denoising = True
sc.render.resolution_x, sc.render.resolution_y = W, H; sc.render.resolution_percentage = 100
sc.render.film_transparent = False
try: sc.view_settings.view_transform = "AgX"; sc.view_settings.look = "AgX - Medium High Contrast"
except Exception: pass
sc.view_settings.exposure = -0.8
sc.render.image_settings.file_format = "PNG"; sc.render.filepath = OUT
bpy.ops.render.render(write_still=True)
print("done", OUT)
