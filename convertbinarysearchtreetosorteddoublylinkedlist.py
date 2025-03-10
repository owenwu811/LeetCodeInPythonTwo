#426
#medium

#Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

#You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

#We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.


#correct python3 solution (could not solve):

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.cur = []
        def f(root):
            if not root:
                return 
            f(root.left)
            self.cur.append(root)
            f(root.right)
        f(root)
        if not self.cur:
            return None  
        cur = self.cur.copy()
        c = len(cur)
        for i in range(c):
            if i - 1 < 0:
                cur[i].left = cur[-1]
            else:
                cur[i].left = cur[i - 1]
            if i + 1 >= len(self.cur):
                cur[i].right = cur[0]
            else:
                cur[i].right = cur[i + 1]
        return cur[0]
