#323
#medium

#You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

#Return the number of connected components in the graph.

#correct python3 solution (could not solve - come back to later!):


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])
        seen = set()
        ans = 0
        def dfs(i):
            seen.add(i)
            for nei in d[i]:
                if nei not in seen:
                    #seen.add(nei)
                    dfs(nei)
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans
