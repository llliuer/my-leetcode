

#leetcode 1370. 上升下降字符串
#https://leetcode-cn.com/problems/increasing-decreasing-string/
#
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


class Solution:
    def sortString(self, s: str) -> str:
        num = [0] * 26
        for ch in s:
            num[ord(ch) - ord('a')] += 1

        ret = list()
        while len(ret) < len(s):
            for i in range(26):
                if num[i]:
                    ret.append(chr(i + ord('a')))
                    num[i] -= 1
            for i in range(25, -1, -1):
                if num[i]:
                    ret.append(chr(i + ord('a')))
                    num[i] -= 1

        return "".join(ret)





