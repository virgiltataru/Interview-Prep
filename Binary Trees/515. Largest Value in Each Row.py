#any here deals with the empty case
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        ln = 0
        lst = [(root, 0)]
        while lst:
            node, level = lst.pop()
            if not node:
                return
            if ln == level:
                res.append([node.val])
                ln += 1
            else:
                res[level].append(node.val)
            if node.left:
                lst.append([node.left, level+1])
            if node.right:
                lst.append([node.right, level+1])

        return [max(x) for x in res]
