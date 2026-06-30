class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

## Explanation
## data stores the value.
## next stores the address of the next node.

## Linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
first = Node(10)
second = Node(20)
third = Node(30)

first.next = second
second.next = third

## Traverse a linked list
current = first
while current:
    print(current.data)
    current = current.next

## Insert a New Node at the End
fourth = Node(40)
third.next = fourth

first.next = third ## deletion of a node