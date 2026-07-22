class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0

        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            total = digit_a + digit_b + carry
            res.append(str(total % 2))
            
            # Update carry (total // 2 will be 1 if total is 2 or 3, else 0)
            carry = total // 2
            
            # Move pointers left
            i -= 1
            j -= 1
            
        # The result is built backwards, so reverse it
        return "".join(res[::-1])