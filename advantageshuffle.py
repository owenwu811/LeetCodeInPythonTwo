#870
#medium

#You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

#Return any permutation of nums1 that maximizes its advantage with respect to nums2.

 

#Example 1:

#Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
#Output: [2,11,7,15]
#Example 2:

#Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
#Output: [24,32,8,12]


#my own solution using python3:

#sort with respect to values and indicies

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new = [(n, i) for i, n in enumerate(nums1)]
        print(new)
        ans = []
        sl = SortedList()
        for n in new:
            sl.add(n[0])
        for num in nums2:
            b = bisect_right(sl, num)
            #print(sl, b)
            if b < len(sl):
                print(sl[b])
                ans.append(sl[b])
                del sl[b]
            else:
                print(sl[0])
                ans.append(sl[0])
                del sl[0]
        return ans
