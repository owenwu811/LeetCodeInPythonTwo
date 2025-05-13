
#433
#medium

#A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

#Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

#For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
#There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

#Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

#Note that the starting point is assumed to be valid, so it might not be included in the bank.

 

#Example 1:

#Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
#Output: 1

#my own solution using python3:

        
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        nei = defaultdict(list)
        if not bank and startGene != endGene:
            return -1
        for b in bank:
            for j in range(len(b)):
                pattern = b[:j] + "*" + b[j + 1:]
                nei[pattern].append(b)
        visited = set()
        visited.add(startGene)
        d = deque([startGene])
        ans = 0
        while d:
            for i in range(len(d)):
                cur = d.popleft()
                if cur == endGene:
                    return ans
                for j in range(len(cur)):
                    pattern = cur[:j] + "*" + cur[j + 1:]
                    for n in nei[pattern]:
                        if n not in visited:
                            visited.add(n)
                            d.append(n)
            ans += 1

        return -1
