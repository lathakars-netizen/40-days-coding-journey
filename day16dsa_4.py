class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def find_max(self):
        if self.head is None:
            print("empty list")
            return
        
        max_val = float('-inf')
        current = self.head
        while current is not None:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        print(f"largest value: {max_val}")

if __name__ == "__main__":
    llist = LinkedList()
    llist.append(10)
    llist.append(20)
    llist.append(5)
    llist.append(15)
    llist.find_max()
