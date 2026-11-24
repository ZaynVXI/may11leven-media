"""Real-sound mix for the Try to break it No. 01 reel (v2). All CC0 recordings (credits in CREDITS.md):
ambient piano loop (85 bpm) + evening ocean waves as the bed, a real Epson receipt printer, rubber-stamp hits,
phone taps and a paper tear, each placed on the frame the picture moves. Target -14 LUFS, true peak <= -1.5 dBTP."""
import numpy as np, soundfile as sf, pyloudnorm as pyln
from scipy.signal import resample_poly
S = "/home/claude/sfx/"; SR = 48000; DUR = 31.0; N = int(SR * DUR)
def ld(n): y, sr = sf.read(S + n + ".wav"); return y if y.ndim == 1 else y.mean(1)
def seg(y, a, b): return y[int(a * SR):int(b * SR)].copy()
mix = np.zeros(N)
def put(y, at, db=0.0, fade=.004):
    y = y * 10 ** (db / 20); f = int(fade * SR)
    if len(y) > 2 * f: y[:f] *= np.linspace(0, 1, f); y[-f:] *= np.linspace(1, 0, f)
    i = int(at * SR); j = min(N, i + len(y)); mix[i:j] += y[:j - i]
# bed: piano loop repeated, sea underneath; both duck slightly under the cues
pia = ld("snd_ambientpianoloop85"); bed = np.tile(pia, int(np.ceil(N / len(pia))) + 1)[:N]
sea = ld("sfx_waves"); sea = seg(sea, 30, 30 + DUR)
env = np.ones(N); env[:int(.6 * SR)] = np.linspace(0, 1, int(.6 * SR)); env[-int(1.2 * SR):] = np.linspace(1, .0, int(1.2 * SR))
mix += bed * env * 10 ** (-17 / 20)
seaenv = np.ones(N) * 10 ** (-21 / 20); a, b = int(19.4 * SR), int(23.0 * SR); seaenv[a:b] = 10 ** (-13 / 20)   # the roof: the sea comes up
mix += sea[:N] * seaenv
typ = ld("sfx_typing"); taps = [seg(typ, o - .01, o + .09) for o in (0.06, 0.36, 0.6, 0.81, 1.74, 2.01)]
prn = ld("sfx_printer"); stp = ld("sfx_stamp2"); stamps = [seg(stp, o - .02, o + .55) for o in (0.23, 3.3, 6.19, 9.16)]
tear = ld("sfx_tear")
# A: the guest's message lands
put(taps[0], .38, -6)
# B: the printer prints the audit slip
put(seg(prn, .15, 3.4), 2.62, -4, fade=.03)
# C: bubbles land, then the refusal is stamped
put(taps[1], 5.62, -8); put(taps[2], 6.17, -8); put(stamps[0], 7.22, -2)
# D: the trace (one soft tap as the panel settles)
put(taps[3], 9.05, -10)
# E: four slips, four stamps on the beat (85 bpm ~ 0.706 s)
for k in range(4): put(stamps[k], 12.75 + k * .706, -4 - k)
# F: fake proof
put(taps[4], 15.82, -8); put(taps[5], 16.27, -9); put(taps[0], 17.02, -8); put(stamps[1], 18.02, -5)
# H: three decisions, three paper tears
for k in range(3): put(tear, 22.82 + k * 1.2, -6)
# I: the question, one last stamp under the ask
put(stamps[2], 27.62, -7)
# loudness to -14 LUFS, then a true-peak guard at -1.5 dBTP (4x oversampled)
meter = pyln.Meter(SR); st = np.stack([mix, mix], 1); mix = mix * 10 ** ((-14.0 - meter.integrated_loudness(st)) / 20)
tp = np.abs(resample_poly(mix, 4, 1)).max(); lim = 10 ** (-1.5 / 20)
if tp > lim: mix *= lim / tp
print("LUFS", round(meter.integrated_loudness(np.stack([mix, mix], 1)), 2), "TP dBTP", round(20 * np.log10(np.abs(resample_poly(mix, 4, 1)).max()), 2))
sf.write("/home/claude/may11leven-media/posts/try-to-break-it/01/v2/reel_sound.wav", np.stack([mix, mix], 1), SR)
