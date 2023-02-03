#!/usr/bin/python3
"""Create LRUCache class that inherits from BaseCaching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Class that simulares a Least Recently Used cache"""

    def __init__(self):
        """Initializes the LRU caching system"""
        super().__init__()
        self.cache_lru = []

    def put(self, key, item):
        """Puts an entry in the LRU caching system"""
        limit = BaseCaching.MAX_ITEMS
        if key and item:
            if len(self.cache_data) == limit and key not in self.cache_data:
                removed = self.cache_lru.pop(0)
                del self.cache_data[removed]
                print(f"DISCARD: {removed}")
            if key not in self.cache_data:
                self.cache_lru.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets and returns an entry from the cache system"""
        if key in self.cache_data:
            self.cache_lru.remove(key)
            self.cache_lru.append(key)
        return self.cache_data.get(key)
