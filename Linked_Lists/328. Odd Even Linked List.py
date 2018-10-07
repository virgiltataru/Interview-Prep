#First check for boundary condition
#Then keep the head of odd list as head and head of even list as head2
#Iteratively change the next for odd and even nodes and go further
#merge odd list and even list
#return head of odd list as result

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd, even = head, head.next
        head2 = even
        while even and even.next:
            odd.next = even.next
            even.next = even.next.next
            odd, even = odd.next, even.next
        odd.next = head2
        return head
