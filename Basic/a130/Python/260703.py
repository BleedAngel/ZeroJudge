# 輸入測資
t = int(input())
for _ in range(t):
    lst = []
    for i in range(10):
        url, relevance = input().split()
        # 陣列格式: (int(相關性), 網址)
        lst.append((int(relevance), url))

    # 依相關度排序
    lst.sort(key = lambda x: x[0], reverse = True)

    # 輸出相關度最高之網址
    max_relevance = lst[0][0]
    print(f"Case #{_+1}:")
    for i in range(10):
        if (lst[i][0] == max_relevance):
            print(lst[i][1])
        else:
            break