#2931
#hard

#You are given a 0-indexed m * n integer matrix values, representing the values of m * n different items in m different shops. Each shop has n items where the jth item in the ith shop has a value of values[i][j]. Additionally, the items in the ith shop are sorted in non-increasing order of value. That is, values[i][j] >= values[i][j + 1] for all 0 <= j < n - 1.

#On each day, you would like to buy a single item from one of the shops. Specifically, On the dth day you can:

#Pick any shop i.
#Buy the rightmost available item j for the price of values[i][j] * d. That is, find the greatest index j such that item j was never bought before, and buy it for the price of values[i][j] * d.
#Note that all items are pairwise different. For example, if you have bought item 0 from shop 1, you can still buy item 0 from any other shop.

#Return the maximum amount of money that can be spent on buying all m * n products.

 

#Example 1:

#Input: values = [[8,5,2],[6,4,1],[9,7,3]]
#Output: 285


#my own solution using python3:

#just do 1.2.3..4 times the numbers in order with no duplicates


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        ans = 0
        #rows = shops
        #each row has n items
        sl = SortedList()
        for i in range(len(values)):
            for j in range(len(values[i])):
                #if values[i][j] not in sl:
                sl.add(values[i][j])
        print(sl)
        cnt = 1
        for s in sl:
            ans += (s * cnt)
            cnt += 1
        return ans
