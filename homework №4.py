# Задание №1

a = float(input())
b = float(input())

square = a * b
perimeter = (a + b) * 2
print(square)
print(perimeter)


# Задание №2

number = int(input())

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
tens_of_thousands = number // 10000
result = (tens ** ones) * hundreds / (tens_of_thousands - thousands)
print(result)