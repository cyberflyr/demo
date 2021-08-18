class Solution:

    @staticmethod
    def _get_predecessor(character):
        d = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        return d[character]

    def isValid(self, s: str) -> bool:
        stack = []
        for character in s:
            if character in ['(', '[', '{']:
                stack.append(character)
            elif character in [')', ']', '}']:
                try:
                    if stack[-1] != self._get_predecessor(character):
                        return False
                    else:
                        stack.pop(-1)
                except Exception as e:
                    return False
        if not stack:
            return True
        return False


if __name__ == '__main__':
    s = '()'
    print(Solution().isValid(s))