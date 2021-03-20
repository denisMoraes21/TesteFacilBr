from random import randint

def pisGenerator():
    insc = [0]*11
    insc2 = [0]*11
    total = 0
    final = ''

    #Número  de inscrição
    for i in range(10):
        insc[i] = randint(0, 9)

    #Pesos
    insc2[0] = insc[0]*3
    insc2[1] = insc[1]*2
    insc2[2] = insc[2]*9
    insc2[3] = insc[3]*8
    insc2[4] = insc[4]*7
    insc2[5] = insc[5]*6
    insc2[6] = insc[6]*5
    insc2[7] = insc[7]*4
    insc2[8] = insc[8]*3
    insc2[9] = insc[9]*2

    #Dígito verificador
    for i in range(10):
        total += insc2[i]

    if (total%11 < 2):
        insc[10] = 0
    else:
        insc[10] = 11 - int(total%11)

    #PIS
    for i in range(11):
        final += str(insc[i])
    return final
