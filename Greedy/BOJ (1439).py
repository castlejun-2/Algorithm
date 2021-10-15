s_list=list(map(int,input()));  
cnt=0
for i in range(len(s_list)-1):    #000111000 은 010으로 표현이 가능, 00110011 은 0101로 표현이 가능하다.
    if s_list[i] != s_list[i+1]:  #0->1 혹은 1->0 이 되는 시점에 cnt++
        cnt+=1
print((cnt+1)//2)                 #010 이면 ->1 이 나오는데 이는 1+1//2, 0101 이면 2가 나오는데 이는 3+1//2 이다.
