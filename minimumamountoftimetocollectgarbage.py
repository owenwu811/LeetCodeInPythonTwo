#2391
#medium

#You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. Picking up one unit of any type of garbage takes 1 minute.

#You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.

#There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house.

#Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything.

#Return the minimum number of minutes needed to pick up all the garbage.

 

#Example 1:

#Input: garbage = ["G","P","GP","GG"], travel = [2,4,3]
#Output: 21


#my own solution using python3:


#this one involved a lot of trail and error since there were a lot of nasty edge cases

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        #["MMM","PGM","GP"]
        #      3     10


        #METAL
    
        #MMM
        #3

        #from MMM to PGM is 3

        #PGM > pick up one metal is 1


        #total metal count is 7

        #PAPER

        #PGM 
        #from MMM to PGM is 3

        #pick up P takes 1

        #from PGM to GP is 10

        #pick up P from GP is 1

        #GLASS


        #from MMM to PGM (3)

        #pick up 1 G from PGM (1)

        #from PGM to GP (10)

        #pick up 1 G from GP (1)




        #37



        #["G","M"]
        #    1

        #3
        finalorig = travel.copy()
        orig = travel.copy()
        origtwo = []
        for t in travel:
            origtwo.append(t)
        totalmetal, totalpaper, totalglass = 0, 0, 0
        for g in garbage:
            for i in range(len(g)):
                if g[i] == "M":
                    totalmetal += 1
                if g[i] == "P":
                    totalpaper += 1
                if g[i] == "G":
                    totalglass += 1
        finishm, finishp, finishg = [], [], []
        curmetal, curpaper, curglass = 0, 0, 0
        resone, restwo, resthree = 0, 0, 0
        #metal
        for i, g in enumerate(garbage):
            for j in range(len(g)):
                if g[j] == "M":
                    curmetal += 1
                if curmetal == totalmetal:
                    finishm.append(i)
        print(finishm)
        if finishm:
            farthestm = min(finishm)
        if farthestm:
            metaltot = 0 #total cost 
            travel = deque(travel)
            for i, g in enumerate(garbage):
                if i >= 1:
                    if travel:
                        a = travel.popleft()
                        metaltot += a
                for j in range(len(g)):
                    if g[j] == "M":
                        metaltot += 1
                print(metaltot, i)
                if i == farthestm:
                    break 
            resone = metaltot
            print(metaltot, "endmetal")
        
        #glass
        
        for i, g in enumerate(garbage):
            for j in range(len(g)):
                if g[j] == "G":
                    curglass += 1
                if curglass == totalglass:
                    finishg.append(i)
        if finishg:
            farthestg = min(finishg)
        if farthestg:
            print(farthestg)
            glasstot = 0 #total cost 
            travel = deque(orig)
            print(travel, "wert")
            for i, g in enumerate(garbage):
                if i >= 1:
                    if travel:
                        a = travel.popleft()
                        glasstot += a
                for j in range(len(g)):
                    if g[j] == "G":
                        glasstot += 1
                if i == farthestg:
                    print(i, glasstot)
                    break 
            restwo = glasstot
            print(glasstot, "endglass")
            print(origtwo, "wt")
        
        #paper
        for i, g in enumerate(garbage):
            for j in range(len(g)):
                if g[j] == "P":
                    curpaper += 1
                if curpaper == totalpaper:
                    finishp.append(i)
        if finishp:
            farthestp = min(finishp)
        if farthestp:
            papertot = 0
            travel = deque(origtwo)
            print(travel)
            for i, g in enumerate(garbage):
                if i >= 1:
                    if travel:
                        a = travel.popleft() 
                        papertot += a
                for j in range(len(g)):
                    if g[j] == "P":
                        papertot += 1
                if i == farthestp:
                    break
            resthree = papertot
            print(papertot, "endpaper")
        together = resone + restwo + resthree
        print(finalorig)
        cnt = 0
        seen = set()
        for g in garbage:
            if len(g) == 1 and g[0] not in seen:
                cnt += 1
                seen.add(g[0])
        if cnt == len(garbage):
            return together + 1
        

        return together 
