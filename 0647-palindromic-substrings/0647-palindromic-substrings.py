class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s and len(s) < 1:
            return s

        count = 0

        def expand_around_center(left,right):
            res=0
            while left>=0 and right < len(s) and s[left]==s[right]:
                res +=1
                left -=1
                right +=1

            return res

        for i in range(len(s)):
            count += expand_around_center(i,i)
            count += expand_around_center(i,i+1)
        
        return count

        