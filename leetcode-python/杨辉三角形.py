
# 118.杨辉三角形
# https://leetcode-cn.com/problems/pascals-triangle/
#



class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # 官方解答
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(row)
        return ret

# My Solution
# 遍历，每个元素的值为上一层一样下标的值加上上一层前一个下标的值，首位为1
        res = [[1], [1, 1]]
        if numRows == 0:
            return []
        if numRows == 1:
            return [res[numRows - 1]]
        if numRows == 2:
            return res
        for i in range(2, numRows):
            # i+1 个
            temp = [1]
            for j in range(1, i):
                temp.append(res[i - 1][j - 1] + res[i - 1][j])

            temp.append(1)

            res.append(temp)
            # print(res)

        return res
