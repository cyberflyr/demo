from typing import List

# class Solution:
#     # time: O(n), space: O(n)
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         sorted_list = list()
#         i, j = 0, 0
#         while i <= len(nums1)-1 and j <= len(nums2)-1:
#             if nums1[i] <= nums2[j]:
#                 sorted_list.append(nums1[i])
#                 i += 1
#                 continue
#             sorted_list.append(nums2[j])
#             j += 1
#         while i <= len(nums1)-1:
#             sorted_list.append(nums1[i])
#             i += 1
#         while j <= len(nums2)-1:
#             sorted_list.append(nums2[j])
#             j += 1
#         if len(sorted_list) % 2 == 1:
#             return sorted_list[int(len(sorted_list)/2)]
#         else:
#              return (sorted_list[int(len(sorted_list)/2)] + sorted_list[int(len(sorted_list)/2)-1]) / 2


class Solution:
    # time: O(log(m+n)), space: O(1)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_list = list()
        i, j = 0, 0
        while i <= len(nums1) - 1 and j <= len(nums2) - 1:
            if nums1[i] <= nums2[j]:
                sorted_list.append(nums1[i])
                i += 1
                continue
            sorted_list.append(nums2[j])
            j += 1
        while i <= len(nums1) - 1:
            sorted_list.append(nums1[i])
            i += 1
        while j <= len(nums2) - 1:
            sorted_list.append(nums2[j])
            j += 1
        if len(sorted_list) % 2 == 1:
            return sorted_list[int(len(sorted_list) / 2)]
        else:
            return (
                sorted_list[int(len(sorted_list) / 2)]
                + sorted_list[int(len(sorted_list) / 2) - 1]
            ) / 2


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
