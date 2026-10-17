# 輸入測資
n, k = map(int,input().split())
lst = [*map(int,input().split())]
ask = [*map(int,input().split())]

# 定義二分搜尋
def binary_search (i,lst):
    start, end = 0, len(lst)-1
    while start <= end:
        mid = (start + end)//2
        if (i == lst[mid]):
            return mid + 1
        elif (i>lst[mid]):
            start = mid + 1
        else:
            end = mid - 1
    return 0

# 逐行輸出
for i in ask:
    print(binary_search (i, lst))