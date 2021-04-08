from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _d = dict()
        for index, num in enumerate(nums):
            diff = target-num
            if _d.get(diff) is not None and _d.get(diff) != index:
                return [index, _d.get(diff)]
            _d[num] = index
        return []


if __name__ == '__main__':
    s = [3, 2, 4]
    target = 6
    print(Solution().twoSum(s, target))