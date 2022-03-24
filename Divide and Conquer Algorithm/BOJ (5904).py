from sys import stdin

#S[N]= S[N-1] + ( 'm'+ 'o' * (N+2) ) + S[N-1] 이므로 moo 배열은 크게 3가지 영역으로 나뉜다고 할 수 있다.
# 1. N이 앞의 S[N-1]의 영역에 있는 경우는 다시 S[N-1]영역을 탐색해서 구해내면 된다.
# 2. N이 오른쪽 S[N-1]의 영역에 있는 경우는 N-len(S[N-1])-len('m'+'o'*(N+2))로 S[N-1]의 몇번째인지로 대체하여 탐색해서 구해내면 된다.
# 3. N이 가운데 ('m'+'o'*(N+2))의 영역에 있는 경우는 N이 len(S[N-1])+1인지 아닌지만 구분 한 후, len(S[N-1])+1이면 m을, 그렇지 않으면 'o'를 출력해주면 된다.
def find_moo(moo_len,moo_center_len,N):
    prev_moo=(moo_len-moo_center_len)//2  #이 전 moo배열의 길이를 구한다.
    if N <= prev_moo: return find_moo(prev_moo,moo_center_len-1,N)  #N이 S[N-1]의 영역에 있으므로 S[N-1]영역을 탐색한다.
    elif N > prev_moo + moo_center_len: return find_moo(prev_moo,moo_center_len-1,N-prev_moo-moo_center_len)  #N이 오른쪽 S[N-1]의 영역에 있으므로 N-len(S[N-1])-len('m'+'o'*(N+2))를 S[N-1]로 대체하여 탐색한다.
    else: return "o" if N-prev_moo-1 else "m" #N이 ('m'+'o'*(N+2))의 영역이므로 len(S[N-1])+1인지 아닌지만 탐색한다.

N=int(stdin.readline())
moo_length,n=3,0

while N > moo_length: #길이를 받아서, 해당 길이가 속하는 moo 배열의 길이 및 index를 찾는다.
    n+=1
    moo_length=moo_length*2+n+3

print(find_moo(moo_length,n+3,N)) #길이를 통해 영역을 찾을 때 까지 분할하여, 영역을 찾으면 해당 영역에서 몇번째에 있는지 탐색하여 결과를 찾아낸다.
