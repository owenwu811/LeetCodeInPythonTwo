#2196
#medium

#You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

#If isLefti == 1, then childi is the left child of parenti.
#If isLefti == 0, then childi is the right child of parenti.
#Construct the binary tree described by descriptions and return its root.

#The test cases will be generated such that the binary tree is valid.



#my own solution using python3:

#use a hashmap and do a level order by setting each node's left and right child, and then don't include the leaf nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        myd = defaultdict(list)
        notroots = []
        noleafs = []
        totalnodes = []
        for d in descriptions:
            myd[d[0]].append([d[1], d[2]])
            totalnodes.append(d[0])
            totalnodes.append(d[1])
            notroots.append(d[1])
        print(myd)
        rootval = []
        for a in myd:
            if a not in notroots:
                rootval.append(a)
                break
        print(rootval)
        leaves = []
        for t in totalnodes:
            if t not in myd:
                leaves.append(t)
        print(leaves)
        root = TreeNode(rootval[0])
        d = deque()
        d.append(root)
        while d:
            cur = d.popleft() 
            if cur:
                print(cur.val)
                if cur.val in myd:
                    print(myd[cur.val])
                    for a in myd[cur.val]:
                        if a[1] == 1:
                            cur.left = TreeNode(a[0])
                            d.append(cur.left)
                        if a[1] == 0:
                            cur.right = TreeNode(a[0])
                            d.append(cur.right)
        return root
 
