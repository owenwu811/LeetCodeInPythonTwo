#2979
#medium

#You are given two distinct prime numbers primeOne and primeTwo.

#Alice and Bob are visiting a market. The market has an infinite number of items, for any positive integer x there exists an item whose price is x. Alice wants to buy some items from the market to gift to Bob. She has an infinite number of coins in the denomination primeOne and primeTwo. She wants to know the most expensive item she can not buy to gift to Bob.

#Return the price of the most expensive item which Alice can not gift to Bob.

 

#Example 1:

#Input: primeOne = 2, primeTwo = 5
#Output: 3
#Explanation: The prices of items which cannot be bought are [1,3]. It can be shown that all items with a price greater than 3 can be bought using a combination of coins of denominations 2 and 5.



#correct python3 solution (could not solve - come back to review later):

class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        return primeOne * primeTwo - (primeOne + primeTwo)
