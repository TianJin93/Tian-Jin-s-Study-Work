from stack import ArrayStack

class BSTNode:
        def __init__(self, key, left=None, right=None, parent = None):
                self.key = key
                self.left = left
                self.right = right
                self.parent = parent
                
def less_than(x, y):
        return x < y

class BinarySearchTree:
        def __init__(self, root = None, less=less_than):
                self.root = root
                self.less = less

        
        def minimum( self, n ) : 
                if n.left: 
                        return self.minimum( n.left )
                else: 
                        return n
                        
        def maximum ( self, n ):
                if n.right:
                        return self.maximum( n.right )
                else:
                        return n
                
        def greatest_parent( self, n ):
                parent = n.parent
                if parent and n == parent.right:
                        return self.greatest_parent( parent )
                else: 
                        return parent
                
        def least_parent( self, n ):
                parent = n.parent
                if parent and n == parent.left:
                        return self.least_parent( parent )
                else:
                        return parent

        # takes value, returns node with key value
        def insert(self, k):
                new_node = BSTNode( k )
                
                
                if self.root == None:
                        self.root = new_node
                        return self.root
                        
                node = self.root
                
                
                while node :
                        
                        if self.less( k, node.key ):
                                
                                if node.left:
                                        node = node.left
                                
                                else:
                                        new_node.parent = node
                                        node.left = new_node
                                        return new_node
                        else:
                                
                                if node.right:
                                        node = node.right
                                
                                else: 
                                        new_node.parent = node
                                        node.right = new_node
                                        return new_node

                
        # takes node, returns node
        # return the node with the smallest key greater than n.key
        def successor(self, n):
                if n == self.maximum( self.root ) :
                        return None
                elif n.right :
                        return self.minimum( n.right )
                else:
                
                        return self.greatest_parent( n )
                        
        
        def predecessor(self, n):
                if n == self.minimum( self.root ):
                        return None
                elif n.left:
                        return self.maximum( n.left )
                else:
                        
                        return self.least_parent ( n )
        
        
        
        def search(self, k):
                
                if self.root == None:
                        return None
                else:
                        node = self.root
                
                
                while node:
                        
                        if node.key == k:
                                return node
                        
                        elif self.less( k, node.key ):
                                if node.left: 
                                        node = node.left
                                
                                else: 
                                        return None
                        
                        else:
                                if node.right :
                                        node = node.right
                                
                                else:
                                        return None
            
        
        def delete_node(self, n):
                if self.root == n:
                        self.root = self.successor( n )
                
                
                if n.left and n.right:
                        
                        temp = self.successor( n )
                        
                        if temp == n.right:
                                temp.left = n.left
                                temp.parent = n.parent
                        
                        elif temp.right:
                                temp.right.parent = temp.parent
                                temp.parent.left = temp.right
                                temp.parent = n.parent
                                temp.left = n.left
                                temp.right = n.right
                        
                        if n.parent.left == n:
                                n.parent.left = temp
                        else:
                                n.parent.right = temp
                        
                        n.left = None
                        n.right = None
                        n.parent = None
                        return n
                                        
                   
                elif n.left:
                        if n == self.root:
                                self.root = n.left
                          
                        n.left.parent = n.parent
                        
                        if n.parent.left == n:
                                n.parent.left = n.left
                        else:
                                n.parent.right = n.left
                        
                        n.left = None
                        n.parent = None
                        return n
                
                   
                elif n.right:
                        if n == self.root:
                                self.root = n.right
                        
                        n.right.parent = n.parent
                        
                        if n.parent.left == n:
                                n.parent.left = n.right
                        else:
                                n.parent.right = n.right
                        
                        n.right = None
                        n.parent = None
                        return n
                
                     
                else:
                        if n == self.root:
                                self.root = None
                        
                        if n.parent.left == n:
                                n.parent.left = None
                        else:
                                n.parent.right = None
                        n.parent = None
                        
                        return n