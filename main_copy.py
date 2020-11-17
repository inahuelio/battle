import random

table_sando = []
table_brita = []
columns = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sandokan_data = {
    # primer elemento indica si se debe colocar de forma vertical, el segundo la cantidad de elementos
    "FT": [False, 6],
    "CD": [True, 3],
    "DA": [False, 2],
    "DN": [True, 2],
    "DS": [False, 1]
}

armada_data = {
    "CP": [False, 6],
    "GL": [True, 3],
    "CO": [False, 2],
    "GR": [True, 2],
    "BA": [False, 1]
}


def jugadores():
    pass


def matrix_init(tamtabl, tab_usar):
    for fila in range(tamtabl):
        tab_usar.append([])
        for columna in range(tamtabl):
            tab_usar[fila].append(0)
        print(tab_usar[fila])
    print(" - " * tamtabl)
    return tab_usar


def validate_space(is_vertical, size, row, col, table):
    if is_vertical:
        for y in range(size):
            aux_row = table[row + y]
            if aux_row[col] != 0:
                return False
    else:
        aux_row = table[row]
        for y in range(size):
            if aux_row[y + col] != 0:
                return False
    return True


def matrix_fill(size, player_data, table):
    for x in player_data:
        space_not_found = True
        while space_not_found:
            col_vertical = random.choice(range(size))
            row_vertical = random.choice(range(size - player_data[x][1]))
            is_vertical = player_data[x][0]
            items = player_data[x][1]

            if is_vertical and validate_space(is_vertical, items, row_vertical, col_vertical, table):
                for y in range(items):
                    row = table[row_vertical + y]
                    row[col_vertical] = x
                space_not_found = False
            elif not is_vertical and validate_space(is_vertical, items, col_vertical, row_vertical, table):
                row = table[col_vertical]
                for y in range(items):
                    row[y + row_vertical] = x
                space_not_found = False
    return 0


def sandokan():
    pass


def arm_britanica():
    pass


def atacar():
    pass


def partespecial():
    pass


def tamtable():
    matrix_size = int(input("Ingrese el tamaño de su tablero nxn (min 10): "))
    if matrix_size >= 10:
        matrix_init(matrix_size, table_sando)
        matrix_init(matrix_size, table_brita)
        matrix_fill(matrix_size, sandokan_data, table_sando)
        matrix_fill(matrix_size, armada_data, table_brita)
    else:
        while matrix_size < 10:
            matrix_size = int(input("El nro ingresado es menor a 10, ingrese un numero mayor o igual: "))
            if matrix_size >= 10:
                matrix_init(matrix_size, table_sando)
                matrix_init(matrix_size, table_brita)


def main():
    tamtable()


main()
