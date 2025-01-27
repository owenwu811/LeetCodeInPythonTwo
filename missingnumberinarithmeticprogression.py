#1228
#easy


#In some array arr, the values were in arithmetic progression: the values arr[i + 1] - arr[i] are all equal for every 0 <= i < arr.length - 1.

#A value from arr was removed that was not the first or last value in the array.

#Given arr, return the removed value.

 

#Example 1:

#Input: arr = [5,7,11,13]
#Output: 9
#Explanation: The previous array was [5,7,9,11,13].
#Example 2:

#Input: arr = [15,13,12]
#Output: 14
#Explanation: The previous array was [15,14,13,12].

#my own solution using python3:

#the clue is that the 1st and last values are not the bad ones, so take the difference of the two and divide by the length to find what the difference is supposed to be

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        if len(set(arr)) == 1:
            return arr[0]
        diff = (max(arr) - min(arr)) // len(arr)
        print(diff)
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) != diff:
                print(arr[i], arr[i + 1])
                if arr[i] > arr[i + 1]:
                    return arr[i] - diff
                else:
                    return arr[i] + diff
            
