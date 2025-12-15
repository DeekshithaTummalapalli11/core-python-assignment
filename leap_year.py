y=list(map(int,input().split()))
for i in range(len(y)):
  if (y[i]%4==0 and y[i]%100!=0) or (y[i]%400==0):
    print("Leap year:",y[i])
  else:
    print("Non-Leap year:",y[i])
