def multiply(num1: str, num2: str) -> str:
    if len(num2) > len(num1):
        num2, num1 = num1, num2

    single_val = []
    for j in range(len(num2) - 1, -1, -1):

        single_val.append('0' * (len(num2)-j-1))
        jw = '0'
        for i in range(len(num1) - 1, -1, -1):
            #print(int(num1(i)) * int(num2(j)) + jw)
            temp = list(str(int(num1[i]) * int(num2[j]) + int(jw)))
            jw = temp[0]

            if len(temp) == 2:  # 如果两个元素乘出来是两位，则高位给jw，低位加到single_val
                single_val[len(num2)-j-1] = temp[1] + single_val[len(num2)-j-1]
            else:
                single_val[len(num2)-j-1] = temp[0] + single_val[len(num2)-j-1]
                jw = '0'
        if jw != '0':
            single_val[len(num2)-j-1] = jw+single_val[len(num2)-j-1]
        single_val[len(num2) - j - 1] = int(single_val[len(num2)-j-1] )
    return sum(single_val)

num1 = '123444424242525'
num2 = '45624234234245236435756375368'
print(multiply(num1,num2))