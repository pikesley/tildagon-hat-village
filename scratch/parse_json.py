import gzip
import json
from pathlib import Path

results = {"upper": {}, "lower": {}, "numbers": {}, "other": {}}
actual = {}
keys = ["x", "y"]

for item in results:
    for character in sorted(Path("chars", "json", item).glob("*")):
        data = json.loads(character.read_text())
        actual[data["id"]] = []
        for y, line in enumerate(data["data"]):
            for x, digit in enumerate(line):
                if digit:
                    actual[data["id"]].append((x, y))


Path("non-rle-font.json.gz").write_bytes(
    gzip.compress(json.dumps(actual, separators=(",", ":")).encode("utf-8"), mtime=0)
)
