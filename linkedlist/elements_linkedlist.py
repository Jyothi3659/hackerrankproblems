class LinkedlistNode():
    def __init__(self,nodedata):
        self.data = nodedata
        self.next = None
class Linkedlist():
    def __init__(self):
        self.head = None

    def insert_node(self, node_data):
        if self.head == None:
            self.head = node_data
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = node_data
    def printlist(self):
        if self.head is None:
            print("empty list")
        temp = self.head
        while temp:
            if temp.next is None:
                break
            print(temp.data)
            temp = temp.next

linkedlist = Linkedlist()
first = LinkedlistNode(1)
second = LinkedlistNode(2)
third = LinkedlistNode(3)
linkedlist.insert_node(first)
linkedlist.insert_node(second)
linkedlist.insert_node(third)
linkedlist.printlist()