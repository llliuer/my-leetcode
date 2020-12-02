
# 34. 在排序数组中查找元素的第一个和最后一个位置
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        if size == 0:
            return [-1, -1]

        first_position = self.__find_first_position(nums, size, target)
        if first_position == -1:
            return [-1, -1]
        last_position = self.__find_last_position(nums, size, target)
        return [first_position, last_position]

    def __find_first_position(self, nums, size, target):
        left = 0
        right = size - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                right = mid
            else:
                # nums[mid] > target
                right = mid - 1

        if nums[left] == target:
            return left
        else:
            return -1

    def __find_last_position(self, nums, size, target):
        left = 0
        right = size - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                left = mid
            else:
                # nums[mid] < target
                left = mid + 1

        # 由于能走到这里，说明在数组中一定找得到目标元素，因此这里不用再做一次判断
        return left


# My solution
# 思路：创建两个指针扫描数组。一个指针从头向后扫描，另一个指针从后向前扫描，
#      当中标时停止扫描，并且记录遇到时的下标。当low>high时表明扫描失败，返回[-1, -1]
#
#时间复杂度：O(n)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == O(n)0:
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

# My solution 2
# 思路：二分查找第一个出现的位置以及第二个出现的位置。
#
#
# 时间复杂度：O(logn)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 :
            return [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        return [self.erfen(nums, target, 0), self.erfen(nums, target, 1)]

    def erfen(self, nums, target, tp):#tp == 0表示查询左边，tp == 1表示茶韵右边
        low = 0
        high = len(nums)-1
        if target not in nums:
            return -1
        if tp == 0:
            while low<=high:

                mid = (low+high) // 2
                if nums[mid]<target:
                    low = mid + 1
                elif nums[mid]>=target:
                    high = mid - 1

            return low
        if tp == 1:
            while low<=high:
                mid = (low+high) // 2
                if nums[mid]<=target:
                    low = mid + 1
                elif nums[mid]>target:
                    high = mid -1

            return low-1


