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
        self.order = list()

    def put(self, key, item):
        """
        Add new item to the cache dict.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            print("DISCARD:", lru_key)
            del self.cache_data[lru_key]
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        """
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]
