# r3d: realism helpers for our Blender scenes

- **`real.py`:** HDRI world, scanned PBR materials, CC0 glTF models, gobo, camera, render and photographic finish. Our own code, first published in the May11Leven Content Kit artifact.
- **`fetch_assets.py`:** pulls CC0 Poly Haven assets (textures, models, HDRIs) through the repo's GitHub download bridge into `$ASSETS` (default `/home/claude/assets`). It pushes only to `study-digest` and removes only the files it fetched.

Example:

`python3 brand/code/r3d/fetch_assets.py . /home/claude/assets tex:black_walnut_veneer_01 tex:coral_stone_wall hdri:courtyard_night hdri:brown_photostudio_02`

Scripts load the helper relative to the repo, so they run from a fresh checkout once the assets are fetched.
