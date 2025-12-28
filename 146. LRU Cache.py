class Node:
    def __init__(self, x=0, key=-1, next=None, prev=None):
        self.val = x
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.lookup = {}
        self.head: Node = Node()
        self.tail: Node = self.head.next
        

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        
        val_node = self.lookup[key]
        if val_node == self.tail:
            return val_node.val
        
        # Update to be recent
        nxt = val_node.next
        pre = val_node.prev

        pre.next = nxt
        nxt.prev = pre

        self.tail.next = val_node
        val_node.prev = self.tail
        val_node.next = None
        self.tail = val_node

        return val_node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.lookup and self.size <= self.capacity:
            self.get(key)
            val_node = self.lookup[key]
            val_node.val = value
            return
        
        # Evict least recently used
        if self.size >= self.capacity:
            new_head = self.head.next.next
            del(self.lookup[self.head.next.key])

            if new_head: 
                new_head.prev = self.head
            else:
                self.tail = None

            self.head.next = new_head
        else:
            self.size += 1

        new_node = Node(value, key)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = None
        else:
            new_node.prev = self.head
            self.head.next = new_node

        self.tail = new_node
        self.lookup[key] = new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
