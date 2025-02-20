#1309
#easy

#You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

#Characters ('a' to 'i') are represented by ('1' to '9') respectively.
#Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
#Return the string formed after mapping.

#The test cases are generated so that a unique mapping will always exist.

 

#Example 1:

#Input: s = "10#11#12"
#Output: "jkab"
#Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
#Example 2:

#Input: s = "1326#"
#Output: "acz"

#my own solution using python3:

#just use string.replace() method exactly as stated 

class Solution:
    def freqAlphabets(self, s: str) -> str:
        s = s.replace("10#", "j")
        s = s.replace("11#", "k")
        s = s.replace("12#", "l")
        s = s.replace("13#", "m")
        s = s.replace("14#", "n")
        s = s.replace("15#", "o")
        s = s.replace("16#", "p")
        s = s.replace("17#", "q")
        s = s.replace("18#", "r")
        s = s.replace("19#", "s")
        s = s.replace("20#", "t")
        s = s.replace("21#", "u")
        s = s.replace("22#", "v")
        s = s.replace("23#", "w")
        s = s.replace("24#", "x")
        s = s.replace("25#", "y")
        s = s.replace("26#", "z")
        s = s.replace("1", "a")
        s = s.replace("2", "b")
        s = s.replace("3", "c")
        s = s.replace("4", "d")
        s = s.replace("5", "e")
        s = s.replace("6", "f")
        s = s.replace("7", "g")
        s = s.replace("8", "h")
        s = s.replace("9", "i")
        return s
