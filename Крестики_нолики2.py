
def draw_area():
    for i in area:
        print(*i)
def row():
    row = int(input('Выберете строку: 1, 2 или 3: ', )) - 1
    return row
def column():
    column = int(input('Выберете столбец: 1, 2 или 3: ', )) - 1
    return column
def check_winner():
    for cross_zero in range(1, 3):
        if cross_zero == 1:
            cell = 'X'
            text_ = 'Победили крестики'
        if cross_zero == 2:
            text_ = 'Победили нолики'
            cell = '0'
        for i in range(0, 3):
            # строки
            if area[i][0] == cell and area[i][1] == cell and area[i][2] == cell:
                winner = text_
                return winner
            # столбцы
            elif area[0][i] == cell and area[1][i] == cell and area[2][i] == cell:
                winner = text_
                return winner
        # Диагональ
        if area[0][0] == cell and area[1][1] == cell and area[2][2] == cell:
            winner = text_
            return winner
        elif area[2][0] == cell and area[1][1] == cell and area[0][2] == cell:
             winner = text_
             return winner
    if (area[0][0] != '*' and area[0][1] != '*' and area[0][2] != '*'
            and area[1][0] != '*' and area[1][1] != '*' and area[1][2] != '*'
            and area[2][2] != '*' and area[2][1] != '*' and area[2][2] != '*'):
        winner = 'Ничья'
        return winner
    else:
        winner = 0
        return winner

area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print('Это игра крестики-нолики')
print('------------------------')
draw_area()
print()

for step_count in range(1, 21):
    if step_count % 2 != 0:
        print(f'Шаг {step_count}. Ход крестиков ')
        cell = 'X'
    else:
        print(f'Шаг {step_count}. Ход ноликов ')
        cell = '0'
    row_ = row()
    column_ = column()
    if area[row_][column_] == '*':
        area[row_][column_] = cell
    else:
        print('Эта клетка уже занята, поэтому вы пропускаете ход')
        continue
    draw_area()
    if step_count >= 3:
        winner = check_winner()
        if winner != 0:
            print(winner)
            break