class Solution:
    def restoreIpAddresses(self, s: str):
        # r = []
        # def restore(count=0, ip='', s=''): # count record split times, ip record ip, s record remaining string
        #     if count == 4:
        #         if s == '':
        #             r.append(ip[:-1])
        #         return
        #     if len(s) > 0:
        #         restore(count+1, ip+s[0]+'.', s[1:])
        #     if len(s) > 1 and s[0] != '0':
        #         restore(count+1, ip+s[:2]+'.', s[2:])
        #     if len(s) > 2 and s[0] != '0' and int(s[0:3]) < 256:
        #         restore(count+1, ip+s[:3]+'.', s[3:])
        # restore(0, '', s)
        # return r

        res = []

        def dfs(count, ip, s):
            if count == 4:
                if s == '':
                    res.append(ip[:-1])
                return

            if len(s) > 0:

                dfs(count+1, ip+ s[0] + '.', s[1:])
            if len(s) > 1 and s[0] != 0:

                dfs(count + 1, ip + s[:2] + '.', s[2:])
            if (len(s) > 2) and (int(s[:3]) < 256) and (s[0] != 0):

                dfs(count + 1, ip + s[:3] + '.', s[3:])

        dfs(0, '', s)
        return res


S = Solution()
res = S.restoreIpAddresses("25525511135")

print(res)
