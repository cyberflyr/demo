class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        max_sub_s = ""
        for index, c in enumerate(s):
            s_from_center = self.from_center_is_Palindrome(s, index)
            s_from_side = self.from_side_is_Palindrome(s, index)

            if len(s_from_center) > len(max_sub_s):
                max_sub_s = s_from_center
            if len(s_from_side) > len(max_sub_s):
                max_sub_s = s_from_side

        return max_sub_s

    def from_center_is_Palindrome(self, s, index) -> str:
        sub_s = ""
        center = index
        left = center - 1
        right = center + 1
        while (not sub_s) and (left >= 0 and right <= len(s) - 1):
            distance = center - left
            if s[left] and s[right] and s[left] == s[right]:
                left -= 1
                right += 1
            elif distance == 1:
                if s[left] == s[center]:
                    sub_s = s[left : center + 1]
                elif s[right] == s[center]:
                    sub_s = s[center : right + 1]
                else:
                    break
            else:
                break
        if not sub_s:
            sub_s = s[left + 1 : right]
        return sub_s

    def from_side_is_Palindrome(self, s, index) -> str:
        left = index
        right = index + 1
        if right > len(s) - 1:
            return s[left]
        if s[left] != s[right]:
            return s[left]
        while (left >= 0 and right <= len(s) - 1) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]
