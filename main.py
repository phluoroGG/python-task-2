def create_array_without_repeating_rows_in_row(matrix):
    new_matrix = [matrix[0]]
    for row_ in range(1, len(matrix)):
        for col in range(len(matrix[row_])):
            if matrix[row_][col] != matrix[row_ - 1][col]:
                new_matrix.append(matrix[row_])
                break
    return new_matrix


if __name__ == '__main__':
    col_size = int(input('Введите количество столбцов в двумерном массиве:'))
    elements = list((map(int, str(input('Введите значения двумерного массива:')).split())))
    matrix_ = []
    for i in range(0, len(elements), col_size):
        matrix_.append(elements[i:col_size + i])
    print('Исходный двумерный массив:')
    for row in matrix_:
        print(row)
    print('Новый двумерный массив:')
    new_matrix_ = create_array_without_repeating_rows_in_row(matrix_)
    for row in new_matrix_:
        print(row)
