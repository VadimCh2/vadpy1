# number_1 = 1
# number_2 = 2
# pass
#
# def print_msg():
#     print('Welcome')
#     print('message')
#
# def get_number_5():
#     print('function get_number_5 was called')
#     number_5_to_give = 5
#     return number_5_to_give
#
# number_5 = get_number_5()
# number_5 = get_number_5()
# number_5 = get_number_5()
# number_5 = get_number_5()
#
# number_5 = get_number_5()
#
# print(f"{number_5=}")
#
# def calculate_summa():
#     pass
#
# print_msg()
# calculate_summa()
# calculate_summa()
# calculate_summa()
# calculate_summa()
# calculate_summa()





def get_travel_info(driver: str, passenger_1: str = "", passenger_2: str = "", passenger_3: str = 'sister') -> str:
    people_in_car = f"DRIVER: {driver.title()}; passengers: {passenger_1}, {passenger_2}, {passenger_3}."
    return people_in_car
