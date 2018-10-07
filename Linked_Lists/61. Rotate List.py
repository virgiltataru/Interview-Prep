#Find the lenght, move two pointers then change the links around them
class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        k = k % self.length(head)
        if k == 0:
            return head


        tail = self.find_tail(head)
        stop_index = self.length(head) - k # if we do not consider side case k == 0, below the stop_index would be the length, out of range.
        p = None
        c = head
        steps = 0
        while steps < stop_index:
            p = c
            c = c.next
            steps += 1
        p.next = None
        tail.next = head
        return c


    def length(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def find_tail(self, head):
        if head == None:
            return head
        else:
            while head.next:
                head = head.next
            return head
