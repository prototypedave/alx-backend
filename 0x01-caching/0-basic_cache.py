#!/usr/bin/python3
"""
Basic Cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ subclass of BaseCaching """

    def put(self, key, item):
    """ adds a new cache to basecaching"""
        if key or item is not None:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
    """ gets all the cache for the given key """
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data.get(key)
