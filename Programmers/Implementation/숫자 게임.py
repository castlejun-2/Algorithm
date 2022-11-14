def solution(A, B):
    answer = 0
    
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    for i in A:       #이길 수 있는 A의 갯수를 Count 한다.
        if i < B[0]:
            answer+=1
            del B[0]
    
    return answer
