class Solution:
    def findMaxAverage(self, arr: List[int], k: int) -> float:
        window_sum = sum(arr[:k])
        max_sum = window_sum

        for i in range(k,len(arr)):
            window_sum = window_sum + arr[i] - arr[i-k]

            max_sum = max(max_sum,window_sum)
        
        return max_sum / float(k)