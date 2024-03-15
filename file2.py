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
    return f"Сигнал с шифром {code} был получен {date_mod} и предназначается для {typ}"


def insertion_sort(lis):
    """Описание функции insertion_sort.

            Описание аргументов:
            lis – список для сортировки


    """
    for i in range(1, len(lis)):
        temp = lis[i]
        j = i - 1
        while j >= 0 and temp < lis[j]:
            lis[j + 1] = lis[j]
            j = j - 1
        lis[j + 1] = temp
    return lis


def main():
    """Описание функции main.

            Описание аргументов:
            f – строки исходной таблицы
            date_dict - словарь дата - запись
            res - список длля ответа
            sortd - отсортированные даты

    """
    with open('rocket.csv', encoding="utf-8") as file:
        f = file.readlines()
        date_dict = dict()
        res = []

        f.pop(0)

        for j in f:
            date = j.split(",")[0]
            if date not in date_dict:
                date_dict[date] = []
            date_dict[date] += [j.split(",")]

        sortd = insertion_sort(list(date_dict.keys()))[:3]

        for k in sortd:
            res += [beautifier(date_dict[k][0])]

        return res


if __name__ == "__main__":
    answer = main()

    for item in answer:
        print(item)

