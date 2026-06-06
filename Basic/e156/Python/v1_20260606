#e156

#提高遞迴限制
import sys
sys.setrecursionlimit(10000)

def f(ans,i,n):
  if(i<=n):
    ans+=i
    return f(ans,i+1,n)
  else:
    return ans

n=int(input())
ans,i=0,1
print(f(ans,i,n))
