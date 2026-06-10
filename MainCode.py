while True:
    print("          Вас приветствует калькулятор          ")
    print("          1. Сложение          ")
    print("          2. Вычитание          ")
    print("          3. Умножение          ")
    print("          4. Деление          ")
    print("          5. Возведение в квадрат    ")
    print("          6. Остаток при делении")
    user_comming = int(input("           Введите действие в соответствии с порядковым номером: "))



    num1 = int(input("          Введите первое число: "))
    num2 = int(input("          Введите второе число: "))



    if user_comming == 1:
        print(num1+num2)
    if user_comming == 2:
        print(num1-num2)
    if user_comming == 3:
        print(num1*num2)
    if user_comming == 4:
        print(num1/num2)
    if user_comming == 5:
        print(num1**num2)
    if user_comming == 6:
        print(num1%num2)
