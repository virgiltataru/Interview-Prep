class BSTIterator(object):
  def __init__(self, root):
    self.stack = []
    self._extract(root)

  def _extract(self, root):
    while root:
      self.stack.append(root)
      root = root.left

  def hasNext(self):
    return len(self.stack) > 0

  def next(self):
    node = self.stack.pop()
    if node.right:
      self._extract(node.right)
    return node.val
