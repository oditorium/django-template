"""
Django settings package for BlockchainProject project
"""

import os

def environ(key):
    """
    returns True if the key exists in os.environ[] and it is not false'ish
    """
    if not key in os.environ.keys(): return False
    if os.environ[key] and os.environ[key] != '0': return True
    return False

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



# import all the modules that contain settings you want to use here
from .logging import *
from .apps import *
from .middleware import *
from .templates import *
from .database import *
from .password import *

from .settings import *
