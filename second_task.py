
import random

def get_numbers_ticket(min, max, quantity):
    """
    функція генерує список з унікальних чисел для 
    лотереї, в заданому діапазоні чисел та кількості 
    чисел, з яких буде складатися список
    """
    
    numbers_list = []
    if min >= 1 and max <= 1000:
        while len(numbers_list) < quantity:
            numb = random.randrange(min, max)
            if numb not in numbers_list:
                numbers_list.append(numb)
                numbers_list.sort()
        return numbers_list
    else:
        print("Не коректні дані", [])        

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа", lottery_numbers)
