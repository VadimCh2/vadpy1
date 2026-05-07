from functions_hw import get_two_num
from functions_hw import get_string
from functions_hw import sum_numbers
# 1.
print(get_two_num(10, 5, "sub"))
print(get_two_num(num1=20, num2=10, operation="sum"))
data = {
    "num1": 30,
    "num2": 15,
    "operation": "sum"
}
print(get_two_num(**data))
 # 2.
print(get_string("Hello","True"))
print(get_string(string1="Hello", upper=False))
data = {
    "string1": "Hello",
    "upper": False,
}
print(get_string(**data))
# 3.
print(sum_numbers("1,2,3"))
print(sum_numbers(text="4,5,6", separator=","))
data = {
    "text": "7,8,9",
    "separator": ","
}

print(sum_numbers(**data))