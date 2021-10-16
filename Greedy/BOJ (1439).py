s_list=list(map(int,input()));  
cnt=0
for i in range(len(s_list)-1):    #000111000 은 010으로 표현이 가능, 00110011 은 0101로 표현이 가능하다.
    if s_list[i] != s_list[i+1]:  #0->1 혹은 1->0 이 되는 시점에 cnt++
        cnt+=1
print((cnt+1)//2)                 #010 이면 ->1 이 나오는데 이는 1+1//2, 0101 이면 2가 나오는데 이는 3+1//2 이다.

--------------------

s_list=list(map(int,input()));
k=s_list[0]
cnt_0=0;
cnt_1=0;
if k == 0:
    cnt_0+=1    #0으로 연결된 수
else:
    cnt_1+=1    #1로 연결된 수
for i in range(1,len(s_list)):
    if s_list[i] == k:  #앞의 수와 같으면 계속 진행
        continue
    else:
        k=s_list[i]     #0->1 혹은 1->0으로 변하면 k 변경
        if s_list[i] == 1:  #바뀐 수에 대해 0->1로 변경시 1로 이루어진 cnt +1증가
            cnt_1+=1
        else:               #바뀐 수에 대해 1->0로 변경시 0로 이루어진 cnt +1증가
            cnt_0+=1
print(min(cnt_1,cnt_0))     #0으로 이루어진 수 혹은 1로 이루어진 수 중 적은 값을 출력
