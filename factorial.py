inputText = 'Введите число, факториал которого вы хотите найти\n'
n = int(input(inputText))

while (type(n) == int):

    factorial = 1

    for i in range(2, n+1):
        factorial *= i

    print('факториал = ', factorial)

    n = input(inputText)

    if (n.isdigit()):
        n = int(n)
