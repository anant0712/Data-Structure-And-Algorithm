class Node:
    def __init__(self,info,next=None):
        self.data = info
        self.next = next


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_beginning(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insert_at_middle(self, value, x):    # 'x' is for location
        temp = Node(value)
        t1 = self.head

        while(t1.next != None):
            if t1.data == x:
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

    def deleteLL(self, value):
        t1=self.head
        prev = t1
        if t1.data == value:
            self.head = t1.next    # This Condition is for the first element to get deleted
        while(t1.next != None):
            if t1.data == value:
                prev.next = t1.next
                break                # This Condition is for specific element to get deleted
            else:
                prev = t1
                t1 = t1.next

        if t1.data == value:
            prev.next= None      # This condition is for last Element to get deleted


    def insert_at_end(self, value):
        temp = Node(value)
        if (self.head != None):
            t1=self.head
            while(t1.next != None):
                t1=t1.next
            t1.next=temp
        else:
            self.head=temp

    def print_list(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)


obj = SinglyLinkedList()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_beginning(5)
obj.insert_at_middle(40, 20)

obj.print_list()

