
#1393
#medium

#Write a solution to report the Capital gain/loss for each stock.

#The Capital gain/loss of a stock is the total gain or loss after buying and selling the stock one or many times.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#simulate buys and sells with a nuetral value of 0

import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    
    seen = set()
    d = defaultdict(int)
    for i, v in enumerate(stocks["stock_name"]):
        seen.add(v)
    for i, v in enumerate(stocks["stock_name"]):
        if stocks["operation"][i] == "Buy":
            d[v] -= stocks["price"][i]
        else:
            d[v] += stocks["price"][i]
    #print(d)
    stocks["capital_gain_loss"] = stocks["price"]
    pairs = list(d.items())
    #print(pairs)
    cnt = 0
    for i, v in enumerate(stocks["stock_name"]):
        if i < len(pairs):
            print(pairs[i])
            stocks["stock_name"][i] = pairs[i][0]
            stocks["capital_gain_loss"][i] = pairs[i][1]
        cnt += 1
    
    return pd.DataFrame(stocks, columns=["stock_name", "capital_gain_loss"]).head(len(seen))
