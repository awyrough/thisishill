"""
Initialize all ThisIsHill system loggers.

Defined in thisishill/settings.py
"""

import logging

logger = logging.getLogger('UNIVERSAL')
user_logger = logging.getLogger('USER')
cache_logger = logging.getLogger('CACHE')