#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/5/12 14:25'


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        m = [-1]*n

        return self.memoized_rob(nums,m, 0,n-1)

    def memoized_rob(self, nums, m, i,end):
        if m[i] > 0:
            return m[i]
        if i == end:
            m[i] = nums[i]
        else:
            for k in range(i,end+1):
                if k + 2 > end:
                    t = nums[k]
                else:
                    t = nums[k] + self.memoized_rob(nums, m, k + 2,end)
                if m[i] < t:
                    m[i] = t
        return m[i]

a=Solution()
a.rob([8,2,3,8,4])
print(a)