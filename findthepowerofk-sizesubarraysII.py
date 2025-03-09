
#3255
#medium

#You are given an array of integers nums of length n and a positive integer k.

#The power of an array is defined as:

#Its maximum element if all of its elements are consecutive and sorted in ascending order.
#-1 otherwise.
#You need to find the power of all subarrays of nums of size k.

#Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

 

#Example 1:

#Input: nums = [1,2,3,4,3,2,5], k = 3

#Output: [3,4,-1,-1,-1]


#my own solution using python3:

#very messy but lots of trial and error lead to a slow but working solution - the idea is to precompute any violation of consecutive order, and then check if the current k size subarray has a violation using a dictionary and a sorted list to check the frequency and then find the maximum element of the k size subarray

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        size = k
        res = []
        status = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                status.append("g")
            else:
                status.append("b")
        sl = SortedList(nums[:size])
        print(status)
        c = Counter(status[:size - 1])
        #['g', 'g'] Counter({'g': 1, 'b': 1})
        #['g', 'g'] Counter({'b': 2})
        #['g', 'b'] Counter({'b': 3, 'g': -1})
        #['b', 'b'] Counter({'b': 2, 'g': -1})
        #['b', 'b'] Counter({'b': 1, 'g': -1})
        for i in range(len(nums) - size + 1):
            #cur = status[i: i + size - 1]
            #print(cur, c, i, i + size - 1)
            #c[status[i]] -= 1
            #if c[status[i]] == 0:
            #    del c[status[i]]
            #if i + size - 1 < len(status):
            #    c[status[i + size - 1]] += 1
            before = i
            after = i + size - 1

            if after - before <= 0:
                res.append(sl[-1])
            #print(cur, c)
            elif "b" in c:
                res.append(-1)
            else:
                res.append(sl[-1])
            sl.remove(nums[i])
            if i + size < len(nums):
                sl.add(nums[i + size])
            if i >= 0 and i < len(status):
                if status[i] in c:
                    c[status[i]] -= 1
                if c[status[i]] == 0:
                    del c[status[i]]
                if i + size - 1 < len(status):
                    c[status[i + size - 1]] += 1
            
        return res

        #SortedList([1, 2, 3]) [1, 2, 3]
        #0 1 now
        #SortedList([2, 2, 3]) [2, 3, 4]
        #1 2 now
        #SortedList([2, 3, 3]) [3, 4, 3]
        #2 3 now
        #SortedList([2, 3, 4]) [4, 3, 2]
        #3 4 now
        #SortedList([2, 3, 3]) [3, 2, 5]
        #4 5 now
