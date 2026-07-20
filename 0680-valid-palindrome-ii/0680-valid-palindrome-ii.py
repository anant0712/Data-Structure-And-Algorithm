class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pallindrome(i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True
        left =0
        right = len(s)-1

        while left < right:
            if s[left] != s[right]:
                return is_pallindrome(left+1,right) or is_pallindrome(left,right-1)
            left +=1
            right -=1
        return True