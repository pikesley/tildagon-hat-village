import gzip
import json
from pathlib import Path

data = json.loads(Path("font.json").read_text())


compressed = {}

for char, bits in data.items():
    compressed[char] = []
    for line in bits:
        compressed[char].append([line["x"], line["y"], line["width"]])

Path("font.json.gz").write_bytes(
    gzip.compress(
        json.dumps(compressed, separators=(",", ":")).encode("utf-8"), mtime=0
    )
)
