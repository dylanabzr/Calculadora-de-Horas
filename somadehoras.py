def hora_lista(horario):
    horario = horario.replace(":", " ")
    horario = horario.split()
    horario_int = []
    for i in horario:
        horario_int.append(int(i))
    horario = horario_int
    if horario[1] > 59 or horario[1] < 0:
        return None
    elif horario[0] > 23 or horario[0] < 0:
        return None
    else:
        return horario


hora = hora_lista(input("Digite uma hora válida: "))
hora2 = hora_lista(input("Digite outra hora válida para ser somada com a anterior: "))
if hora is not None and hora2 is not None:
    hora3 = [0, 0]
    hora3[0] = hora[0] + hora2[0]
    hora3[1] = hora[1] + hora2[1]
    if hora3[0] > 23:
        while hora3[0] > 23 or hora3[1] > 59:
            if hora3[0] > 24:
                hora3[0] = hora3[0] - 23
                if hora3[1] > 59:
                    hora3[1] = hora3[1] - 60
                    hora3[0] = hora3[0] + 1
            else:
                hora3[0] = 0
                if hora3[1] > 59:
                    hora3[1] = hora3[1] - 60
                    hora3[0] = hora3[0] + 1
    elif hora3[0] <= 23 and hora3[1] > 59:
        hora3[1] = hora3[1] - 60
        hora3[0] = hora3[0] + 1
        if hora3[0] == 24:
            hora3[0] = 0
    hora3 = map(str, hora3)
    hora3 = ":".join(hora3)
    print(f"A hora final é {hora3}")
else:
    print("Horário inválido")
