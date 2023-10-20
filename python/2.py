def add_atms(n, k, distances):
    distances_dict = {key: [value] for key, value in enumerate(distances)}
    sorted_dict = dict(
        sorted(distances_dict.items(), key=lambda item: item[1], reverse=True))

    for _ in range(k):
        max_distance = max(distances)
        max_distance_index = distances.index(max_distance)

        for key, value in sorted_dict.items():
            if max(value) == max_distance:
                divider = len(value) + 1
                avg = sum(value) / divider
                sorted_dict[key] = [avg] * divider
                distances[max_distance_index] = avg

    new_dict = {key: sorted_dict[key] for key in sorted(sorted_dict.keys())}
    result = [item for i in new_dict.values() for item in i]
    return result


n = int(input('Введите кол. банкоматов: '))
k = int(input('Введите кол. банкоматов, которые будут добавлять: '))

distances = [
    int(input(f'Расстояние между банкоматами {i}-{i+1}: ')) for i in range(1, n)]

result = add_atms(n, k, distances)
print(result)
