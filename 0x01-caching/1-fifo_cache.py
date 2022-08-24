#!/usr/bin/python3
"""
FIFOCache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ subclass of BaseCaching """
    def __init__(self):
        super().__init__()
        self.data = {}
        self.item_in = 0
        self.item_out = 0

    def put(self, key, item):
        """ adds a new cache to basecaching"""
        if key or item is not None:
            self.cache_data[key] = item
        else:
            self.add_item(key, item)

    def get(self, key):
        """ gets all the cache for the given key """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            return value

    def remove_item():
        self.item_out += 1
        key = self.data[self.item_out]
        del self.data[self.item_out], self.cache_data[key]

    def add_item(self, key, item):
        itemsCount = self.cache_data.count(item)
       
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.data[self.item_out + 1]))
            self.remove_item()
        self.cache_data[key] = item
        self.item_in += 1
        self.data[self.item_in] = key
