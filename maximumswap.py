
#670
#medium

#You are given an integer num. You can swap two digits at most once to get the maximum valued number.

#Return the maximum valued number you can get.

 

#Example 1:

#Input: num = 2736
#Output: 7236
#Explanation: Swap the number 2 and the number 7.
#Example 2:

#Input: num = 9973
#Output: 9973
#Explanation: No swap.


#my own solution using python3:

#you know that the place to the left is bigger than to the right, so line up the key how you want it, and find the position that is out of place first, and you know this is the one you want to choose, and then choose the biggest number to the right of that index where it's the last occuring biggest number, and then swap it

class Solution:
    def maximumSwap(self, num: int) -> int:

        #98368
        sortedr = list(str(num))
        second = sorted(sortedr, reverse=True)
        print(second, "second")
        print(sortedr, "sortedr")
        for i in range(len(sortedr)):
            if sortedr[i] != second[i]:
                print(sortedr[i], "bad")
                cur = sortedr[i + 1:]
                print(cur)
                biggest = max(cur)
                for j in range(len(sortedr)):
                    if sortedr[j] == biggest and j > i and biggest not in sortedr[j + 1:]:
                        print(i, j, "swapper")
                        sortedr[i], sortedr[j] = sortedr[j], sortedr[i]
                        print(sortedr)
                        return int("".join(sortedr))

        return int("".join(sortedr))

                #break
     
