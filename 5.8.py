#Входные данные
#С клавиатуры вводится натуральное трехзначное число.
#
#Выходные данные
#Выведите через пробел в одну строку сумму цифр числа и новое число, образованное перестановкой единиц и десятков.
# 
#
#Примеры
#№	Входные данные	Выходные данные
#1	123	            6 132

n = int(input())
ed = n % 10
des = int( (n % 100 - ed) / 10 )
sot = int( (n % 1000 - des * 10 - ed) / 100 )

print(ed + des + sot, ' ', sot, ed, des, sep='')