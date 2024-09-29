class Node:
    def __init__(self, count):
        self.keys = set()
        self.count = count
        self.prev = None
        self.next = None
    
    def remove_element(self, key):
        self.keys.remove(key)
    
    def add_element(self, key):
        self.keys.add(key)


class LinkedList:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, node, count):
        next_node = node.next
        
        new_node = Node(count)
        new_node.prev = node
        new_node.next = next_node

        node.next = new_node
        next_node.prev = new_node

        return new_node

    def pop(self, node):
        if node.count == 0 or node.count == float('inf'):
            return
        node.prev.next, node.next.prev = node.next, node.prev
        return

    def dec_element(self, node, key):
        node.remove_element(key)
        new_count = node.count - 1
        prev_node = node.prev
        if prev_node.count == new_count:
            correct_node = prev_node
        else:
            correct_node = self.insert(prev_node, new_count)
        if not node.keys:
            self.pop(node)
        correct_node.add_element(key)
        return correct_node

    def inc_element(self, node, key):
        if node.count != 0:
            node.remove_element(key)
        new_count = node.count + 1
        if node.next.count == new_count:
            correct_node = node.next
        else:
            correct_node = self.insert(node, new_count)
        
        correct_node.add_element(key)
        if not node.keys:
            self.pop(node)
        return correct_node


class AllOne:

    def __init__(self):
        self.bucket = LinkedList()
        self.mapper = {}        

    def inc(self, key: str) -> None:
        node = self.bucket.head if key not in self.mapper else self.mapper[key]
        new_node = self.bucket.inc_element(node, key)
        self.mapper[key] = new_node        

    def dec(self, key: str) -> None:
        node = self.mapper[key]
        new_node = self.bucket.dec_element(node, key)
        if new_node.count == 0:
            new_node.remove_element(key)
            del self.mapper[key]
        else:
            self.mapper[key] = new_node

    def getMaxKey(self) -> str:
        max_node = self.bucket.tail.prev
        if max_node.count == 0: return ''
        for e in max_node.keys:
            return e

    def getMinKey(self) -> str:
        min_node = self.bucket.head.next
        if min_node.count < float('inf'):
            for e in min_node.keys:
                return e
        else: return ''
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()