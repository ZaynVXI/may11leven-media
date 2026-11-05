"""Brand clinic v4 hero: a logo eye-test card leaning on a cool grey wall, magnifier in front.
No AI imagery. usage: OUT W H SAMPLES"""
import sys, math, bpy
from mathutils import Vector
sys.path.insert(0, "/home/claude/r3d"); import real as R
OUT, W, H, SAMP = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
sc = R.reset()

def mat(name, col, rough=.5, metal=0.):
    m = bpy.data.materials.new(name); m.use_nodes = True; p = m.node_tree.nodes["Principled BSDF"]
    p.inputs["Base Color"].default_value = R.lin(col); p.inputs["Roughness"].default_value = rough
    p.inputs["Metallic"].default_value = metal; return m, p

# seamless cool-grey paper sweep (floor curving up into the wall)
import bmesh
me = bpy.data.meshes.new("sweep"); bm = bmesh.new(); prof = []
for i in range(41):
    t = i / 40
    if t < .5: y, z = -1.2 + t * 2 * 1.2, 0
    else:
        a = (t - .5) * 2 * math.pi / 2; y, z = .25 * math.sin(a), .25 * (1 - math.cos(a))
    prof.append((y, z))
prof += [(.25, .25 + k * .1) for k in range(1, 16)]
rows = [[bm.verts.new((x, y, z)) for (y, z) in prof] for x in (-1.5, 1.5)]
for i in range(len(prof) - 1): bm.faces.new((rows[0][i], rows[1][i], rows[1][i + 1], rows[0][i + 1]))
bm.to_mesh(me); sw = bpy.data.objects.new("sweep", me); sc.collection.objects.link(sw)
for p in me.polygons: p.use_smooth = True
pm, pp = mat("paper", "A9ADB0", .9)
nz = pm.node_tree.nodes.new("ShaderNodeTexNoise"); nz.inputs["Scale"].default_value = 900; bb = pm.node_tree.nodes.new("ShaderNodeBump"); bb.inputs["Strength"].default_value = .03
pm.node_tree.links.new(nz.outputs["Fac"], bb.inputs["Height"]); pm.node_tree.links.new(bb.outputs["Normal"], pp.inputs["Normal"])
sw.data.materials.append(pm)


CW, CH, CT = .21, .297, .0025
cols = ["B4532A","2F5D8A","2A45E8","C9922E","4F6B3A","1F5E5A","E8D23A"]
import math
def card(col, z, ang, tex=None, dx=0, dy=0):
    bpy.ops.mesh.primitive_cube_add(size=1); c = bpy.context.object; c.scale = (CW, CH, CT); bpy.ops.object.transform_apply(scale=True)
    bv = c.modifiers.new("bv", "BEVEL"); bv.width = .0008; bv.segments = 2
    m, p = mat("c"+col, col, .55); c.data.materials.append(m)
    # pivot at the bottom-left corner so the deck fans like cards in a hand
    c.location = (dx, dy, z)
    c.rotation_euler = (0, 0, math.radians(ang))
    if tex:
        bpy.ops.mesh.primitive_plane_add(size=1); f = bpy.context.object; f.scale = (CW, CH, 1); bpy.ops.object.transform_apply(scale=True)
        f.location = (0, 0, CT/2 + .0002); f.parent = c
        fm, fp = mat("face", "FFFFFF", .7)
        tx = fm.node_tree.nodes.new("ShaderNodeTexImage"); tx.image = bpy.data.images.load(tex); tx.interpolation = "Cubic"
        fm.node_tree.links.new(tx.outputs["Color"], fp.inputs["Base Color"])
        fz = fm.node_tree.nodes.new("ShaderNodeTexNoise"); fz.inputs["Scale"].default_value = 1600; fb = fm.node_tree.nodes.new("ShaderNodeBump"); fb.inputs["Strength"].default_value = .05
        fm.node_tree.links.new(fz.outputs["Fac"], fb.inputs["Height"]); fm.node_tree.links.new(fb.outputs["Normal"], fp.inputs["Normal"])
        f.data.materials.append(fm)
    return c
for i, col in enumerate(cols):
    card(col, CT/2 + i*CT*1.05, 29 - i*4.2, dx=-.08 + i*.011, dy=-.12 + i*.005)
card("ECEAE4", CT/2 + 7*CT*1.05, -2, tex="/home/claude/svc/topcard.png", dx=.005, dy=-.1)
R.world_hdri("photo_studio_loft_hall", strength=.18, rot=70)
R.area((-.8, -.6, .9), target=(0,-.1,0), size=.6, energy=75, color=(1, .99, .97))
R.area((.7, -.5, .5), size=1.0, energy=10, color=(.92, .95, 1))
R.camera((.05, -.62, .62), (-.03, -.1, 0), lens=60, fstop=5.6, focus=(-.03, -.1, .01))
bpy.context.scene.view_settings.exposure = float(__import__("os").environ.get("EXP", "-1.3"))
R.render(OUT, W, H, SAMP)
R.finish(OUT, grain=.008, vignette=.08, warm=0)
