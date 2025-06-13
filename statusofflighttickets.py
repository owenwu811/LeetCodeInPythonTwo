
#2793
#hard

#Passengers book tickets for flights in advance. If a passenger books a ticket for a flight and there are still empty seats available on the flight, the passenger's ticket will be confirmed. However, the passenger will be on a waitlist if the flight is already at full capacity.

#Write a solution to determine the current status of flight tickets for each passenger.

#Return the result table ordered by passenger_id in ascending order.

#The result format is in the following example.


#my own solution using python3:

#sort by the passengers["passenger_id"] first, and then grab the capacity, and then divide it, and then use a hashmap to get the status, and then reconstruct the result table

import pandas as pd

def ticket_status(flights: pd.DataFrame, passengers: pd.DataFrame) -> pd.DataFrame:
    h = []
    d = defaultdict(list)
    cap = dict()
    #print(passengers)
    flights["passenger_id"] = passengers["passenger_id"]
    for i, v in enumerate(flights["flight_id"]):
        cap[v] = flights["capacity"][i]
    up = []
    for i, v in enumerate(passengers["passenger_id"]):
        #print(passengers["passenger_id"][i])
        up.append(v)
        pid, fid, bt = passengers["passenger_id"][i], passengers["flight_id"][i], passengers["booking_time"][i]
        d[fid].append([bt, pid])
        d[fid].sort()
    up.sort()
    cd = dict()
    wd = dict()
    for k in d:
        cc = cap[k]
        conf = d[k][:cc]
        wl = d[k][cc:]
        for c in conf:
            #print(c[-1])
            cd[c[-1]] = "Confirmed"
        for w in wl:
            wd[w[-1]] = "Waitlist"
    print(up)
    print(cd, wd)
    passengers["Status"] = passengers["booking_time"]
    for i, v in enumerate(passengers["passenger_id"]):
        passengers["passenger_id"][i] = up[i]
        #passengers["Status"]
        if up[i] in cd:
            passengers["Status"][i] = "Confirmed"
        else:
            passengers["Status"][i] = "Waitlist"

        
    return pd.DataFrame(passengers, columns = ["passenger_id", "Status"])
