def lengthOfLongestSubstring(s):
    candidate = []
    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            if s[j] in s[i:j]:
                candidate.append(len(s[i:j]))
                break
            if j == len(s) - 1:
                candidate.append(len(s[i:j + 1]))

    return max(candidate)


def lolss(s):
    ans = ''
    tmp = ''

    for i in s:
        if i not in tmp:
            tmp = tmp + i
        else:
            tmp = tmp[tmp.index(i) + 1:]
            tmp = tmp + i
        if len(tmp) > len(ans):
            ans = tmp
    return len(ans)
enum

print(lolss("a"))
