bracket_arr=list(input())

stack=[]
answer=0
temp=1

for i in range(len(bracket_arr)):   #문자열이 ()와 []로 닫혔을 때를 기준으로 현재 쌓여 있는 값을 answer에 더한다.
    if bracket_arr[i]=='(':
        stack.append('(')
        temp*=2
    elif bracket_arr[i]=='[':
        stack.append('[')
        temp*=3
    elif bracket_arr[i]==')':
        if not stack or stack[-1]=='[':
            answer=0
            break
        if bracket_arr[i-1]=='(':
            answer+=temp
        stack.pop()
        temp//=2
    elif bracket_arr[i]==']':
        if not stack or stack[-1]=='(':
            answer=0
            break
        if bracket_arr[i-1]=='[':
            answer+=temp
        stack.pop()
        temp//=3
if stack:
    print(0)
else:
    print(answer)   