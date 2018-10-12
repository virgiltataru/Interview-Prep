import collections

def find_max_depth(node):
    if not node:
        return 0
    max_depth = max(find_max_depth(node.left), find_max_depth(node.right))
    return max_depth + 1

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        max_depth = find_max_depth(root)

        # build matrix
        matrix_depth = max_depth
        matrix_width = (2**max_depth) - 1
        matrix = [[""] * matrix_width for _ in xrange(matrix_depth)]

        # run level order / breadth first search
        queue = collections.deque()
        queue.append([root, 0, matrix_width - 1, 0]) # node, start, end, level
        while queue:
            node, start, end, level = queue.popleft()
            if not node: continue
            mid = start + (end-start)/2
            matrix[level][mid] = str(node.val)
            queue.append([node.left, start, mid-1, level+1])
            queue.append([node.right, mid+1, end, level+1])
        return matrix
