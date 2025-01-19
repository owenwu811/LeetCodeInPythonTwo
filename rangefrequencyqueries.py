#2080
#medium

#Design a data structure to find the frequency of a given value in a given subarray.

#The frequency of a value in a subarray is the number of occurrences of that value in the subarray.

#Implement the RangeFreqQuery class:

#RangeFreqQuery(int[] arr) Constructs an instance of the class with the given 0-indexed integer array arr.
#int query(int left, int right, int value) Returns the frequency of value in the subarray arr[left...right].
#A subarray is a contiguous sequence of elements within an array. arr[left...right] denotes the subarray that contains the elements of nums between indices left and right (inclusive).


#my own solution that got TLE 16/20:

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.cur = arr

    def query(self, left: int, right: int, value: int) -> int:
        
        return self.cur[left: right + 1].count(value)

#correct python3 solution:

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.d = defaultdict(list)
        for i, a in enumerate(arr):
            self.d[a].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.d:
            return 0
        lookingfor = self.d[value]
        leftside = bisect_left(lookingfor, left)
        rightside = bisect_right(lookingfor, right)
        return rightside - leftside
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
