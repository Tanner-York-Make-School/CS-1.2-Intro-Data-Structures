#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item

class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0
        self.node = self.head
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def __iter__(self):
        return LinkedListIterator(self.head)

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
        Best and Worst Case Running time: O(n) for n item in the list (length)
            because we always need to loop through all the items in the list"""
        return self.size

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and Worst Case Running time: O(1) because it takes O(1) 
            to create a new node and to set the next and tail variables."""
        node = Node(item)
        self.size += 1
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and Worst Case Running time: O(1) because it takes O(1) 
            time to create node and to set the next and head variables."""
        node = Node(item)
        self.size += 1
        if self.tail is None:
            node.next = self.head
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) if the item that satisfies quality
            is the first element
        Worst case running time: O(n) for n items in the list (length) because
            if the item that satisfies quality is the last item, them it has to go 
            all the items in the list"""
        node = self.head
        while node is not None:
            if quality(node.data) == True:
                return node.data
            node = node.next
        return None

    def replace(self, item, value):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) if the item that satisfies quality
            is the first element
        Worst case running time: O(n) for n items in the list (length) because
            if the item that satisfies quality is the last item, them it has to go 
            all the items in the list"""
        node = self.head
        while node is not None:
            if node.data == item:
                node.data = value
                return
            node = node.next
        raise ValueError('Item not found: {}'.replace(item))

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) beause setting variables takes O(1) time 
            and if the item is the first in the list, then it doesnt go through 
            all of the items in the list.
        Worst case running time: O(n) for n items in list (length) beause setting 
            variables takes O(1) time and if the item is the last in the list, then 
            it hast to go through all of the items in the list."""
        if self.head is None:
            raise ValueError('Item not found: {}'.format(item)) 
        prev_node = None
        node = self.head
        next_node = self.head.next

        # Check for best case and edge cases
        if node.data == item and next_node is None:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        elif node.data == item:
            self.head = next_node
            self.size -= 1
            return

        # Loop through the list and find the correct node and the nodes around it
        while node.next is not None and node.data is not item:
            prev_node = node
            node = node.next
            next_node = node.next

        # Check if the node it the item
        if node.data == item and next_node is None:
            prev_node.next = None
            self.tail = prev_node
            # If theres is only one node, set the tail the the new value aswell
            if prev_node == self.head:
                self.tail = self.head
            self.size -= 1
            return
        elif node.data == item: 
            prev_node.next = next_node
            self.size -= 1
            return
        raise ValueError('Item not found: {}'.format(item)) 

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
    delete_implemented = False
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
