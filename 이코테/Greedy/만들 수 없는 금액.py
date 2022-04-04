from sys import stdin

N=int(stdin.readline().strip())
coin_list=list(map(int,stdin.readline().split()))

coin_list.sort()
money=1

for i in coin_list:
    if i > money:   #해당 coin으로 money를 만들 수 있는지 확인
        break   #만들 수 없다면 break
    else:
        money+=i    #만들 수 있다면 (만들 수 있는 금액 + i 이전 까지의 값)까지 만들 수 있으므로 +i를 현재 money에 더한다.
print(money)    #만들 수 없는 가장 작은 금액이 money에 들어있게 된다.