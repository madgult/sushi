lista1 = []
lista2 = []
lista3 = []

print ('--' * 80)
print ('seja bem-vindo ao banco ! ^-^')

while True:
    nome = input('\n qual eh seu nome? ')
    pref = input('escolha sua preferencia I- Idoso, G - Gestante ou N - Normal? ').upper()

    if pref == 'I':
        lista1.append(nome)
    elif pref == 'G':
        lista2.append(nome)
    elif pref == 'N':
        lista3.append(nome)
    else:
        print ('este comando eh invalido')

    print ('\n fila idosos:', lista1)
    print ('\n fila gestantes: ', lista2)
    print ('\n fila menos preferencial: ', lista3)

    rem = input('\n deseja atender alguem da fila? S/N ').upper()

    if rem == 'S':
        if len(lista1) > 0:
            lista1.pop(0)
        elif len(lista2) > 0:
            lista2.pop(0)
        elif len(lista3) > 0:
            lista3.pop(0)
        else:
            print ('este comando eh invalido')

    else:
        print ('este comando eh invalido')

    print ('idosos: ', lista1)
    print ('gestantes: ', lista2)
    print ('menos preferencial: ', lista3)  
            
            

   














