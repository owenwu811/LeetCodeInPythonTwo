
#1618
#medium

#Example 1:

#Input: text = "helloworld", w = 80, h = 20, fonts = [6,8,10,12,14,16,18,24,36]
#Output: 6

#my own solution using python3:

# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
        res = 0
        l, r = 0, len(fonts) - 1
        while l <= r:
            mid = (l + r) // 2
            cur = fonts[mid]
            now = 0
            for i in range(len(text)):
                now += fontInfo.getWidth(cur, text[i])
            hh = fontInfo.getHeight(cur)
            if now <= w and hh <= h:
                res = max(res, cur)
                l = mid + 1
            else:
                r = mid - 1
        if res == 0: return -1
        return res
            
        
