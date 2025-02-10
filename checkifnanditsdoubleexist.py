#1346
#easy


#Given an array arr of integers, check if there exist two indices i and j such that :

#i != j
#0 <= i, j < arr.length
#arr[i] == 2 * arr[j]
 

#Example 1:

#Input: arr = [10,2,5,3]
#Output: true
#Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]


#my own solution using python3:

#just do a nested loop following the instructions

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j:
                    if arr[i] == 2 * arr[j]:
                        return True  
        return False
