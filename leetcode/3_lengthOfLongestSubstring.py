class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charactor_map = dict()
        if len(s) == 1:
            return 1
        pre_cursor, max_length = 0, 0
        charactors = list(s)
        for cursor, charactor in enumerate(charactors):
            if charactor not in charactor_map:
                charactor_map[charactor] = cursor
                continue
            if len(charactor_map) > max_length:
                max_length = len(charactor_map)
            while charactor_map.get(charactor) is not None and pre_cursor <= charactor_map[charactor]:
                del (charactor_map[charactors[pre_cursor]])
                pre_cursor += 1
            charactor_map[charactor] = cursor
        if len(charactor_map) > max_length:
            max_length = len(charactor_map)
        return max_length


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    # print(" ".split())
    # print(len(" "))