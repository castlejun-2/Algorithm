def solution(n, t, m, p):
    dic = { 10:'A', 11:'B',12:'C',13:'D',14:'E',15:'F' }
    
    def change(num,k):  #진법 변환 함수
        result=''
        while num > 0:
            num,mod = divmod(num,k)
            if k>=10 and 10<=int(mod)<=15:  #진법이 10이상이고 나머지가 10-15 사이일 때 A-F로 치환
                result+=dic[mod]
            else:
                result+=str(mod)
        return result[::-1]
    
    answer = '0' #0부터 시작
    for i in range(1,m*t):  #최대 m*t만큼 필요하므로 해당 횟차까지 반복
        answer+=change(i,n)
    return answer[p-1:m*t:m]
