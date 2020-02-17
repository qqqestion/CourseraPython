def calculate(data, findall):
    matches = findall(r"([abc])([+-]?)=([abc]?)([+-]?\d*)")  # Если придумать хорошую регулярку, будет просто
    for v1, sign, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
        right_value = data.get(v2, 0) + int(n or 0)
        if sign == '+':
            data[v1] += right_value
        elif sign == '-':
            data[v1] -= right_value
        else:
            data[v1] = right_value
    return data
