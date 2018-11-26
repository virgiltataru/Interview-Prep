from collections import OrderedDict, defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.freq = 1

class LFUCache:
    def __init__(self, capacity):
        self.d = {}     # key -> val
        self.freqs = defaultdict(OrderedDict) # freq -> OrderedDict(key -> val)
        self.capacity = capacity
        self.size = 0
        self.min_freq = 1

    def get(self, key):
        if key not in self.d: return -1
        else:
            self.increaseFreq(key)
            return self.d[key].val

    def increaseFreq(self, key):
        curr = self.d[key]

        # Remove key from self.freqs[freq]
        del self.freqs[curr.freq][key]
        if self.min_freq == curr.freq and len(self.freqs[curr.freq]) == 0:
            self.min_freq += 1

        # Add key to self.freqs[freq+1]
        curr.freq += 1
        self.freqs[curr.freq][key] = curr


    def put(self, key, value):
        if self.capacity == 0: return
        elif key in self.d:
            self.increaseFreq(key)
            self.d[key].val = value
        else:
            # Evict first
            if self.size == self.capacity:
                evictKey, evictVal = self.freqs[self.min_freq].popitem(last=False)
                del self.d[evictKey]
            else:
                self.size += 1

            # Add the new (key, value) to self.d
            curr = Node(value)
            self.d[key] = curr
            self.freqs[1][key] = curr
            self.min_freq = 1
