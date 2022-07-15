import math

def solution(w,h):
    return w*h-(w+h-math.gcd(w,h))  #전체사각형 - (반복되는 사각형에서 제외되는 사각형)*최대공약수 = w*h - ((w//gcd+h//gcd-1)*gcd)=w*h-(w+h-gcd) 식이 성립한다.
