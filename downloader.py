import os
import time

import requests

FILES = {
    "geoip.dat": "https://github.com/v2fly/geoip/releases/latest/download/geoip.dat",
    "geosite.dat": "https://github.com/v2fly/domain-list-community/releases/latest/download/dlc.dat",
}

DEST_DIR = "/opt/geofiles"

os.makedirs(DEST_DIR, exist_ok=True)


def download_file(url, path):
    print(f"Downloading {url} → {path}")
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    with open(path, "wb") as f:
        f.write(r.content)


while True:
    for name, url in FILES.items():
        dest = os.path.join(DEST_DIR, name)
        try:
            download_file(url, dest)
            print(f"{name} updated")
        except Exception as e:
            print(f"Error updating {name}: {e}")

    print("Sleeping for 24 hours…")
    time.sleep(60 * 60 * 24)
