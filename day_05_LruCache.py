"""
缓存剔除策略-LruCache
"""

from collections import OrderedDict


class LruCache(object):
    """
    当缓存空间不够用的时候，替换掉最近最少使用的对象
    """
    def __init__(self, capacity=8):
        self.od = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.od:
            val = self.od[key]
            self.od.move_to_end(key)  # 每次访问更新最新访问的key
            return val
        return -1

    def put(self, key, value):
        if key in self.od: # 更新k/v
            del self.od[key]
            self.od[key] = value # 更新key到表头
        else:  # insert
            self.od[key] = value
            if len(self.od) > self.capacity:  # 判断容量是否满了
                self.od.popitem(last=False)


def test():

    lru = LruCache()
    assert lru.get(1) == -1
    for idx, i in enumerate(range(8)):
        lru.put(idx, i)

    assert lru.get(2) == 2
    assert lru.get(7) == 7
    assert lru.get(0) == 0

    lru.put(9, 6)
    assert lru.get(9) == 6







