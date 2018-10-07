# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        runner = head
        slow = head
        for i in xrange(n):
            runner = runner.next
        if runner is None:       # case where n is the length of the list -- remove first node
            head = head.next
            return head
        while runner.next != None:
            runner = runner.next
            slow = slow.next
        slow.next = slow.next.next
        return head
