from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        value = self.cache.pop(key, None)
        if value:
            self.cache[key] = value

        return value

    def set(self, key, value):
        self.cache.pop(key, None)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(0)


t = LRUCache(3)

t.set('1', 1)
print(t.get('1'))
t.set('2', 2)
t.set('3', 3)
t.set('4', 4)
print(t.get('1'))
print(t.cache)
