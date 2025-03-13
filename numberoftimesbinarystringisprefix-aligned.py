#1375
#medium

#You have a 1-indexed binary string of length n where all the bits are 0 initially. We will flip all the bits of this binary string (i.e., change them from 0 to 1) one by one. You are given a 1-indexed integer array flips where flips[i] indicates that the bit at index i will be flipped in the ith step.

#A binary string is prefix-aligned if, after the ith step, all the bits in the inclusive range [1, i] are ones and all the other bits are zeros.

#Return the number of times the binary string is prefix-aligned during the flipping process.

 

#Example 1:

#Input: flips = [3,2,4,1,5]
#Output: 2
#Explanation: The binary string is initially "00000".
#After applying step 1: The string becomes "00100", which is not prefix-aligned.
#After applying step 2: The string becomes "01100", which is not prefix-aligned.
#After applying step 3: The string becomes "01110", which is not prefix-aligned.
#After applying step 4: The string becomes "11110", which is prefix-aligned.
#After applying step 5: The string becomes "11111", which is prefix-aligned.
#We can see that the string was prefix-aligned 2 times, so we return 2.

#my own solution using python3: 

#to find if the current subarray has a 0 in it or not - reflect everything that changed plus elements that you have seen before that have now changed from 0 to 1

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        tot = len(flips)
        start = [0] * len(flips)
        d = defaultdict(int)
        for i in range(len(start)):
            d[i] = 0
        d = dict(sorted(d.items(), key=lambda x: x[0]))
        zc = len(flips)
        res = 0
        ss = 0
        seen = set()
        ts = 0
        p = []
        for i in range(len(flips)):
            seen.add(i)
            cur = flips[i] - 1
            p.append(start[cur])
            start[cur] = 1
            #p.append(start[cur])
            #print(start[i])
            d[cur] = 1
            zc -= 1
            #c[start[cur]] += 1
            #print(start[i])
            ss += start[i]
            #now = start[:i + 1]
            if cur < i and cur in seen:
                #print(now, ss, "ww")
                ss += 1


                
            
            #print(now, ss)
 
            #0 [0] 2 {0} cur seen
            #1 [0, 1] 1 {0, 1} cur seen
            #2 [0, 1, 1] 3 {0, 1, 2} cur seen
            #3 [1, 1, 1, 1] 0 {0, 1, 2, 3} cur seen
            #4 [1, 1, 1, 1, 1] 4 {0, 1, 2, 3, 4} cur seen

            if ss == i + 1:
                #if zc >= tot - i - 1:
                res += 1
  
                
                #
        return res
