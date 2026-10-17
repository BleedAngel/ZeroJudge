while True:
    try:

        # 輸入測資
        n=int(input())

        # 輸出
        print(f"'C' can use printf(\"%d\",n); to show integer like {n}")
    
    except EOFError:
        break