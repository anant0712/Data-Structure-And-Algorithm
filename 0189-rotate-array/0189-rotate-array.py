class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k = k % n
        
        def rev(l,j):
            while l<j:
                nums[l],nums[j]=nums[j],nums[l]
                l+=1
                j-=1
        rev(0,n-1)
        rev(0,k-1)
        rev(k,n-1)
            
        """
        Do not return anything, modify nums in-place instead.
        """
        