# 匯入模組
from collections import deque

# 輸入測資與初始化陣列
n = int(input())
line = deque()
for i in range(n):
    lst = [*map(int,input().split())]

    if (lst[0] == 1):
        line.append(lst[1])
    elif (lst[0] == 2):
        if (len(line) == 0):
            print(-1)
        else:
            print(line[0])
    elif (lst[0] == 3):
        if (len(line) > 0):
            line.popleft()