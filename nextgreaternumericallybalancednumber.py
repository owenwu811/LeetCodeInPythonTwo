#2048
#medium

#An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.

#Given an integer n, return the smallest numerically balanced number strictly greater than n.

 

#Example 1:

#Input: n = 1
#Output: 22
#Explanation: 
#22 is numerically balanced since:
#- The digit 2 occurs 2 times. 
#It is also the smallest numerically balanced number strictly greater than 1.


#my own solution using python3:

#just use a for loop and create a dictionary for each number, counting the frequencies

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        bigger = max(5000, n * n)
        for i in range(n + 1, bigger + 1):
            cur = str(i)
            if "0" in cur:
                continue
            c = Counter(cur)
            flag = True
            for a, b in c.items():
                if int(a) != b:
                    flag = False
                    break
            if flag:
                print(i)
                return i
