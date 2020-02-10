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
        pass


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

        # insert the node into the linked list in storage at generated index
        cur = self.storage[index]
        if cur is None:
            self.storage[index] = new_node
            return
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

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


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



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
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
