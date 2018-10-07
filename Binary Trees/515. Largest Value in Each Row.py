#any here deals with the empty case
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        ans = []
        queue = [[root]]
        
        while queue:
            new_level = []
            level = queue.pop(0)
            ans.append(max([node.val for node in level]))
            for node in level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            if len(new_level):
                queue.append(new_level)
        return ans
