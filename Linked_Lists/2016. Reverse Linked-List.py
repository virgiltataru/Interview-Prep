class Solution:
    def reverseList(self, head):
        if not head:
            return None
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
