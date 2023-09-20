# Export the version given in project metadata
from importlib import metadata

__version__ = metadata.version(__package__)
del metadata

from cnsr.paths import EDADataManager, ERNDataManager, FAADataManager, HRVDataManager
