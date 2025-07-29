#1683
#easy

#Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#just loop through the tweets content column and ask if the size if bigger than 15, and, if so, include that tweet id in the ans

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    ans = []
    for i, t in enumerate(tweets["content"]):
        if len(t) > 15:
            print(tweets["tweet_id"][i])
            ans.append(tweets["tweet_id"][i])
    res = pd.DataFrame()
    res["tweet_id"] = ans
    return res
