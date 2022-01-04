from sys import stdin

A,B=stdin.readline().split()

max_num=int(A.replace('5','6'))+int(B.replace('5','6'))
min_num=int(A.replace('6','5'))+int(B.replace('6','5'))

print(min_num,max_num)
