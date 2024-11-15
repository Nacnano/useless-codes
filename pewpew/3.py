class Node:
    """Doubly linked list node."""
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        # Hash map to store key-node pairs
        self.cache = {} 

        # Initialize the doubly linked list
        self.head = Node(0, 0)  
        self.tail = Node(0, 0)  
        self.head.next = self.tail  
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove node from the doubly linked list."""
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add(self, node: Node):
        """Add node right after head (most recent position)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """Return the value if key exists, otherwise return -1."""
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int):
        """Update or insert the value, and evict the least recently used if capacity is exceeded."""
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add(node)
        else:
            if len(self.cache) >= self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            new_node = Node(key, value)
            self._add(new_node)
            self.cache[key] = new_node

# Time Complexity: get(key) = O(1), put(key, value) = O(1)
# Space Complexity = O(n), where n is the capacity of the LRU cache.

cache = LRUCache(2)  # Init LRU Cache with capacity 2
cache.put(1, 1)      # Cache stores {1=1}
cache.put(2, 2)      # Cache stores {1=1, 2=2}
print(cache.get(1))  # Output: 1, Cache updates to {2=2, 1=1}
cache.put(3, 3)      # LRU key 2 is evicted, Cache stores {1=1, 3=3}
print(cache.get(2))  # Output: -1 (not found)
cache.put(4, 4)      # LRU key 1 is evicted, Cache stores {3=3, 4=4}
print(cache.get(1))  # Output: -1 (not found)
print(cache.get(3))  # Output: 3
print(cache.get(4))  # Output: 4