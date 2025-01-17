#2070
#medium

#You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.

#You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.

#Return an array answer of the same length as queries where answer[j] is the answer to the jth query.

 

#Example 1:

#Input: items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
#Output: [2,4,5,5,6,6]
#Explanation:
#- For queries[0]=1, [1,2] is the only item which has price <= 1. Hence, the answer for this query is 2.
#- For queries[1]=2, the items which can be considered are [1,2] and [2,4]. 
#  The maximum beauty among them is 4.
# For queries[2]=3 and queries[3]=4, the items which can be considered are [1,2], [3,2], [2,4], and [3,5].
#  The maximum beauty among them is 5.
#- For queries[4]=5 and queries[5]=6, all items can be considered.
#  Hence, the answer for them is the maximum beauty of all items, i.e., 6.


#my own solution using python3:

#use binary search during each iteration to get the optimal pivot point

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        #[price, beauty]

        #each q > max beauty price <= q
        d = defaultdict(list)
        for i in items:
            heapq.heappush(d[i[0]], i[1])
        d = dict(sorted(d.items(), key=lambda x: x[0]))
        cur = 0
        newd = dict()
        for k in d:
            cur = max(cur, d[k][-1])
            newd[k] = cur
        print(newd)
        #[1, 2, 3, 5]
        #4 > 3
        ans = []
        a = sorted(list(d.keys()))
        for q in queries:
            biggest = float('-inf')
            l, r = 0, len(a) - 1
            now = []
            while l <= r:
                mid = (l + r) // 2
                #print(a[mid])
                if a[mid] <= q:
                    now.append(a[mid])
                    l = mid + 1
                elif a[mid] > q:
                    r = mid - 1
                #print(a[mid], q, "mid, q")
            print(now)
            if now:
                ans.append(newd[now[-1]])
            else:
                ans.append(0)
        return ans
