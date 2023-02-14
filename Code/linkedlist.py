#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        count = 0
        for item in self.items():
            count += 1
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Create new node to hold given item
        node = Node(item)
        # If self.is_empty() == True set the head and the tail to the new node
        if self.is_empty() == True:
            self.head = node
            self.tail = node
        # Else append node after tail
        else:
            self.tail.next = node
            self.tail = node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Create new node to hold given item
        node = Node(item)
        # Prepend node before head, if it exists
        if self.is_empty() == True:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def find(self, matcher):
        """Return an item from this linked list if it is present.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # Loop through all nodes to find item, if present return True otherwise False

        # def find_next(current_node):
        #     if current_node is None:
        #         return False
        #     elif matcher(current_node.data) is True:
        #         return True
        #     else:
        #         return find_next(current_node.next)

        def find_next(current_node):
            if current_node is None:
                return None
            elif matcher(current_node.data) is True:
                return current_node
            else:
                return find_next(current_node.next)

        return find_next(self.head).data if find_next(self.head) is not None else None


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # Loop through all nodes to find one whose data matches given item
        try:
            found = False
            if self.head.data == item:
                self.head = self.head.next if self.head.next is not None else None
                if self.head is None:
                    self.tail = None
                found = True
            node = self.head

            while found is False and node.next is not None:
                if node.next.data == item:
                    if node.next.next is None:
                        node.next = None
                        self.tail = node
                        found = True
                    else:
                        node.next = node.next.next
                        found = True
                node = node.next
            # Update previous node to skip around node with matching data
            # Otherwise raise error to tell user that delete has failed
            if (found is False):
                raise ValueError('Item not found: {}'.format(item))
        except:
            raise ValueError('Item not found: {}'.format(item))
        # Hint: raise ValueError('Item not found: {}'.format(item))

    def replace(self, item_being_replaced, item_to_replace_with):
        found = False
        node = self.head
        while found is False and node.next is not None:
            if node.data == item_being_replaced:
                node.data = item_to_replace_with
                found = True
            node = node.next


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
