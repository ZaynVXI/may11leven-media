# Graph Report - code  (2026-11-05)

## Corpus Check
- 40 files · ~11,895 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 224 nodes · 441 edges · 15 communities (9 shown, 6 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 35 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `dd961e1b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- mm.py
- numpy
- sys
- boxes.py
- type2.py
- phone3d.py
- compose.py
- bathu2/slides.py
- pil
- run.py
- webaudit.js
- README.md
- run.sh
- gimp.sh script

## God Nodes (most connected - your core abstractions)
1. `mono()` - 13 edges
2. `outline()` - 10 edges
3. `head()` - 10 edges
4. `rich()` - 9 edges
5. `tt()` - 8 edges
6. `lum()` - 7 edges
7. `_check_fill()` - 7 edges
8. `top()` - 7 edges
9. `segC()` - 7 edges
10. `list_card()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `labels()` --calls--> `mono()`  [INFERRED]
  bathu2/slides.py → v3/mm.py
- `labels()` --calls--> `mono()`  [INFERRED]
  imz/slides.py → v3/mm.py
- `save()` --calls--> `grain()`  [INFERRED]
  bathu2/slides.py → v3/mm.py
- `save()` --calls--> `grain()`  [INFERRED]
  imz/slides.py → v3/mm.py
- `frame()` --indirect_call--> `mono()`  [INFERRED]
  practice/reel_opacity.py → v3/mm.py

## Import Cycles
- None detected.

## Communities (15 total, 6 thin omitted)

### Community 0 - "mm.py"
Cohesion: 0.13
Nodes (25): ease(), segA(), segB(), segC(), segD(), segE(), top(), zoom() (+17 more)

### Community 1 - "numpy"
Cohesion: 0.11
Nodes (17): _check_fill(), rr(), _lin(), lum(), _mix(), patch_mm(), tt(), ratio() (+9 more)

### Community 2 - "sys"
Cohesion: 0.10
Nodes (11): save(), main(), num(), q(), step(), labels(), save(), save() (+3 more)

### Community 3 - "boxes.py"
Cohesion: 0.12
Nodes (12): lathe(), cube(), decal(), mat_decal(), mat_paper(), shoebox(), srgb(), rubber() (+4 more)

### Community 4 - "type2.py"
Cohesion: 0.28
Nodes (14): close_card(), corners2(), list_card(), photo_slide(), font(), label(), mark(), MONO() (+6 more)

### Community 5 - "phone3d.py"
Cohesion: 0.15
Nodes (5): _dump(), load(), put(), img(), mat()

### Community 6 - "compose.py"
Cohesion: 0.17
Nodes (8): ez(), text_layer(), put(), ttf(), ez(), text_layer(), put(), ttf()

### Community 7 - "bathu2/slides.py"
Cohesion: 0.21
Nodes (7): lid(), mark(), labels(), sole_poly(), chaikin(), outline(), tread()

### Community 8 - "pil"
Cohesion: 0.18
Nodes (4): polys(), ring(), grid(), thumb()

## Knowledge Gaps
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `grain()` connect `sys` to `mm.py`, `numpy`?**
  _High betweenness centrality (0.017) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `mono()` (e.g. with `segC()` and `segE()`) actually correct?**
  _`mono()` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Should `mm.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13086770981507823 - nodes in this community are weakly interconnected._
- **Why does `mono()` connect `mm.py` to `numpy`, `sys`, `bathu2/slides.py`?**
  _High betweenness centrality (0.012) - this node is a cross-community bridge._
- **Should `numpy` be split into smaller, more focused modules?**
  _Cohesion score 0.11494252873563218 - nodes in this community are weakly interconnected._
- **Should `sys` be split into smaller, more focused modules?**
  _Cohesion score 0.09523809523809523 - nodes in this community are weakly interconnected._
- **Should `boxes.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1168091168091168 - nodes in this community are weakly interconnected._