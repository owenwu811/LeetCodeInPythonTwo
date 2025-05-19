#2179
#hard

#You are given two 0-indexed arrays nums1 and nums2 of length n, both of which are permutations of [0, 1, ..., n - 1].

#A good triplet is a set of 3 distinct values which are present in increasing order by position both in nums1 and nums2. In other words, if we consider pos1v as the index of the value v in nums1 and pos2v as the index of the value v in nums2, then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.

#Return the total number of good triplets.

 

#Example 1:

#Input: nums1 = [2,0,1,3], nums2 = [0,1,2,3]
#Output: 1
#Explanation: 
#There are 4 triplets (x,y,z) such that pos1x < pos1y < pos1z. They are (2,0,1), (2,0,3), (2,1,3), and (0,1,3). 
#Out of those triplets, only the triplet (0,1,3) satisfies pos2x < pos2y < pos2z. Hence, there is only 1 good triplet.


#my own solution using python3:

#sorted list and find how many elements smaller to left and bigger to right and multiply lengths

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        left = []
        right = []
        d = dict()
        for i, n in enumerate(nums2):
            d[n] = i
        ans = 0
        left.append(d[nums1[0]])
        for i in range(1, len(nums1)):
            n = nums1[i]
            bl = bisect_left(right, d[n])
            right.insert(bl, d[n])
        for i in range(1, len(nums1) - 1):
            bl = bisect_left(right, d[nums1[i]])
            del right[bl]
            cur = d[nums1[i]]
            if left[0] < cur:
                #print(left, cur, right)
                bl = bisect_left(left, cur) 
                br = bisect_right(right, cur) 
                #print(left[:bl], cur, right[br:])
                ans += (bl * (len(right) - br))
            bl = bisect_left(left, d[nums1[i]])
            left.insert(bl, d[nums1[i]])
        return ans
