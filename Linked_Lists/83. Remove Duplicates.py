class Solution(object):
    def deleteDuplicates(self, head):

        if head ==None:
            return []

        result = head
        while head.next != None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return result
