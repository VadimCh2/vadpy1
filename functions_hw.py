# 1.
def get_two_num(num1: int | float, num2: int | float, operation: str = "sum") -> int | float:
    if operation == "sum":
        sum_result = num1 + num2
        return sum_result
    else:
        difference = num1 - num2
        return difference
# 2.
def get_string(string1: str, upper: bool = True) -> str:
    if upper:
        return string1.upper()
    else:
        return string1.lower()
# 3.
def sum_numbers(text: str, separator: str = ",") -> int:
    parts = text.split(separator)

    total = 0
    for i in parts:
        total += int(i)

    return total