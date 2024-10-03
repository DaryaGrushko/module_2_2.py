#Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
first = int (input ("Введите первое целое число :"))
second = int (input ("Введите второе целое число :"))
third = int (input ("Введите третье целое число :"))
if first == second == third :
    print ('Все три числа равны.')
elif first == second or second == third or first == third:
    print('Два числа равны.')
else :
    print('Нет одинаковых чисел.')