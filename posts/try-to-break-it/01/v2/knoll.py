"""Try to break it No. 01, slide 4: the night's four audit slips laid out on the walnut counter from above,
each stamped, with a pen and the room key (knolling). CC0 walnut veneer + HDRI. usage: python3 knoll.py OUT W H SAMPLES"""
import sys, math, bpy, bmesh
from mathutils import Vector
sys.path.insert(0, "/home/claude/r3d"); import real as R
OUT, W, H, SAMP = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
D = "/home/claude/may11leven-media/posts/try-to-break-it/01/v2/"
sc = R.reset()
def mat(name, col, rough=.5, metal=0.):
    m = bpy.data.materials.new(name); m.use_nodes = True; p = m.node_tree.nodes["Principled BSDF"]
    p.inputs["Base Color"].default_value = R.lin(col); p.inputs["Roughness"].default_value = rough; p.inputs["Metallic"].default_value = metal; return m, p
bpy.ops.mesh.primitive_plane_add(size=1.2); top = bpy.context.object
top.data.materials.append(R.pbr("black_walnut_veneer_01", scale=.55, tint="5A3F2E", rough_mul=.7))

def slip(name, x, y, rot, curl=.0025):
    img = bpy.data.images.load(D + f"slip_{name}.png"); iw, ih = img.size
    w = .08; h = w * ih / iw; nx, ny = 8, 60
    bm = bmesh.new()
    for j in range(ny + 1):
        for i in range(nx + 1):
            u, v = i / nx, j / ny
            z = curl * (math.sin(v * math.pi) ** 2) * .6 + curl * (abs(u - .5) * 2) ** 3 + .00015 * math.sin(v * 9)   # paper never lies flat
            bm.verts.new(((u - .5) * w, (v - .5) * h, z + .0003))
    bm.verts.ensure_lookup_table(); bm.verts.index_update()
    for j in range(ny):
        for i in range(nx):
            a = j * (nx + 1) + i; bm.faces.new((bm.verts[a], bm.verts[a + 1], bm.verts[a + nx + 2], bm.verts[a + nx + 1]))
    uv = bm.loops.layers.uv.new()
    for f in bm.faces:
        for lo in f.loops: k = lo.vert.index; lo[uv].uv = ((k % (nx + 1)) / nx, (k // (nx + 1)) / ny)
    me = bpy.data.meshes.new(name); bm.to_mesh(me); o = bpy.data.objects.new(name, me); sc.collection.objects.link(o)
    m, p = mat("p_" + name, "FFFFFF", .62); t = m.node_tree.nodes.new("ShaderNodeTexImage"); t.image = img
    m.node_tree.links.new(t.outputs["Color"], p.inputs["Base Color"]); o.data.materials.append(m)
    o.modifiers.new("s", "SOLIDIFY").thickness = .00012; o.location = (x, y, 0); o.rotation_euler[2] = math.radians(rot)
    bpy.context.view_layer.objects.active = o; o.select_set(True); bpy.ops.object.shade_smooth(); o.select_set(False)
    return o
# four slips in time order, a 1 cm gutter, the smallest tilts
slip("deal", -.129, .025, 1.2); slip("cousin", -.043, .02, -.6); slip("code", .043, .032, .8); slip("shot", .129, .026, -1.0)
# pen and key along the bottom edge, square to the grid
pen = mat("pen", "141416", .25)[0]
bpy.ops.mesh.primitive_cylinder_add(radius=.0045, depth=.14, location=(-.085, -.085, .0045), rotation=(0, math.radians(90), 0), vertices=48); bpy.context.object.data.materials.append(pen); bpy.ops.object.shade_smooth()
brass = mat("brass", "C39A52", .24, 1.)[0]; fob = mat("fob", "6B4A2E", .5)[0]
bpy.ops.mesh.primitive_cylinder_add(radius=.011, depth=.07, location=(.045, -.085, .011), rotation=(0, math.radians(90), 0), vertices=48); bpy.context.object.data.materials.append(fob); bpy.ops.object.shade_smooth()
bpy.ops.mesh.primitive_torus_add(major_radius=.012, minor_radius=.0016, location=(.092, -.085, .0018)); bpy.context.object.data.materials.append(brass)
bpy.ops.mesh.primitive_cube_add(size=1, location=(.125, -.085, .0013)); k = bpy.context.object; k.scale = (.045, .008, .0025); k.data.materials.append(brass)
# light: one warm lamp from the upper left, long soft shadows; night HDRI for reflections
R.world_hdri("courtyard_night", strength=.15, rot=200)
R.area((-.55, .35, .45), target=(0, 0, 0), size=.35, energy=30, color=(1, .74, .5))
R.area((.6, -.4, .5), target=(0, 0, 0), size=.8, energy=4, color=(.55, .68, .95))
R.camera((0, -.005, .62), (0, -.005, 0), lens=50, fstop=11)
R.render(OUT, W, H, SAMP); R.finish(OUT, grain=.012, vignette=.2, warm=.02)
