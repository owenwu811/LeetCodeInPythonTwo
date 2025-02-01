#2641
#medium

#Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

#Two nodes of a binary tree are cousins if they have the same depth with different parents.

#Return the root of the modified tree.

#Note that the depth of a node is the number of edges in the path from the root node to it.

#Input: root = [5,4,9,1,10,null,7]
#Output: [0,0,0,7,7,null,11]
#Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
#- Node with value 5 does not have any cousins so its sum is 0.
#- Node with value 4 does not have any cousins so its sum is 0.
#- Node with value 9 does not have any cousins so its sum is 0.
#- Node with value 1 has a cousin with value 7 so its sum is 7.
#- Node with value 10 has a cousin with value 7 so its sum is 7.
#- Node with value 7 has cousins with values 1 and 10 so its sum is 11.





#my own solution using python3:

#get each level sum and then match each level in the res to the current level of the tree starting from index 0 so you don't mess up future values 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d = deque()
        d.append(root)
        res = []
        while d:
            level = []
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    level.append(cur.val)
                    d.append(cur.left)
                    d.append(cur.right)
            if level:
                res.append(sum(level))
        print(res)
        #[5, 13, 18]
        d = deque()
        d.append([root, 0])
        while d:
            for i in range(len(d)):
                cur, lev = d.popleft()
                if cur:
                    #print(cur.val, lev)
                    if lev >= 1:
                        #print(cur.val, lev)
                        cursum = 0
                        if cur.left:
                            cursum += cur.left.val
                        if cur.right:
                            cursum += cur.right.val
                        if lev + 1 < len(res):
                            print(cursum, lev + 1)
                        if cur.left:
                            cur.left.val = res[lev + 1] - cursum 
                        if cur.right:
                            cur.right.val = res[lev + 1] - cursum
                    if lev == 0 or lev == 1:
                        cur.val = 0
                    d.append([cur.left, lev + 1])
                    d.append([cur.right, lev + 1])
        return root
            
