#1095
#hard

#(This problem is an interactive problem.)

#You may recall that an array arr is a mountain array if and only if:

#arr.length >= 3
#There exists some i with 0 < i < arr.length - 1 such that:
#arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

#You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

#MountainArray.get(k) returns the element of the array at index k (0-indexed).
#MountainArray.length() returns the length of the array.
#Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

#Example 1:

#Input: mountainArr = [1,2,3,4,5,3,1], target = 3
#Output: 2
#Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.


#my own solution using python3:

#use binary search to find the peak and then do left and right of peak in ascending and descending order

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l, r = 0, mountainArr.length() - 1
        ans = float('inf')
        sl = SortedList()
        while l < r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)
            sl.add((val, mid))
            if mountainArr.get(mid) == target:
                ans = min(ans, mid)
            if mid - 1 >= 0:
                if mountainArr.get(mid - 1) == target:
                    ans = min(ans, mid - 1)
            if mid + 1 < mountainArr.length():
                if mountainArr.get(mid + 1) == target:
                    ans = min(ans, mid + 1)
            if mountainArr.get(l) < mountainArr.get(r):
                l = mid + 1
            else:
                r = mid - 1
        peakidx = sl[-1][-1]
        peakval = sl[-1][0]
        if peakval > target:
            ll, rr = 0, peakidx
            while ll <= rr:
                mid = (ll + rr) // 2
                val = mountainArr.get(mid)
                if val == target:
                    ans = min(ans, mid)
                    break
                if val > target:
                    rr = mid - 1
                else:
                    ll = mid + 1
            l, r = peakidx, mountainArr.length() - 1
            while l <= r:
                mid = (l + r) // 2
                val = mountainArr.get(mid)
                if val == target:
                    ans = min(ans, mid)
                    break
                if val > target:
                    l = mid + 1
                else:
                    r = mid - 1
            
        else:
            l, r = peakidx, mountainArr.length() - 1
            while l <= r:
                mid = (l + r) // 2
                val = mountainArr.get(mid)
                if val == target:
                    ans = min(ans, mid)
                    break
                if val > target:
                    r = mid - 1
                else:
                    l = mid + 1
        if ans == float('inf'):
            return -1
        return ans
