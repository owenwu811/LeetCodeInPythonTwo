
#6/28/25 contest question 1
#medium

#Given a string s, partition it into unique segments according to the following procedure:

#Start building a segment beginning at index 0.
#Continue extending the current segment character by character until the current segment has not been seen before.
#Once the segment is unique, add it to your list of segments, mark it as seen, and begin a new segment from the next index.
#Repeat until you reach the end of s.
#Return an array of strings segments, where segments[i] is the ith segment created.

#Note: Please do not copy the description during the contest to maintain the integrity of your submissions.©leetcode

#my own solution using python3:

#just start with each letter, and keep extending until it's a duplicate; break, and continue.

class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = []
        ss = set()
        i = 0
        while i < len(s):
            cur = ""
            for j in range(i, len(s)):
                cur += s[j]
                if cur not in ss:
                    seen.append(cur)
                    ss.add(cur)
                    break
            i = j + 1
        return seen
