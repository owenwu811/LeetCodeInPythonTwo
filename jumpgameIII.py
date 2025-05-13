#1306
#medium

#Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

#Notice that you can not jump outside of the array at any time.

 

#Example 1:

#Input: arr = [4,2,3,0,3,1,2], start = 5
#Output: true
#Explanation: 
#All possible ways to reach at index 3 with value 0 are: 
#index 5 -> index 4 -> index 1 -> index 3 
#index 5 -> index 6 -> index 4 -> index 1 -> index 3 

#my own solution using python3:

#very simple BFS

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        seen = set()
        seen.add(start)
        d = deque([start])
        while d:
            for i in range(len(d)):
                cur = d.popleft()
                print(arr[cur], "beg")
                if arr[cur] == 0:
                    return True
                if cur + arr[cur] < len(arr):
                    if cur + arr[cur] not in seen:

                        seen.add(cur + arr[cur])
                        d.append(cur + arr[cur])
                if cur - arr[cur] >= 0:
                    if cur - arr[cur] not in seen:
                        seen.add(cur - arr[cur])
                        d.append(cur - arr[cur])
        return False
