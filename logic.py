def simplify_kmap(values):
    simplified_expression = []

    # Проверка на полное покрытие
    if all(v == 1 for v in values):
        return "1"

    # Проверка горизонтальных и вертикальных пар
    if values[0] and values[1]:
        simplified_expression.append("NOT A")
    elif values[2] and values[3]:
        simplified_expression.append("A")

    if values[0] and values[2]:
        simplified_expression.append("NOT B")
    elif values[1] and values[3]:
        simplified_expression.append("B")

    # Проверка одиночных единиц
    if values[0] and not any(values[1:]):
        simplified_expression.append("NOT A AND NOT B")
    if values[1] and not any([values[0], values[2], values[3]]):
        simplified_expression.append("NOT A AND B")
    if values[2] and not any([values[0], values[1], values[3]]):
        simplified_expression.append("A AND NOT B")
    if values[3] and not any(values[:3]):
        simplified_expression.append("A AND B")

    return " OR ".join(simplified_expression) if simplified_expression else "0"