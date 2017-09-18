# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 23:32:52 2017

@author: Vamshidhar P
"""

class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None
        
    def insert(self, data):
        if self.value == data:
            return False
        elif data < self.value:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        elif data > self.value:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True                         
     
    def find(self, data):
        if self.value == data:
            return True
        elif data < self.value:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        elif data > self.value:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False
            
    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()
             
         
    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()        
            print(str(self.value))
        
    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()        
            
    def getHeight(self):
        if self.leftChild and self.rightChild:
            return 1+ max(self.leftChild.getHeight(), self.rightChild.getHeight())
        
        elif self.leftChild:
            return 1+ self.leftChild.getHeight()
        
        elif self.rightChild:
            return 1+ self.rightChild.getHeight()
        
        else:
            return 1
    
    def isBalanced(self):
        if self.leftChild and self.rightChild:
            if abs(self.leftChild.getHeight() - self.rightChild.getHeight()) > 1:
                return False
            else:
                return True
        else:
            return False
        
    
class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
        
    def preorder(self)        :
        print("Pre-Order Traversal")
        self.root.preorder()
        
    def postorder(self)        :
        print("Post-Order Traversal")
        self.root.postorder()
        
    def inorder(self)        :
        print("In-Order Traversal")
        self.root.inorder()
        
    def getHeight(self):
        if self.root:
            return self.root.getHeight()
        else:
            return -1
     
    def isBalanced(self):
        if self.root is None:
            return False
        else:
            return self.root.isBalanced()
            
            
        
        
        
        
        
bst = Tree()        
print(bst.insert(10))
print(bst.insert(15))
print(bst.insert(28))

print(bst.insert(5))
print(bst.insert(12))
print(bst.insert(9))
print(bst.insert(4))
print(bst.insert(11))

print(bst.insert(13))

bst.inorder()
bst.postorder()
bst.preorder()
