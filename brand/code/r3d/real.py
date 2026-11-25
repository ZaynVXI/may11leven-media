"""Realism helpers for May11Leven Blender scenes: HDRI light, scanned PBR materials, CC0 models,
leaf-shadow gobo, filmic camera. Assets from Poly Haven (CC0), fetched through the GitHub bridge into ASSETS."""
import os, math, bpy
from mathutils import Vector
ASSETS = os.environ.get("ASSETS", "/home/claude/assets")

def reset():
    bpy.ops.wm.read_factory_settings(use_empty=True); return bpy.context.scene

def lin(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return tuple((x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4) for x in c) + (1,)

def world_hdri(name, strength=1.0, rot=0.0, bg=None):
    sc = bpy.context.scene; w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True; nt = w.node_tree
    bgn = nt.nodes["Background"]; env = nt.nodes.new("ShaderNodeTexEnvironment")
    env.image = bpy.data.images.load(f"{ASSETS}/hdri/{name}.hdr")
    mp = nt.nodes.new("ShaderNodeMapping"); tc = nt.nodes.new("ShaderNodeTexCoord")
    mp.inputs["Rotation"].default_value[2] = math.radians(rot)
    nt.links.new(tc.outputs["Generated"], mp.inputs["Vector"]); nt.links.new(mp.outputs["Vector"], env.inputs["Vector"])
    nt.links.new(env.outputs["Color"], bgn.inputs["Color"]); bgn.inputs["Strength"].default_value = strength
    if bg is not None:  # light with the HDRI, but show a plain colour to the camera
        lp = nt.nodes.new("ShaderNodeLightPath"); mix = nt.nodes.new("ShaderNodeMixShader")
        b2 = nt.nodes.new("ShaderNodeBackground"); b2.inputs["Color"].default_value = lin(bg)
        out = nt.nodes["World Output"]
        nt.links.new(bgn.outputs[0], mix.inputs[1]); nt.links.new(b2.outputs[0], mix.inputs[2])
        nt.links.new(lp.outputs["Is Camera Ray"], mix.inputs["Fac"]); nt.links.new(mix.outputs[0], out.inputs["Surface"])

def pbr(name, scale=1.0, tint=None, rough_mul=1.0):
    """Scanned texture set: tex/<name>/<name>_{Diffuse,nor_gl,Rough}.jpg"""
    m = bpy.data.materials.new(name); m.use_nodes = True; nt = m.node_tree; p = nt.nodes["Principled BSDF"]
    tc = nt.nodes.new("ShaderNodeTexCoord"); mp = nt.nodes.new("ShaderNodeMapping")
    mp.inputs["Scale"].default_value = (scale, scale, scale); nt.links.new(tc.outputs["UV"], mp.inputs["Vector"])
    def tex(kind, cs):
        t = nt.nodes.new("ShaderNodeTexImage"); t.image = bpy.data.images.load(f"{ASSETS}/tex/{name}/{name}_{kind}.jpg")
        t.image.colorspace_settings.name = cs; nt.links.new(mp.outputs["Vector"], t.inputs["Vector"]); return t
    d = tex("Diffuse", "sRGB")
    if tint:
        mx = nt.nodes.new("ShaderNodeMix"); mx.data_type = "RGBA"; mx.blend_type = "MULTIPLY"; mx.inputs["Factor"].default_value = 1
        nt.links.new(d.outputs["Color"], mx.inputs[6]); mx.inputs[7].default_value = lin(tint)
        nt.links.new(mx.outputs[2], p.inputs["Base Color"])
    else: nt.links.new(d.outputs["Color"], p.inputs["Base Color"])
    r = tex("Rough", "Non-Color"); mm = nt.nodes.new("ShaderNodeMath"); mm.operation = "MULTIPLY"; mm.inputs[1].default_value = rough_mul
    nt.links.new(r.outputs["Color"], mm.inputs[0]); nt.links.new(mm.outputs[0], p.inputs["Roughness"])
    n = tex("nor_gl", "Non-Color"); nm = nt.nodes.new("ShaderNodeNormalMap")
    nt.links.new(n.outputs["Color"], nm.inputs["Color"]); nt.links.new(nm.outputs["Normal"], p.inputs["Normal"])
    return m

def model(name, loc=(0, 0, 0), rot=(0, 0, 0), scale=1.0, keep=None):
    """Import a CC0 glTF model; returns a parent empty. keep: substring filter on object names."""
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=f"{ASSETS}/models/{name}/{name}.gltf")
    new = [o for o in bpy.data.objects if o not in before]
    root = bpy.data.objects.new(name + "_root", None); bpy.context.scene.collection.objects.link(root)
    for o in new:
        if keep and o.type == "MESH" and not any(k in o.name for k in keep):
            bpy.data.objects.remove(o); continue
        if o.parent is None: o.parent = root
    root.location = loc; root.rotation_euler = [math.radians(a) for a in rot]; root.scale = (scale,) * 3
    return root

def leaf_gobo(target=(0, 0, 0), dist=1.2, elev=38, azim=-60, scale=1.0):
    """A real plant model hidden from camera, between a hard sun and the set: soft leaf shadows."""
    t = Vector(target); d = math.radians(azim); e = math.radians(elev)
    dirv = Vector((math.cos(e) * math.cos(d), math.cos(e) * math.sin(d), math.sin(e)))
    root = model("potted_plant_02", loc=t + dirv * dist - Vector((0, 0, .45 * scale)), scale=scale, keep=["leaves"])
    for o in root.children: o.visible_camera = False; o.visible_glossy = False
    return dirv

def sun(dirv, energy=4.0, angle=2.0, color=(1, .9, .78)):
    s = bpy.data.lights.new("sun", "SUN"); s.energy = energy; s.angle = math.radians(angle); s.color = color
    o = bpy.data.objects.new("sun", s); bpy.context.scene.collection.objects.link(o)
    o.rotation_euler = (-dirv).to_track_quat("-Z", "Y").to_euler(); return o

def area(loc, target=(0, 0, 0), size=1.0, energy=20, color=(1, 1, 1)):
    l = bpy.data.lights.new("a", "AREA"); l.size = size; l.energy = energy; l.color = color
    o = bpy.data.objects.new("a", l); bpy.context.scene.collection.objects.link(o); o.location = loc
    o.rotation_euler = (Vector(target) - o.location).to_track_quat("-Z", "Y").to_euler(); return o

def camera(loc, target, lens=50, fstop=2.8, focus=None):
    sc = bpy.context.scene; cam = bpy.data.cameras.new("cam"); cam.lens = lens
    co = bpy.data.objects.new("cam", cam); sc.collection.objects.link(co); sc.camera = co
    co.location = loc; co.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()
    cam.dof.use_dof = True; cam.dof.aperture_fstop = fstop
    cam.dof.focus_distance = (Vector(focus or target) - Vector(loc)).length; return co

def render(out, w, h, samples=96):
    sc = bpy.context.scene; sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"
    sc.cycles.samples = samples; sc.cycles.use_denoising = True
    sc.render.resolution_x, sc.render.resolution_y = w, h
    sc.view_settings.view_transform = "AgX"; sc.view_settings.look = "AgX - Medium High Contrast"
    sc.render.filepath = out; bpy.ops.render.render(write_still=True); print("done", out)

def finish(path, grain=0.018, vignette=0.22, warm=0.0):
    """Photographic finish: fine film grain, soft vignette, slight warmth."""
    import numpy as np
    from PIL import Image
    im = np.asarray(Image.open(path).convert("RGB")).astype(np.float32) / 255
    h, w, _ = im.shape; y, x = np.mgrid[0:h, 0:w]
    r = np.sqrt(((x - w / 2) / (w / 2)) ** 2 + ((y - h / 2) / (h / 2)) ** 2)
    im *= (1 - vignette * np.clip(r - .35, 0, 1) ** 1.6)[..., None]
    if warm: im[..., 0] *= 1 + warm; im[..., 2] *= 1 - warm
    im += np.random.default_rng(3).normal(0, grain, (h, w, 1))
    Image.fromarray((np.clip(im, 0, 1) * 255).astype(np.uint8)).save(path)
