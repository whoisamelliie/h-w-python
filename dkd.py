
# print("hello ")
# print("это моя первая программа.")

# name = input("как тебя зовут ")
# print("приятно познакомиться,", name)

#3 task
number1= int(input("Введите число: ")) 
if number1 % 2 == 0:
    print("Число четное.")
else:
    print("Число нечетное.")

#1 task
number = int(input("Введите число: "))
if number > 0:
    print("Число положительное.")
elif number < 0:
    print("Число отрицательное.")
else:
    print("Число равно нулю.")

#2 task
age= int(input("Скажите ваш возраст: "))
if age < 18:
    print ("Доступ закрыт.")
else:
    print ("Добро пожаловать")



#4 task
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
    print("Первое число больше второго.")
elif a < b:
    print("Второе число больше первого.")
else:
    print("Числа равны.")   

#5 task
month = int(input("Введите номер месяца (1-12): "))
if month == 12 or month == 1 or month == 2:
    print("Зима")
elif month == 3 or month == 4 or month == 5:
    print("Весна")
elif month == 6 or month == 7 or month == 8:
    print("Лето")
elif month == 9 or month == 10 or month == 11:
    print("Осень")
else:
    print("Некорректный номер месяца.")

#6 task
score = int(input("Введите количество баллов (0-100): "))
if score >= 90:
    print("Оценка: 5")
elif score >= 75:
    print("Оценка: 4")
elif score >= 60:
    print("Оценка: 3")
else:
    print("Оценка: 2")

#7 task
year = int(input("Введите год: "))  
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Год високосный.")
else:
    print("Год не високосный.")

#8 task
a = int(input("Введите первую сторону: "))
b = int(input("Введите вторую сторону: "))
c = int(input("Введите третью сторону: "))  
if a == b == c:
    print("Это равносторонний треугольник.")
elif a == b or b == c or a == c:
    print("Это равнобедренный треугольник.")
else:
    print("Это разносторонний треугольник.")     


#9 task
password = input("Введите пароль: ")
if len(password) < 8:
    print("Пароль слишком короткий. Он должен содержать не менее 8 символов.")
elif password == "password":
    print("Пароль не должен совпадать со словом 'password'.")
else:
    print("Пароль принят.")

    #10.1 task
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")    
if operation == "+":
    result = a + b
    print("Результат:", result)
elif operation == "-":
    result = a - b
    print("Результат:", result)
elif operation == "*":
    result = a * b
    print("Результат:", result)
elif operation == "/":
    if b != 0:
        result = a / b
        print("Результат:", result)
    else:
        print("Ошибка: деление на ноль.")
else:
    print("Ошибка: неизвестная операция.")  

    #10.2 task
c = float(input("Введите первое число: "))
d = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")

match operation:
    case "+":
        result = c + d
        print("Результат:", result)
    case "-":
        result = c - d
        print("Результат:", result)
    case "*":
        result = c * d
        print("Результат:", result)
    case "/":
        if d != 0:
            result = c / d
            print("Результат:", result)
        else:
            print("Ошибка: деление на ноль.")
    case _:
        print("Ошибка: неизвестная операция.")  
