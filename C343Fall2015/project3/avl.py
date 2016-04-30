# AVL Trees, by Elizabeth Feicke
from compiler.ast import Node

class AVLNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = None
        self.height = 1
        
    def setParent(self, n):
        self.parent = n;
        
    def calcHeight(self):
        if self.left and self.right:
            return max(self.left.height, self.right.height) + 1
        elif self.left:
            return 1 + self.left.height
        elif self.right:
            return 1 + self.right.height
        else:
            return 1
                    
    def is_leaf(self):
        return (self.height == 0)
    
    
    def rightRotate(self,oldRoot):
        newRoot = oldRoot.Left
        newLeft = newRoot.right
        oldRoot.left = newLeft
        newLeft.parent = oldRoot
        newRoot.left = oldRoot
        newRoot.right = oldRoot
        oldRoot.parent = newRoot
        self.balanceCheck()
    """    
    def rightRotate(self,node):
        newTop = node.Left
        midleft = newTop.right
        newTop.right = Node
        node.left = midleft
    """    
    def left_rotate(self,node):
        newTop = node.Right
        newTop.parent = node.parent
        midRight = newTop.left
        newTop.left = node
        node.parent = newTop
        node.right = midRight
        midRight.parent = node
        self.balanceCheck()
        
    def insertLeft(self,k):
            if self.left == None:
                parent = self
                child = AVLNode(k,None,None,)
                parent.left = child
                child.parent = parent
            else:
                self.left.insert(k)
                
    def insertRight(self,k):
            if self.right == None:
                parent = self
                child = AVLNode(k,None,None,)
                parent.right = child
                child.parent = parent
            else:
                self.right.insert(k)
                
    def smallest(self):
            if self.left:
                return self.left.smallest()
            else:
                return self
            
    def sucLookup(self):
        #return node above self when node has no right subtree
        if self.parent:
            if self.parent.left == self:
                return self
            else:
                if self.parent.right == self:
                    return self.parent.sucLookup()
                    
    def largest(self):
        if self.right:  
            return self.right.largest()
        else:
            return self
        
    def predLookup(self):
        if self.parent:
            if self.parent.right == self:
                return self
            else:
                if self.parent.left == self:
                    return self.parent.predLookup()
                else:
                    return None
                
    def search(self,k,less):
        if less(k, self.key):
            if self.left:
                return self.left.search(k,less)
            else:
                return None
        else:
            if self.right:
                return self.right.search(k,less)
            else: return None
    
    
        
           
        
def less_than(x,y):
    return x < y


class AVLTree:
    def __init__(self, root = None, less=less_than):
        self.root = root
        self.less = less
        
    def balanceCheck(self):
        while self.parent:
            if self.right.height - self.left.height <= abs(1):
                pass
            else:
                if self.right.height > self.left.height:
                    self.left_rotate() 
                else:
                    self.rightRotate()
            self.parent.balanceCheck()
        
        

    # takes value, returns node with key value
    def insert(self,k):
        if self.root:
            if self.root.key < k:
                self.root.leftInsert(self,k)
                self.balanceCheck()
            else:
                self.root.rightInsert(self,k)
                self.balanceCheck()

    # takes node, returns node
    # return the node with the smallest key greater than n.key
    
    def successor(self, n):
        if n:
            if n.right:
                return n.right.smallest()
                n.smallest.balanceCheck()
            else:
                self.root.sucLookup()
                n.balanceCheck()

    # return the node with the largest key smaller than n.key
    def predecessor(self, n):
        if n:
            if n.right:
                return n.left.largest()
                n.smallest.balanceCheck()
            else:
                self.root.predLookup()
                n.balanceCheck()

    # takes key returns node
    # can return None
    def search(self,k):
        if self.root:
            self.root.search(k,self.less)
        else:
            return None
            
    # takes node, returns node
    def delete_node(self, n):
        if n.left == None and n.right == None:
            if n.parent.left == n:
                n.parent.left = None
            else: 
                n.parent.right = None
        else:
            if n.left == None and n.right:
                if n.parent.right ==n:
                    n.parent.right = n.successor(n)
                else: n.parent.left = n.successor(n)
                n.successor.parent = n.parent()
            else:
                if n.left and n.right:
                    if n.parent:
                        if n.parent.left == n:
                            n.parent.left = n.successor()
                        else:
                            n.parent.right = n.successor()
                            n.successor.parent = n.parent
        n.balanceCheck()                
        
                   


