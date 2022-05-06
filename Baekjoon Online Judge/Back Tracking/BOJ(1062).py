from sys import stdin

N,K=map(int,stdin.readline().split())
word_list=[stdin.readline().strip() for _ in range(N)]
learn_alpha=[False]*26
answer=0
   
for i in ('a','n','t','i','c'): #5개의 a,n,t,i,c는 읽을 수 있다.
    learn_alpha[ord(i)-ord('a')]=True

def dfs(idx,cnt):
    global answer
    if cnt==K-5:
        temp_answer=0
        for word in word_list:
            state=True
            for w in range(4,len(word)-4):  #앞과 뒤의 글자는 읽을 수 있으므로 생략 가능
                if not learn_alpha[ord(word[w])-ord('a')]:
                    state=False
                    break
            if state:
                temp_answer+=1
        answer=max(temp_answer,answer)
        return
    else:
        for i in range(idx,26): #가능한 모든 조합을 돌려가며 배울 수 있는 글자들을 탐색한다.
            if not learn_alpha[i]:
                learn_alpha[i]=True
                dfs(i+1,cnt+1)  #글자를 배우지 않았다면 하나 배운 후 깊이 탐색
                learn_alpha[i]=False    #돌아와서 다시 배우지 않았다고 가정하고 다음 반복문을 실행한다.
                
if K < 5:   #5개의 a,n,t,i,c는 반드시 읽을 수 있어야 한다.
    print(0)
elif K == 26:   #모든 글자를 배웠다면 전부 읽을 수 있다.
    print(N)
else:
    dfs(0,0)
    print(answer)
            
        


