class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        self.backtrack(result, [], nums, 0)
        return result

    def backtrack(self, result, path, nums, start):
        result.append(path)
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.backtrack(result, path, nums, i+1)
            path.pop()
