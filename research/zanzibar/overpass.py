# Lists every hotel, guest house and similar place on Unguja (Zanzibar) that OpenStreetMap records with its own website.
import json, urllib.request, urllib.parse, re
q = """[out:json][timeout:120];
(
  nwr["tourism"~"^(hotel|guest_house|hostel|apartment|chalet|motel)$"]["website"](-6.50,39.05,-5.70,39.60);
  nwr["tourism"~"^(hotel|guest_house|hostel|apartment|chalet|motel)$"]["contact:website"](-6.50,39.05,-5.70,39.60);
);
out tags center;"""
req = urllib.request.Request("https://overpass-api.de/api/interpreter", data=urllib.parse.urlencode({"data": q}).encode(), headers={"User-Agent": "may11leven-research/1.0"})
data = json.load(urllib.request.urlopen(req, timeout=180))
OTA = re.compile(r"(booking\.com|tripadvisor|airbnb|expedia|hotels\.com|agoda|facebook\.com|instagram\.com)", re.I)
seen, rows = set(), []
for e in data["elements"]:
    t = e.get("tags", {})
    url = (t.get("website") or t.get("contact:website") or "").strip()
    if not url or OTA.search(url): continue
    if not url.startswith("http"): url = "https://" + url
    host = urllib.parse.urlparse(url).netloc.lower().removeprefix("www.")
    if host in seen: continue
    seen.add(host)
    rows.append({"name": t.get("name", ""), "type": t.get("tourism"), "rooms": t.get("rooms"), "url": url, "host": host})
json.dump(rows, open("out/sites.json", "w"), indent=1)
print(len(rows), "sites")
