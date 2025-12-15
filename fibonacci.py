n=int(input())
a=0
b=1
for i in range(n): 
  print(a,end="")
  a,b=b,a+b

#recurssion
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

n = int(input("Enter n: "))
print(fib(n))
