N=int(input())
p_list=[]
p_list.append(0)        #0일 때의 초기값 p_list[0] 설정
p_list.append(1)        #1일 때의 초기값 p_list[1] 설정
for i in range(2,N+1):  #N>=2 이상일 때 해당 반복문 실행
    p_list.append(p_list[i-1]+p_list[i-2])
print(p_list[N])        #N번째 p_list의 값 출력
