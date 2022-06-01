N=int(input())
cup_holder=input()

cnt=cup_holder.count('LL')
if cnt>1:
    print(N-cnt+1)
else:
    print(N)