"""Try to break it No. 01 hero: a night-desk receipt printer on a Lamu hardwood counter (Blender, Cycles).
usage: python3 hero.py slip.png out.png W H SAMPLES [cam]   cam: hero | top"""
import bpy, sys, math, bmesh, mathutils
a = sys.argv[1:]
SLIP, OUT, W, H, SAMP = a[0], a[1], int(a[2]), int(a[3]), int(a[4]); CAM = a[5] if len(a) > 5 else 'hero'
def lin(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c] + [1]
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; sc.render.engine = 'CYCLES'; sc.cycles.samples = SAMP; sc.cycles.use_denoising = True
sc.cycles.max_bounces = 6; sc.render.resolution_x, sc.render.resolution_y = W, H
sc.view_settings.view_transform = 'AgX'; sc.view_settings.look = 'AgX - Medium High Contrast'; sc.view_settings.exposure = 0.0
def mat(name, base, rough, metal=0.0):
    m = bpy.data.materials.new(name); m.use_nodes = True; b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = base; b.inputs['Roughness'].default_value = rough; b.inputs['Metallic'].default_value = metal
    return m, b
def box(sx, sy, sz, loc, m, bev=0.002, seg=4):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc); o = bpy.context.object; o.scale = (sx, sy, sz); bpy.ops.object.transform_apply(scale=True)
    b = o.modifiers.new('b', 'BEVEL'); b.width = bev; b.segments = seg; o.data.materials.append(m); bpy.ops.object.shade_smooth(); return o
def cyl(r, d, loc, m, rot=(0, 0, 0), v=48):
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=d, location=loc, rotation=rot, vertices=v); o = bpy.context.object
    o.data.materials.append(m); bpy.ops.object.shade_smooth(); b = o.modifiers.new('b', 'BEVEL'); b.width = min(r, d) * .15; b.segments = 3; return o

# --- hardwood counter: dark mahogany grain along X, oiled
wm, wb = mat('wood', lin('3A2216'), 0.38); wb.inputs['Coat Weight'].default_value = 0.25; wb.inputs['Coat Roughness'].default_value = 0.2
N, L = wm.node_tree.nodes, wm.node_tree.links
tc = N.new('ShaderNodeTexCoord'); mp = N.new('ShaderNodeMapping'); mp.inputs['Scale'].default_value = (2.5, 40, 2.5)
wv = N.new('ShaderNodeTexWave'); wv.wave_type = 'BANDS'; wv.inputs['Scale'].default_value = 3; wv.inputs['Distortion'].default_value = 6; wv.inputs['Detail'].default_value = 6; wv.inputs['Detail Roughness'].default_value = .7
nz = N.new('ShaderNodeTexNoise'); nz.inputs['Scale'].default_value = 300; nz.inputs['Detail'].default_value = 8
cr = N.new('ShaderNodeValToRGB'); cr.color_ramp.elements[0].color = lin('24130B'); cr.color_ramp.elements[1].color = lin('5A3420')
mix = N.new('ShaderNodeMath'); mix.operation = 'MULTIPLY_ADD'; mix.inputs[1].default_value = .85; mix.inputs[2].default_value = 0
L.new(tc.outputs['Object'], mp.inputs['Vector']); L.new(mp.outputs['Vector'], wv.inputs['Vector']); L.new(mp.outputs['Vector'], nz.inputs['Vector'])
ad = N.new('ShaderNodeMath'); ad.operation = 'ADD'; L.new(wv.outputs['Fac'], ad.inputs[0]); m2 = N.new('ShaderNodeMath'); m2.operation = 'MULTIPLY'; m2.inputs[1].default_value = .18
L.new(nz.outputs['Fac'], m2.inputs[0]); L.new(m2.outputs[0], ad.inputs[1]); L.new(ad.outputs[0], cr.inputs['Fac']); L.new(cr.outputs['Color'], wb.inputs['Base Color'])
bu = N.new('ShaderNodeBump'); bu.inputs['Strength'].default_value = .08; bu.inputs['Distance'].default_value = .0003; L.new(nz.outputs['Fac'], bu.inputs['Height']); L.new(bu.outputs['Normal'], wb.inputs['Normal'])
counter = box(1.6, 0.7, 0.05, (0, 0.05, -0.025), wm, 0.006)
# carved front band (a step and a bead along the front edge)
box(1.6, 0.03, 0.03, (0, -0.31, -0.07), wm, 0.004)
# --- lime plaster wall behind, out of focus
pm, pb = mat('plaster', lin('E6DED0'), 0.92)
pn = pm.node_tree.nodes; pl = pm.node_tree.links
n2 = pn.new('ShaderNodeTexNoise'); n2.inputs['Scale'].default_value = 18; n2.inputs['Detail'].default_value = 10; n2.inputs['Roughness'].default_value = .65
b2 = pn.new('ShaderNodeBump'); b2.inputs['Strength'].default_value = .35; pl.new(n2.outputs['Fac'], b2.inputs['Height']); pl.new(b2.outputs['Normal'], pb.inputs['Normal'])
bpy.ops.mesh.primitive_plane_add(size=3, location=(0, 0.42, 0.6), rotation=(math.radians(90), 0, 0)); bpy.context.object.data.materials.append(pm)
# --- receipt printer: warm-grey plastic body, black lid, paper slot
body_m, _ = mat('printer', lin('2C2B2A'), 0.5)
lid_m, _ = mat('lid', lin('1B1B1C'), 0.32)
PX, PY = 0.03, 0.06
body = box(0.105, 0.15, 0.07, (PX, PY, 0.035), body_m, 0.014, 6)
lid = box(0.10, 0.085, 0.012, (PX, PY + 0.03, 0.075), lid_m, 0.006, 5)
slot = box(0.088, 0.004, 0.004, (PX, PY - 0.016, 0.0805), lin and mat('slot', lin('050505'), .8)[0], 0.001, 2)
led_m, led_b = mat('led', lin('2E6B45'), .3); led_b.inputs['Emission Color'].default_value = lin('59D98A'); led_b.inputs['Emission Strength'].default_value = 6
cyl(0.0022, 0.002, (PX + 0.04, PY - 0.065, 0.071), led_m)
feed_m, _ = mat('feed', lin('3A3938'), .4); cyl(0.007, 0.004, (PX - 0.03, PY - 0.06, 0.071), feed_m)
# --- the slip: a strip that rises from the slot and curls toward the camera
img = bpy.data.images.load(SLIP); iw, ih = img.size
PW = 0.08; PL = PW * ih / iw
bm = bmesh.new(); n = 120
pos = mathutils.Vector((PX, PY - 0.016, 0.081)); ang = 0.0; pts = []
for i in range(n + 1):
    s = i / n; pts.append((pos.copy(), ang))
    k = 0 if s < .45 else (s - .45) / .55; ang = math.radians(78) * k ** 1.6          # bend forward (toward -Y)
    pos += mathutils.Vector((0, -math.sin(ang), math.cos(ang))) * (PL / n)
uvl = []
for i, (p, an) in enumerate(pts):
    tw = math.radians(4) * (i / n)                                                  # slight twist
    for sx in (-1, 1):
        x = sx * PW / 2; v = bm.verts.new((p.x + x * math.cos(tw), p.y + x * math.sin(tw) * .3, p.z + sx * 0.0006 * math.sin(i * .3)))
bm.verts.ensure_lookup_table()
for i in range(n):
    f = bm.faces.new((bm.verts[2 * i], bm.verts[2 * i + 1], bm.verts[2 * i + 3], bm.verts[2 * i + 2]))
uv = bm.loops.layers.uv.new()
for f in bm.faces:
    for lp in f.loops:
        idx = lp.vert.index; i, sx = idx // 2, idx % 2
        lp[uv].uv = (sx, i / n)   # v=0 at the slot = bottom of the slip (last printed)
me = bpy.data.meshes.new('slip'); bm.to_mesh(me); slip = bpy.data.objects.new('slip', me); sc.collection.objects.link(slip)
sm, sb = mat('paper', (1, 1, 1, 1), 0.55); sb.inputs['Subsurface Weight'].default_value = 0.0
it = sm.node_tree.nodes.new('ShaderNodeTexImage'); it.image = img; it.extension = 'EXTEND'
gm = sm.node_tree.nodes.new('ShaderNodeGamma'); gm.inputs['Gamma'].default_value = 1.08
sm.node_tree.links.new(it.outputs['Color'], gm.inputs['Color']); sm.node_tree.links.new(gm.outputs['Color'], sb.inputs['Base Color'])
# thin paper: let a little light through from behind
tr = sm.node_tree.nodes.new('ShaderNodeBsdfTranslucent'); tr.inputs['Color'].default_value = lin('F2E7D2')
mx = sm.node_tree.nodes.new('ShaderNodeMixShader'); mx.inputs['Fac'].default_value = 0.12
outn = sm.node_tree.nodes['Material Output']
sm.node_tree.links.new(sb.outputs['BSDF'], mx.inputs[1]); sm.node_tree.links.new(tr.outputs['BSDF'], mx.inputs[2]); sm.node_tree.links.new(mx.outputs['Shader'], outn.inputs['Surface'])
slip.data.materials.append(sm); sol = slip.modifiers.new('s', 'SOLIDIFY'); sol.thickness = 0.00012
bpy.context.view_layer.objects.active = slip; slip.select_set(True); bpy.ops.object.shade_smooth()
# --- brass bell on a wooden base
brass, _ = mat('brass', lin('C39A52'), 0.22, 1.0)
cyl(0.034, 0.01, (-0.17, 0.15, 0.005), wm)
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.03, location=(-0.17, 0.15, 0.01), segments=64, ring_count=32); bell = bpy.context.object
bell.scale = (1, 1, .82); bell.data.materials.append(brass); bpy.ops.object.shade_smooth()
cyl(0.003, 0.012, (-0.17, 0.15, 0.04), brass); cyl(0.006, 0.003, (-0.17, 0.15, 0.047), brass)
# --- room key: carved wooden fob with a brass ring and key
fob_m, _ = mat('fob', lin('6B4A2E'), .5)
k_ang = math.radians(28)
cyl(0.011, 0.07, (0.17, -0.07, 0.011), fob_m, rot=(0, math.radians(90), k_ang))
bpy.ops.mesh.primitive_torus_add(major_radius=0.012, minor_radius=0.0016, location=(0.13 - 0.00, -0.09, 0.002)); tor = bpy.context.object; tor.data.materials.append(brass)
key = box(0.045, 0.008, 0.0025, (0.10, -0.105, 0.0013), brass, 0.001); key.rotation_euler[2] = k_ang
# --- pen on a guest card
card_m, _ = mat('card', lin('EDE7DA'), .7)
cd = box(0.09, 0.055, 0.0006, (-0.12, -0.08, 0.0003), card_m, 0.0003, 1); cd.rotation_euler[2] = math.radians(-12)
pen_m, _ = mat('pen', lin('101012'), .25)
cyl(0.0045, 0.14, (-0.115, -0.075, 0.005), pen_m, rot=(0, math.radians(90), math.radians(-30)))
# --- light: warm desk lamp from the left (out of frame), cool night spill from the right doorway
def area(loc, rot, size, power, col):
    bpy.ops.object.light_add(type='AREA', location=loc, rotation=[math.radians(r) for r in rot]); l = bpy.context.object
    l.data.size = size; l.data.energy = power; l.data.color = col; return l
area((-0.42, -0.08, 0.32), (0, -52, 10), 0.14, 14, (1.0, 0.70, 0.42))
area((0.55, 0.25, 0.25), (70, 0, 115), 0.6, 4, (0.45, 0.60, 0.95))
area((0.05, 0.36, 0.30), (-60, 0, 0), 0.25, 1.4, (1.0, 0.8, 0.6))   # bounce on the wall behind the slip
w0 = bpy.data.worlds.new('w'); sc.world = w0; w0.use_nodes = True; w0.node_tree.nodes['Background'].inputs['Color'].default_value = lin('0B0D12'); w0.node_tree.nodes['Background'].inputs['Strength'].default_value = 0.4
# --- camera
bpy.ops.object.camera_add(); cam = bpy.context.object; sc.camera = cam
if CAM == 'top':
    cam.location = (0.0, 0.0, 0.62); cam.rotation_euler = (0, 0, 0); cam.data.lens = 50
else:
    cam.location = (0.16, -0.50, 0.115); cam.data.lens = 70
    tgt = mathutils.Vector((0.035, 0.03, 0.11)); d = tgt - cam.location; cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    cam.data.dof.use_dof = True; cam.data.dof.aperture_fstop = 2.8
    cam.data.dof.focus_distance = (mathutils.Vector((PX, PY - 0.03, 0.1)) - cam.location).length
sc.render.filepath = OUT; bpy.ops.render.render(write_still=True); print('Saved:', OUT)
