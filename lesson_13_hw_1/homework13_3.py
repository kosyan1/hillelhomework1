from datetime import datetime, timedelta

def get_date_list(from_date: str, to_date: str) -> list[str]:
    date_list = []
    current_date = datetime.strptime(from_date, "%Y-%m-%d")
    end_date = datetime.strptime(to_date, "%Y-%m-%d")

    if current_date <= end_date:
        while current_date <= end_date:
            date_list.append(current_date.strftime("%Y-%m-%d"))
            current_date += timedelta(days=1)
    else:
        while current_date >= end_date:
            date_list.append(current_date.strftime("%Y-%m-%d"))
            current_date -= timedelta(days=1)

    return date_list

while True:
    from_date = input("Введіть дату початку (в форматі YYYY-MM-DD): ")
    to_date = input("Введіть дату кінця (в форматі YYYY-MM-DD): ")

    dates = get_date_list(from_date, to_date)

    print(dates)
