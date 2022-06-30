def convert(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

def isPrime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):    #소수 갯수를 구할 때 시간 단축을 위해 제곱근까지만 구해준다.
        if n%i==0:
            return False
    return True

def solution(n, k):
    convertednum=convert(n,k)
    answer = 0
    for r in convertednum.split('0'):   #0으로 나누었을 때의 값이 소수인지 판별해주면 된다.
        if r.isdigit():
            if isPrime(int(r)):
                answer+=1
    return answer