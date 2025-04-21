#3006
#medium

#You are given a 0-indexed string s, a string a, a string b, and an integer k.

#An index i is beautiful if:

#0 <= i <= s.length - a.length
#s[i..(i + a.length - 1)] == a
#There exists an index j such that:
#0 <= j <= s.length - b.length
#s[j..(j + b.length - 1)] == b
#|j - i| <= k
#Return the array that contains beautiful indices in sorted order from smallest to largest.

 

#Example 1:

#Input: s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15
#Output: [16,33]


#my own solution using python3:

#use binary search

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        ans = []
        alen = len(a)
        blen = len(b)
        seen = set()
        slen = len(s)
        ad = defaultdict(SortedSet)
        bd = defaultdict(SortedSet)
        bega = deque(s[:alen])
        for i in range(slen - alen + 1):
            ad["".join(bega)].add(i)
            if i + alen < slen:
                bega.append(s[i + alen])
            bega.popleft()
        begb = deque(s[:blen])
        for i in range(slen - blen + 1):
            bd["".join(begb)].add(i)
            if i + blen < slen:
                begb.append(s[i + blen])
            begb.popleft()
        if a in ad and b in bd:
            for c in ad[a]:
                #print(c)
                #i#f abs(bd[b][0] - c) > k and abs(bd[b][-1] - c) > k:
                #    continue
                bb = bisect_left(bd[b], abs(c + k)) - 1
                br = bb + 1
                #print(c, bd[b])
                if abs(c - bd[b][0]) <= k:
                    if c not in seen:
                        ans.append(c)
                        seen.add(c)

                #print(bb, br)
                if bb < len(bd[b]) and br < len(bd[b]):
                    if abs(bd[b][bb] - c) > k and abs(bd[b][br] - c) > k:
                        continue

                if bb < len(bd[b]):
                    for h in bd[b][bb:]:
                        if abs(h - c) <= k:
                            if c not in seen:
                                ans.append(c)
                                seen.add(c)
        return ans
