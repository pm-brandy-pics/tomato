#Check whether it's a palindrome or not
a=input('Enter a string:')
if a==a[::-1]:
    print('Palindrome')
else:
    print('Not palindrome')