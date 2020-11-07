def findlength(nums):

    #nums.sort()
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1

    length = [1]
    state = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            if state == 0:
                length.append(2)
                state = 1
            if state == 1:
                length[-1] = length[-1] + 1
        else:
            state = 0
    return length
findlength([1,3,5,4,7])