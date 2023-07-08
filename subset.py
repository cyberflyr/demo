
def subset(items: list):
    res = [[]]
    if not items:
        return res
    for idx, item in enumerate(items):
        for _item in subset(items[idx+1:]):
            res.append([item] +_item)
    return res


if __name__ == "__main__":
    l = [1, 2,3]
    print(subset(l))

    # [] -> []
    # [1] -> [[], [1]]
    # [2] -> [[], [2], [1,2]]
    # []