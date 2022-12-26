from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1
        res = []
        while start <= end:
            pow_start = pow(nums[start], 2)
            pow_end = pow(nums[end], 2)
            if pow_start >= pow_end:
                res.append(pow_start)
                start += 1
            else:
                res.append(pow_end)
                end -= 1
        res.sort()
        return res
