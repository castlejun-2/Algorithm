while True:
    str=input()
    if str=='.':                                  #문장의 첫 문자열이 '.'이면 프로그램 종료
        break;
    str_open=[]
    status=True                                   #문장의 균형여부를 판단해줄 변수
    for ch in str:                    
        if ch=='[' or ch=='(':                    #여는 괄호의 문자열일 경우 str_open list에 삽입
            str_open.append(ch)
        elif ch==']':                             #닫는 괄호의 ']'일 경우, str_open이 비어있거나, 가장 마지막에 삽입된 괄호가 '['가 아닐경우 균형실패로 바꾼 후 break
            if not str_open or str_open[-1]!='[':
                status=False
                break
            elif str_open[-1]=='[':               #닫는 괄호의 ']'일 경우, 가장 마지막에 삽입된 괄호가 '['가 맞는경우 균형이 잘 잡혀가고 있으므로 마지막에 삽입된 '[' 을 pop
                str_open.pop()
        elif ch==')':                             #위의 ']'와 같이 판단하여 실행
            if not str_open or str_open[-1]!='(':
                status=False
                break
            elif str_open[-1]=='(':
                str_open.pop()
    if not str_open and status==True:             #str_open의 list가 비어있고, 균형여부가 True일 경우 "yes" 출력
        print("yes")
    else:                                         #그 외의 경우들은 전부 "no" 
        print("no")
