class Solution(object):
  def isPalindrome(self, x):
    return str(x) == str(x)[::-1]

#palindrome is any number which remains same if we invert it
#for example 121 

#we cannot reverse a number directly using int, so we convert it into string
#we then invert the string 
#then we compare both, for a number to be palindrome it should be equal to its reversed form
