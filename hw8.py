# numbers = [3, 7, 2, 9, 4, 6, 1, 8]
# even_numbers = []
# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
# print(even_numbers)
# doubled_even =[]
# for doubl_num in even_numbers:
#     doubled_even.append(doubl_num * 2)
# print(doubled_even)
# if 8 in doubled_even:
#     doubled_even.remove(8)
#     print(doubled_even)

# ex2
words = ["apple", "banana", "kiwi", "pear", "banana", "plum"]
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)
long_words = []
for word_2 in unique_words:
    if len(word_2) > 4:
        long_words.append(word_2)
upper_words = []
for word_3 in long_words:
    upper_words.append(word_3.upper())
if "BANANA" in upper_words:
        print("BANANA в списку")
else:
    print("немає там")
print(upper_words)