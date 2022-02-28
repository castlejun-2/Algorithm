N,M=map(int,stdin.readline().split())
pk_list=[]
one_list=[]

for _ in range(M):
    price=tuple(map(int,stdin.readline.split()))
    pk_list.append(price)
    one_list.append(price)

pk_list.sort()
one_list.sort()
