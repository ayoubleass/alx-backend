#!/usr/bin/python3
"""
BasicCache that inherits from BaseCaching and is a caching system.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system.
    """

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        the item value for the key key.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns the items in the self.cache_data dict.
        """
        if key is None or key not in self.cache_data.keys():
            return
        return self.cache_data[key]
