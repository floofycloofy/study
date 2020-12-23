def double_char(string: str) -> str:
    if len(string) == 1:
        return string * 2
    return double_char(string[0]) + double_char(string[1:])

while True:
	a = input('Введите строку: ')
	a = double_char(a)
	print(a)