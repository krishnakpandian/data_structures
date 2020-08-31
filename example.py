#!/usr/bin/env python3
import pdb

class node:
    incrementer = 5
    def __init__(self,value):
        self.value = value
        self.next = None
    def printValue(self):
        print("value {}".format(self.value), end='\n')
    def increment(self):
        self.value +=self.incrementer
    @classmethod
    def set_increment(cls,newIncrement):
        cls.incrementer = newIncrement

class treeNode:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

def deleteNode(root:treeNode, val):
    if not root:
        return root
    if root.value == val:
        if root.right and root.left:
           temp = root.right
           while temp.left:
               temp = temp.left
           temp.left = root.left
           return root.right
        if root.right:
           return root.right
        return root.left
    elif root.value > val:
        root.left = deleteNode(root.left,val)
    else:
        root.right = deleteNode(root.right,val)
    return root
def printTree(root: treeNode):
    if root is None:
        return 
    printTree(root.left)
    print(root.value)
    printTree(root.right)


def insertRecursive(root,value):
    if root is None:
        return treeNode(value)
    if value > root.value:
        root.right = insertRecursive(root.right,value)
    else:
        root.left = insertRecursive(root.left,value)
    return root

def main():
    breakpoint()
    person = node(1)
    person.printValue()
    person.increment()
    person.printValue()
    node.set_increment(3)
    print(person.incrementer)
    print(person)

def main2():
    node = treeNode(4)
    printTree(node)
    print('')
    insertRecursive(node, 5)
    insertRecursive(node,7)    
    insertRecursive(node,2)
    insertRecursive(node,1)
    insertRecursive(node,3)
    printTree(node)
    print('')
    node = deleteNode(node,3)
    printTree(node)
    print('')
    node = deleteNode(node, 5)
    printTree(node)
    print('')
    node = deleteNode(node,4)
    printTree(node)


def BSTtoArr(root,arr= []):
    if not root:
        return arr
    BSTtoArr(root.left,arr)
    arr.append(root.value)
    BSTtoArr(root.right,arr)
    return arr


def main3():
    node = treeNode(4)
    printTree(node)
    print('')
    insertRecursive(node, 5)
    insertRecursive(node,7)    
    insertRecursive(node,2)
    insertRecursive(node,1)
    insertRecursive(node,3)
    print(BSTtoArr(node))


if __name__== '__main__':
    main3() 
