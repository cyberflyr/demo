from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        length = len(matrix[0])
        height = len(matrix)
        min_of_matrix = matrix[0][0]
        max_of_matrix = matrix[height-1][length-1]
        if (target < min_of_matrix or target > max_of_matrix):
            return False
        for line, l in enumerate(matrix):
            if target <= l[0]:
                break
        if target == l[0]:
            return True
        l = matrix[line-1] if target < l[0] else matrix[line]
        start, end = 0, len(l)-1
        while start <= end:
            mid = ((start + end) >> 1)
            if l[mid] > target:
                end = mid - 1
            elif l[mid] < target:
                start = mid + 1
            else:
                return True
        return False


if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    print(Solution().searchMatrix(matrix, 30))