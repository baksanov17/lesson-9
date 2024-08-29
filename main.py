First =int(input('Введите число: '))
Second =int(input('Введите число: '))
Third = int(input('Введите число: '))
if First == Second == Third:
    print(3)
elif First == Second or Second == Third or First == Third:
    print(2)
else:
    print(0)


