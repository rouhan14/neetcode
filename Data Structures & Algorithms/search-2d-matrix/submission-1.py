class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = (len(matrix[0]) * len(matrix)) - 1

        while left <= right:

            mid = (left + right) //2
            r = mid//len(matrix[0])
            c = mid%len(matrix[0])

            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                left = mid + 1
            else:
                right = mid - 1
            
        return False

