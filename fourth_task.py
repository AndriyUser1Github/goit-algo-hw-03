
from datetime import datetime as dt
from datetime import timedelta 

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Joana Smith", "birthday": "2000.02.02"},
    {"name": "Jack Custo", "birthday": "2015.05.24"},
    {"name": "Alex Reno", "birthday": "2016.01.31"}
]

def get_upcoming_birthdays(users=None):
    """
    функція визначає кого з колег потрібно привітати
    з днем народження, якщо день народження випадає на 
    вихідний день, то дата привітання переноситься 
    на наступний робочий день 
    """
    
    today = dt.today().date()
    congratulation_list = []
    for user in users:
        congratulation_dict = {}
        user_birthday = dt.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = dt(year = today.year,
                                      month = user_birthday.month,
                                      day = user_birthday.day).date()
        
        if birthday_this_year < today:
            continue
        elif birthday_this_year.toordinal() - today.toordinal() > 7:
            continue
        else:
            congratulation_date = dt(year = today.year,
                                           month = birthday_this_year.month,
                                           day = birthday_this_year.day).date()
            if congratulation_date.weekday() == 6:
                congratulation_date += timedelta(1)
            elif congratulation_date.weekday() == 5:
                congratulation_date += timedelta(2)

            congratulation_date = congratulation_date.strftime("%Y.%m.%d")
            congratulation_dict.update({"name": user["name"],
                                        "congratulation_date": congratulation_date})
            congratulation_list.append(congratulation_dict)
    return congratulation_list

upcoming_birthdays = get_upcoming_birthdays(users)
print(f"Список привітань на цьому тижні:\n{upcoming_birthdays}")




     
