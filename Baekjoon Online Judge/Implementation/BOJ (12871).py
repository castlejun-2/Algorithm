f=input()
s=input()
flag=1

for i in range(len(f)*len(s)):    #강 문자열의 길이를 곱해서 같은지 비교 (최소 공배수를 구하면 시간을 단축시킬 수 있다.)
    if f[i%len(f)]==s[i%len(s)]:  #나머지를 활용
        continue
    flag=0
    break
if flag:
    print(1)
else:
    print(0)
