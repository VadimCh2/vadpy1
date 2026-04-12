numbers = [1, 3, 4]
names = ['Anna', "Ivan"]
mixed = [
    1,
    90.901,
    True,
    False,
    "some text",

    ['123', 1232],

]

first_element = mixed[0]
print(first_element)

third_element = mixed[2]
print(third_element)

last_element = mixed[-1]
print(last_element)

last_element_in_last_element = last_element[-1]
print(last_element_in_last_element)

# change lists
string = '123'
print(id(string))
string = string + '1'
print(id(string))

number = 123
print(id(number))
number = number + 1
print(id(number))

# add values
numbers.append(3000)
numbers.append(3000)
print(numbers)
print(id(numbers))
numbers.insert(1, 22)
print(numbers)
print(id(numbers))
# sorting
numbers2 = [1, 7, 2, 3]
print(numbers2)
numbers2.sort(reverse=True)
print(numbers2)
print(numbers2)

numbers3 = sorted(numbers2)
print(numbers3, 'sorted')
print(numbers2)
# slices
#             age, weight, salary,   name, surname,      hobbies
person_data = [22,    85,    56000, "Alex", "Bush", ['soccer', "tennis"]]
hobbies = person_data[-1]
print(hobbies)
name_surname = person_data[3:5]
print(name_surname)
print(id(person_data))
copy_of_person_data = person_data[:]
print(copy_of_person_data)
print(id(copy_of_person_data))
