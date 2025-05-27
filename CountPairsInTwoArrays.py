
#1885
#medium

#Given two integer arrays nums1 and nums2 of length n, count the pairs of indices (i, j) such that i < j and nums1[i] + nums1[j] > nums2[i] + nums2[j].

#Return the number of pairs satisfying the condition.

 

#Example 1:

#Input: nums1 = [2,1,2,1], nums2 = [1,2,1,2]
#Output: 1
#Explanation: The pairs satisfying the condition are:
#- (0, 2) where 2 + 2 > 1 + 1.
#Example 2:

#Input: nums1 = [1,10,6,2], nums2 = [1,4,1,5]
#Output: 5
#Explanation: The pairs satisfying the condition are:
#- (0, 1) where 1 + 10 > 1 + 4.
#- (0, 2) where 1 + 6 > 1 + 1.
#- (1, 2) where 10 + 6 > 4 + 1.
#- (1, 3) where 10 + 2 > 4 + 5.
#- (2, 3) where 6 + 2 > 1 + 5.

#my own solution using python3:

#think about nums1i - nums2i, and then finding a same one to the right that, when added with current nums1i - nums2i, is bigger than 0

class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        #nums1j > nums2i + nums2j - nums1i
        #nums1j > nums2i - nums1i + nums2j
        cur = []
        ans = 0
        for i, n in enumerate(nums2):
            cur.append(nums1[i] - nums2[i])
        #5 1
        #1 3
        #4 
        sl = SortedList(cur)
        #print(sl)
        for i in range(len(nums1)):
            diff = nums1[i] - nums2[i]
            sl.discard(diff)
            del cur[0]
            bl = bisect_right(sl, -diff)
            if bl < len(sl):
                #print(diff, sl, bl)
                ans += (len(sl) - bl)
            #for a in cur:
            #    if diff + a > 0:
            #        ans += 1
        return ans
