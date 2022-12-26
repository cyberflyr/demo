def find_min_window(s: str, t: str):
    t_map = {}
    for char in t:
        t_map[char] = []
    main_line = []
    min_window_length = float("inf")
    min_window = []
    for index, char in enumerate(s):
        if char in t_map:
            t_map[char].append(index)
            main_line.append(index)
    for index in main_line:
        tmp_window = [index]
        char = s[index]
        other_chars = [key for key in t_map.keys() if key != char]
        for other_char in other_chars:
            for other_index in t_map[other_char]:
                if other_index > index:
                    tmp_window.append(other_index)
        tmp_window.sort()
        if len(tmp_window) == len(t):
            left, right = tmp_window[0], tmp_window[-1]
            distance = right - left
            if distance < min_window_length:
                min_window_length = distance
                min_window = s[left : right + 1]
    return min_window


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(find_min_window(s, t))
