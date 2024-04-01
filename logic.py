def simplify_kmap(values):
    simplified_expression = []

    # Проверка на полное покрытие и полное отсутствие
    if all(v == 1 for v in values):
        return "1"
    if all(v == 0 for v in values):
        return "0"

    # Функция для проверки пар и добавления упрощений
    def check_pairs():
        # Проверка горизонтальных и вертикальных пар
        if values[0] == values[1] == 1:
            simplified_expression.append("NOT A")
        if values[2] == values[3] == 1:
            simplified_expression.append("A")
        if values[0] == values[2] == 1:
            simplified_expression.append("NOT B")
        if values[1] == values[3] == 1:
            simplified_expression.append("B")

    # Проверка диагональных пар для дополнительного упрощения
    def check_diagonals():
        if values[0] == values[3] == 1 and not (values[1] or values[2]):
            simplified_expression.append("(A XOR B)")
        if values[1] == values[2] == 1 and not (values[0] or values[3]):
            simplified_expression.append("NOT (A XOR B)")

    # Проверка одиночных единиц
    def check_singles():
        if values.count(1) == 1:
            index = values.index(1)
            # Добавляем условия в зависимости от положения единицы
            if index == 0:
                simplified_expression.append("NOT A AND NOT B")
            elif index == 1:
                simplified_expression.append("NOT A AND B")
            elif index == 2:
                simplified_expression.append("A AND NOT B")
            elif index == 3:
                simplified_expression.append("A AND B")

    check_pairs()
    check_diagonals()
    check_singles()

    return " OR ".join(simplified_expression) if simplified_expression else "0"
