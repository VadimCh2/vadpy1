# 1.
def get_average(a: float | int, b: float | int, c: float | int) -> float:
    result = (a + b + c) / 3
    rounded_result = round(result, 2)
    return rounded_result

average_result = get_average(a=1,b=2,c=4)
print(average_result)

# 2.

def get_number_that_more_then_10(number: int | float) -> bool:
    if number > 10 and number % 2 == 0:
        return True
    else:
        return False

result_number_that_more_then_10 = get_number_that_more_then_10(number=67)
print(result_number_that_more_then_10)

#3.

def get_vowels(text: str) -> int:
    text = text.lower()
    vowels_letters = "aeiouy"
    vowels_count = 0
    for letter in text:
        if letter in vowels_letters:
            vowels_count += 1

    return vowels_count
count_vowels_number = get_vowels(text='Extraculicular')
print(count_vowels_number)