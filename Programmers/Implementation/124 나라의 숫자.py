def solution(n):
    n_arr=["1","2","4"]
    answer=""
    while (n>0):    # 3진법의 원리를 활용하여 나머지들을 출력해가며 붙혀나가준다.
        n-=1
        answer=n_arr[n%3]+answer
        n//=3
    return answer