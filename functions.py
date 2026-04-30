number_1 = 1
number_2 = 2
pass

def print_msg():
    print('Welcome')
    print('message')

def get_number_5():
    print('function get_number_5 was called')
    number_5_to_give = 5
    return number_5_to_give

number_5 = get_number_5()
number_5 = get_number_5()
number_5 = get_number_5()
number_5 = get_number_5()

number_5 = get_number_5()

print(f"{number_5=}")

def calculate_summa():
    print(2222)
    pass

print_msg()
calculate_summa()
calculate_summa()
calculate_summa()
calculate_summa()
calculate_summa()

def calculate_summa(number_1: int | float, number_2: int | float) -> float:
    result = number_1 + number_2
    return result * 1.0

result_calculate_summa = calculate_summa(number_1=1, number_2=9.6)
print(result_calculate_summa)
mult = result_calculate_summa * 20
print(mult)