#1996
#medium

#You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

#A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

#Return the number of weak characters.

 

#Example 1:

#Input: properties = [[5,5],[6,3],[3,6]]
#Output: 0
#Explanation: No character has strictly greater attack and defense than the other.


#correct python3 solution (could not solve):

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        maxdefense = 0
        count = 0
        for a, d in properties:
            if d < maxdefense:
                count += 1
            else:
                maxdefense = d
        return count
