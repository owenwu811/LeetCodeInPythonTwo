#635
#medium

#You are given several logs, where each log contains a unique ID and timestamp. Timestamp is a string that has the following format: Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59. All domains are zero-padded decimal numbers.

#Implement the LogSystem class:

#LogSystem() Initializes the LogSystem object.
#void put(int id, string timestamp) Stores the given log (id, timestamp) in your storage system.
#int[] retrieve(string start, string end, string granularity) Returns the IDs of the logs whose timestamps are within the range from start to end inclusive. start and end all have the same format as timestamp, and granularity means how precise the range should be (i.e. to the exact Day, Minute, etc.). For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", and granularity = "Day" means that we need to find the logs within the inclusive range from Jan. 1st 2017 to Jan. 2nd 2017, and the Hour, Minute, and Second for each log entry can be ignored.

#my own solution using python3:

#use a sorted list, and use colon splits to get the precision for each granularity 

class LogSystem:

    def __init__(self):
        self.sl = SortedList()

    def put(self, id: int, timestamp: str) -> None:
        self.sl.add((timestamp, id))
        

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        print(start, end, granularity)
        now = SortedList()
        if granularity == "Year":
            start = start.split(":")[0]
            end = end.split(":")[0]
            for s in self.sl:
                cur = s[0].split(":")
                now.add((cur[0], s[1]))
            print(now, granularity)
            ans = []
            for a in now:
                if start <= a[0] <= end:
                    ans.append(a[1])
            return ans
        elif granularity == "Month":
            start = start.split(":")[0] + start.split(":")[1]
            end = end.split(":")[0] + end.split(":")[1]
            for s in self.sl:
                cur = s[0].split(":")
                y = cur[0] + cur[1]
                now.add((y, s[1]))
            print(now, granularity)
            ans = []
            for a in now:
                if start <= a[0] <= end:
                    ans.append(a[1])
            return ans

        elif granularity == "Day":
            start = start.split(":")[0] + start.split(":")[1] + start.split(":")[2]
            end = end.split(":")[0] + end.split(":")[1] + end.split(":")[2]
            for s in self.sl:
                cur = s[0].split(":")
                y = cur[0] + cur[1] + cur[2]
                now.add((y, s[1]))
            ans = []
            for a in now:
                if start <= a[0] <= end:
                    ans.append(a[1])
            return ans

        elif granularity == "Hour":
            start = start.split(":")[0] + start.split(":")[1] + start.split(":")[2] + start.split(":")[3]
            end = end.split(":")[0] + end.split(":")[1] + end.split(":")[2] + end.split(":")[3]
            for s in self.sl:
                cur = s[0].split(":")
                y = cur[0] + cur[1] + cur[2] + cur[3]
                now.add((y, s[1]))
            ans = []
            for a in now:
                if start <= a[0] <= end:
                    ans.append(a[1])
            return ans
        
        elif granularity == "Minute":
            start = start.split(":")[0] + start.split(":")[1] + start.split(":")[2] + start.split(":")[3] + start.split(":")[4]
            end = end.split(":")[0] + end.split(":")[1] + end.split(":")[2] + end.split(":")[3] + end.split(":")[4]
            for s in self.sl:
                cur = s[0].split(":")
                y = cur[0] + cur[1] + cur[2] + cur[3] + cur[4]
                now.add((y, s[1]))
            ans = []
            for a in now:
                if start <= a[0] <= end:
                    ans.append(a[1])
            return ans
        elif granularity == "Second":
            now = SortedList()
            print(self.sl)
            for s in self.sl:
                cur = s[0]
                now.add((cur, s[1]))
            print(now, granularity)
            #now = self.sl.copy()
            ans = []
            for a in now:
                if start <= a[0] <= end:
                    ans.append(a[1])
            return ans
        



# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
