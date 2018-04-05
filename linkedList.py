
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList(object):
    def __init__(self, head):
        self.head = head
        self.tail = head


    def append(self, newNode):
        # This is O(1) runtime because appending to tail which is known
        tail = self.tail
        if self.head:
            tail.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode


    def remove(self, value):
        # This is O(n) where n = length of LinkedList
        current = self.head
        previous = None
        while current:
            if current.val == value:
                if previous:
                    previous.next = current.next
                    break
                else:
                    self.head = current.next
                    break
            else:
                previous = current
                current = current.next


    #def insert(self, newNode, position):
    #    current = self.head
    #    if position > 1:
    #        while current:
    #            if current.val == position:
    #                newNode.next = current.next
    #                current.next = newNode
    #                break
    #            current = current.next
    #    elif position == 1:
    #        newNode.next = sel




n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)


ll = LinkedList(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)
ll.append(n5)


print ll.head.val
print ll.head.next.val
print ll.head.next.next.val
print ll.head.next.next.next.val
print ll.head.next.next.next.next.val

ll.remove(3)
print ll.head.val
print ll.head.next.val
print ll.head.next.next.val
print ll.head.next.next.next.val
