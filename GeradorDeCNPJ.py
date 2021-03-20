from random import randint

def cnpjGenerator():
    filial = [0]*14
    filial2 = [0]*14
    filial3 = [0]*14
    total = 0
    total1 = 0
    final = ''

#Número de inscrição
    for i in range(8):
        filial[i] = randint(0, 9)  
    for i in range(8, 12):
        filial[i] = randint(0, 9)
    filial2[0] = filial[0]*5
    filial2[1] = filial[1]*4
    filial2[2] = filial[2]*3
    filial2[3] = filial[3]*2

#Número de filiais
    filial2[4] = filial[4]*9
    filial2[5] = filial[5]*8
    filial2[6] = filial[6]*7
    filial2[7] = filial[7]*6
    filial2[8] = filial[8]*5
    filial2[9] = filial[9]*4
    filial2[10] = filial[10]*3
    filial2[11] = filial[11]*2
    for i in range(13):
        total += filial2[i]

#Primeiro dígito verificador
    if (total%11 < 2):
        filial[12] = 0
    else:
        filial[12] = 11 - int(total%11)

#Segundo dígito verificador
    filial3[0] = filial[0]*6
    filial3[1] = filial[1]*5
    filial3[2] = filial[2]*4
    filial3[3] = filial[3]*3
    filial3[4] = filial[4]*2
    filial3[5] = filial[5]*9
    filial3[6] = filial[6]*8
    filial3[7] = filial[7]*7
    filial3[8] = filial[8]*6
    filial3[9] = filial[9]*5
    filial3[10] = filial[10]*4
    filial3[11] = filial[11]*3
    filial3[12] = filial[12]*2
    for i in range(14):
        total1 += filial3[i]

    if (total1%11 < 2):
        filial[13] = 0
    else:
        filial[13] = 11 - int(total1%11)
    #CNPJ
    for i in range(14):
        final += str(filial[i])
    return final