def search(nums, target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            left = mid
            right = mid

        elif nums[left] < nums[mid]:
            if target < nums[mid] and target >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        elif nums[mid + 1] < nums[right]:
            if target <= nums[right] and target >= nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[left] == target:
                right = left
            elif nums[right] == target:
                left = right
            else:
                right = left
    if nums[left] == target:
        return left
    else:
        return -1

nums = [4,5,6,7,8,1,2,3]
target = 2
print(search(nums,target))