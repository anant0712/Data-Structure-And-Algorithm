class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_count = {0:1}
        running_sum = 0
        total_subarray = 0

        for num in nums:
            running_sum += num

            needed_sum = running_sum - k
            if needed_sum in sum_count:
                total_subarray += sum_count[needed_sum]

            sum_count[running_sum] = sum_count.get(running_sum,0)+1
        return total_subarray