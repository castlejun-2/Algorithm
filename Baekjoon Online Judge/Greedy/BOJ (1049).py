from sys import stdin

N,M=map(int,stdin.readline().split())
pk_list=[]
one_list=[]
nsum=0

for _ in range(M):
    price=tuple(map(int,stdin.readline().split()))
    pk_list.append(price)
    one_list.append(price)

pk_list.sort(key=lambda x:x[0])     #package 작은순
one_list.sort(key=lambda x:x[1])    #낱개 작은순

if one_list[0][1]*6 < pk_list[0][0]:    #낱개 6개가 가장 저렴한 package보다 저렴할 때
    nsum=one_list[0][1]*N
else:                                   
    nsum=min(pk_list[0][0]*(N//6)+one_list[0][1]*(N%6),pk_list[0][0]*((N//6)+1))    #나머지를 package로 다 채운것과 package로 채우고 나머지는 낱개로 채운것중 더 저렴한 것과 비교
print(nsum)
