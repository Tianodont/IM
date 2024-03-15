def beautifier(a):
    """Описание функции beautifier.

        Описание аргументов:
        a – запись
        code – код
        date_year – разница годов
        typ – первые буквы названия детали
        mut_code - измененный код

    """
    code = a[1].upper()
    date_year = str(abs(int(a[0].split("-")[0])-CURRENT_YEAR))
    typ = "".join([x[0] for x in a[2][:-1].split()]).upper()
    mut_code = ""
    for t in code:
        if t in "0123456789":
            mut_code += t
    for t in code:
        if t in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            mut_code += t
    for t in code:
        if t in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
            mut_code += t

    return f"{a[0]},{a[1]},{a[2][:-1]},{typ+mut_code+date_year}\n"


def main():
    """Описание функции main.

            Описание аргументов:
            f – строки исходной таблицы
            newfile - новая таблица

    """

    with open('rocket.csv', encoding="utf-8") as file:
        with open('rocket_commands.csv', "w+", encoding="utf-8") as newfile:
            f = file.readlines()
            newfile.write("date,code,rocketparts,startcode\n")
            f.pop(0)

            for j in f:
                print(beautifier(j.split(",")))
                newfile.write(beautifier(j.split(",")))

            return 0


if __name__ == "__main__":
    CURRENT_YEAR = 2024
    main()