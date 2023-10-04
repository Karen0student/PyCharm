#print("Hello, World!")

#if 5 > 2:
#	print("Five is greater than two!")

#x = str(5)
#y = " Hello World!"
#print(x + y)
"""
x, y = z = "Orange", "Banana"
print(x)
print(y)
print(z)

"""

"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
"""

"""
def myfunc(x):
	print("IN FUNCTION: " + x)

x = "Hello function"
myfunc(x)
"""

"""
x = 5
print(str(x) + " DONE")
"""

"""
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
"""

"""
import random

x = random.randrange(1, 10)
if(x == 9):
	print("You win!")
else:
	print("Bad luck!")
"""

"""
x = input("Enter something: ")
print(x)
"""

"""
#RUN BY python3
print(f"{1234:0>9}")
print(f"{1234:0<9}")
print(f"{1234:0^9}")
"""

"""
# ord() -> can be used to convert a character to its corresponding ASCII integer value.
# chr() -> converts an integer to its unicode character and returns it.
x = 't'
print(ord(x))
"""


"""
# Working in python 3.10 version
variable = input()
match variable:
	case 'red' | 'yellow':
		print('Стоп.')
	case 'green':
        	print('Можно ехать.')
	case _:
        	print('Некорректное значение.')
"""

"""
saved_pwd = "right_password"
pwd = input("Введите пароль для входа: ")
while pwd != saved_pwd:
    pwd = input("False, Введите пароль для входа: ")
print("Пароль верный. Вход разрешён.")
"""

"""
check_pass_quantity = 3
saved_pwd = "right"
while input("Enter password: ") != saved_pwd:
    check_pass_quantity -= 1
    if check_pass_quantity == 0:
    	print("*EXITING*")
    	break
    print("***WRONG PASSWORD, TRIES LEFT: " , check_pass_quantity, " ***", sep="")

if check_pass_quantity > 0:
	print("SUCCESS")
"""

"""
while (name := input("Enter name: ")) != "STOP":
    print(f"Hello {name}!")

print("SSUCCESS")
"""

"""
name = input("Enter name: ")
while name != "STOP":
    print(f"Hello {name}!")
    name = input("Enter name: ")

print("SUCCESS")
"""

"""
# end="" -> make print without newline
for i in range(26):
    print("\n")
    for j in range(26):
        print(f"{chr(ord('a') + i)}{chr(ord('a') + j)} ", end="")
"""

"""
check_pass_quantity = 3
password = "right"
while True:
    if input("Введите пароль: ") == password:
        print("Пароль принимается")
        break
    check_pass_quantity -= 1
    if check_pass_quantity == 0:
        print("*EXITING*")
        break
    print("***WRONG PASSWORD, TRIES LEFT: " , check_pass_quantity, " ***", sep="")
if check_pass_quantity > 0:
  print("SUCCESS")
else:
  print("FAILURE")
"""

"""
text = "Привет, мир!"
print(text[8:11]) # from 8-th char to 11-th
print(text[:6])   # first 6 chars
print(text[8:])   # after 8 chars
print(text[:])    # everything
print(text[::2])  # each 2-nd char starting from 0
"""

"""
# NO INDEXES, Key --> Value
list = {"France" : "Paris",
        "Russia" : "Moscow"}
print(list["France"])
"""

# создаём пустой словарь
countries = dict()
# вводим первую строку до цикла (можно заменить, использовав оператор-морж)
country = input()
# создаём счётчик номеров строк
str_number = 0
# продолжаем цикл, пока не введена строка «СТОП»
while country != "STOP":
    # если введённой страны нет в словаре, создаём ключ и записываем по ключу список из одного номера строки
    if country in countries:
        countries[country].append(str_number)
    # иначе добавляем в список по ключу новое значение номера строки
    else:
        countries[country] = [str_number]
    # увеличиваем счётчик
    str_number += 1
    # вводим следующую строку
    country = input()
# выводим название страны и полученные списки с новой строки
for country in countries:
    print(f"{country}: {countries[country]}")