
#You are given a 1-indexed array of integers nums of length n.

#We define a function greaterCount such that greaterCount(arr, val) returns the number of elements in arr that are strictly greater than val.

#3072
#hard

#You need to distribute all the elements of nums between two arrays arr1 and arr2 using n operations. In the first operation, append nums[1] to arr1. In the second operation, append nums[2] to arr2. Afterwards, in the ith operation:

#If greaterCount(arr1, nums[i]) > greaterCount(arr2, nums[i]), append nums[i] to arr1.
#If greaterCount(arr1, nums[i]) < greaterCount(arr2, nums[i]), append nums[i] to arr2.
#If greaterCount(arr1, nums[i]) == greaterCount(arr2, nums[i]), append nums[i] to the array with a lesser number of elements.
#If there is still a tie, append nums[i] to arr1.
#The array result is formed by concatenating the arrays arr1 and arr2. For example, if arr1 == [1,2,3] and arr2 == [4,5,6], then result = [1,2,3,4,5,6].

#Return the integer array result.

 

#Example 1:

#Input: nums = [2,1,3,3]
#Output: [2,3,1,3]
#Explanation: After the first 2 operations, arr1 = [2] and arr2 = [1].
#In the 3rd operation, the number of elements greater than 3 is zero in both arrays. Also, the lengths are equal, hence, append nums[3] to arr1.
#In the 4th operation, the number of elements greater than 3 is zero in both arrays. As the length of arr2 is lesser, hence, append nums[4] to arr2.
#After 4 operations, arr1 = [2,3] and arr2 = [1,3].
#Hence, the array result formed by concatenation is [2,3,1,3].

#my own solution using python3:

#sl and binary search

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        arr1.append(nums[0])
        arr2.append(nums[1])
        onesl = SortedList(arr1)
        twosl = SortedList(arr2)
        
        for i in range(2, len(nums)):
            #print(nums[i], arr1, arr2)
            bro = bisect_right(onesl, nums[i])
            brt = bisect_right(twosl, nums[i])
            one = abs(len(arr1) - bro)
            two = abs(len(arr2) - brt)
            #for a in arr1:
            #    if a > nums[i]:
            #        one += 1
            #for a in arr2:
            #    if a > nums[i]:
            #        two += 1
            #print(one, two)
            #print(bro - len(arr1), brt - len(arr2))
            if one > two:
                arr1.append(nums[i])
                onesl.add(nums[i])
            elif one < two:
                arr2.append(nums[i])
                twosl.add(nums[i])
            else:
                if len(arr1) <= len(arr2):
                    arr1.append(nums[i])
                    onesl.add(nums[i])
                else:
                    arr2.append(nums[i])
                    twosl.add(nums[i])
    
        return arr1 + arr2
