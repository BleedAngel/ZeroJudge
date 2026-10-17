# 匯入模組
from collections import deque

# 定義 check函式
def check(lst_a, lst_b, station):

    # 條件判斷
    while (len(lst_b) != 0):
        try:
            if (len(station) > 0):

                # station 移至 b
                if (lst_b[0] == station[-1]):
                    lst_b.popleft()
                    station.pop()
                
                elif (lst_b[0] < station[-1]):
                    return "No"
                
                # a 移至 station
                else:
                    station.append(lst_a[0])
                    lst_a.popleft()

            # a 移至 b
            elif (lst_a[0] == lst_b[0]):
                lst_b.popleft()
                lst_a.popleft()
            
            # a 移至 station
            else:
                station.append(lst_a[0])
                lst_a.popleft()
        except:
            return "No"
    return "Yes"

while True:

    #輸入測資
    n = int(input())
    if (n == 0):
        break
    while True:
        lst_b = deque([*map(int,input().split())])
        if (lst_b[0] == 0):
            print()
            break

        # 初始化陣列
        lst_a = deque(range(1,n+1))
        station = []

        # 檢查與輸出
        answer = check(lst_a, lst_b, station)
        print(answer)