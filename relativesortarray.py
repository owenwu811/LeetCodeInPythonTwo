
#1122
#easy

#Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

#Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 

#Example 1:

#Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
#Output: [2,2,2,1,4,3,3,9,6,7,19]
#Example 2:

#Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
#Output: [22,28,8,6,17,44]

#my own solution using python3:


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for a in arr2:
            cur = arr1.count(a)
            while cur > 0:
                res.append(a)
                cur -= 1
        print(res)
        diff = []
        for a in arr1:
            if a not in res:
                diff.append(a)
        diff.sort()
        print(diff)
        res.extend(diff)
        return res
