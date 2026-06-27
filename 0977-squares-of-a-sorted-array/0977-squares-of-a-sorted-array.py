class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            res.append(i**2)
        
        res.sort()
        return res

       # sorted(nums[i]**2 for i in range(len(nums)))