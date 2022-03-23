from sys import stdin

T=int(stdin.readline())
for _ in range(T):
    changes=int(stdin.readline())
    print(changes//25,end=" ")
    
    changes-=(changes//25)*25
    print(changes//10,end=" ")
    changes-=(changes//10)*10
    
    print(changes//5,end=" ")
    changes-=(changes//5)*5
    
    print(changes%5)
