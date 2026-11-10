"""May11Leven merch: business card in a brushed steel case on linen (Blender, Cycles).
usage: python3 cardcase.py card_texture.png out.png W H SAMPLES [linen_hex]"""
import bpy, sys, math
a = sys.argv[1:]
cardtex, out, W, H, SAMP = a[0], a[1], int(a[2]), int(a[3]), int(a[4])
LIN = a[5] if len(a) > 5 else '1E1D20'
def lin(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c] + [1]
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; sc.render.engine = 'CYCLES'; sc.cycles.samples = SAMP; sc.cycles.use_denoising = True
sc.render.resolution_x, sc.render.resolution_y = W, H; sc.view_settings.view_transform = 'AgX'; sc.view_settings.exposure = 0.6; sc.view_settings.look = 'AgX - Base Contrast'
def mat(name, base, rough, metal=0.0):
    m = bpy.data.materials.new(name); m.use_nodes = True; b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = base; b.inputs['Roughness'].default_value = rough; b.inputs['Metallic'].default_value = metal
    return m, b
# linen table
bpy.ops.mesh.primitive_plane_add(size=1.2); t = bpy.context.object
lm, lb = mat('linen', lin(LIN), 0.9); lb.inputs['Sheen Weight'].default_value = 0.5
N = lm.node_tree.nodes; L = lm.node_tree.links
tc = N.new('ShaderNodeTexCoord'); mp = N.new('ShaderNodeMapping'); mp.inputs['Scale'].default_value = (260, 260, 1)
wx = N.new('ShaderNodeTexWave'); wx.bands_direction = 'X'; wx.inputs['Distortion'].default_value = 3; wx.inputs['Detail'].default_value = 3
wy = N.new('ShaderNodeTexWave'); wy.bands_direction = 'Y'; wy.inputs['Distortion'].default_value = 3; wy.inputs['Detail'].default_value = 3
mx = N.new('ShaderNodeMath'); mx.operation = 'MAXIMUM'
bu = N.new('ShaderNodeBump'); bu.inputs['Strength'].default_value = 0.35; bu.inputs['Distance'].default_value = 0.0005
for x in (wx, wy): L.new(mp.outputs['Vector'], x.inputs['Vector'])
L.new(tc.outputs['UV'], mp.inputs['Vector']); L.new(wx.outputs['Fac'], mx.inputs[0]); L.new(wy.outputs['Fac'], mx.inputs[1])
L.new(mx.outputs[0], bu.inputs['Height']); L.new(bu.outputs['Normal'], lb.inputs['Normal']); t.data.materials.append(lm)
# steel case (open): base tray + lid hinged up
steel, sb = mat('steel', lin('C9CACC'), 0.22, 1.0)
an = steel.node_tree.nodes.new('ShaderNodeTexNoise'); an.inputs['Scale'].default_value = 3; an.inputs['Detail'].default_value = 15
mpp = steel.node_tree.nodes.new('ShaderNodeMapping'); mpp.inputs['Scale'].default_value = (1, 400, 1)
tcc = steel.node_tree.nodes.new('ShaderNodeTexCoord')
rr = steel.node_tree.nodes.new('ShaderNodeMapRange'); rr.inputs['To Min'].default_value = 0.16; rr.inputs['To Max'].default_value = 0.30
steel.node_tree.links.new(tcc.outputs['Object'], mpp.inputs['Vector']); steel.node_tree.links.new(mpp.outputs['Vector'], an.inputs['Vector'])
steel.node_tree.links.new(an.outputs['Fac'], rr.inputs['Value']); steel.node_tree.links.new(rr.outputs['Result'], sb.inputs['Roughness'])
def box(sx, sy, sz, loc, m, bev=0.0012):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc); o = bpy.context.object; o.scale = (sx, sy, sz); bpy.ops.object.transform_apply(scale=True)
    b = o.modifiers.new('b', 'BEVEL'); b.width = bev; b.segments = 3; o.data.materials.append(m); return o
CW, CH = 0.064, 0.098   # case outer (portrait)
tray = box(CW, CH, 0.004, (0, -0.012, 0.002), steel)
for sx in (-1,1): box(0.0035, CH-0.004, 0.0038, (sx*(CW/2-0.0017), -0.012, 0.0045), steel, 0.0008)
box(CW, 0.0035, 0.0038, (0, -0.012-CH/2+0.0017, 0.0045), steel, 0.0008)
# card (85x55 portrait) sitting in tray, top part showing
cm, cb = mat('card', (1, 1, 1, 1), 0.85)
img = cm.node_tree.nodes.new('ShaderNodeTexImage'); img.image = bpy.data.images.load(cardtex)
cm.node_tree.links.new(img.outputs['Color'], cb.inputs['Base Color'])
bpy.ops.mesh.primitive_plane_add(size=1, location=(0, -0.014, 0.0043)); card = bpy.context.object; card.scale = (0.055, 0.085, 1)
bpy.ops.object.transform_apply(scale=True); card.data.materials.append(cm)
bpy.ops.object.mode_set(mode='EDIT'); bpy.ops.uv.reset(); bpy.ops.object.mode_set(mode='OBJECT')
# lid: hinged at top edge of the tray's lower third, opened back flat-ish
lid = box(CW, CH * 0.62, 0.0018, (0, 0, 0), steel)
lid.location = (0, -0.012 + CH / 2 - CH * 0.62 / 2 + 0.002, 0.0045)
# make lid cover only the top part: shift it up, it rests flat (closed over the top part)
# open state: lid sits flat beyond the tray top, like a flipped-open case
lid.location = (0, -0.012 + CH / 2 + CH * 0.62 / 2 - 0.006, 0.006); lid.rotation_euler[0] = math.radians(-9)
# light: soft window from the top right, gentle fill
bpy.ops.object.light_add(type='AREA', location=(0.35, 0.4, 0.5)); k = bpy.context.object; k.data.energy = 3.0; k.data.size = 0.7
k.rotation_euler = (math.radians(-40), math.radians(30), 0)
bpy.ops.object.light_add(type='AREA', location=(-0.3, -0.35, 0.4)); f = bpy.context.object; f.data.energy = 0.4; f.data.size = 1.0
f.rotation_euler = (math.radians(40), math.radians(-30), 0)
w0 = bpy.data.worlds.new('w'); sc.world = w0; w0.use_nodes = True; w0.node_tree.nodes['Background'].inputs['Strength'].default_value = 0.03
bpy.ops.object.camera_add(location=(0.0, -0.075, 0.30), rotation=(math.radians(14), 0, math.radians(-8))); cam = bpy.context.object
cam.data.lens = 55; sc.camera = cam
for o in [x for x in bpy.data.objects if x.type=='MESH' and x is not t]: o.rotation_euler[2] += math.radians(-8)
sc.render.filepath = out; bpy.ops.render.render(write_still=True); print('Saved:', out)
