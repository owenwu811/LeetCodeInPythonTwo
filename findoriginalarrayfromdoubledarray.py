
#2007
#medium

#An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

#Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.

 

#Example 1:

#Input: changed = [1,3,4,2,6,8]
#Output: [1,3,4]
#Explanation: One possible original array could be [1,3,4]:
#- Twice the value of 1 is 1 * 2 = 2.
#- Twice the value of 3 is 3 * 2 = 6.
#- Twice the value of 4 is 4 * 2 = 8.
#Other original arrays could be [4,3,1] or [3,1,4].


#my own solution using python3:

#use a sorted list, and keep track of everything bigger than smallest

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        sl = SortedList(changed)
        half = len(changed) / 2
        c = Counter(sl)
        ans = []
        while sl:
            #print(c, sl[0], sl[1:])
            c[sl[0]] -= 1
            if c[sl[0]] <= 0:
                del c[sl[0]]
            double = sl[0] * 2
            if double in c:
                a = sl[0]
                b = 2 * sl[0]
                ans.append(a)
                sl.discard(a)
                c[a] -= 1
                if c[a] <= 0:
                    del c[a]
                sl.discard(b)
                if a != b:
                    c[b] -= 1
                    if c[b] <= 0:
                        del c[b]
            else:
                break
        if len(ans) == half:
            return ans
        return []
