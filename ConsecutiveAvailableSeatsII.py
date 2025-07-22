#3140
#medium

#Write a solution to find the length of longest consecutive sequence of available seats in the cinema.

#Note:

#There will always be at most one longest consecutive sequence.
#If there are multiple consecutive sequences with the same length, include all of them in the output.
#Return the result table ordered by first_seat_id in ascending order.

#The result format is in the following example.


#my own solution using python3:

#get the maximum, and then record all results that have the maximum, and also sort the seat ids in ascending order

import pandas as pd

def consecutive_available_seats(cinema: pd.DataFrame) -> pd.DataFrame:
    biggest = 0
    for i in range(len(cinema["free"])):
        if cinema["free"][i] == 1:
            j = i + 1
            cnt = 1
            while j < len(cinema["free"]) and cinema["free"][j] == 1:
                cnt += 1
                j += 1
            print(cnt)
            biggest = max(biggest, cnt)
    ans = []
    one, two, three = [], [], []
    for i in range(len(cinema["free"])):
        cur = []
        if cinema["free"][i] == 1:
            cur.append(cinema["seat_id"][i])
            j = i + 1
            cnt = 1
            while j < len(cinema["free"]) and cinema["free"][j] == 1:
                cnt += 1
                cur.append(cinema["seat_id"][j])
                j += 1
            cur.sort()
            if cnt == biggest:
                print(cur, biggest)
                ans.append([cur[0], cur[-1], biggest])
    ans.sort()
    for a in ans:
        one.append(a[0])
        two.append(a[1])
        three.append(a[2])
    res = pd.DataFrame()
    res["first_seat_id"] = one
    res["last_seat_id"] = two
    res["consecutive_seats_len"] = three
    return res

