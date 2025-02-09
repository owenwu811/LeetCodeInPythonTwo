

#2076
#easy

#You are given an integer array prices representing the prices of various chocolates in a store. You are also given a single integer money, which represents your initial amount of money.

#You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.

#Return the amount of money you will have leftover after buying the two chocolates. If there is no way for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.

 

#Example 1:

#Input: prices = [1,2,2], money = 3
#Output: 0
#Explanation: Purchase the chocolates priced at 1 and 2 units respectively. You will have 3 - 3 = 0 units of money afterwards. Thus, we return 0.


#my own solution using python3:

#use a double loop to find the minimum sum of two chocolates that is less than or equal to money, and then return money - res at the end because that's what you have as a leftover 

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        res = float('inf')
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                cursum = prices[i] + prices[j]
                if cursum <= money:
                    res = min(res, cursum)
        if res == float('inf'):
            return money 
        return money - res
