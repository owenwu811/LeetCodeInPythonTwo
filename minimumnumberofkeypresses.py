
#2268
#medium

#You have a keypad with 9 buttons, numbered from 1 to 9, each mapped to lowercase English letters. You can choose which characters each button is matched to as long as:

#All 26 lowercase English letters are mapped to.
#Each character is mapped to by exactly 1 button.
#Each button maps to at most 3 characters.
#To type the first character matched to a button, you press the button once. To type the second character, you press the button twice, and so on.

#Given a string s, return the minimum number of keypresses needed to type s using your keypad.

#Note that the characters mapped to by each button, and the order they are mapped in cannot be changed.


#correct python3 solution (could not solve):

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        c = Counter(s)
        d = dict(c)
        print(d)
        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        print(d)
        i = 0
        res = 0
        for k in d:
            cur = d[k]
            h = (i // 9) + 1
            res += (cur * h)
            i += 1
        return res
