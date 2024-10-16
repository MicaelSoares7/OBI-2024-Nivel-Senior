def verifica_placa(placa):
    if len(placa) == 8 and placa[0:3].isupper() and placa[3] == '-' and placa[4:8].isdigit():
        return 1
    elif len(placa) == 7 and placa[0:3].isupper() and placa[3].isdigit() and placa[4].isupper() and placa[5:7].isdigit():
        return 2
    else:
        return 0

placa = input()
print(verifica_placa(placa))