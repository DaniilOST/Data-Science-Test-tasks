class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0  

    def push(self, value):
        new_node = Node(value)
        self.length += 1  
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if not self.tail:  
            return None
        removed_value = self.tail.value
        self.length -= 1  
        if self.head == self.tail:  
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return removed_value

    def shift(self):
        if not self.head: 
            return None
        removed_value = self.head.value
        self.length -= 1  
        if self.head == self.tail:  
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return removed_value

    def unshift(self, value):
        new_node = Node(value)
        self.length += 1  
        if not self.head:  
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.push(1)
    dll.push(2)
    dll.unshift(0)
    dll.push(3)
    dll.push(4)
    
    for e in dll:
        print(e)

    popped_value = dll.pop()
    print(popped_value)
    for e in dll:
        print(e)
    print(dll.length)

    shifted_value = dll.shift()
    print(shifted_value)
    for e in dll:
        print(e)
    print(dll.length)


