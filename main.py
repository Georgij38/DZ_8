from datetime import date, datetime,timedelta


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    if len(users) == 0:
        return {}

    today = date.today()
    dict_date = {today.strftime('%A'): today}
    for el in range(1, 7):
        today += timedelta(days=1)
        dict_date[today.strftime('%A')] = today

    result = {}
    for el in dict_date:
        result[el] = []

    for el_users in users:
        dt_users = el_users["birthday"]

        for el in dict_date:
            x = dict_date[el]

            if x.month == dt_users.month and x.day == dt_users.day:
                if 'Sunday' == el or 'Saturday' == el:
                    result['Monday'].append(el_users["name"])
                else:
                    result[el].append(el_users["name"])
    itr = 1
    while itr <= 7:
        for el in result:
            if len(result[el]) == 0:
                del result[el]
                break
            else:
                itr += 1

    return result


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 11, 22).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
