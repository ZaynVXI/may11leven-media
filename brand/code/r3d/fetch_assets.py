"""Pull free CC0 Poly Haven assets into ASSETS through the media repo's GitHub download bridge.
usage: python3 fetch_assets.py REPO_DIR ASSETS_DIR model:magnifying_glass_01 hdri:brown_photostudio_02 tex:american_walnut_veneer ...
Two passes: (1) fetch each asset's file list from api.polyhaven.com, (2) fetch the 2k files. Cleans fetch/ after."""
import sys, os, json, time, shutil, subprocess
REPO, ASSETS, items = sys.argv[1], sys.argv[2], sys.argv[3:]
ATTR = "\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_019pcNfRHGxsRYW5k4Gc3WRr"
def git(*a): return subprocess.run(["git", "-C", REPO, *a], capture_output=True, text=True)
def bridge(lines, expect):
    os.makedirs(f"{REPO}/fetch", exist_ok=True); open(f"{REPO}/fetch/urls.txt", "w").write("\n".join(lines) + "\n")
    git("pull", "-q", "origin", "study-digest"); git("add", "fetch/urls.txt"); git("commit", "-qm", "fetch assets" + ATTR)
    for _ in range(3):
        if git("push", "-q", "origin", "study-digest").returncode == 0: break
    for _ in range(60):
        time.sleep(5); git("pull", "-q", "origin", "study-digest")
        if all(os.path.exists(f"{REPO}/fetch/out/{n}") for n in expect): return
    raise SystemExit("bridge timed out")
kinds = [i.split(":", 1) for i in items]
bridge([f"f_{n}.json https://api.polyhaven.com/files/{n}" for _, n in kinds], [f"f_{n}.json" for _, n in kinds])
lines, man = [], {}
def add(rel, url): n = rel.replace("/", "__"); lines.append(f"{n} {url}"); man[n] = rel
for k, n in kinds:
    d = json.load(open(f"{REPO}/fetch/out/f_{n}.json"))
    if k == "model":
        g = d["gltf"]["2k"]["gltf"]; add(f"models/{n}/{n}.gltf", g["url"])
        for r, v in g["include"].items(): add(f"models/{n}/{r}", v["url"])
    elif k == "hdri": add(f"hdri/{n}.hdr", d["hdri"]["2k"]["hdr"]["url"])
    elif k == "tex":
        for t in ("Diffuse", "nor_gl", "Rough"): add(f"tex/{n}/{n}_{t}.jpg", d[t]["2k"]["jpg"]["url"])
bridge(lines, list(man))
for n, rel in man.items():
    p = f"{ASSETS}/{rel}"; os.makedirs(os.path.dirname(p), exist_ok=True); shutil.copy(f"{REPO}/fetch/out/{n}", p)
mine=[f"fetch/out/{n}" for n in man]+[f"fetch/out/f_{n}.json" for _, n in kinds]
git("rm", "-q", *mine); git("commit", "-qm", "clear fetched asset files" + ATTR); git("push", "-q", "origin", "study-digest")
print("assets ready:", len(man), "files in", ASSETS)
