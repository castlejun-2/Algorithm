# from itertools import permutations

# def back(case):
#     tmp=0
#     for i in range(len(case)-1):
#         tmp+=abs(case[i]-case[i-1])
#     return tmp

# N=int(input())
# num_list=list(map(int,input().split()))
# answer=0

# for case in permutations(num_list,N):   #N의 갯수가 적으므로 전체탐색이 가능
#     answer=max(answer,back(case))
# print(answer)

def back(case):
    global answer
    if len(case)==N:
        tmp_sum=0
        for i in range(N-1):
            tmp_sum+=abs(case[i]-case[i+1])
        answer=max(answer,tmp_sum)  #생성된 길이 N의 case로 나온 tmp_sum과 answer의 값 비교
        return
    
    for i in range(N):  #조합으로 순열 생성
        if not visited[i]:
            visited[i]=1
            case.append(num_list[i])
            back(case)
            case.pop()
            visited[i]=0
            
N=int(input())
num_list=list(map(int,input().split()))
visited=[0]*N
answer=0

back([])
print(answer)