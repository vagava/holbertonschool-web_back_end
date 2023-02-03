#!/usr/bin/python3
"""Create MRUCache class that inherits from BaseCaching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Class that simulares a MRU caching system"""

    def __init__(self):
        """Inicializes the MRU caching system"""
        super().__init__()
        self.cache_mru = []

    def put(self, key, item):
        """Puts an entry in the MRU caching system"""
        limit = BaseCaching.MAX_ITEMS
        if key and item:
            if len(self.cache_data) == limit and key not in self.cache_data:
                removed = self.cache_mru.pop()
                del self.cache_data[removed]
                print(f"DISCARD: {removed}")
            if key not in self.cache_data:
                self.cache_mru.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets an entry from the MUR caching system"""
        if key in self.cache_data:
            self.cache_mru.remove(key)
            self.cache_mru.append(key)
        return self.cache_data.get(key)
