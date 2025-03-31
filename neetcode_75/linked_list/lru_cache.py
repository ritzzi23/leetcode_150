from typing import List
from typing import Optional

#Brute Force 
#Time Complexity: O(n) for both get, put
#Space Complexity: O(n) for both get, put

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []
        

    def get(self, key: int) -> int:
        for i, (k,v) in enumerate(self.cache):
            if k == key:
                self.cache.pop(i)
                self.cache.insert(0,((k,v)))
                return v
        return -1

        

    def put(self, key: int, value: int) -> None:
        for i, (k,_) in enumerate(self.cache):
            if k == key:
                self.cache.pop(i)
                self.cache.insert(0,(key,value))
                return
        if len(self.cache) == self.capacity:
            self.cache.pop()
        self.cache.insert(0,(key,value))
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#------========------------------===========------------------------========-----------------------


class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self,node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in (self.cache):
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            new_node = Node(key,value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            if (len(self.cache)> self.capacity):
                tail_node = self.tail.prev
                self._remove(tail_node)
                del self.cache[tail_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



'''✅ Time Complexity:
1. get(key):
Dictionary lookup: O(1)

Removing node from DLL: O(1)

Adding node to head of DLL: O(1)

🔹 Overall: O(1)

2. put(key, value):
Dictionary lookup/update: O(1)

If updating: remove and add node (DLL ops): O(1)

If inserting new:

Add node to DLL: O(1)

Insert into dictionary: O(1)

If over capacity:

Remove tail node from DLL: O(1)

Delete from dictionary: O(1)

🔹 Overall: O(1)


✅ Space Complexity:
The cache stores up to capacity number of nodes.

Each node has a key, value, and two pointers → constant space per node.

Dictionary stores capacity key-node mappings.

🔹 Overall: O(capacity)


'''