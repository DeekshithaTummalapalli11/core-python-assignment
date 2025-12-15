s=input()
n=int(input())
for i in range(1,n+1):
  print(" "*(n-1),end="")
  k=0
  for j in range(i):
    print(s[k],end="")
    k+=1
    if k==len(s):
      k=0
  print()


'''
s=abc
n=5
     a
    ab
   abc 
  abca
 abcab

'''
 
