from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_char_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        l = [digit_char_map[i] for i in digits]
        res = []
        for index in range(len(l) - 1, -1, -1):
            if res:
                tmp_res = []
                for char in l[index]:
                    for c in res:
                        s = char + c
                        tmp_res.append(s)
                res = tmp_res
            else:
                res = l[index][:]
        return res
