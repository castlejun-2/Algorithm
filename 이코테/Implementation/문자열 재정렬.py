from sys import stdin

S=list(map(str,stdin.readline().strip()))
num_sum=0
result_list=[]

for s in S:
    if '0'<=s<='9': #or isAlpha() 함수 존재
        num_sum+=int(s)
    else:
        result_list.append(s)
result_list.sort()
if num_sum: #숫자가 존재한다면 이어붙혀서 출력 !예외처리가 중요
    print(''.join(map(str,result_list))+str(num_sum))
else:   #존재하지 않는다면 문자열만 출력
    print(''.join(map(str,result_list)))