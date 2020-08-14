class singlylinkedlist:
    def __init__(self):
        self.length = 0
        self.head = None
    def addElement(self,value):
        if not self.head:
            self.head = node(value)
            self.length += 1
        else:
            temp = self.head
            while temp and temp.next:
                temp = temp.next
            temp.next = node(value)
            self.length += 1

    def removeElement(self,value):
        if not self.head:
            return
        else:
            temp = self.head
            prev = None
            while temp and temp.value != value:
                prev = temp
                temp = temp.next
            if temp and temp != head:
                prev.next = temp.next
                self.length -= 1
            elif temp and temp == head:
                self.head = temp.next
                self.length -= 1
            
class node:
    def __init__(self,value):
        self.value = value
        self.next = None
    

