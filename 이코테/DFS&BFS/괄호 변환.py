from sys import stdin
p="()))((()"

def divide(p):  # 문자열 p를 u, v로 분리하는 함수
    open_p = 0
    close_p = 0

    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[:i + 1], p[i + 1:]

def check(u):   # 문자열 u가 올바른 괄호 문자열인지 확인하는 함수
    stack = []

    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()

    return True

def solution(p):
    # 1
    if not p:
        return ""
    
    # 2
    u, v = divide(p)
    
    # 3
    if check(u):
        # 3-1
        return u + solution(v)
    # 4
    else:
        # 4-1
        answer = '('
        # 4-2
        answer += solution(v)
        # 4-3
        answer += ')'

        # 4-4
        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('

        # 4-5
        return answer

print(solution(p))