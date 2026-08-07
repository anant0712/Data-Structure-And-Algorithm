class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        majority_element = 0

        for num in nums:
            if majority_element ==0:
                candidate = num
            
            if num == candidate:
                majority_element +=1
            else:
                majority_element -= 1
        return candidate