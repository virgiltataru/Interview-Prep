def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        node_map = {}
        if head is None: return None
        new_head = RandomListNode(head.label)
        ptr = head.next
        new_ptr = new_head
        node_map.update({head: new_head})
        # Set only next nodes
        while ptr is not None:
            new_node = RandomListNode(ptr.label)
            new_ptr.next = new_node
            new_ptr = new_node
            node_map.update({ptr: new_ptr})
            ptr = ptr.next
        # Set random pointers
        ptr = head
        new_ptr = new_head
        while ptr is not None:
            if ptr.random is not None:
                new_ptr.random = node_map[ptr.random]
            ptr = ptr.next
            new_ptr = new_ptr.next
        return new_head
