

#copied from 720...

#correct python3 solution:

class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        res = ""
        words.sort()
        visited = {""}
        for word in words:
            if word[:-1] in visited:
                visited.add(word)
                if len(word) > len(res):
                    res = word
        return res
