class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverse = 0
        xcopy = x
        while x > 0:
            rem = x % 10
            reverse = (reverse * 10)+rem
            x= x//10
        
        return reverse == xcopy 
       