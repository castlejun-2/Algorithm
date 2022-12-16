N=int(input())
h_list=list(map(int,input().split()))

def answer(heights):
    if sum(heights)%3!=0:   #h_list가 3의 배수가 아니라면, h_list는 만들지 못한다.
        return "NO"
    quotient_2=0
    for h in heights:
        quotient_2+=h//2    #h_list가 2로 나누어지는 나무의 몫을 계산한다.
    if quotient_2>=sum(heights)//3:     #2로 나누어지는 몫의 합 quotient_2가 sum(heights)//3 보다 크다면 나머지는 1을 K번해서 채울 수 있다.
        return "YES"
    return "NO" 
    
print(answer(h_list))