#2102
#hard

#A scenic location is represented by its name and attractiveness score, where name is a unique string among all locations and score is an integer. Locations can be ranked from the best to the worst. The higher the score, the better the location. If the scores of two locations are equal, then the location with the lexicographically smaller name is better.

#You are building a system that tracks the ranking of locations with the system initially starting with no locations. It supports:

#Adding scenic locations, one at a time.
#Querying the ith best location of all locations already added, where i is the number of times the system has been queried (including the current query).
#For example, when the system is queried for the 4th time, it returns the 4th best location of all locations already added.
#Note that the test data are generated so that at any time, the number of queries does not exceed the number of locations added to the system.

#Implement the SORTracker class:

#SORTracker() Initializes the tracker system.
#void add(string name, int score) Adds a scenic location with name and score to the system.
#string get() Queries and returns the ith best location, where i is the number of times this method has been invoked (including this invocation).
 


#my own solution using python3:

class SORTracker:

    def __init__(self):
        self.cur = SortedList()
        self.cnt = 0
        

    def add(self, name: str, score: int) -> None:
        self.cur.add([-score, name])
        

    def get(self) -> str:
        self.cnt += 1
        return self.cur[self.cnt - 1][1]
        


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
