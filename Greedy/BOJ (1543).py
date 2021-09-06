import sys

if __name__=="__main__":
    dic=input()
    word=input()
    
    leng=len(dic)-len(word)              #반복문에서 len 함수의 사용을 줄이기 위해서 변수로 선언하여 준다.
    cnt = 0
    n = 0
    while n <= leng:                     #n이 leng의 길이보다 넘어가게 되면 반복을 멈춘다.
        if dic[n:n+len(word)] == word:   #문서에서 word가 나오는지 word의 길이만큼 짤라서 확인하여준다.
            cnt+=1
            n+=len(word)                 #word와 일치한다면 word의 길이만큼 index를 더해준다.
        else:
            n+=1                         #그렇지 않다면 n에 +1만을 더해준다.
    
    print(cnt)                           #cnt의 갯수를 출력하고 종료한다.
