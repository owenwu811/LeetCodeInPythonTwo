#352
#hard

#Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

#Implement the SummaryRanges class:

#SummaryRanges() Initializes the object with an empty stream.
#void addNum(int value) Adds the integer value to the stream.
#int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.
 

#Example 1:

#Input
#["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
#[[], [1], [], [3], [], [7], [], [2], [], [6], []]
#Output
#[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]


#my own solution using python3:

#just use brute force

class SummaryRanges:

    def __init__(self):
        self.sl = SortedList()

    def addNum(self, value: int) -> None:
        #print(value)
        self.sl.add(value)

    def getIntervals(self) -> List[List[int]]:
        print(self.sl)
        #SortedList([1, 2, 3, 7])
        if self.sl:
            biggest = self.sl[-1]
            ans = []
            now = [0] * (biggest + 1)
            #print(now)
            for s in self.sl:
                now[s] = 1
            print(now)
            i = 0
            while i < len(now):
                start = i
                end = i
                if now[i] == 1:
                    for j in range(i, len(now)):
                        if now[j] == 1:
                            end = max(end, j)
                        else:
                            break
                    print(start, end)
                    ans.append([start, end])
                    i = max(i, end + 1)
                else:
                    i += 1
            return ans
        else:
            return []
