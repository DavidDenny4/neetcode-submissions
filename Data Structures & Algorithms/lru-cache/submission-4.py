class Node:
    
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        
        node = self.key_map[key]
        self.remove(node)
        newNode = Node(key, node.val)
        self.insert(newNode)
        self.key_map[key] = newNode
        return newNode.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            node = self.key_map[key]
            self.remove(node)
            newNode = Node(key, value)
            self.insert(newNode)
            self.key_map[key] = newNode
        else:
            newNode = Node(key, value)
            self.insert(newNode)
            self.key_map[key] = newNode
            if len(self.key_map) > self.capacity:
                oldest = self.head.next
                self.key_map.pop(oldest.key)
                self.remove(oldest)
                
            



        

