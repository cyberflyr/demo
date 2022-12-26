from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left, right = 0, len(height) - 1
        while left < right:
            length = right - left
            width = min(height[left], height[right])
            tmp_area = length * width
            if tmp_area > area:
                area = tmp_area
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return area
