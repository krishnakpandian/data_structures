class bst:
    def __init__(self):
        self.parent = None
    def addNode(self, value):
        if self.parent == None:
            self.parent = bstNode(value)
        else:
            temp = self.parent
            prev = None
            while temp:
                if temp.val > value:
                    temp = temp.left
                else:
                    temp = temp.right
            if prev:
                if prev.val > value:
                    temp.left = bstNode(value)
                else:
                    temp.right = bstNode(value)
            else:
                self.parent = bstNode(value)
    def removeNode(self,value):
        temp = self.parent
        prev = None
        while temp and temp.val != value:
            if temp.val < value:
                prev = temp
                temp = temp.right
            else:
                prev = temp
                temp = temp.left
        if temp is None:
            return

        if prev is None:
            left = temp.left
            right = temp.right
            if right:
                self.parent = right
                temp = right
                while temp.left:
                    temp = temp.left
                temp.left = left
            elif left:
                self.parent = left
            else:
                self.parent = None
        else:
            if prev.right == temp:
                left = temp.left
                right = temp.right
                if right:
                    prev.right = right
                    temp = right
                    while temp.left:
                        temp = temp.left
                    temp.left = left
                elif left:
                    prev.right = left
                else:
                    prev.right = None
            else:
                left = temp.left
                right = temp.right
                if right:
                    prev.left = right
                    temp = right
                    while temp.left:
                        temp = temp.left
                    temp.left = left
                elif left:
                    prev.left = left
                else:
                    prev.left = None

        


class bstNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

