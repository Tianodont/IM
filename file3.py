def beautifier(a):
    """Описание функции beautifier.

        Описание аргументов:
        a – запись
        code – код
        date_mod – дата
        typ – название детали

    """
    code = a[1]
    date_mod = ".".join(a[0].split("-")[::-1])
    typ = a[2][:-1]
    return f"Шифр: {code} от: {typ} был получен {date_mod}"


def main():
    """Описание функции main.

            Описание аргументов:
            f – строки исходной таблицы
            inp - введенная дата

    """
    inp = input()
    if inp == "sleep":
        return "sleep entered"

    with open('rocket.csv', encoding="utf-8") as file:
        f = file.readlines()
        f.pop(0)

        for j in f:
            date = j.split(",")[0]
            if date == inp:
                return beautifier(j.split(","))
        return "в этот день космос молчал"


if __name__ == "__main__":
    print(main())