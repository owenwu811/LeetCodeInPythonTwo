#250
#medium

#Given the root of a binary tree, return the number of uni-value 
#subtrees
#.
#
#A uni-value subtree means all nodes of the subtree have the same value.



#correct python3 solution (could not solve):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def f(root):
            if not root:
                return True
            l = f(root.left)
            r = f(root.right)
            if l and r:
                if root and root.left:
                    if root.val != root.left.val:
                        return False
                if root and root.right:
                    if root.val != root.right.val:
                        return False
                self.res += 1
                return True
            return False


        f(root)
        return self.res
