# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.size = 0
        self.is_resized = False

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381
        for c in key:
            hash = ((hash << 5) + hash) + ord(c)
        return hash % self.capacity


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # find an index using the key
        index = self._hash_mod(key)

        # create a new linked list node using key and value
        new_node = LinkedPair(key, value)

        # traverse the linked list in storage at generated index
        cur = self.storage[index]
        # if no list exists, new node becomes the head
        if cur is None:
            self.storage[index] = new_node
            return
        prev = None
        while cur is not None:
            # if key in list matches given key, overwrite value
            if cur.key == key:
                cur.value = value
                return
            prev = cur
            cur = cur.next
        # if reach end of list, append new node
        prev.next = new_node
        self.size += 1
        # find load factor
        lf = self.size / self.capacity
        # if load factor is greater than 0.7, resize hash table
        if lf > 0.7:
            self.resize(2)
        return


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # find the index using the given key
        index = self._hash_mod(key)

        # traverse the linked list in storage at that index
        prev = None
        cur = self.storage[index]
        while cur is not None:
            # if key is found, remove node from list
            if cur.key == key:
                # if node is head of list, point storage to next value
                if prev is None:
                    self.storage[index] = cur.next
                # otherwise, connect prev node to next node
                else:
                    prev.next = cur.next
                self.size -= 1

                # if load factor is less than 0.2, resize hash table
                lf = self.size / self.capacity
                if self.is_resized and lf < 0.2:
                    self.resize(0.5)
                return
            prev = cur
            cur = cur.next

        # if key not found, print a warning
        print("Error: key not found")
        return

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # find the index using the given key
        index = self._hash_mod(key)

        # traverse the linked list at that index in storage until keys match
        cur = self.storage[index]
        while cur is not None:
            if cur.key == key:
                # return value at given key
                return cur.value
            cur = cur.next

        # if key not found, return None
        return None


    def resize(self, factor):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity = int(self.capacity * factor)
        self.storage = [None] * self.capacity

        # for each linked list in storage
        for i in range(len(old_storage)):
            # for each node in the linked list
            cur = old_storage[i]
            while cur is not None:
                # insert new key/value pair into resized list
                self.insert(cur.key, cur.value)
                cur = cur.next

        # if hasn't been resized before and just grew larger, 
        # tell hash table that it's been resized past its initial size
        # remove() checks for is_resized to avoid unnecesary shrinking
        if not self.is_resized and factor > 1:
            self.is_resized = True




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize(2)
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

    print(ht._hash_djb2('hello'))
    print(ht._hash_djb2('hello'))
    print(ht._hash_djb2('hi'))
    print(ht._hash_djb2('world'))
    print(ht._hash_djb2('bing'))
    print(ht._hash_djb2('bong'))
