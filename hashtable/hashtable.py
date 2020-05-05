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
        self.head = None

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
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        my_key = self.hash_index(key)

        node = self.storage[my_key]

        if node is None:
            self.storage[my_key] = HashTableEntry(key, value)
            return

        prev = node

        while node is not None:
            prev = node
            node = node.next

        prev.next = HashTableEntry(my_key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        my_key = self.hash_index(key)

        node = self.storage[my_key]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None

        else:
            result = node.value

            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            return result

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        my_key = self.hash_index(key)

        node = self.storage[my_key]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:

            return node.value

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """


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

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
