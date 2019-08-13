import os

__version__ = '0.3'

# define all global variables in here
BASE_PATH = os.path.join(os.path.expandvars("$HOME"), ".v2sub")
SUBSCRIBE_CONFIG = os.path.join(BASE_PATH, 'subscribes.json')
SERVER_CONFIG = os.path.join(BASE_PATH, 'servers.json')
DEFAULT_SUBSCRIBE = "default"
