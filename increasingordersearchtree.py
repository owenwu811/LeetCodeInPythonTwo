#897
#easy

#Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

#Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
#Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

#my own solution using python3:

#my idea is to get all node values in the tree, sort the list, and then reconstruct the tree in the fashion depicited in the picture: set the right child to whatever the next element in the deque is while setting the left child to None - keep doing this until the deque is empty, and then return the root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.cur = []
        def f(root):
            if not root:
                return 
            self.cur.append(root.val)
            f(root.left)
            f(root.right)


        f(root)
        self.cur.sort()
        print(self.cur)
        self.cur = deque(self.cur)
        node = TreeNode(self.cur.popleft())
        dummy = node
        while self.cur:
            node.right = TreeNode(self.cur.popleft())
            node.left = None 
            node = node.right
        return dummy
