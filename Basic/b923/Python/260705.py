# 初始化stack陣列
stack = []

# 輸入測資
n = int(input())
for i in range(n):
    lst = [*map(int,input().split())]

    # 條件判斷
    if (lst[0] == 1):
        stack.pop()
    elif (lst[0] == 2):
        print(stack[-1])
    elif (lst[0] == 3):
        stack.append(lst[1])