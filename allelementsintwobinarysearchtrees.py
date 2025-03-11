
#1305
#medium

#Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

#Input: root1 = [2,1,4], root2 = [1,0,3]
#Output: [0,1,1,2,3,4]


#my own solution using python3 on 3/10/25 (originall solved in August of 2024 but forgot to create the file):

#get all nodes from both trees, put them in a list, sort that list, and return the list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        self.res = []
        def f(root1):
            if not root1:
                return None
            self.res.append(root1.val)
            f(root1.left)
            f(root1.right)
        f(root1)
        def f(root2):
            if not root2:
                return None
            self.res.append(root2.val)
            f(root2.left)
            f(root2.right)
        f(root2)
        self.res.sort()
        return self.res
