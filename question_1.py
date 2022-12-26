#
# def find_solution(nums: list, target: int) -> list:
#     nums.sort()
#     print(nums)
#     res = []
#     left = 0
#     right = len(nums) - 1
#     while left < right:
#         if nums[left] + nums[right] > target:
#             right -= 1
#             # breakpoint()
#             continue
#         elif nums[left] + nums[right] < target:
#             # breakpoint()
#             tmp_sum = nums[left] + nums[right]
#             tmp_res = [nums[left]]
#             tmp_left = left + 1
#             while tmp_left < right:
#                 if tmp_sum + nums[tmp_left] >= target:
#                     break
#                 else:
#                     tmp_sum += nums[tmp_left]
#                     tmp_res.append(nums[tmp_left])
#                     tmp_left += 1
#             if tmp_sum == target:
#                 tmp_res.append(nums[right])
#                 res.append(tmp_res)
#         else:
#             # breakpoint()
#             if [nums[left], nums[right]] not in res:
#                 res.append([nums[left], nums[right]])
#         left += 1
#     return res
def find_solution_recursive(nums: list, target: int) -> list:
    res = []
    if not nums:
        return res
    for index, num in enumerate(nums):
        tmp_res = []
        new_target = target - num
        if target - num > 0:
            tmp_res = find_solution_recursive(nums[index + 1 :], new_target)
        elif target == num:
            res.append([num])
            continue
        else:
            break
        if tmp_res:
            for item in tmp_res:
                item.extend([num])
                if item not in res:
                    res.append(item)
    return res


if __name__ == "__main__":
    l = [3, 5, 3, 6, 6, 2, 5, 9]
    l.sort()
    target = 2
    # print(find_solution(nums=l, target=target))
    # l.sort()
    print(find_solution_recursive(nums=l, target=target))
    #
    # return [[3,3,2], [3,5], [2,6]]
