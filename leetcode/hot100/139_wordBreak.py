from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            prefix = s[: i + 1]
            if prefix in wordDict or dp[i]:
                dp[i] = True
                for j in range(i + 1, len(s)):
                    sub_s = s[i + 1 : j + 1]
                    if sub_s in wordDict:
                        dp[j] = True
        return dp[-1]


if __name__ == "__main__":
    print(Solution().wordBreak("applepenapple", ["apple", "pen"]))
