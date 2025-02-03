#2368
#medium

#There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

#You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.

#Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.

#Note that node 0 will not be a restricted node.

#Input: n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
#Output: 4
#Explanation: The diagram above shows the tree.
#We have that [0,1,2,3] are the only nodes that can be reached from node 0 without visiting a restricted node.


#my own solution using python3:

#apply bfs and check if you can visit the current node or not

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        d = defaultdict(set)
        for e in edges:
            d[e[0]].add(e[1])
            d[e[1]].add(e[0])
        seen = set()
        r = set(restricted)
        seen.add(0)
        myd = deque([0])
        res = set()
        while myd:
            cur = myd.popleft()
            res.add(cur)
            seen.add(cur)
            for nei in d[cur]:
                if nei not in r and nei not in seen:
                    myd.append(nei)
                seen.add(nei)
        return len(res)
