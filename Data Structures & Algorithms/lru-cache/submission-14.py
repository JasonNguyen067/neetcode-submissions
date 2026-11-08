# 8:29

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prev = self.right.prev 
        
        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node

    def remove(self, node):
        left = node.prev
        right = node.next

        left.next = right
        right.prev = left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
