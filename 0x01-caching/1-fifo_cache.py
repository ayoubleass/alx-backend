#!/usr/bin/python3
"""
This module has a class that inherits from
BaseCaching and is a caching system.
"""
from base_caching import BaseCaching


class FIFOCache (BaseCaching):
    """
    Inherits from BaseCaching and is a caching system.
    """

    def put(self, key, item):
        """
        assign to the dictionary `self.cache_data`.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = list(self.cache_data.keys())[0]
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))
        self.cache_data[key] = item

    def get(self, key):
        """
        return the value in `self.cache_data` using a key.
        """
        if key is None or key not in self.cache_data.keys():
            return
        return self.cache_data[key]
