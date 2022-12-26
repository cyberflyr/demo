# 去重仍保持顺序


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe_dict(items, key_func=None):
    seen = set()
    for item in items:
        val = item if key_func is None else key_func(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == "__main__":
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    list(dedupe(a))

    b = [{"x": 1, "y": 2}, {"x": 1, "y": 3}, {"x": 1, "y": 2}, {"x": 2, "y": 4}]
    s = list(dedupe_dict(b, lambda d: (d["x"], d["y"])))
    print(s)
