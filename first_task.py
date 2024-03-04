
import datetime as dt
import math


def get_days_from_today(date):
    """
    функція розраховує кількість днів між заданою
    датою та поточною датою
    """
    
    try:
        date = dt.datetime.strptime(date, "%Y-%m-%d")
    except Exception as e:
        print(f"Error {e}")
        print("\nЗапустіть програму заново та введіть дату в форматі 'РРРР-ММ-ДД'\n")
        exit()

    today = dt.datetime.today()
    delta_days = (date - today).days
    target_days = dt.datetime.strftime(date, "%Y-%m-%d")
    if delta_days > 0:
        delta_days = int(math.copysign(delta_days, -0.0))
        print(f"{delta_days} днів/день/дня залишилося до {target_days}")
    else:
        delta_days = abs(delta_days)
        print(f"{delta_days} днів/дня/день минуло після {target_days}")

get_days_from_today(input("Введіть дату в форматі 'РРРР-ММ-ДД': "))














