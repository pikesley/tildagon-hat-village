import json

from .asset_path import ASSET_PATH

with open(ASSET_PATH + "conf.json") as j:  # noqa: PTH123
    conf = json.loads(j.read())

with open(ASSET_PATH + "font.json") as j:  # noqa: PTH123
    font = json.loads(j.read())
