
# def subset(items: list):
#     res = [[]]
#     if not items:
#         return res
#     for idx, item in enumerate(items):
#         for _item in subset(items[idx+1:]):
#             res.append([item] +_item)
#     return res

def subset(arr: list[int]):
    ans = []
    items = []
    def backtrack(i):
        ans.append(items[:])
        for j in range(i, len(arr)):
            items.append(arr[j])
            backtrack(j+1)
            items.pop()
    backtrack(0)
    return ans


if __name__ == "__main__":
    l = [1, 2, 3, 4]
    print(subset(l))

    # [] -> []
    # [1] -> [[], [1]]
    # [2] -> [[], [2], [1,2]]
    # []