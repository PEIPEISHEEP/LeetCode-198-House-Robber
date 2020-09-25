class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        now = pre = 0
        for i in nums:
            pre, now = now, max(i+pre, now)
        return now
        