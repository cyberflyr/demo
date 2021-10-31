
# '(', ')', '{', '}', '[' and ']'.
# {}()[]
# {[()[]]}
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         all_pattern = {'{', '[', '(', '}', ']', ')'}
#         left_pattern = {'{', '[', '('}
#         right_match = {
#             '}': '{',
#             ']': '[',
#             ')': '('
#         }
#         for c in s:
#             if c not in all_pattern:
#                 return False
#             if c in left_pattern:
#                 stack.append(c)
#             elif c in right_match:
#                 if stack and stack.pop(-1) == right_match[c]:
#                     continue
#                 return False
#
#         return False if stack else True

class ListNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        faster, slower = head, head
        while (slower and faster) and slower is not faster:
            slower = slower.next
            if faster.next:
                faster = faster.next.next
            else:
                break
        if slower is faster:
            return True
        return False


if __name__ == '__main__':
    s = '({}[)]'
    print(Solution().isValid(s))

