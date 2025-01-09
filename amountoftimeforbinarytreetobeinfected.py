#2385
#medium

#You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

#Each minute, a node becomes infected if:

#The node is currently uninfected.
#The node is adjacent to an infected node.
#Return the number of minutes needed for the entire tree to be infected.



#my own solution using python3 after checking out chatgpt's solution: (could not solve):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        d = defaultdict(list)
        def f(root):
            if not root:
                return 
            if root.left:
                d[root.val].append(root.left.val)
                d[root.left.val].append(root.val)
            if root.right:
                d[root.val].append(root.right.val)
                d[root.right.val].append(root.val)
            f(root.left)
            f(root.right)
        f(root)
        print(d)
        res = -1
        q = deque()
        seen = set()
        q.append(start)
        seen.add(start)
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                for a in d[cur]:
                    if a not in seen:
                        q.append(a)
                    seen.add(a)
            res += 1
        return res
