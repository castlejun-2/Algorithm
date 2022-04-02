n_list = list(input())
n_list.sort(reverse=True)             #주어진수에서 아래의 식을 통과한다면 내림차순으로 된 값이 최대값이다.

sum = 0
for i in n_list:
    sum += int(i)
if '0' not in n_list or sum % 3 !=0:  #끝자리가 0이 될 수 없거나, 합이 3의배수가 아니면 30의 배수가 될 수 없다.
    print(-1)
else:
    print("".join(n_list))
