#578
#medium

#The answer rate for a question is the number of times a user answered the question by the number of times a user showed the question.

#Write a solution to report the question that has the highest answer rate. If multiple questions have the same maximum answer rate, report the question with the smallest question_id.

#The result format is in the following example.

#my own solution using python3:

#use error handling to see if the cell is null. if it is, then use binary 0. if not, then 1, and then get ratios of all the question ids and calculate the biggest ratio's lowest id, and return that

import pandas as pd

def get_the_question(survey_log: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, s in enumerate(survey_log["question_id"]):
        try:
            print(int(survey_log["answer_id"][i]))
            #print(1)
            d[s].append(1)
        except:
            #print(0)
            d[s].append(0)
    cur = []
    biggest = float('-inf')
    for k in d:
        print(k, d[k])
        ratio = sum(d[k]) / len(d[k])
        biggest = max(biggest, ratio)
        cur.append([ratio, k])
        cur.sort()
    ans = float('inf')
    for k in d:
        ratio = sum(d[k]) / len(d[k])
        if ratio == biggest:
            ans = min(ans, k)
    res = pd.DataFrame()
    if ans != float('inf'):
        res["survey_log"] = [ans]
    else:
        res["survey_log"] = []
    return res
    #print(ans)
