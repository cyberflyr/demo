from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for index in range(1, len(nums)):
            start, end = 0, len(nums) - 1
            target = 0 - nums[index]
            if index > 1 and nums[index] == nums[index - 1]:
                start = index - 1
            while start < index < end:
                if start > 0 and nums[start] == nums[start - 1]:
                    start += 1
                    continue
                if end < len(nums) - 1 and nums[end] == nums[end + 1]:
                    end -= 1
                    continue
                if nums[start] + nums[end] < target:
                    start += 1
                elif nums[start] + nums[end] > target:
                    end -= 1
                else:
                    res.append([nums[start], nums[index], nums[end]])
                    start += 1
                    end -= 1
        return res


if __name__ == "__main__":
    res = Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4])
    print(res)
