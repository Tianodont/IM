import hashlib


def has_almost_mine(a):
    return int(hashlib.sha256(a.encode("UTF-8")).hexdigest(), 16)


class Rocket:
    """Описание класса Rocket.

            Описание методов:
            update - обновление информации о ракете

    """
    def __init__(self, code, date, name):
        """Описание функции __init__.

                Описание аргументов:
                self.code - код детали
                self.date - дата получения сигнала в формате ГГГГ.ММ.ДД
                self.name - название детали

        """
        self.code = code
        self.date = date
        self.name = name

    def update(self, ch_date=None, ch_name=None):
        if ch_date:
            self.date = ch_date
        if ch_name:
            self.name = ch_name

def main():
    """Описание функции main.

            Описание аргументов:
            f – строки исходной таблицы

    """
    global storage
    with open('rocket.csv', encoding="utf-8") as file:
        f = file.readlines()
        f.pop(0)

        for j in f:
            date = j.split(",")
            storage[has_almost_mine(date[1]) % 100000] = Rocket(date[1], date[0], date[2][:-1])

        return 0


def add_in_storage(code, date, name):
    """Описание функции main.

            Добавление в таблицу

    """
    global storage
    storage[has_almost_mine(code) % 100000] = Rocket(code, date, name)
    return 0


def ex_update(code, date=None, name=None):
    """Описание функции main.

            Обновление в таблице

    """
    global storage
    storage[has_almost_mine(code) % 100000].update(date if date else None, name if name else None)
    return 0

if __name__ == "__main__":
    storage = [None for _ in range(100000)]
    main()





