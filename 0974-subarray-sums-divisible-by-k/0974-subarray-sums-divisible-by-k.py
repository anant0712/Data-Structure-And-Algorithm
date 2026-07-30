class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_count = {0:1}
        total_subarray = 0
        running_sum = 0

        for num in nums:
            running_sum += num
            rem = running_sum % k
            if rem in rem_count:
                total_subarray += rem_count[rem]
            rem_count[rem] = rem_count.get(rem,0)+1
        return total_subarray

