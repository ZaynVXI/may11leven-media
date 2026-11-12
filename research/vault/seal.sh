#!/usr/bin/env bash
# Encrypts a results folder so it can be committed to this public repo safely: only the studio's private key can open it.
# usage: seal.sh <dir> <name>
set -e
dir="$1"; name="$2"; here="$(cd "$(dirname "$0")" && pwd)"
key=$(openssl rand -hex 32)
tar czf - -C "$dir" . | openssl enc -aes-256-cbc -pbkdf2 -salt -pass "pass:$key" -out "$here/$name.tgz.enc"
printf '%s' "$key" | openssl pkeyutl -encrypt -pubin -inkey "$here/pub.pem" -pkeyopt rsa_padding_mode:oaep -out "$here/$name.key.enc"
