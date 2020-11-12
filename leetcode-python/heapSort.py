ARR=[26,44,38,5,47,15,36,3,27,2,46,4,19,50,48]
ARR = [0]+ARR

def BuildHeap(a):
    n = len(a)
    for i in range(n//2, 0, -1):
        AdjustHeap(a, i, n)


def AdjustHeap(a, k, n):#调整a数组第k个元素为根的子树为大顶树

    a[0] = a[k]
    i= 2*k
    while i < n:

        if a[i] < a[i+1]:
            i = i + 1

        if a[0] <= a[i]:
            a[k] = a[i]
            k = i
        else:
            break
        i = i * 2
    a[k] = a[0]

n = len(ARR)-1
#1建立一颗大根树
BuildHeap(ARR)
for i in range (n, 1, -1):
    ARR[1], ARR[i] = ARR[i], ARR[1]
    AdjustHeap(ARR, 1, i-1)

print(ARR)