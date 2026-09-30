class ListNode:

    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hash_map = [ListNode() for i in range(10 ** 4)]

    def put(self, key: int, value: int) -> None:
        curr = self.hash_map[key % (10 ** 4)]
        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
        curr.next = ListNode(key, value)
    
    def get(self, key: int) -> int:
        curr = self.hash_map[key % (10 ** 4)]
        while curr.next:
            if curr.next.key == key:
                return curr.next.value
        return -1

    def remove(self, key: int) -> None:
        curr = self.hash_map[key % (10 ** 4)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)