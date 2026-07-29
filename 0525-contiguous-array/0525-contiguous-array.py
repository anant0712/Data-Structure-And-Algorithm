class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_count = {0:-1}
        max_len = 0
        count = 0

        for i,num in enumerate(nums):
            if num ==1:
                count+=1
            else:
                count -=1

            if count in sum_count:

                needed_len = i-sum_count[count]
                if needed_len > max_len:
                    max_len = needed_len
            else:
                sum_count[count]=i
        return max_len

                