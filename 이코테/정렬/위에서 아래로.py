N=int(input())
Data=[]

for i in range(N):
    data=int(input())    
    Data.append(data)
    
print(" ".join(map(str,sorted(Data,reverse=True)))) 