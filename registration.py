import messeges
name = input(messeges.MSG_INPUT_NAME).strip()
print(name)
is_correct_name = name.isalpha()
if is_correct_name:
    print(messeges.MSG_NAME_OK.format(name = name))
else:
    print(messeges.MSG_NAME_ERROR)
# Ось це вік
age = input(messeges.MSG_INPUT_AGE).strip("0").strip()
cor_age = age.isdigit()
if cor_age:
    print(messeges.MSG_AGE_OK.format(age = age))
else:
    print(messeges.MSG_AGE_ERROR)
#Це номер тел
phone = input(messeges.MSG_INPUT_PHONE).strip( )
if phone.isdigit():
    print(messeges.MSG_PHONE_OK.format(phone = phone))
else:
    print(messeges.MSG_PHONE_ERROR)
print(messeges.MSG_FINISH)