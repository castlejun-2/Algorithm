from sys import stdin

N=int(stdin.readline().strip())
cnt=0

#24*60*60 < 1,000,000 이므로 완전탐색을 해도 1초도 걸리지 않는다.
#시간제한 1초, Data 100만개 이하이하면 -> O(NlogN)
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                cnt+=1
print(cnt)                            