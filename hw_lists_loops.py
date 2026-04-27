# ex 1
numbers = [5, 2, 9, 1, 7]
biggest = 0
smallest = 0
for number in numbers:
    if number > biggest:
        biggest = number

    if smallest == 0:
        smallest = number

    if number < smallest:
        smallest = number

print("Найбільше число:", biggest)
print("Найменше число:", smallest)

# ex 2
grades = [10, 8, 12, 7, 9]
total = 0
for grade in grades:
    total += grade
average = total / len(grades)
print("Середній бал:", average)
print("Оцінки вище середнього:")
for grade in grades:
    if grade > average:
        print(grade)