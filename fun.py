a=int(input('Enter value for a:'))
b=int(input('Enter value for b:'))
c=int(input('Enter value for c:'))
d=int(input('Enter value for d:'))
x=int(input('Enter value for x:'))
k=int(input('Enter value for k:'))
if x>k:
    print('f(x) is',a*x**3-b*x**2+c*x-d)
elif x==0:
    print('f(x) is 0')
else:
    print('f(x) is',-a*x**3+b*x**2-c*x+d)