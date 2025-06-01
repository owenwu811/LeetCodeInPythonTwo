#2471
#medium

#You are given the root of a binary tree with unique values.

#In one operation, you can choose any two nodes at the same level and swap their values.

#Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

#The level of a node is the number of edges along the path between it and the root node.

#my own solution using python3:

#scan the unsorted array from left to right, and try to find the correct element on the right side and swap

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        d = deque()
        d.append(root)
        levels = []
        cur = []
        c = []
        res = 0
        while d:
            level = []
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    level.append(cur.val)
                    d.append(cur.left)
                    d.append(cur.right)
            if level:
                levels.append(level)
                c.append(sorted(level))
        for u, l in enumerate(levels):
            key = c[u]
            d = dict()
            for i, v in enumerate(l):
                d[v] = i
            if l != key:
                ans = 0
                for i in range(len(l)):
                    if l[i] != key[i]:
                        if d[key[i]] > i:
                            idx = d[key[i]]
                            beforel = l[i]
                            #print(d)
                            #print(i, idx)
                            bv = l[i]
                            br = l[idx]
                            #print(bv, br)
                            l[i], l[idx] = l[idx], l[i]
                            d[bv] = idx
                            d[br] = i

                            ans += 1
                        #for y in range(i + 1, len(l)):
                        #    if l[y] == key[i]:
                        #        l[i], l[y] = l[y], l[i]
                        #        ans += 1
                        #        break
                res += ans

        return res
