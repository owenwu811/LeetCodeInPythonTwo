#2288
#medium

#A sentence is a string of single-space separated words where each word can contain digits, lowercase letters, and the dollar sign '$'. A word represents a price if it is a sequence of digits preceded by a dollar sign.

#For example, "$100", "$23", and "$6" represent prices while "100", "$", and "$1e5" do not.
#You are given a string sentence representing a sentence and an integer discount. For each word representing a price, apply a discount of discount% on the price and update the word in the sentence. All updated prices should be represented with exactly two decimal places.

#Return a string representing the modified sentence.

#Note that all prices will contain at most 10 digits.

 

#Example 1:

#Input: sentence = "there are $1 $2 and 5$ candies in the shop", discount = 50
#Output: "there are $0.50 $1.00 and 5$ candies in the shop"
#Explanation: 
#The words which represent prices are "$1" and "$2". 
#- A 50% discount on "$1" yields "$0.50", so "$1" is replaced by "$0.50".
#- A 50% discount on "$2" yields "$1". Since we need to have exactly 2 decimal places after a price, we replace "$2" with "$1.00".


#my own solution using python3:

#lots of edge cases

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        s = sentence.split(" ")
        new = []
        for c in s:
            if c[0] == "$" and c[-1] != "$":
                if c[1:].isdigit():
                    digit = int(c[1:]) - (int(c[1:]) * (discount / 100))
                    digit = round(digit, 2)
                    
                    if discount == 100:
                        digit = int(c[1:]) * 0 
                    final = list(c[0] + str(digit))
                    mystr = "".join(final)
                    if "." not in final:
                        final.insert(2, ".")
                    if len(final) < 5:
                        diff = 5 - len(final)
                        while diff > 0:
                            final.append("0")
                            diff -= 1
                    #print(final)
                    start = final.index(".")
                    final = final[: start + 3]
                    print(final)
                    f = "".join(final)
                    print(f)
                    after = final[start:]
                    print(after)
                    if f[-2:] == ".0" or len(after) < 3:
                        f += "0"

                    new.append(f)
                else:
                    new.append(c)
            else:
                new.append(c)
        return " ".join(new)
