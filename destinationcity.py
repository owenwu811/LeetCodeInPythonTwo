#1436
#easy


#You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

#It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 

#Example 1:

#Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
#Output: "Sao Paulo" 
#Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".


#my own solution using python3:

#track the coordinates for each word

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = defaultdict(list)
        for p in paths:
            d[p[0]].append(0)
            d[p[1]].append(1)
        print(d)
        for k in d:
            if 0 not in d[k]:
                print(k)
                return k

