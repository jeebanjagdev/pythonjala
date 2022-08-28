num=int(input('enter a number:'))
sum=0
count=0
n=num
while num!=0:
    count=count+1
    num=num//10
num=n
while num!=0:
    d=num%10
    sum=sum+d**count
    num=num//10
if n==sum:
    print('armstrong number')
else:
    print('not armstrong number')
