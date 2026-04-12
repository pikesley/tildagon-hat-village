# https://tildagon.badge.emfcamp.org/tildagon-apps/reference/ctx/#adding-images
import os

apps = os.listdir("/apps")
path = ""
ASSET_PATH = "apps/"

if "pikesley_tildagon_hat_village" in apps:
    ASSET_PATH = "/apps/pikesley_tildagon_hat_village/"

if "hat_village" in apps:
    ASSET_PATH = "apps/hat_village/"
