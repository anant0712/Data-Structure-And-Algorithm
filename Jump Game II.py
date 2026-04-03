from typing import List


class Solution:
    def Jumps(self, arr: List[int]) -> int:
        ans =0
        end = 0
        farthest = 0

        for i in range(len(arr)-1):
            farthest = max(farthest, i+ arr[i])
            if farthest >= len(arr):
                ans +=1
                break
            if i == end:
                ans += 1
                end = farthest
        return ans


obj = Solution()
print(obj.Jumps([2,3,1,1,4]))
