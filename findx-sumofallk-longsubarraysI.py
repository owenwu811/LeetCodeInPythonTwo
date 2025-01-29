#3318
#easy

#You are given an array nums of n integers and two integers k and x.

#The x-sum of an array is calculated by the following procedure:

#Count the occurrences of all elements in the array.
#Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
#Calculate the sum of the resulting array.
#Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

#Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the 
#subarray
# nums[i..i + k - 1].

 

#Example 1:

#Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

#Output: [6,10,12]

#Explanation:

#For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
#For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
#For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.


#my own solution using python3:

#lots of requirements for this one

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        windowlen = k
        for i in range(len(nums) - windowlen + 1):
            subarr = nums[i: i + windowlen]
            print(subarr)
            d = defaultdict(int)
            for s in subarr:
                d[s] += 1
            d = sorted(d.items(), key=lambda x: (x[1], x[0]), reverse=True)
            print(d)
            now = 0
            cur = d[:x]
            for c in cur:
                now += (c[0] * c[1])
            res.append(now)
        return res
            
