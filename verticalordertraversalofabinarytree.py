
#987
#Hard

#Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

#For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

#The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

#Return the vertical order traversal of the binary tree.



#my own solution using python3:

#use dictionaries to keep track of the coordinate and then another dictionary to keep track of how to sort each level according to its row

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = deque()
        d.append([root, 0, 0])
        mydict = defaultdict(list)
        secondd = defaultdict(list)
        if root:
            mydict[0].append(root.val)
            secondd[root.val].append([0, 0])
        while d:
            for i in range(len(d)):
                cur, x, y = d.popleft()
                if cur:
                    #print(cur.val)
                    if cur.left:
                        d.append([cur.left, x + 1, y - 1])
                        mydict[y - 1].append(cur.left.val)
                        secondd[cur.left.val].append([x + 1, y - 1])
                    if cur.right:
                        d.append([cur.right, x + 1, y + 1])
                        mydict[y + 1].append(cur.right.val)
                        secondd[cur.right.val].append([x + 1, y + 1])
        print(secondd)
        m = dict(sorted(mydict.items(), key=lambda x: x[0]))
        res = []
        for k in m:
            res.append(m[k])
        print(res)
        ans = []
        for r in res:
            new = []
            td = defaultdict(list)
            for c in r:
                if c in secondd:
                    #print(secondd[c])
                    h = tuple(secondd[c][0])
                    #print(h)
                    td[h].append(c)
            print(td)
            print(r)
            a = []
            for t in td:
                a.extend(sorted(td[t]))
            print(a)
            ans.append(a)
        print(ans)
            


                    #td[tuple(secondd[c])].append(c)
    
                    

        return ans
                 
