import math

# import TestHashTable from test


class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.

    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.size = 0

    def get_load(self):
        return float(self.size / self.capacity)

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function
        hash = (())
        Implement this, and/or DJB2.
        http://www.isthe.com/chongo/tech/comp/fnv/#FNV-param

        The core of the FNV-1 hash algorithm is as follows:
        hash = offset_basis
        for each octet_of_data to be hashed
        hash = hash * FNV_prime
        hash = hash xor octet_of_data
        return hash
        """

        hash = 14695981039346656037
        fnv_prime = 1099511628211
        for char in key:
            hash = hash * fnv_prime
            # ^ is a xor bitwise operator, or exclusion
            # 1 xor 1 = 0,
            # 1 xor 0 = 1,
            # 0 xor 1 = 1
            hash = hash ^ ord(char)
        return hash

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        https://brilliant.org/wiki/hash-tables/
        """
        hash = 5381
        byte_array = key.encode('utf-8')

        for byte in byte_array:
            # the modulus keeps it 32-bit, python ints don't overflow
            hash = ((hash * 33) ^ byte) % 0x100000000
            # ^ is a xor bitwise operator, or exclusion
            # 1 xor 1 = 0,
            # 1 xor 0 = 1,
            # 0 xor 1 = 1

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return int(self.fnv1(key) % self.capacity)
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        if self.get_load() > 0.8:
            self.resize()

        my_hash_index = self.hash_index(key)

        node = self.storage[my_hash_index]

        if node is None:
            self.storage[my_hash_index] = HashTableEntry(key, value)
            self.size += 1
            return

        prev = node

        while node is not None:

            if node.key == key:
                node.value = value
                return

            prev = node
            node = node.next

        prev.next = HashTableEntry(key, value)
        self.size += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        my_hash_index = self.hash_index(key)

        node = self.storage[my_hash_index]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            print('Sorry, I cannot find that key.')

        else:
            self.size -= 1

            if prev is None:
                self.storage[my_hash_index] = node.next
            else:
                prev.next = prev.next.next
            if self.get_load() < 0.2:
                self.desize()

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        my_hash_index = self.hash_index(key)

        node = self.storage[my_hash_index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            print("Sorry, couldn't find that key")
        else:
            return node.value

    def resize(self, given_size=None):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

        if given_size is None:
            return

        old_array = self.storage
        self.capacity = self.capacity * 2
        new_array = [None] * self.capacity
        self.storage = new_array

        self.size = 0

        for element in old_array:
            if element is not None:
                while element is not None:
                    self.put(element.key, element.value)
                    element = element.next

    def desize(self):
        old_array = self.storage
        self.capacity = self.capacity / 2
        new_array = [None] * math.ceil(self.capacity)
        self.storage = new_array
        self.size = 0
        for element in old_array:
            if element is not None:
                self.put(element.key, element.value)
                element = element.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    ht.delete("line_2")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"), "should be None")
    print(ht.get("line_3"))
    print(ht.get("line_4"))  # doesn't exist

    print("")
