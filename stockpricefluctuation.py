#2034
#medium


#You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

#Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

#Design an algorithm that:

#Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
#Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
#Finds the maximum price the stock has been based on the current records.
#Finds the minimum price the stock has been based on the current records.
#Implement the StockPrice class:

#StockPrice() Initializes the object with no price records.
#void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
#int current() Returns the latest price of the stock.
#int maximum() Returns the maximum price of the stock.
#int minimum() Returns the minimum price of the stock.



#my own solution using python3:

#use sortedlist to quickly get the max and min of the values of all keys in the dictionary

class StockPrice:

    def __init__(self):
        self.d = defaultdict(int)
        self.latest = 0
        self.cur = SortedList()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.d:
            self.cur.remove(self.d[timestamp])
        self.d[timestamp] = price
        self.cur.add(self.d[timestamp])
        self.latest = max(self.latest, timestamp)

        

    def current(self) -> int:
        return self.d[self.latest]

        

    def maximum(self) -> int:
        return self.cur[-1]
        

    def minimum(self) -> int:
        return self.cur[0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
