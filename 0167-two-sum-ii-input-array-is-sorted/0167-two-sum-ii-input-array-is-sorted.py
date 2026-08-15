class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Since in this question Two sum is mention,hence we get a hint of using Two pointer approach. 
        #Thus,I created left pointer to point the first element of the array and right pointer to point the last element of an array.
        left = 0
        right = len(numbers)-1
        # We check the condition until left is smaller than right.
        while left<right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1,right+1]
            
            elif total < target:
                left +=1
            else:
                right -= 1
        
            
