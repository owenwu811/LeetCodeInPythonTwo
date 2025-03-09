
#1609
#medium

#A binary tree is named Even-Odd if it meets the following conditions:

#The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
#For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
#For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
#Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.


#my own solution using python3 on 3/5/25 - originally solved on August 10, 2024 but did not create the file:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        d = deque()
        d.append(root)
        idx = 0
        while d:
            level = []
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    level.append(cur.val)
                    d.append(cur.left)
                    d.append(cur.right)
            if level:
                print(level, idx)
                if idx % 2 == 0:
                    for j in range(len(level)):
                        
                        if level[j] % 2 == 0:
                            return False
                    if level != sorted(level) or len(set(level)) != len(level):
                        return False
                else:
                    for j in range(len(level)):
                        
                        if level[j] % 2 != 0:
                            return False
                    if level != sorted(level, reverse=True) or len(set(level)) != len(level):
                        return False



            idx += 1
        return True


