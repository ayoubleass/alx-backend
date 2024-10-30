#!/usr/bin/python3
"""
This module has a class that inherits from
BaseCaching and is a caching system.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    This class inherits from BaseCaching and is a caching system.
    """

    def put(self, key, item):
        """
        Adds a new item in the cache.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem()
            print("DISCARD: {}".format(last_key))
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns an item in the cashe dict.
        """
        if key is None or key not in self.cache_data.keys():
            return
        return self.cache_data[key]
