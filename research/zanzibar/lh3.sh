#!/usr/bin/env bash
# Three Lighthouse mobile runs per final site; the analysis uses the median.
mkdir -p out/lh3
while read -r host url; do
  for i in 1 2 3; do
    timeout 150 npx -y lighthouse@12 "$url" --only-categories=performance,accessibility --form-factor=mobile \
      --output=json --output-path="out/lh3/${host}-${i}.json" --quiet --chrome-flags="--headless=new --no-sandbox" || echo "lh failed $host $i"
  done
done < final_sites.txt
