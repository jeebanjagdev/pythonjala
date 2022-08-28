num=int(input('enter a number:'))
i=2
while i<num:
    if num%i==0:
        break
    i=i+1
if i==num:
    print('prime number')
else:
    print('not prime number')
