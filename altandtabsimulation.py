
#3237
#medium

#There are n windows open numbered from 1 to n, we want to simulate using alt + tab to navigate between the windows.

#You are given an array windows which contains the initial order of the windows (the first element is at the top and the last one is at the bottom).

#You are also given an array queries where for each query, the window queries[i] is brought to the top.

#Return the final state of the array windows.

 

#Example 1:

#Input: windows = [1,2,3], queries = [3,3,2]

#Output: [2,3,1]

#Explanation:

#Here is the window array after each query:

#Initial order: [1,2,3]
#After the first query: [3,1,2]
#After the second query: [3,1,2]
#After the last query: [2,3,1]



#my own solution using python3:

#loop over in reverse before getting the elements and then get the difference between windows and queries, and add that difference to the result before returning the result

class Solution:
    def simulationResult(self, windows: List[int], queries: List[int]) -> List[int]:
        cur = []
        window = set(windows)
        seen = set()
        queries = queries[::-1]
        for q in queries:
            if q in seen:
                continue
            cur.append(q)
            window.discard(q)
            seen.add(q)
        print(window)
        for w in windows:
            if w not in seen:
                cur.append(w)
        
        return cur
