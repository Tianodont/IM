def beautifier(month, code):
	"""Описание функции beautifier.

		Описание аргументов:
		month – номер месяца
		code – кол-во шифров

	"""
	return f"В {month} было получено - {code} шифров"


def main():
	"""Описание функции main.

			Описание аргументов:
			inp – введенный номер месяца
			f – строки исходной таблицы
			ans - кол-во шифров для месяца


	"""
	inp = input()
	with open('rocket.csv', encoding="utf-8") as file:
		f = file.readlines()
		f.pop(0)
		ans = 0
		for i in f:
			if i.split(",")[0].split("-")[1] == inp:
				ans += 1

		return beautifier(inp, ans)


if __name__ == "__main__":
	print(main())
