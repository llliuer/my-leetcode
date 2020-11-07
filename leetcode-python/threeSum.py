def threeSum(nums):
    if len(nums) < 3:
        return []
    res = []
    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append(sorted([nums[i], nums[j], nums[k]]))
    index = 0
    res_len = len(res)
    while index <= res_len:
        if len(res) > 0:

            i = res.pop(0)
            print(i)
            if not (i in res):
                res.append(i)
        index = index + 1
    return res


def new_threeSUM(nums):
    if len(nums) < 3: return []

    nums = sorted(nums)
    res = []
    for i in range(0, len(nums)):

        if (i > 0) and (nums[i] == nums[i - 1]): continue

        begin, end = i + 1, len(nums) - 1
        while begin < end:
            if nums[i] + nums[begin] + nums[end] < 0:
                begin = begin + 1
            elif nums[i] + nums[begin] + nums[end] > 0:
                end = end - 1
            else:
                if (begin > i + 1) and (nums[begin] == nums[begin - 1]):
                    begin = begin + 1
                elif (end < len(nums) - 1) and nums[end] == nums[end + 1]:
                    end = end - 1
                else:
                    res.append([nums[i], nums[begin], nums[end]])
                    begin = begin + 1
                    end = end - 1

        if nums[i] > 0: break
    return res


a = [0, 0, 0]
print(new_threeSUM(a))
