
#547
#medium

#There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

#A province is a group of directly or indirectly connected cities and no other cities outside of the group.

#You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

#Return the total number of provinces.


#my own solution using python3:

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        d = defaultdict(list)
        for i in range(len(isConnected)):
            now = []
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    now.append(j)
            d[tuple(now)].append(isConnected[i])
        keys = list(d.keys())
        #print(keys)
        kk = []
        for key in keys:
            kk.append(set(key))
        for i in range(len(kk)):
            for j in range(len(kk)):
                
                if len(kk[i].intersection(kk[j])) >= 1:
                    if j != i and kk[j]:
                        kk[i] |= kk[j]
                         
                       
        #print(kk)
        j = []
        for fuck in kk:
            if fuck not in j:
                j.append(fuck)
        #print(j)
        for a in range(len(j)):
            for b in range(len(j)):
                if b != a:
                    if len(j[a].intersection(j[b])) >= 1:
                        j[a] |= j[b]
        print(j)
        y = []
        for u in j:
            if u not in y:
                y.append(u)
        return len(y)
         
