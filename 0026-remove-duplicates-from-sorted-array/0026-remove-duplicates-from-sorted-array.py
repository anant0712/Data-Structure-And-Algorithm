class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        unique_index = 1  # As first element will always be unique
        for j in range(1,len(nums)):
            if nums[j] != nums[j-1]:
                nums[unique_index]=nums[j]  
                unique_index += 1      
        return unique_index