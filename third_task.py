
import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 501 234 567",
    "    +38(050)123-32-34",
    "      0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11"
]

def normalize_phone(phone_number):
    """
    функція нормалізує телефоні номери до стандартного
    формату, залишаючи тільки цифри та символ '+' на 
    початку
    """

    p = r"[\d\+]+"
    phone_number = "".join(re.findall(p, phone_number))
    if len(phone_number) == 10:
        phone_number = "+38" + phone_number
    elif len(phone_number) == 12:
        phone_number = "+" + phone_number
    return phone_number

for num in raw_numbers:
    normalize_phone(num)

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:\n", sanitized_numbers)

