class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = None

    def push(self, newNode):
        if self.head is None:
            self.head = newNode

        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = newNode

    def pop(self):
        cur_node = self.head
    
        while cur_node.next:
            prev_node = cur_node
            cur_node = cur_node.next
           
        prev_node.next = None
        
    def Peek(self):
        cur_node = self.head
    
        while cur_node.next:
            prev_node = cur_node
            cur_node = cur_node.next
           
        return prev_node.next
        
            

        
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        

    def printList(self):
        self.reverse()
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        self.reverse()
        



n1 = Node('Print')
n2 = Node('List')
n3 = Node('Map')

s = Stack()
s.push(n1)
s.push(n2)
s.push(n3)
s.printList()