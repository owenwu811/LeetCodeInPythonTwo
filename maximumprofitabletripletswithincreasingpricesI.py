
#2907
#medium

#Given the 0-indexed arrays prices and profits of length n. There are n items in an store where the ith item has a price of prices[i] and a profit of profits[i].

#We have to pick three items with the following condition:

#prices[i] < prices[j] < prices[k] where i < j < k.
#If we pick items with indices i, j and k satisfying the above condition, the profit would be profits[i] + profits[j] + profits[k].

#Return the maximum profit we can get, and -1 if it's not possible to pick three items with the given condition.

 

#Example 1:

#Input: prices = [10,2,3,4], profits = [100,2,7,10]
#Output: 19
#Explanation: We can't pick the item with index i=0 since there are no indices j and k such that the condition holds.
#So the only triplet we can pick, are the items with indices 1, 2 and 3 and it's a valid pick since prices[1] < prices[2] < prices[3].
#The answer would be sum of their profits which is 2 + 7 + 10 = 19.



#my own messy but working solution using python3:

class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        if len(prices) < 100 and len(profits) < 100:
            res = 0
            p = len(prices)
            for i in range(p):
                for j in range(i + 1, p):
                    for k in range(j + 1, p):
                        if prices[i] < prices[j] < prices[k]:
                            cursum = profits[i] + profits[j] + profits[k]
                            if cursum >= res:
                                res = cursum
            if res == 0:
                return -1
            return res

        d = defaultdict(SortedList)
        for i, p in enumerate(prices):
            d[p].add(profits[i])
        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        #print(d)
        #prices [1,6,3,6]
        #profits [74,33,48,32]

        #{1: [74], 3: [48], 6: [32, 33]}
        #[1] [6] 3
        #[74]
        #[32, 33]


        #[5,2,10,5,9]
        #[50,6,25,1,35]
        #{9: SortedList([(35, 4)]), 10: SortedList([(25, 2)]), 2: SortedList([(6, 1)]), 5: SortedList([(1, 3), (50, 0)])} [2] 5 [9]
        res = 0
        lefts, rights = SortedList(), SortedList(prices)
        for i in range(len(prices)):
            #lefts.add(prices[i])
            rights.remove(prices[i])
            if lefts and rights:
                if lefts[0] < prices[i] < rights[-1]:
                    #print(lefts, rights, prices[i])
                    bl = bisect_left(lefts, prices[i])
                    br = bisect_right(rights, prices[i])
                    #print(bl, br)
                    ll = lefts[:bl]
                    rr = rights[br:]
                    #print(ll, prices[i], rr)
                    cur = d[prices[i]][-1]
                    maxl = 0
                    for l in ll:

                        maxl = max(maxl, d[l][-1])
                    maxr = 0
                    for r in rr:
                        maxr = max(maxr, d[r][-1])
                    res = max(res, maxl + cur + maxr)
            lefts.add(prices[i])
        if res == 0:
            return -1
        return res
