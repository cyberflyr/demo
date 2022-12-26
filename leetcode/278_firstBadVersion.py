# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start < end:
            mid = (start + end) >> 1
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
        if isBadVersion(start):
            return start
        else:
            return start + 1
