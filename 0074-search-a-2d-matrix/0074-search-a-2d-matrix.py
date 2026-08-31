class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # Binary Search on the "virtual" 1D array
        left = 0
        right = ROWS * COLS - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Map the 1D mid index back to 2D coordinates
            row = mid // COLS
            col = mid % COLS
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False