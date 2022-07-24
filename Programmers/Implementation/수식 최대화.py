#연산자의 index 위치를 활용한 문제풀이
from itertools import permutations
import copy

def solution(expression):
    answer = []
    num = []
    tmp = ""
    for i in range(len(expression)):
        if expression[i].isdecimal():
            tmp+=expression[i]
        else:
            num.append(tmp)
            num.append(expression[i])
            tmp = ""
    num.append(tmp) #숫자와 연산자로 구분하여 list 생성
        
    for per in list(permutations(['*','-','+'],3)): #각 연산자의 우선순위 가능 조합 생성
        tnum=copy.deepcopy(num)
        cnt=0
        for op in per:  #우선순위 별로 연산 수행
            while op in tnum: #해당 list에 현재 연산자가 없을 때 까지 반복
                tmp=eval(str(tnum[tnum.index(op)-1])+op+str(tnum[tnum.index(op)+1]))  #연산자의 index에서 앞 뒤값 연산
                tnum.pop(tnum.index(op)+1)  #연산 후 뒤의 값부터 제거
                tnum.pop(tnum.index(op)-1)  #연산 후 앞의 값 제거
                tnum[tnum.index(op)]=tmp  #연산자의 가장 앞의 위치를 연산한 값으로 대체
        answer.append(abs(tnum[0]))  #최후에 계산된 값 answer에 추가
    return max(answer) #answer값중 최대값을 반환 

#f-string을 활용한 역발상 문제풀이(모범 답안)                                            
def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a): #최 우선 연산자를 기준으로 문자열을 split
            temp = [f"({i})" for i in e.split(b)] #그 다음 우선순위 연산자를 기준으로 문자열을 split 하며 ()를 씌워줌
            temp_list.append(f'({b.join(temp)})') #다시 괄호를 쒸운 상태로 b 연산자를 추가해 한번더 괄호를 씌워줌
        answer.append(abs(eval(a.join(temp_list)))) #각 연산자 우선순위를 기준으로 ()가 씌워져서 역순으로 계산됨
    return max(answer) 
