#579
#Hard
 

#Write a solution to calculate the cumulative salary summary for every employee in a single unified table.

#The cumulative salary summary for an employee can be calculated as follows:

#For each month that the employee worked, sum up the salaries in that month and the previous two months. This is their 3-month sum for that month. If an employee did not work for the company in previous months, their effective salary for those months is 0.
#Do not include the 3-month sum for the most recent month that the employee worked for in the summary.
#Do not include the 3-month sum for any month the employee did not work.
#Return the result table ordered by id in ascending order. In case of a tie, order it by month in descending order.

#The result format is in the following example.

#my own solution using python3:

#messy but working

import pandas as pd

def cumulative_salary(employee: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(list)
    for i, v in enumerate(employee["id"]):
        d[v].append([employee["month"][i], employee["salary"][i]])
        d[v].sort()
    ans = []
    for k in d:
        now = d[k][:-1]
        print(k, now)
        #print(k, now[0][0], now[0][1])
        if now:
            ans.append([k, now[0][0], now[0][1]])
            cur = now[0][1]
            for i in range(1, len(now)):
                if now[i][0] == now[i - 1][0] + 1:
                    if i >= 2:
                        segment = now[i - 2: i + 1]
                        print(segment)
                        cnt = 0
                        for j, s in enumerate(segment):
                            if j > 0:
                                if segment[j][0] != segment[j - 1][0] + 1:
                                    cnt = segment[j][1]
                                else:
                                    cnt += s[1]
                            else:
                                cnt += s[1]
                            print(cnt)
                        ans.append([k, now[i][0], cnt])
                    else:
                        segment = now[:i + 1]
                        cnt = 0
                        for j, s in enumerate(segment):
                            if j > 0:
                                if segment[j][0] != segment[j - 1][0] + 1:
                                    cnt = segment[j][1]
                                else:
                                    cnt += s[1]
                            else:
                                cnt += s[1]
                        ans.append([k, now[i][0], cnt])
                else:
                    cnt = now[i][1]
                    ans.append([k, now[i][0], cnt])
    ans.sort(key=lambda x: (x[0], -x[1]))
    print(ans)
    one, two, three = [], [], []
    for a in ans:
        one.append(a[0])
        two.append(a[1])
        three.append(a[2])
    res = pd.DataFrame()
    res["id"] = one
    res["month"] = two
    res["Salary"] = three
    return res
                
                
