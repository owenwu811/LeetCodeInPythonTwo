
#2829
#medium

#You are given two integers, n and k.

#An array of distinct positive integers is called a k-avoiding array if there does not exist any pair of distinct elements that sum to k.

#Return the minimum possible sum of a k-avoiding array of length n.

 

#Example 1:

#Input: n = 5, k = 4
#Output: 18
#Explanation: Consider the k-avoiding array [1,2,4,5,6], which has a sum of 18.
#It can be proven that there is no k-avoiding array with a sum less than 18.

#my own solution using python3:

#just brute force it

class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        now = []
        for i in range(1, n * n + 1):
            print(now)
            
            
            flag = True
            if now:
                for j in range(len(now)):
                    if now[j] + i == k:
                        flag = False
                        break
                if flag:
                    now.append(i)
            else:
                now.append(i)
            if len(now) == n:
                print(now)
                return sum(now)
        return sum(now)
