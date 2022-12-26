class Solution:
    def longestxx(self, s: str) -> str:
        longest_sub_s = ""
        if len(s) == 1:
            return s
        for index, c in enumerate(s):
            sub_s_from_single = self.sub_s_from_single(s, index)
            sub_s_from_pair = self.sub_s_from_pair(s, index)
            if len(sub_s_from_single) > len(longest_sub_s):
                longest_sub_s = sub_s_from_single
            if len(sub_s_from_pair) > len(longest_sub_s):
                longest_sub_s = sub_s_from_pair
        return longest_sub_s

    def sub_s_from_single(self, s: str, index: int) -> str:
        left = index - 1
        right = index + 1
        while left >= 0 and right <= len(s) - 1:
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        return s[left + 1 : right]

    def sub_s_from_pair(self, s: str, index: int) -> str:
        left = index
        right = index + 1
        while left >= 0 and right <= len(s) - 1:
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        return s[left + 1 : right]


if __name__ == "__main__":
    # s = "babad"
    s = "cbbd"
    res = Solution().longestxx(s)
    print(res)
