#binary tree

class tree:
    def __init__(self):
        self.root = None
    def addval(self, v):
        n = Node(v)
        if self.root == None:
            self.root = n
        else:
            self.root.addnode(n)

    def sort(self):
        self.root.sort2(self.root)


class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right= None
    def addnode(self, v):
        if self.val > v.val:
            if self.left == None:
                self.left = v
            else:
                self.left.addnode(v)
        elif self.val < v.val:
            if self.right ==None:
                self.right = v
            else:
                self.right.addnode(v)
    def sort2(self,b):
        if b.left != None:
            b.sort2(b.left)
        print(b.val)
        if b.right != None:
            b.sort2(b.right)
            
            
            
tree = tree()
tree.addval(8)
tree.addval(3)
tree.addval(1)
tree.addval(6)
tree.addval(4)
tree.addval(7)
tree.addval(10)
tree.addval(14)
tree.addval(13)
tree.sort()
############5
##########4###6
########2####x###8

