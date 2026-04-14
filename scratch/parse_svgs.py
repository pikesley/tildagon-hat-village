import json
import xml.etree.ElementTree as ET
from pathlib import Path

results = {"upper": {}, "lower": {}, "numbers": {}, "other": {}}
also = {}
keys = ["x", "y", "width", "height"]

for item in results:  # noqa: PLC0206
    for character in sorted(Path("chars", "svg", item).glob("*")):
        tree = ET.parse(character)  # noqa: S314
        root = tree.getroot()

        results[item][character.stem] = []
        also[character.stem] = []
        for rect in tree.findall(".//{http://www.w3.org/2000/svg}rect"):
            data = {}
            for key in keys:
                data[key] = int(rect.get(key))
            results[item][character.stem].append(data)
            also[character.stem].append(data)

Path("font.json").write_text(json.dumps(also))
