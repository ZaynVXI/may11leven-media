"""May11Leven merch: back-neck embroidery close-up on a heavyweight knit (Blender, Cycles).
usage: python3 embroidery.py out.png W H SAMPLES [fabric_hex] [thread_hex]"""
import bpy, sys, math
a = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else sys.argv[1:]
out, W, H, SAMP = a[0], int(a[1]), int(a[2]), int(a[3])
FAB = a[4] if len(a) > 4 else '1C1B1D'
THR = a[5] if len(a) > 5 else 'FF4A1C'
def lin(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c] + [1]
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; sc.render.engine = 'CYCLES'; sc.cycles.samples = SAMP; sc.cycles.use_denoising = True
sc.render.resolution_x, sc.render.resolution_y = W, H; sc.view_settings.view_transform = 'AgX'; sc.view_settings.look = 'AgX - Base Contrast'
sc.view_settings.exposure = 0.7
# --- fabric: subdivided plane with gentle folds + knit bump
bpy.ops.mesh.primitive_plane_add(size=0.6); fab = bpy.context.object
bpy.ops.object.modifier_add(type='SUBSURF'); fab.modifiers[0].levels = 5; fab.modifiers[0].render_levels = 6; fab.modifiers[0].subdivision_type = 'SIMPLE'
tex = bpy.data.textures.new('folds', 'CLOUDS'); tex.noise_scale = 0.22
d = fab.modifiers.new('fold', 'DISPLACE'); d.texture = tex; d.strength = 0.02
m = bpy.data.materials.new('knit'); m.use_nodes = True; nt = m.node_tree; N = nt.nodes; L = nt.links
bs = N['Principled BSDF']; bs.inputs['Base Color'].default_value = lin(FAB); bs.inputs['Roughness'].default_value = 0.92
bs.inputs['Sheen Weight'].default_value = 0.6; bs.inputs['Sheen Roughness'].default_value = 0.5; bs.inputs['Sheen Tint'].default_value = (0.6, 0.6, 0.6, 1)
tc = N.new('ShaderNodeTexCoord'); mp = N.new('ShaderNodeMapping'); mp.inputs['Scale'].default_value = (420, 300, 1)
w = N.new('ShaderNodeTexWave'); w.wave_type = 'BANDS'; w.bands_direction = 'X'; w.inputs['Distortion'].default_value = 1.2; w.inputs['Detail'].default_value = 2
w2 = N.new('ShaderNodeTexWave'); w2.wave_type = 'BANDS'; w2.bands_direction = 'Y'; w2.inputs['Scale'].default_value = 1.4
nz = N.new('ShaderNodeTexNoise'); nz.inputs['Scale'].default_value = 900; nz.inputs['Detail'].default_value = 4
mx = N.new('ShaderNodeMath'); mx.operation = 'MULTIPLY'
mx2 = N.new('ShaderNodeMix'); mx2.data_type = 'FLOAT'; mx2.inputs[0].default_value = 0.25
bump = N.new('ShaderNodeBump'); bump.inputs['Strength'].default_value = 0.9; bump.inputs['Distance'].default_value = 0.0006
L.new(tc.outputs['UV'], mp.inputs['Vector']); L.new(mp.outputs['Vector'], w.inputs['Vector']); L.new(mp.outputs['Vector'], w2.inputs['Vector'])
L.new(w.outputs['Fac'], mx.inputs[0]); L.new(w2.outputs['Fac'], mx.inputs[1])
L.new(mx.outputs[0], mx2.inputs[2]); L.new(nz.outputs['Fac'], mx2.inputs[3]); L.new(mx2.outputs[0], bump.inputs['Height'])
L.new(bump.outputs['Normal'], bs.inputs['Normal'])
# colour variation (dye mottling)
nz2 = N.new('ShaderNodeTexNoise'); nz2.inputs['Scale'].default_value = 6
ramp = N.new('ShaderNodeMix'); ramp.data_type = 'RGBA'; ramp.inputs['Factor'].default_value = 0.0
hsv = N.new('ShaderNodeHueSaturation'); hsv.inputs['Value'].default_value = 1.0
L.new(nz2.outputs['Fac'], hsv.inputs['Fac'])
fab.data.materials.append(m)
# --- embroidery: two offset bars (the 11 mark), satin stitch along the long axis
def bar(x, y, w, h, name):
    bpy.ops.mesh.primitive_cube_add(size=1); o = bpy.context.object; o.name = name
    o.scale = (w / 2, h / 2, 0.0011); o.location = (x, y, 0.0016 + 0.012 * 0)
    bpy.ops.object.transform_apply(scale=True)
    bv = o.modifiers.new('bev', 'BEVEL'); bv.width = 0.0010; bv.segments = 4
    sb = o.modifiers.new('sub', 'SUBSURF'); sb.levels = 2; sb.render_levels = 3
    return o
u = 0.0082  # logo ratios: bar 41, gap 29, height 181, offset 30
b1 = bar(-0.0070, 0.0030, u, 0.036, 'bar1'); b2 = bar(0.0070, -0.0030, u, 0.036, 'bar2')
th = bpy.data.materials.new('thread'); th.use_nodes = True; tn = th.node_tree; TN = tn.nodes; TL = tn.links
tb = TN['Principled BSDF']; tb.inputs['Base Color'].default_value = lin(THR); tb.inputs['Roughness'].default_value = 0.42
tb.inputs['Sheen Weight'].default_value = 0.8; tb.inputs['Sheen Tint'].default_value = (1, 1, 1, 1); tb.inputs['Specular IOR Level'].default_value = 0.6
ttc = TN.new('ShaderNodeTexCoord'); tw = TN.new('ShaderNodeTexWave'); tw.wave_type = 'BANDS'; tw.bands_direction = 'Y'
tw.inputs['Scale'].default_value = 900; tw.inputs['Distortion'].default_value = 0.4; tw.inputs['Detail Scale'].default_value = 3
tbu = TN.new('ShaderNodeBump'); tbu.inputs['Strength'].default_value = 0.8; tbu.inputs['Distance'].default_value = 0.0004
TL.new(ttc.outputs['Object'], tw.inputs['Vector']); TL.new(tw.outputs['Fac'], tbu.inputs['Height']); TL.new(tbu.outputs['Normal'], tb.inputs['Normal'])
for o in (b1, b2):
    o.data.materials.append(th)
    o.rotation_euler[2] = math.radians(0)
# satin stitches run across the bar: rotate the wave by bars direction X
tw.bands_direction = 'X'

# --- ribbed collar band across the top of the frame
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.053, 0.0045)); col = bpy.context.object
col.scale = (0.5, 0.028, 0.003); bpy.ops.object.transform_apply(scale=True)
cb = col.modifiers.new('b', 'BEVEL'); cb.width = 0.002; cb.segments = 4
rm = bpy.data.materials.new('rib'); rm.use_nodes = True; rn = rm.node_tree; rb = rn.nodes['Principled BSDF']
rb.inputs['Base Color'].default_value = lin(FAB); rb.inputs['Roughness'].default_value = 0.9; rb.inputs['Sheen Weight'].default_value = 0.6
rw = rn.nodes.new('ShaderNodeTexWave'); rw.bands_direction = 'X'; rw.inputs['Scale'].default_value = 300; rw.inputs['Distortion'].default_value = 0.3
rbu = rn.nodes.new('ShaderNodeBump'); rbu.inputs['Strength'].default_value = 1.0; rbu.inputs['Distance'].default_value = 0.001
rtc = rn.nodes.new('ShaderNodeTexCoord'); rn.links.new(rtc.outputs['Object'], rw.inputs['Vector']); rn.links.new(rw.outputs['Fac'], rbu.inputs['Height']); rn.links.new(rbu.outputs['Normal'], rb.inputs['Normal'])
col.data.materials.append(rm)
# --- light: big soft window key from upper left, faint fill
bpy.ops.object.light_add(type='AREA', location=(-0.35, 0.45, 0.55)); k = bpy.context.object; k.data.energy = 4.5; k.data.size = 0.5
k.rotation_euler = (math.radians(-38), math.radians(-28), 0)
bpy.ops.object.light_add(type='AREA', location=(0.4, -0.3, 0.4)); f = bpy.context.object; f.data.energy = 0.6; f.data.size = 0.8
f.rotation_euler = (math.radians(35), math.radians(30), 0)
w0 = bpy.data.worlds.new('w'); sc.world = w0; w0.use_nodes = True; w0.node_tree.nodes['Background'].inputs['Strength'].default_value = 0.02
# --- camera: straight down, slight tilt, 50mm-ish tight crop
bpy.ops.object.camera_add(location=(0, -0.02, 0.19), rotation=(math.radians(6), 0, 0)); cam = bpy.context.object
cam.data.lens = 70; cam.data.dof.use_dof = True; cam.data.dof.focus_distance = 0.19; cam.data.dof.aperture_fstop = 4.0
sc.camera = cam
sc.render.filepath = out; bpy.ops.render.render(write_still=True); print('Saved:', out)
