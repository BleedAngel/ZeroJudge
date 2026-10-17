#a044

#提高遞迴限制
import sys
sys.setrecursionlimit(10000)

def f(n,i,d,ans):
  if(i<n):
    d+=i
    ans+=d
    return f(n,i+1,d,ans)
  else:
    return ans

while True:
  try:
    n=int(input())
    i,d,ans=0,1,1
    print(f(n,i,d,ans))
  except EOFError:
    break
