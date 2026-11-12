#!/usr/bin/env bash
# Lighthouse mobile performance (simulated mid-range phone on slow 4G) for each reachable site.
mkdir -p out/lh
python3 -c "import json;[print(r['host'],r['finalUrl']) for r in json.load(open('out/audit.json')) if not r.get('error')]" | while read -r host url; do
  timeout 120 npx -y lighthouse@12 "$url" --only-categories=performance,accessibility --form-factor=mobile \
    --output=json --output-path="out/lh/${host//[^a-zA-Z0-9.-]/_}.json" --quiet --chrome-flags="--headless=new --no-sandbox" || echo "lh failed $host"
done
