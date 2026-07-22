import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = [0]*n
        mxi = 0

        for i in range(n):
            mxi = max(mxi,nums[i])
            prefixGcd[i] = math.gcd(nums[i], mxi)

        prefixGcd.sort()

        total_sum = 0
        for i in range(n//2):
            total_sum += math.gcd(prefixGcd[i],prefixGcd[n-1-i])
        
        return total_sum