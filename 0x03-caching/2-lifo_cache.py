#!/usr/bin/python3
"""Create LIFOCache class that inherits from BaseCaching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Simulates a LIFO cache system"""

    def __init__(self):
        """Initializes the LIFO cache system"""
        super().__init__()
        self.cache_lifo = []

    def put(self, key, item):
        """Puts an entry in the LIFO system"""
        limit = BaseCaching.MAX_ITEMS
        if key and item:
            if len(self.cache_data) == limit and key not in self.cache_data:
                removed = self.cache_lifo.pop()
                del self.cache_data[removed]
                print(f"DISCARD: {removed}")
            if key not in self.cache_data:
                self.cache_lifo.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets and returns an entry from the cache system"""
        return self.cache_data.get(key)
