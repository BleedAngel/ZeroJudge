# 定義f91函式
def f91 (n):
    if (n <= 100):
        return f91(f91(n+11))
    else:
        return n-10

while True:
    
    # 輸入測資
    n = int(input())

    # n == 0 代表結束
    if (n == 0):
        break

    # 輸出
    print(f"f91({n}) = {f91(n)}")