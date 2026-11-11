from fontTools.ttLib import TTFont
from fontTools.pens.recordingPen import RecordingPen
import json, sys
f = TTFont(str(__import__('pathlib').Path(__file__).resolve().parents[2]/'brand/fonts/InterTight-Medium.ttf'))
gs = f.getGlyphSet(); cmap = f.getBestCmap()
upm = f['head'].unitsPerEm; os2 = f['OS/2']
p = RecordingPen(); gs[cmap[ord('a')]].draw(p)
json.dump({'upm': upm, 'xh': os2.sxHeight, 'cap': os2.sCapHeight, 'asc': f['hhea'].ascent, 'desc': f['hhea'].descent,
           'adv': gs[cmap[ord('a')]].width, 'ops': p.value}, open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'a.json'), 'w'))
print(upm, os2.sxHeight, os2.sCapHeight, len(p.value))
