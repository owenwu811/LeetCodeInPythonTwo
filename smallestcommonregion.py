#1257
#medium


#You are given some lists of regions where the first region of each list includes all other regions in that list.

#Naturally, if a region x contains another region y then x is bigger than y. Also, by definition, a region x contains itself.

#Given two regions: region1 and region2, return the smallest region that contains both of them.

#If you are given regions r1, r2, and r3 such that r1 includes r3, it is guaranteed there is no r2 such that r2 includes r3.

#It is guaranteed the smallest region exists.

 

#Example 1:

#Input:
#regions = [["Earth","North America","South America"],
#["North America","United States","Canada"],
#["United States","New York","Boston"],
#["Canada","Ontario","Quebec"],
#["South America","Brazil"]],
#region1 = "Quebec",
#region2 = "New York"
#Output: "North America"

#my own solution using python3:

#just use dfs and union find

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        d = dict()
        for r in regions:
            d[r[0]] = r[1:]
        sl = SortedList()
        def dfs(a, seen):
            for h in d[a]:
                if h in d:
                    seen.add(h)
                    dfs(h, seen)
        for k in d:
            cur = k
            seen = set()
            seen.add(cur)
            for a in d[k]:
                if a in d:
                    seen.add(a)
                    dfs(a, seen)
            now = set()
            for s in seen:
                if s in d:
                    now.update(set(d[s]))
            if region1 in now and region2 in now or region1 == cur and region2 in now or region2 == cur and region1 in now:
                print(cur, now)
                sl.add((len(now), cur))
        return sl[0][1]
