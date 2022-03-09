from sys import stdin

N=int(stdin.readline())

for _ in range(N):
    T=int(stdin.readline())
    costume_list={}
    for i in range(T):
        costume,costume_type=map(str,stdin.readline().split())
        if costume_type in costume_list:
            costume_list[costume_type].append(costume)
        else:
            costume_list[costume_type] = [costume]
     #저장한 딕셔너리 값들을 어떻게 끌어 사용할지 고민 or 값을 일일이 저장하지 않고 사용 할 수 있는 방법 고민
