
#911
#medium

#You are given two integer arrays persons and times. In an election, the ith vote was cast for persons[i] at time times[i].

#For each query at a time t, find the person that was leading the election at time t. Votes cast at time t will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.

#Implement the TopVotedCandidate class:

#TopVotedCandidate(int[] persons, int[] times) Initializes the object with the persons and times arrays.
#int q(int t) Returns the number of the person that was leading the election at time t according to the mentioned rules.
 

#Example 1:

#Input
#["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
#[[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
#Output
#[null, 0, 1, 1, 0, 0, 1]

#my own solution using python3:

#precompute the winner at each time and use binary search to get the closest

class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.d = defaultdict(list)
        self.sl = SortedList()
        self.c = Counter()
        self.mostrecent = 0
        self.dd = defaultdict(int)
        self.freq = defaultdict(list)
        self.biggest = float('-inf')
        self.winner = float('-inf')
        self.final = defaultdict(int)
        print(persons, times)
        for i, p in enumerate(persons):
            self.d[times[i]].append(p)
            self.c[p] += 1
            self.mostrecent = p
            self.freq[self.c[p]].append(p)
            #print(self.d)
            if self.c[p] >= self.biggest:
                self.biggest = self.c[p]
                self.winner = self.freq[self.biggest][-1]
            self.final[times[i]] = self.winner
        self.k = SortedList(self.final.keys())
        self.order = []
        for f in self.final:
            self.order.append([f, self.final[f]])


    def q(self, t: int) -> int:
        right = bisect_left(self.k, t)
        left = right - 1
        #print(t, self.k, left, right, self.final)
        if right >= len(self.k):
            return self.order[-1][-1]
            #return self.final.popitem()[1]
        if left < len(self.k) and right < len(self.k):
            if self.k[right] == t:
                return self.final[self.k[right]]
            else:
                return self.final[self.k[left]]
