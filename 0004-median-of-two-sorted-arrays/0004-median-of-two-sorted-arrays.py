class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        m = len(merged)
        if m%2 == 1:
            return float(merged[m//2])
        else:
            return float(merged[m//2 -1] + merged[m//2])/2.0
