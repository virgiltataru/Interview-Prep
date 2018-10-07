class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Heapify the list of nodes
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))

        # Create a dummy head and a tail pointer for inserting the next node
        dummy_head = ListNode('head')
        tail = dummy_head

        while heap:
            # Pop min node from heap
            val, min_node = heapq.heappop(heap)

            # Insert it at the tail of the sorted list
            tail.next = min_node
            tail = tail.next

            # If there is node after the min_node, add it into the heap
            if min_node.next:
                heapq.heappush(heap, (min_node.next.val, min_node.next))

        # Return the sorted list of nodes
        return dummy_head.next
