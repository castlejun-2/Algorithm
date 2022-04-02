from sys import stdin

N = int(stdin.readline().strip())
s_list = ['  *   ',' * *  ','***** ']                   #복사되어 붙혀질 때 한칸의 공백이 존재함으로 끝에 한칸 띄워준다.

def draw(blank):
    if blank == N:                    
        print('\n'.join(s_list))                        #공백이 N과 같아지면 별찍기를 멈추고 출력한다.
    else:
        length=len(s_list)
        for i in range(length):                         
            s_list.append(s_list[i]+s_list[i])          #반복횟수가 증가할 때마다 이 전까지 그려진 그림이 2개 복사되어 아래에 이어 붙혀지는데
            s_list[i]=' '*blank+s_list[i]+' '*blank     #이 때 이 전까지 그려진 그림은 N=3일 때 0칸, N=6일 때 3칸, N=12일 때 6칸 즉 N/2만큼 밀려서 출력되므로 왼쪽의 식이 성립한다.
        draw(blank*2)                                   #공백은 2배씩 커지므로 다음 공백시 *2를 해준다.
        
draw(3)
