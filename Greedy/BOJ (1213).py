from sys import stdin

p_list=list(map(str,stdin.readline().strip()))

asci_list=[0]*26
odd_num=0
odd_chr=''
answer=''

for i in p_list:
    asci_list[ord(i)-65]+=1
    
for i in range(26):
    if asci_list[i]%2==1:
        odd_num+=1
        odd_chr=chr(i+65)
    answer+=chr(i+65)*(asci_list[i]//2) #뒤는 반복되는 수열이므로 각 문자의 절반갯수만큼을 answer에 삽입한다.

if odd_num > 1:   #홀수인 갯수가 1개 이상이면 팰린드롬 문자열은 만들어지지 않는다.
    print("I'm Sorry Hansoo")
else:
    reverse_anser=reversed(answer)  #반복되는 문자열을 저장한다.
    answer+=odd_chr #홀수개인 문자열이 존재한다면 반복뒤기 전 앞의 answer의 끝에 삽입하여준다.
    print(answer + ''.join(reverse_anser))  #두 문자열을 이어준다.
