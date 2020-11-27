
#454. 四数相加 II
#https://leetcode-cn.com/problems/4sum-ii/
#
# 1. 时间不够->拿空间换时间
# 官方答案：hash+分组
#
#



class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # 1. 时间不够->拿空间换时间

        # 官方答案：hash+分组
        h = {}
        res = 0
        N = len(A)
        for i in range(N):
            for j in range(N):
                if A[i] + B[j] not in h:
                    h[A[i] + B[j]] = 1
                else:
                    h[A[i] + B[j]] += 1

        for k in range(N):
            for l in range(N):
                if -(C[k] + D[l]) in h:
                    res += h[-(C[k] + D[l])]
        return res

        # N = len(A)
        # sum = 0
        # for i in range(N):
        #     for j in range(N):
        #         for k in range(N):
        #             for l in range(N):
        #                 if A[i]+B[j]+C[k]+D[l] == 0:
        #                     sum += 1
        # return sum
