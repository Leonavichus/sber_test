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
