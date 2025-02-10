#3450
#easy


#You are given a 2D integer array of student data students, where students[i] = [student_id, bench_id] represents that student student_id is sitting on the bench bench_id.

#Return the maximum number of unique students sitting on any single bench. If no students are present, return 0.

#Note: A student can appear multiple times on the same bench in the input, but they should be counted only once per bench.

 

#Example 1:

#Input: students = [[1,2],[2,2],[3,3],[1,3],[2,3]]

#Output: 3

#Explanation:

#Bench 2 has two unique students: [1, 2].
#Bench 3 has three unique students: [1, 2, 3].
#The maximum number of unique students on a single bench is 3.

#my own solution using python3:

#just use a hashmap and find the largest length of any key's value

class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        d = defaultdict(list)
        res = 0
        for s in students:
            if s[0] not in d[s[1]]:
                d[s[1]].append(s[0])
                res = max(res, len(d[s[1]]))
        return res
