class Solution:
    def wordPattern(self, s, t):
        return [s.find(c) for c in s] == [t.find(d) for d in t]
