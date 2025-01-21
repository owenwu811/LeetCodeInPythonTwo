
#916
#medium

#You are given two string arrays words1 and words2.

#A string b is a subset of string a if every letter in b occurs in a including multiplicity.

#For example, "wrr" is a subset of "warrior" but is not a subset of "world".
#A string a from words1 is universal if for every string b in words2, b is a subset of a.

#Return an array of all the universal strings in words1. You may return the answer in any order.

 
#my solution that got TLE 45/56:

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        for word in words1:
            flag = True
            myset = set()
            curw = Counter(word)
            for w in words2:
                if w in myset:
                    continue
                myset.add(w)
                cur = Counter(w)
                for i in range(len(w)):
                    if cur[w[i]] > curw[w[i]]:
                        flag = False
                        break
            if flag:
                res.append(word)
        return res

#correct python3 solution (could not solve):

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Precompute the maximum frequency of each character across all words in words2
        max_freq = Counter()
        for word in words2:
            word_freq = Counter(word)
            for char, freq in word_freq.items():
                max_freq[char] = max(max_freq[char], freq)
        
        # Check if each word in words1 is a universal word
        result = []
        for word in words1:
            word_freq = Counter(word)
            if all(word_freq[char] >= max_freq[char] for char in max_freq):
                result.append(word)
        
        return result
