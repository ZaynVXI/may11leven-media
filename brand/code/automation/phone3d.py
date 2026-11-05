"""Friday hero v3 (no AI imagery): the queue app on a phone on a marble barbershop counter, next to the paper ticket it replaces,
a real comb-like prop and window-blind light. usage: DIR OUT W H SAMPLES"""
import sys, math, bpy
from mathutils import Vector, noise
sys.path.insert(0, "/home/claude/r3d"); import real as R
OUT, W, H, SAMP = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
sc = R.reset()

def mat(name, col, rough=.5, metal=0., coat=0.):
    m = bpy.data.materials.new(name); m.use_nodes = True; p = m.node_tree.nodes["Principled BSDF"]
    p.inputs["Base Color"].default_value = R.lin(col); p.inputs["Roughness"].default_value = rough
    p.inputs["Metallic"].default_value = metal; p.inputs["Coat Weight"].default_value = coat; return m, p
def img(name, path, rough=.4, emit=0.):
    m, p = mat(name, "FFFFFF", rough)
    t = m.node_tree.nodes.new("ShaderNodeTexImage"); t.image = bpy.data.images.load(path); t.interpolation = "Cubic"
    m.node_tree.links.new(t.outputs["Color"], p.inputs["Base Color"])
    if emit: m.node_tree.links.new(t.outputs["Color"], p.inputs["Emission Color"]); p.inputs["Emission Strength"].default_value = emit
    return m


# surface: cool sage plaster (clinic-clean), tinted
bpy.ops.mesh.primitive_plane_add(size=3); fl = bpy.context.object
pm, pp = mat("sage", "C7D0C3", .85)
nz = pm.node_tree.nodes.new("ShaderNodeTexNoise"); nz.inputs["Scale"].default_value = 260; nz.inputs["Detail"].default_value = 8
bb = pm.node_tree.nodes.new("ShaderNodeBump"); bb.inputs["Strength"].default_value = .06
pm.node_tree.links.new(nz.outputs["Fac"], bb.inputs["Height"]); pm.node_tree.links.new(bb.outputs["Normal"], pp.inputs["Normal"])
n2 = pm.node_tree.nodes.new("ShaderNodeTexNoise"); n2.inputs["Scale"].default_value = 6
mx = pm.node_tree.nodes.new("ShaderNodeMix"); mx.data_type = "RGBA"; mx.inputs[6].default_value = R.lin("C2CCBF"); mx.inputs[7].default_value = R.lin("CDD5C9")
pm.node_tree.links.new(n2.outputs["Fac"], mx.inputs["Factor"]); pm.node_tree.links.new(mx.outputs[2], pp.inputs["Base Color"])
fl.data.materials.append(pm)
# phone 71.5 x 147 x 7.8 mm: brushed titanium frame, glossy glass over the live screen
PW, PH, PT = .0715, .147, .0078
root = bpy.data.objects.new("phone", None); sc.collection.objects.link(root)
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, PT / 2)); body = bpy.context.object
body.scale = (PW, PH, PT); bpy.ops.object.transform_apply(scale=True)
bv = body.modifiers.new("bv", "BEVEL"); bv.width = .0095; bv.segments = 14; bv.limit_method = "ANGLE"
body.data.materials.append(mat("ti", "1A1A1C", .3, 1.0)[0]); bpy.ops.object.shade_smooth(); body.parent = root
bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 0, PT + .0002)); scr = bpy.context.object
scr.scale = (PW - .0046, PH - .0046, 1); bpy.ops.object.transform_apply(scale=True)
sb = scr.modifiers.new("bv", "BEVEL"); sb.width = .0086; sb.segments = 10; sb.affect = "VERTICES"
sm, sp = mat("glass", "020203", .03, coat=1.0); scr.data.materials.append(sm); scr.parent = root
bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 0, PT + .0001)); bz = bpy.context.object
bz.scale = (PW - .0014, PH - .0014, 1); bpy.ops.object.transform_apply(scale=True)
bzb = bz.modifiers.new("bv", "BEVEL"); bzb.width = .0092; bzb.segments = 10; bzb.affect = "VERTICES"
bm, bp = mat("bezel", "040405", .05, coat=1.0); bz.data.materials.append(bm); bz.parent = root
root.location = (0, -.004, 0); root.rotation_euler = (0, 0, math.radians(-5))


# soft daylight from top-left through a big diffuser + faint leaf gobo for life
R.world_hdri("photo_studio_loft_hall", strength=.35, rot=40)
R.area((-.9, .2, .45), target=(0,0,0), size=1.6, energy=42, color=(1, .985, .96))
R.area((.6, -.5, .5), size=1.0, energy=6, color=(.9, .95, 1))
d = R.leaf_gobo(target=(0,0,0), dist=1.1, elev=48, azim=135, scale=1.0)
R.sun(d, energy=1.6, angle=3.0, color=(1, .95, .88))
R.camera((0, .018, .4), (0, .018, 0), lens=50, fstop=5.6, focus=(0, 0, .008))
bpy.context.scene.view_settings.exposure = -0.2
R.render(OUT, W, H, SAMP)
# project the screen corners (inner glass rect) to pixels for compositing
from bpy_extras.object_utils import world_to_camera_view
cam = bpy.context.scene.camera; mw = scr.matrix_world
import json
bpy.context.view_layer.update()
hw, hh = (PW - .0046) / 2, (PH - .0046) / 2
pts = []
for (x, y) in [(-hw, hh), (hw, hh), (hw, -hh), (-hw, -hh)]:
    co = world_to_camera_view(bpy.context.scene, cam, mw @ Vector((x, y, 0)))
    pts.append([co.x * W, (1 - co.y) * H])
json.dump(pts, open(OUT + ".json", "w")); print("corners", pts)
R.finish(OUT, grain=.007, vignette=.1, warm=0)
