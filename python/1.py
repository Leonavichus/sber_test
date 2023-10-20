import re

input_string = str(input('Введите строку: '))
# input_string = 'Адрес 5467\456. Номер 405\549'

# Без регулярных выражений
parts = input_string.split()


def is_digit_pair(t):
    digits = t.split('\\')
    if len(digits) == 2 and 2 <= len(digits[0]) <= 4 and \
            2 <= len(digits[1]) <= 5 and digits[0].isdigit() and \
            digits[1].isdigit():
        return True
    return False


print('Без регулярных выражений:')
for part in parts:
    cleaned_part = ''.join(c for c in part if c.isdigit() or c == '\\')
    if is_digit_pair(cleaned_part):
        digits = cleaned_part.split('\\')
        formatted_string = '{:04d}\\{:05d}'.format(
            int(digits[0]), int(digits[1]))
        print(formatted_string)


# С регулярными выражениями
pattern = r'\d{2,4}\\\d{2,5}'

matchs = re.findall(pattern, input_string)

print('С регулярными выражениями:')
for match in matchs:
    digits = match.split('\\')
    formatted_string = '{:04d}\\{:05d}'.format(
        int(digits[0]), int(digits[1]))
    print(formatted_string)
