from collections import Counter
class Solution:
    def checkRecord(self, s: str) -> bool:
        # if 'LLL' in s or "AA" in s:
        #     return False
        # else:
        #     return True
        
        c=Counter(s)
        if "LLL" in s or s.count("A")>=2:
            return False
        else:
            return True
        