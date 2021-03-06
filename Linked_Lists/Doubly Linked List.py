class Node():
    def __init__(self, next_node=None, previous_node=None, data=None):
        self.next_node = next_node
        self.previous_node = previous_node
        self.data = data



class LinkedList():
    def __init__(self, node):
        assert isinstance(node, Node)
        self.first_node = node
        self.last_node = node

    def push(self, node):
        '''Pushes the node <node> at the "front" of the ll
        '''
        node.next_node = self.first_node
        node.previous_node = None
        self.first_node.previous_node = node
        self.first_node = node

    def pop(self):
        '''Pops the last node out of the list'''
        old_last_node = self.last_node
        to_be_last = self.last_node.previous_node
        to_be_last.next_node = None
        old_last_node.previous_node = None

        # Set the last node to the "to_be_last"
        self.previous_node = to_be_last

        return old_last_node

    def remove(self, node):
        '''Removes and returns node, and connects the previous and next
        nicely
        '''
        next_node = node.next_node
        previous_node = node.previous_node

        previous_node.next_node = next_node
        next_node.previous_node = previous_node

        # Make it "free"
        node.next_node = node.previous_node = None

        return node
