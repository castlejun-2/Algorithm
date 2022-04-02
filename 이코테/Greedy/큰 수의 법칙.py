from sys import stdin

N,M,K=map(int,stdin.readline().split())
num_list=list(map(int,stdin.readline().split()))

cnt_list=[0]*N
sum=0

num_list.sort(reverse=True)
first_num=num_list[0]
second_num=num_list[1]

first_sum=0
second_sum=0

if M%(K+1)==0:
    first_sum=(M//(K+1))*K*first_num
else:
    first_sum=((M//(K+1))*K + M%(K+1))*first_num
second_sum=(M//(K+1))*second_num

print(first_sum + second_sum)

#최대 반복횟수가 K인경우 K+1의 주기적인 수열이 생성
#이 때 반복되는 각 수열은 K개의 가장 큰 수와 1개의 두번 째 큰 수를 갖는다.
#따라서 K+1로 나누었을 때 나누어 떨어지면 몫*K 개의 가장 큰 수 + 몫의 갯수만큼의 두번째 큰 수의 합이 가장 큰 수 이고,
#나누어 떨어지지 않는 경우 몫*K개의 가장 큰 수와 + M%(K+1)개의 가장 큰 수 + 몫의 갯수만큼의 두번째 큰 수의 합이 가장 큰 수가 된다.