class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, max_sum = nums[0], float('-inf')
        # res = 0

        for i in range(len(nums)):
            max_sum = max(max_sum + nums[i],nums[i])

            res = max(max_sum,res)

        return res
            
            # sum +=nums[i]
            # if sum > max_sum:
                # max_sum = sum
            # if sum < 0:
                # sum = 0
        # return max_sum'''