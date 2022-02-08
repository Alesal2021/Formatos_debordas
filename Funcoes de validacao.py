def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while tam < min or tam > max:
        s1 = input(pergunta)
        tam = len(s1)
    return s1

#Programa Principal
x = valida_string('Digite uma string: ', 10, 30)
print('Voce digitou string: {} \n Dado valido. Encerrando o programa'.format(x))