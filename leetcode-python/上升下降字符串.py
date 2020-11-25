

#leetcode 1370. 上升下降字符串
#
#

class Solution:
    def sortString(self, s: str) -> str:
        bucket = [0] * 26
        for i in s:
            bucket[ord(i) - 97] += 1
        index = 0
        flag = 1  # =1表示正序遍历，=0表示逆序遍历
        res = ""
        while (sum(bucket) != 0):

            if flag == 1:
                if index == 26:
                    flag = 0
                    index -= 1
                    continue

                if bucket[index] != 0:
                    res = res + chr(index + 97)
                    bucket[index] -= 1
                index += 1
            elif flag == 0:
                if index == -1:
                    flag = 1
                    index += 1
                    continue
                if bucket[index] != 0:
                    res = res + chr(index + 97)
                    bucket[index] -= 1
                index -= 1
        return res


