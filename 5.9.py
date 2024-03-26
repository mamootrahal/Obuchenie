# Напишите программу, которая по исходному пятизначному числу находит сумму квадратов цифр данного числа.

# Входные данные
# На вход программы подается натуральное пятизначное число.

# Выходные данные
# Выведите ответ на задачу.

# Примеры
# №	Входные данные	Выходные данные
# 1	    12345	    55

n = int(input())

ed = n % 10
des = int( (n % 100 - ed) / 10 )
sot = int( (n % 1000 - des * 10 - ed) / 100 )
t = int ( (n % 10000 - sot * 100 - des * 10 - ed) / 1000 )
dt = int ( (n % 100000 - t * 1000 -sot * 100 - des * 10 - ed) / 10000 )

print(ed ** 2 + des ** 2 + sot ** 2 + t ** 2 + dt ** 2)