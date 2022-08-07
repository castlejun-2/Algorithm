import re

def solution(dartResult):
    dic = {'S': 1, 'D': 2, 'T': 3, '*': 2, '#': -1}
    stack = []
    for score,bonus in zip(re.findall('\d+',dartResult),re.findall('\D+',dartResult)):  #숫자와 문자로 분류
        num=int(score)**int(dic[bonus[0]])  #제곱근의 숫자를 먼저 계산
        stack.append(num)                   #stack에 삽입
        if '#' in bonus or '*' in bonus:    #만약 bonus에 특수문자가 존재한다면
            if bonus[-1]=='*':              #*라면,
                if len(stack) > 1:          #값이 2개 이상이면 뒤에서 2번째까지 *2
                    stack[-1]*=2
                    stack[-2]*=2
                else:                       #1개라면 가장 앞의 값만 *2
                    stack[-1]*=2
            else:                           #나머지는 *(-1)
                stack[-1]*=(-1)
    return sum(stack)                       #값들을 전부 더해준다. 귳
