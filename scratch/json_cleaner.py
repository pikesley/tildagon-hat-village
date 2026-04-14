import json
from pathlib import Path

for thing in Path("chars", "json").glob("*/*"):
    print(thing)
    j = json.loads(thing.read_text())

    thing.write_text(json.dumps(j))
