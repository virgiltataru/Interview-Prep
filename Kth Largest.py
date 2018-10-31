import heapq

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        heap = [-n for n in nums]

        heapq.heapify(heap)

        for i in range(k):
            result = heapq.heappop(heap)

        return -result
