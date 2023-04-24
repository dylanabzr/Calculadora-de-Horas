class SomaHoras:
    def __new__(cls, hora1, hora2):
        """Função que recebe duas horas diferentes válidas e as soma"""
        def hora_lista(horario):
            """Função que transforma uma string de hora no formato "XX:XX" em uma lista no formato [XX, XX]"""
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

        hora1 = hora_lista(hora1)
        hora2 = hora_lista(hora2)
        if hora1 is not None and hora2 is not None:
            hora3 = [0, 0]
            hora3[0] = hora1[0] + hora2[0]
            hora3[1] = hora1[1] + hora2[1]
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
            pass
            if hora3[0] > 9 and hora3[1] > 9:
                hora3 = map(str, hora3)
                hora3 = ":".join(hora3)
                return hora3
            elif hora3[0] < 9 < hora3[1]:
                hora3[0] = str(hora3[0])
                hora3[0] = "0" + hora3[0]
                hora3 = map(str, hora3)
                hora3 = ":".join(hora3)
                return hora3
            elif hora3[1] < 9 < hora3[0]:
                hora3[1] = str(hora3[1])
                hora3[1] = "0" + hora3[1]
                hora3 = map(str, hora3)
                hora3 = ":".join(hora3)
                return hora3
            elif hora3[1] < 9 and hora3[0] < 9:
                hora3[0] = str(hora3[0])
                hora3[0] = "0" + hora3[0]
                hora3[1] = str(hora3[1])
                hora3[1] = "0" + hora3[1]
                hora3 = map(str, hora3)
                hora3 = ":".join(hora3)
                return hora3
        else:
            hora3 = "Horário inválido"
            return hora3


a = input("Digite uma hora válida: ")
b = input("Digite outra hora válida para ser somada com a anterior: ")
operação = input("Digite a operação desejada(+,-): ")
if operação == "+":
        print(SomaHoras(a, b))
elif operação == "-":
        a = a.replace(":", " ")
        a = a.split()
        a_int = []
        b = b.replace(":", " ")
        b = b.split()
        b_int = []
        for i in a:
                a_int.append(int(i))
        a = a_int
        if a[1] > 59 or a[1] < 0:
                print("Horário inválido")
        elif a[0] > 23 or a[0] < 0:
                print("Horário inválido")
        for i in b:
                b_int.append(int(i))
        b = b_int
        if b [1] > 59 or b[1] < 0:
                print("Horário inválido")
        elif a[0] > 23 or a[0] < 0:
                print("Horário inválido")


        hora1 = a
        hora2 = b
        hora3 = [0, 0]
        hora3[0] = hora1[0] - hora2[0]
        if hora3[0] < 0:
                hora3[0] += 24
        elif hora3[0] == 24:
                hora3[0] = 0
        if hora1[1] >= hora2[1]:
                hora3[1] = hora1[1] - hora2[1]
        elif hora1[1] < hora2[1]:
                hora3[1] = (hora1[1] + 60) - hora2[1]
                hora3[0] -= 1
        if hora3[0] > 9 and hora3[1] > 9:
                hora3 = map(str, hora3)
                hora3 = ":".join(hora3)
                print(hora3)
        elif hora3[0] < 9 < hora3[1]:
                hora3[0] = str(hora3[0])
                hora3[0] = "0" + hora3[0]
                hora3 = map(str, hora3)
                hora3 = ":".join(hora3)
                print(hora3)
        elif hora3[1] < 9 < hora3[0]:
                hora3[1] = str(hora3[1])
                hora3[1] = "0" + hora3[1]
                hora3 = map(str, hora3)
                hora3 = ":".join(hora3)
                print(hora3)
        elif hora3[1] < 9 and hora3[0] < 9:
                hora3[0] = str(hora3[0])
                hora3[0] = "0" + hora3[0]
                hora3[1] = str(hora3[1])
                hora3[1] = "0" + hora3[1]
                hora3 = map(str, hora3)
                hora3 = ":".join(hora3)
                print(hora3)

