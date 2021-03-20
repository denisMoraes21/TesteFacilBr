from random import randint

def cpfGenerator():
    cpf = [0]*11
    cpf2 = [0]*11
    cpf3 = [0]*11
    total = 0
    total1 = 0
    final = ''

    for i in range(9):
        cpf[i] = randint(0, 9)
        
    #Geração de Primeiro dígito verificador
    for i in range(10, 1, -1):
        cpf2[10-i] = cpf[10-i]*i
    for i in range(9):
        total += cpf2[i]
    if (total%11 < 2):
        cpf[9] = 0
    else:
        cpf[9] = 11 - int(total%11)
    
    #Geração de Segundo dígito verificador
    for i in range(11, 1, -1):
        cpf3[11-i] = cpf[11-i]*i    
    for i in range(10):
        total1 += cpf3[i]
    if (total1%11 >= 2):
        try:
            cpf[10] = 11 - int(total%11)
        finally:
            cpf[10] = randint(0, 9)
    else:
        cpf[10] = 0
    
    #CPF
    for i in range(11):
        final += str(cpf[i])
    return final

