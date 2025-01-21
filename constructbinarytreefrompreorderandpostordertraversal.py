#889
#medium

#Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

#If there exist multiple answers, you can return any of them.



#correct python3 solution (could not solve):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #[1,2,4,5,3,6,7]
        #[4,5,2,6,7,3,1]
        if not preorder or not postorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        leftsubtreeroot = preorder[1]
        leftsubtreesize = postorder.index(leftsubtreeroot) + 1
        root.left = self.constructFromPrePost(preorder[1:leftsubtreesize + 1], postorder[:leftsubtreesize])
        root.right = self.constructFromPrePost(preorder[leftsubtreesize + 1:], postorder[leftsubtreesize:-1])
        return root
