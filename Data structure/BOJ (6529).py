from sys import stdin
while True:
    h_list=list(map(int,stdin.readline().split()))
    if not h_list[0]:
        break;
    stack=[]
    max_h=0
    for i in range(1,h_list[0]+1):
        i-=1
        expand=i
        while stack and stack[-1][0]>=h_list[i]:
            h,expand=stack.pop()
            tmp_width=h*(i-expand)
            max_h=max(max_h,tmp_width)
        stack.append([h_list[i],expand])
    for h,expand in stack:
        max_h=max(max_h,h*(h_list[0]-expand))
    print(max_h)
