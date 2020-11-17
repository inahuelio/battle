tabl_sando = []
table_brita = []


def jugadores():
    pass


def tamtabl_init(tamtabl, tab_usar):
    for fila in range(tamtabl):
        tab_usar.append([])
        for columna in range(tamtabl):
            tab_usar[fila].append(0)
        print(tab_usar[fila])
    print(" - " * tamtabl)
    return tab_usar


def sandokan():
    pass


def arm_britanica():
    pass


def atacar():
    pass


def partespecial():
    pass


def tamtable():
    tamtabl = int(input("Ingrese el tamaño de su tablero nxn (min 10): "))
    if tamtabl >= 10:
        tamtabl_init(tamtabl, tabl_sando)
        tamtabl_init(tamtabl, table_brita)
    else:
        while tamtabl < 10:
            tamtabl = int(input("El nro ingresado es menor a 10, ingrese un numero mayor o igual: "))
            if tamtabl >= 10:
                tamtabl_init(tamtabl, tabl_sando)
                tamtabl_init(tamtabl, table_brita)


def main():
    table_brita = []
    tamtable()


main()
