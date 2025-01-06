
#2299
#easy

#A password is said to be strong if it satisfies all the following criteria:

#It has at least 8 characters.
#It contains at least one lowercase letter.
#It contains at least one uppercase letter.
#It contains at least one digit.
#It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
#It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
#Given a string password, return true if it is a strong password. Otherwise, return false.

 

#Example 1:

#Input: password = "IloveLe3tcode!"
#Output: true
#Explanation: The password meets all the requirements. Therefore, we return true.

#my own solution using python3:

#simply follow the instructions and use a boolean flag for each condition 

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        lengthcheck = False
        uppercheck = False  
        lowercheck = False
        digitcheck = False 
        specialcheck = False
        adjacentcheck = True
        if len(password) >= 8:
            lengthcheck = True
        for p in password:
            if p.isupper():
                uppercheck = True
            if p.islower():
                lowercheck = True
            if p.isdigit():
                digitcheck = True
            if p in "!@#$%^&*()-+":
                specialcheck = True
        for i in range(1, len(password) - 1):
            if password[i - 1] == password[i] or password[i] == password[i + 1]:
                adjacentcheck = False
        return lengthcheck and uppercheck and lowercheck and digitcheck and specialcheck and adjacentcheck
        
        
            
