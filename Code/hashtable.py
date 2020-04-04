#!python

from linkedlist.linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Best and Worst Running time: O(k) for k items in all buckets because
            the size of the list of buckets is constant but the size of items in
            each bucket varies, causing the time it takes to complete the function
            increase linerally with the size of all the bukets not the list itself."""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Best and Worst Running time: O(k) for k items in all buckets because
            the size of the list of buckets is constant but the size of items in
            each bucket varies, causing the time it takes to complete the function
            increase linerally with the size of all the bukets not the list itself."""
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Best and Worst Running time: O(n) for n items in all buckets because
            the size of the list of buckets is constant but the size of items in
            each bucket varies, causing the time it takes to complete the function
            increase linerally with the size of all the bukets not the list itself."""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Best and Worst Case Running time: O(1) (constant time) because of the
            length property."""
        return self.size

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Best Case Running time: O(1) if the first item is the item we're 
            looking for
        Worst Case Runnin Time: O(n) for n items in the bucket and the key is the last
            item in the list because as the size of the list increaces the time it
            takes to complete the function increases lineraly"""
        bucket = self.buckets[self._bucket_index(key)]
        for item_key, value in bucket.items():
            if item_key is key:
                return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Best Case Running time: O(1) if the item is the first item in the first
            bucket.
        Worst Case Running Time: O(n) for n items in the bucket and the item is the 
            last item in the bucket because as the size of the bucket increases, the 
            time it takes to complete the function increases lineraly."""
        bucket = self.buckets[self._bucket_index(key)]
        for item_key, item_value in bucket.items():
            if item_key is key:
                return int(item_value)
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Best Case Running time: O(1) if the item is the first item in the first
            bucket.
        Worst Case Running Time: O(n) for n items in the bucket and the item is 
            not in the bucket because as the size of the bucket increases, the 
            time it takes to complete the function increases lineraly."""
        bucket = self.buckets[self._bucket_index(key)]
        # Get the old key-value pair 
        for item_key, item_value in bucket.items():
            if item_key == key:
                bucket.delete((item_key, item_value))
                self.size -= 1
        bucket.append((key, value))
        self.size += 1

    def delete(self, key):
        """Insert or update the given key with its associated value.
        Best Case Running time: O(1) if the item is the first item in the first
            bucket.
        Worst Case Running Time: O(n) for n items in the bucket and the item is the 
            last item in the bucket because as the size of the bucket increases, the 
            time it takes to complete the function increases lineraly."""
        bucket = self.buckets[self._bucket_index(key)]
        for item_key, item_value in bucket.items():
            if item_key is key:
                bucket.delete((item_key, item_value))
                self.size -= 1
                return
        raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()