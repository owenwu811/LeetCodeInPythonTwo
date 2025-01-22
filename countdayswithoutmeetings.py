
#3169
#medium

#You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

#Return the count of days when the employee is available for work but no meetings are scheduled.

#Note: The meetings may overlap.

 

#Example 1:

#Input: days = 10, meetings = [[5,7],[1,3],[9,10]]

#Output: 2

#Explanation:

#There is no meeting scheduled on the 4th and 8th days.


#my own solution that got TLE 560/578:


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        res = 0
        print(meetings)
        for i in range(1, days + 1):
            flag = False
            for m in meetings:
                if m[0] <= i <= m[1]:
                    flag = True
            if not flag:
                print(i)
                res += 1
        return res


#correct python3 solution:

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        tot = days
        cur = [meetings[0]]
        for a in meetings[1:]:
            if a[0] <= cur[-1][1]:
                cur[-1][1] = max(a[1], cur[-1][-1])
            else:
                cur.append(a)
        print(cur)
        for a, b in cur:
            diff = b - a + 1
            tot -= diff
        return tot
