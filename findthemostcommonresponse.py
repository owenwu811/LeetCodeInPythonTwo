
#3527
#medium

#You are given a 2D string array responses where each responses[i] is an array of strings representing survey responses from the ith day.

#Return the most common response across all days after removing duplicate responses within each responses[i]. If there is a tie, return the lexicographically smallest response.

 

#Example 1:

#Input: responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]

#Output: "good"

#Explanation:

#After removing duplicates within each list, responses = [["good", "ok"], ["ok", "bad", "good"], ["good"], ["bad"]].
#"good" appears 3 times, "ok" appears 2 times, and "bad" appears 2 times.
#Return "good" because it has the highest frequency.

#my own solution using python3:

#just use a set and hashmap

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        c = Counter()
        for r in responses:
            print(set(r))
            for h in set(r):
                c[h] += 1
        ans = SortedList()
        biggest = max(c.values())
        for a, b in c.items():
            if b == biggest:
                print(a)
                #return a
                ans.add(a)
        return ans[0]
      
