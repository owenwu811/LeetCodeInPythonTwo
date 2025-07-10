
#1440
#medium

#Evaluate the boolean expressions in Expressions table.

#Return the result table in any order.

#The result format is in the following example.

#my own solution using python3:

#map the variable to it's value, and then compare it 

import pandas as pd

def eval_expression(variables: pd.DataFrame, expressions: pd.DataFrame) -> pd.DataFrame:
    ans = []
    d = dict()
    for i, v in enumerate(variables["name"]):
        d[v] = variables["value"][i]
    print(d)
    for i, o in enumerate(expressions["operator"]):
        if o == '>':
            cur = d[expressions["left_operand"][i]] > d[expressions["right_operand"][i]]
        elif o == '=':
            cur = d[expressions["left_operand"][i]] == d[expressions["right_operand"][i]]
        else:
            cur = d[expressions["left_operand"][i]] < d[expressions["right_operand"][i]]
        if cur:
            ans.append([expressions["left_operand"][i], o, expressions["right_operand"][i], "true"])
        else:
            ans.append([expressions["left_operand"][i], o, expressions["right_operand"][i], "false"])
    print(ans)
    one, two, three, four = [], [], [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
        three.append(a[2])
        four.append(a[3])
    res = pd.DataFrame()
    res["left_operand"] = one
    res["operator"] = two
    res["right_operand"] = three
    res["value"] = four
    return res
