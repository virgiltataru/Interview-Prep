# the logic here is that you first just try to fit all the elements you need for
# the subsequence, than move the start index up until you meet an element you
# need in the final result, at which point you can't move up anymore    

# refer here:
# https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems?page=6

class Solution(object):
    def minWindow(self, string, target):
        """
        :type string: str
        :type target: str
        :rtype: str
        """
        # counter represents the number of chars of t to be found in s
        target_map = collections.Counter(target)

        count = len(target)
        start = end = head = 0
        min_substring_length = sys.maxsize
        # Move end to find a valid window.
        while end < len(string):
            #if character doesn't exist in map it returns 0
            if target_map[string[end]] > 0:
                count -= 1
            target_map[string[end]] -= 1
            end += 1
            # When we found a valid window, move start to find smaller window.
            while count == 0:
                if (end - start) < min_substring_length:
                    min_substring_length = end - start
                    head = start
                target_map[string[start]] += 1
                # When char exists in target, increase counter.
                if target_map[string[start]] >0:
                    count += 1

                start += 1
        return "" if min_substring_length == sys.maxsize else string[head:head + min_substring_length]
