
#3491
#easy

#You are given a string array numbers that represents phone numbers. Return true if no phone number is a prefix of any other phone number; otherwise, return false.

 

#Example 1:

#Input: numbers = ["1","2","4","3"]

#Output: true

#Explanation:

#No number is a prefix of another number, so the output is true.


#my own solution using python3:

#just do a double loop and check if one starts with the other at any point

class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i != j:
                    if numbers[i].startswith(numbers[j]) or numbers[j].startswith(numbers[i]): return False
        return True
