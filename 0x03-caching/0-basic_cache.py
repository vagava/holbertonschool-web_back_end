#!/usr/bin/python3
"""
Create BasicCache class that
inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """This class is a caching system"""

    def __init__(self):
        """Initialize with parent init"""
        super().__init__()

    def put(self, key, item):
        """Puts a value into the cache dictionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Gets and returns an entry from the cache dict"""
        return self.cache_data.get(key, None)
