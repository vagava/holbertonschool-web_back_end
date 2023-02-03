#!/usr/bin/python3
"""Create FIFOCache class that inherits from BaseCaching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Simulates a FIFO cache system"""

    def __init__(self):
        """Initializes the FIFO cache system"""
        super().__init__()
        self.cache_queue = []

    def put(self, key, item):
        """Puts an entry in the FIFO system"""
        limit = BaseCaching.MAX_ITEMS
        if key and item:
            if len(self.cache_data) == limit and key not in self.cache_data:
                removed = self.cache_queue.pop(0)
                del self.cache_data[removed]
                print(f"DISCARD: {removed}")
            if key not in self.cache_data:
                self.cache_queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets and returns an entry from the cache system"""
        return self.cache_data.get(key)
