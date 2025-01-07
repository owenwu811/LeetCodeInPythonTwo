#1485
#medium


#A binary tree is given such that each node contains an additional random pointer which could point to any node in the tree or null.

#Return a deep copy of the tree.

#The tree is represented in the same input/output way as normal binary trees where each node is represented as a pair of [val, random_index] where:

#val: an integer representing Node.val
#random_index: the index of the node (in the input) where the random pointer points to, or null if it does not point to any node.
#You will be given the tree in class Node and you should return the cloned tree in class NodeCopy. NodeCopy class is just a clone of Node class with the same attributes and constructors.


#correct python3 solution (could not solve):

# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        self.d = dict()
        def f(root):
            if not root:
                return 
            if root in self.d:
                return self.d[root]
            self.d[root] = NodeCopy(root.val)
            self.d[root].left = f(root.left)
            self.d[root].right = f(root.right)
            self.d[root].random = f(root.random)
            return self.d[root]
        return f(root)
