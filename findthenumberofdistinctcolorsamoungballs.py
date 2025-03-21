#3160
#medium


#dumbest fucking question where an o(n) gets memory limit exceeded:

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        d = dict()
        for i in range(limit + 1):
            d[i] = float('inf')
        start = 0
        cd = dict()
        res = []
        for q in queries:
            a = cd.get(d[q[0]], None)
            if a:
                cd[d[q[0]]] -= 1
                if cd[d[q[0]]] == 0:
                    start -= 1
                    del cd[d[q[0]]]
            d[q[0]] = q[1]
            if q[1] not in cd:
                start += 1
                cd[q[1]] = 1
            else:
                cd[q[1]] += 1
            res.append(start)
        return res

#you have to resort to this to pass:


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        d = dict()
        start = 0
        cd = dict()
        res = []
        for turn, (idx, value) in enumerate(queries):
            prev = d.get(idx, None)
            if prev is not None:
                cd[prev] -= 1
                if cd[prev] == 0:
                    start -= 1
                    del cd[prev]
            d[idx] = value
            if value not in cd:
                start += 1
                cd[value] = 1
            else:
                cd[value] += 1
            res.append(start)
        return res
