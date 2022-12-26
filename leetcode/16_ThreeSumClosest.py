from typing import List


class Solution:
    def __init__(self):
        self.closest_val = float("+inf")
        self.three_sum = []
        self.two_sum = []

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        for index, num in enumerate(nums):
            if index + 1 > len(nums) - 1:
                break
            val = num + self.twoSumClosest(nums[index + 1 :], target=target - num)
            if val < self.closest_val:
                temp_res = [num]
                temp_res.extend(self.two_sum)
                self.three_sum = temp_res
                self.closest_val = val
            self.two_sum = []
        res = 0
        for num in self.three_sum:
            res += num
        return res

    def twoSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 2:
            return nums[0]
        distance = float("+inf") - target
        two_sum = []
        head = 0
        tail = len(nums) - 1
        while head != tail:
            result = nums[head] + nums[tail]
            if abs(result - target) < distance:
                distance = abs(result - target)
                two_sum = [nums[head], nums[tail]]

            if result == target:
                break
            elif result > target:
                tail -= 1
            else:
                head += 1

        return two_sum[0] + two_sum[1]
