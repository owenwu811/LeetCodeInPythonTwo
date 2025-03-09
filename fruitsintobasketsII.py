#weekly contest 440 question #1


#You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

#From left to right, place the fruits according to these rules:

#Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
#Each basket can hold only one type of fruit.
#If a fruit type cannot be placed in any basket, it remains unplaced.
#Return the number of fruit types that remain unplaced after all possible allocations are made.

 

#Example 1:

#Input: fruits = [4,2,5], baskets = [3,5,4]

#Output: 1

#Explanation:

#fruits[0] = 4 is placed in baskets[1] = 5.
#fruits[1] = 2 is placed in baskets[0] = 3.
#fruits[2] = 5 cannot be placed in baskets[2] = 4.
#Since one fruit type remains unplaced, we return 1.



#my own solution using python3 (solved during contest):

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = set()
        res = 0
        for i in range(len(fruits)):
            cur = fruits[i]
            if baskets:
                for j in range(len(baskets)):
                    print(cur, baskets[j])
                    if baskets[j] >= cur:
                        res += 1
                        baskets.pop(j)
                        break
        print(res, len(fruits))
        return len(fruits) - res
