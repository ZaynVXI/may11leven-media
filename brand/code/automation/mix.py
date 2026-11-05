"""Real-sound mix for the automation reel: CC0 piano bed + CC0 room tone + CC0 uisfx 'minimal' cues + a real iPhone tap,
each placed on the frame the picture moves. Target -14 LUFS, true peak <= -1.5 dBTP (approx, 4x oversampled)."""
import numpy as np, librosa, soundfile as sf, pyloudnorm as pyln, json
SR = 48000; DUR = 14.0; N = int(SR * DUR)
U = '/home/claude/may11leven-media/brand/tools/real-sfx/vendor/node_modules/uisfx/sounds/minimal/'
def load(p, gain_db=0.0, start=0.0, length=None):
    y, _ = librosa.load(p, sr=SR, mono=True, offset=start, duration=length)
    return y * 10 ** (gain_db / 20)
mix = np.zeros(N)
def put(y, at, fade_ms=4):
    i = int(at * SR); j = min(N, i + len(y)); y = y[:j - i].copy()
    f = int(fade_ms / 1000 * SR)
    if f and len(y) > 2 * f: y[:f] *= np.linspace(0, 1, f); y[-f:] *= np.linspace(1, 0, f)
    mix[i:j] += y
# bed: CC0 ambient piano (Erokia, freesound 426750), gentle in, long tail out
bed = load('snd/snd_hakrenjazzy.mp3', -6, 0.0, DUR)
env = np.ones(len(bed)); a = int(.8 * SR); r = int(2.2 * SR)
env[:a] = np.linspace(0, 1, a); env[-r:] = np.linspace(1, 0, r) ** 1.5
put(bed * env, 0.0, 0)
# room tone: CC0 quiet office (mzui, freesound 135097), very low, for air
rt = load('snd/snd_roomtoneofficequie.mp3', -14, 5.0, DUR); put(rt * np.minimum(1, np.arange(len(rt)) / SR / .5), 0, 0)
# a real iPhone tap (figgy78, freesound 171424): one clean onset trimmed to 90 ms
tap = load('snd/snd_iphonetaps.mp3', 4, 1.546, .09)
CUES = [('send.mp3', 1.4, -4), ('receive.mp3', 3.1, -6), ('send.mp3', 5.2, -4), ('receive.mp3', 6.8, -6),
        ('purchase.mp3', 8.4, -5), ('receive.mp3', 9.4, -6)]
for f, at, g in CUES: put(load(U + f, g), at)
for at in (4.75, 8.15): put(tap, at)
# loudness to -14 LUFS, then a soft peak ceiling
meter = pyln.Meter(SR); L = meter.integrated_loudness(mix); mix *= 10 ** ((-14 - L) / 20)
up = librosa.resample(mix, orig_sr=SR, target_sr=SR * 4); tp = np.abs(up).max()
ceil = 10 ** (-1.5 / 20)
if tp > ceil:
    k = ceil / tp; mix = np.where(np.abs(mix) > ceil * .7, np.sign(mix) * (ceil * .7 + np.tanh((np.abs(mix) - ceil * .7) / (ceil * .3)) * ceil * .3), mix)
    mix = mix * min(1, ceil / np.abs(librosa.resample(mix, orig_sr=SR, target_sr=SR * 4)).max())
st = np.stack([mix, mix], 1)
sf.write('real_mix.wav', st, SR, subtype='PCM_24')
print(json.dumps({'lufs': round(meter.integrated_loudness(mix), 2), 'tp_dbfs': round(20 * np.log10(np.abs(librosa.resample(mix, orig_sr=SR, target_sr=SR * 4)).max()), 2)}))
