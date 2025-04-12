#2933
#medium

#You are given a 2D 0-indexed array of strings, access_times, with size n. For each i where 0 <= i <= n - 1, access_times[i][0] represents the name of an employee, and access_times[i][1] represents the access time of that employee. All entries in access_times are within the same day.

#The access time is represented as four digits using a 24-hour time format, for example, "0800" or "2250".

#An employee is said to be high-access if he has accessed the system three or more times within a one-hour period.

#Times with exactly one hour of difference are not considered part of the same one-hour period. For example, "0815" and "0915" are not part of the same one-hour period.

#Access times at the start and end of the day are not counted within the same one-hour period. For example, "0005" and "2350" are not part of the same one-hour period.

#Return a list that contains the names of high-access employees with any order you want.

 

#Example 1:

#Input: access_times = [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]
#Output: ["a"]
#Explanation: "a" has three access times in the one-hour period of [05:32, 06:31] which are 05:32, 05:49, and 06:21.
#But "b" does not have more than two access times at all.
#So the answer is ["a"].

#my own solution using python3:

#just use brute force to find triplets within the range

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        #[name, access_time]

        d = defaultdict(SortedList)
        for a in access_times:
            d[a[0]].add(int(a[1]))
        #print(d)
        ans = []
        for k in d:
            print(d[k])
            for i in range(len(d[k])):
                high = d[k][i] + 99
                for j in range(i + 1, len(d[k])):
                    for y in range(j + 1, len(d[k])):
                        if d[k][j] <= high and d[k][y] <= high:
                            if k not in ans:
                                ans.append(k)
                                break

        return ans
