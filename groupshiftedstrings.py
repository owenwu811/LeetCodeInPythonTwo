#249
#medium

#Perform the following shift operations on a string:

#Right shift: Replace every letter with the successive letter of the English alphabet, where 'z' is replaced by 'a'. For example, "abc" can be right-shifted to "bcd" or "xyz" can be right-shifted to "yza".
#Left shift: Replace every letter with the preceding letter of the English alphabet, where 'a' is replaced by 'z'. For example, "bcd" can be left-shifted to "abc" or "yza" can be left-shifted to "xyz".
#We can keep shifting the string in both directions to form an endless shifting sequence.

#For example, shift "abc" to form the sequence: ... <-> "abc" <-> "bcd" <-> ... <-> "xyz" <-> "yza" <-> .... <-> "zab" <-> "abc" <-> ...
#You are given an array of strings strings, group together all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 

#Example 1:

#Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]

#Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]



#my own solution using python3:

#lots and lots of trial and error, but it finally worked:

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        letters = "abcdefghijklmnopqrstuvwxyz"
        for s in strings:
            diff = []
            for i in range(1, len(s)):
                cur = letters.index(s[i]) - letters.index(s[i - 1])
                if cur < 0:
                    cur = cur % 26
                diff.append(cur)
                #d[tuple(diff)].append(s)
            #print(diff, s)
            if not diff:
                d[len(s)].append(s)
            else:

                d[tuple(diff)].append(s)
        h = []
        seen = set()
        for c in list(d.values()):
            if len(c) == 1:
                seen.add(c[0])
            if c not in h:
                h.append(c)
        print(seen, h)
        


        return h
