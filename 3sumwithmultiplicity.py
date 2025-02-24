#923
#medium

#Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

#As the answer can be very large, return it modulo 109 + 7.

 

#Example 1:

#Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
#Output: 20
#Explanation: 
#Enumerating by the values (arr[i], arr[j], arr[k]):
#(1, 2, 5) occurs 8 times;
#(1, 3, 4) occurs 8 times;
#(2, 2, 4) occurs 2 times;
#(2, 3, 3) occurs 2 times.



#my own solution using python3:

#use a dictionary to track the 3rd pointer idx to the end and find the difference frequency 

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        res = 0
        mod = ((10 ** 9) + 7)
        c = Counter(arr)
        ans = []
        
        for i in range(len(arr)):
            orig = c.copy()
            c[arr[i]] -= 1
            if c[arr[i]] == 0:
                del c[arr[i]]
            for j in range(i + 1, len(arr)):
                c[arr[j]] -= 1
                if c[arr[j]] == 0:
                    del c[arr[j]]
                pairsum = arr[i] + arr[j]
                diff = target - pairsum
                ans.append(c[diff] / 2)
            c = orig


        return int(sum(ans)) % mod
