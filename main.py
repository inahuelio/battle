def jugadores():
    pass


def tamtabl_sando(tamtabl):
    tabl_sando = []
    for fila in range(tamtabl):
        tabl_sando.append([])
        for columna in range(tamtabl):
            tabl_sando[fila].append(0)
        print(tabl_sando[fila])
    print(" - " * tamtabl)
    return tabl_sando


def tamtabl_brita(tamtabl):
    table_brita = []
    for fila in range(tamtabl):
        table_brita.append([])
        for columna in range(tamtabl):
            table_brita[fila].append(0)
        print(table_brita[fila])
    return table_brita


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
        tamtabl_sando(tamtabl)
        tamtabl_brita(tamtabl)
    else:
        while tamtabl < 10:
            tamtabl = int(input("El nro ingresado es menor a 10, ingrese un numero mayor o igual: "))
            if tamtabl >= 10:
                tamtabl_sando(tamtabl)
                tamtabl_brita(tamtabl)


def main():
    table_brita = []
    tamtable()


main()
