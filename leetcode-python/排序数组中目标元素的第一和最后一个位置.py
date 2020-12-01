
# 34. 在排序数组中查找元素的第一个和最后一个位置
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#


# My solution
#
#
#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        low = 0
        high = len(nums) - 1

        res = [-1] * 2
        lowflag = 1
        highflag = 1
        while low <= high and lowflag + highflag != 0:
            if lowflag:

                if nums[low] == target:
                    res[0] = low
                    lowflag = 0
                else:
                    low += 1
            if highflag:

                if nums[high] == target:
                    res[1] = high
                    highflag = 0
                else:
                    high -= 1

        return res