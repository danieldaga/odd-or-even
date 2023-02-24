def oddOrEven(number):
    if number % 2 == 0:
        return print('This number is odd')
    else:
        return print('this number is even')

num=int(input('Enter a number'))

print(oddOrEven(num))