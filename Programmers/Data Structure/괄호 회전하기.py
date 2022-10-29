def solution(s):
    def check(str):
        stack=[]
        for s in str:
            if s=='[' or s=='(' or s=='{': stack.append(s)
            elif s==']' and stack and stack[-1]=='[': stack.pop()
            elif s=='}' and stack and stack[-1]=='{': stack.pop()
            elif s==')' and stack and stack[-1]=='(': stack.pop()
            else: return False
        if stack: return False
        return True
    
    answer = 0
    for i in range(len(s)): 
        if check(s[i:]+s[:i]):  #문자열을 Slicing해서 옳바른 괄호 여부 탐색
            answer+=1
    return answer
