class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0

        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            total = carry
        
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
                
        # Determine the current bit (0 or 1) and the new carry
            res.append(str(total % 2))
            carry = total // 2

    # Reverse the array and join into a single string
        return "".join(reversed(res))