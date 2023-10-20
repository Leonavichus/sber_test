## Python

#### Задание №1

Особенный номер – строка формата [2-4 цифры]\[2-5 цифр]. Хороший номер - строка формата [4 цифры]\[5 цифр]. Хороший номер можно получить из особенного дополнением нулей слева к обоим числам.

Пример:
17\234 => 0017\00234

Напишите функцию, которая принимает на вход строку и для каждого особенного номера, встречающегося в строке, выводит соответствующий хороший номер.

| Ввод                          |         Вывод         |
| ----------------------------- | :-------------------: |
| Адрес 5467\456. Номер 405\549 | 5467\00456 0405\00549 |

Реализация:

```
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
```

<img src='/img/python1.png'/>

#### Задание №2

На прямой дороге расположено n банкоматов. Было решено построить ещё k банкоматов для того, чтобы уменьшить расстояние между соседними банкоматами.
На вход подаются натуральные числа n и k, а также n-1 расстояний L, где – расстояние между банкоматами i и i+1. Напишите функцию, которая добавляет k банкоматов таким образом, чтобы максимальное расстояние между соседними банкоматами являлось минимально возможным, и возвращает список новых расстояний между банкоматами.

Пример:

| Ввод             |           Вывод            |
| ---------------- | :------------------------: |
| 5 3 100 30 20 80 | 33.3 33.3 33.3 30 20 40 40 |

Реализация:

```
def add_atms(n, k, distances):
    distances_dict = {key: [value] for key, value in enumerate(distances)}

    for _ in range(k):
        max_distance = max(distances)
        max_distance_index = distances.index(max_distance)

        for key, value in distances_dict.items():
            if max(value) == max_distance:
                divider = len(value) + 1
                avg = sum(value) / divider
                distances_dict[key] = [avg] * divider
                distances[max_distance_index] = avg

    result = [item for i in distances_dict.values() for item in i]
    return result


n = int(input('Введите кол. банкоматов: '))
k = int(input('Введите кол. банкоматов, которые будут добавлять: '))

distances = [
    int(input(f'Расстояние между банкоматами {i}-{i+1}: ')) for i in range(1, n)]

result = add_atms(n, k, distances)
print(*result, sep=', ')
```

<img src='/img/python2.png'/>

## SQL

#### Задание №1

Требуется составить расписание случайных проверок. Создайте оператор выбора, который выдаст 100 дат, начиная с текущей, при этом каждая дата отличается от предыдущей на 2-7 дней.

Пример:

| Даты       |
| ---------- |
| 25.02.2023 |
| 28.02.2023 |
| 04.03.2023 |
| 06.03.2023 |
| 13.03.2023 |
| 16.03.2023 |
| ....       |

Реализация:

```
-- MySql
WITH RECURSIVE date_generator AS (
    SELECT 1 AS row_num,
        CURDATE() AS random_date
    UNION ALL
    SELECT row_num + 1,
        DATE_ADD(random_date, INTERVAL (ABS(RAND()) % 6 + 2) DAY)
    FROM date_generator
    WHERE row_num < 100
)
SELECT random_date
FROM date_generator;
-- SQL
WITH date_generator AS (
    SELECT 1 AS row_num,
        CAST(GETDATE() AS DATE) AS random_date
    UNION ALL
    SELECT row_num + 1,
        DATEADD(DAY, RAND() * 6 + 2, random_date)
    FROM date_generator
    WHERE row_num < 100
)
SELECT random_date
FROM date_generator;
```

<img src='/img/sql1.png'/>

#### Задание №2

Требуется оценить эффективность продавцов. Создайте запрос, который вернёт количество и сумму продаж для каждого продавца, а также ранжирует продавцов по количеству продаж и по сумме продаж.

Результат запроса должен содержать столбцы id, name из таблицы employee, а также столбцы:\
sales_c - количество продаж, \
sales_rank_c - ранг по количеству продаж, \
sales_s - сумма продаж, \
sales_rank_s - ранг по сумме продаж.

Реализация:

```
WITH sales_summary AS (
    SELECT e.id AS e_id,
        e.name AS e_name,
        COUNT(s.id) AS sales_c,
        RANK() OVER (
            ORDER BY COUNT(s.id) DESC
        ) AS sales_rank_c,
        SUM(s.price) AS sales_s,
        RANK() OVER (
            ORDER BY SUM(s.price) DESC
        ) AS sales_rank_s
    FROM employee e
        LEFT JOIN sales s ON e.id = s.employee_id
    GROUP BY e.id,
        e.name
)
SELECT e_id,
    e_name,
    sales_c,
    sales_rank_c,
    sales_s,
    sales_rank_s
FROM sales_summary;
```

<img src='/img/sql2.png'/>
