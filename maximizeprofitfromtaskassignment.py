
#3476
#medium

#You are given an integer array workers, where workers[i] represents the skill level of the ith worker. You are also given a 2D integer array tasks, where:

#tasks[i][0] represents the skill requirement needed to complete the task.
#tasks[i][1] represents the profit earned from completing the task.
#Each worker can complete at most one task, and they can only take a task if their skill level is equal to the task's skill requirement. An additional worker joins today who can take up any task, regardless of the skill requirement.

#Return the maximum total profit that can be earned by optimally assigning the tasks to the workers.



#my own solution using python3:

#understand the requirements carefully 

class Solution:
    def maxProfit(self, workers: List[int], tasks: List[List[int]]) -> int:
        d = defaultdict(SortedList)
        for t in tasks:
            d[t[0]].add(t[1])
        #print(d)
        res = 0
        seen = set()
        for w in workers:
            if w in d:
                res += d[w][-1]
                seen.add(d[w][-1])
                d[w].pop()
                if not d[w]:
                    del d[w]
        #print(seen)
        print(res)
        cur = list()
        print(d)
        for k in d:
            cur.extend(d[k])
        cur = set(cur)
        print(res, cur)
        if not cur:
            return res
        return res + max(cur)
