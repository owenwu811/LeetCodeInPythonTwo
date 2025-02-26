
#2615
#medium

#You are given a 0-indexed integer array nums. There exists an array arr of length nums.length, where arr[i] is the sum of |i - j| over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.

#Return the array arr.

 

#Example 1:

#Input: nums = [1,3,1,1,2]
#Output: [5,0,3,4,0]
#Explanation: 
#When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5. 
#When i = 1, arr[1] = 0 because there is no other index with value 3.
#When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3. 
#When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4. 
#When i = 4, arr[4] = 0 because there is no other index with value 2. 

#Example 2:

#Input: nums = [0,5,3]
#Output: [0,0,0]
#Explanation: Since each element in nums is distinct, arr[i] = 0 for all i.



#my own solution using python3:

#use two dictionaries: one for tracking indicies in order and another for accumulating the prefix sums of all indicies, and then use binary search on the corresponding element's value in both dictionaries as keys

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)
        pds = dict()
        for k in d:
            pds[k] = list(itertools.accumulate(d[k]))
        print(pds)
        res = []
        for i, n in enumerate(nums):
            now = 0
            p = pds[n]
            l = bisect_left(d[n], i)
            r = bisect_right(d[n], i)
            totlen = len(d[n])
            if l > 0:
                high = (i * l)
                low = p[l - 1]
                now += (high - low)
            if r < totlen:
                if r <= 0:
                    high = p[-1]
                else:
                    high = p[-1] - p[r - 1]
                low = ((totlen - r) * i)
                now += (high - low)
            res.append(now)
        return res
            
