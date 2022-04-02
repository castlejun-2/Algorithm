from sys import stdin

def back(lotto):
    global l_list
    if len(lotto)==6:
        print(' '.join(lotto))
    else:
        for i in l_list[1:]:
            if not lotto:                           #lotto 번호가 비어있다면 조건 비교 없이 lotto list에 추가
                lotto.append(i)
                back(lotto)
                lotto.pop()
            elif int(lotto[-1])<int(i):             #현재 lotto 번호에 들어있는 마지막 값보다 들어갈 값이 클 경우에만 lotto list에 추가
                lotto.append(i)
                back(lotto)
                lotto.pop()
while True:
    l_list=list(map(str,stdin.readline().split()))
    lotto=[]
    if l_list[0]=='0':                              #'0'이 들어오면 프로그램 종료
        break
    back(lotto)
    print('')
