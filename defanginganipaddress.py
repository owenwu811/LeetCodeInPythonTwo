#1108
#easy

#Given a valid (IPv4) IP address, return a defanged version of that IP address.

#A defanged IP address replaces every period "." with "[.]".

 

#Example 1:

#Input: address = "1.1.1.1"
#Output: "1[.]1[.]1[.]1"
#Example 2:

#Input: address = "255.100.50.0"
#Output: "255[.]100[.]50[.]0"



#my own solution using python3 on 3/10/25 (originally solved in August of 2024 but forgot to upload the file):

#just track every index where a dot appears and create a new list and replace those indexes with [.] instead, leaving the rest the same as input, and return a string with no spaces of your list

class Solution:
    def defangIPaddr(self, address: str) -> str:
        idx = []
        for i, a in enumerate(address):
            if a == ".":
                idx.append(i)
        h = list(address)
        res = []
        for i, val in enumerate(h):
            if i in idx:
                res.append("[.]")
            else:
                res.append(val)
        return "".join(res)
