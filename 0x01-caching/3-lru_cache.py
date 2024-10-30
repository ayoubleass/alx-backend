#!/usr/bin/python3
"""
This module has a class that inherits from
BaseCaching and is a caching system.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    This class inherits from BaseCaching and is a caching system.
    """

    def __init__(self):
        """
        initialize the cache
        """
        super().__init__()

    def put(self, key, item):
        """
        Add new item to the cache dict.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            lru_key = list(self.cache_data.keys())[0]
            print("DISCARD:", lru_key)
            del self.cache_data[lru_key]
        self.cache_data[key] = item

    def get(self, key):
        """
        returns an item in the cashe dict.
        """
        if key is None or key not in self.cache_data:
            return
        item = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = item
        return self.cache_data[key]
