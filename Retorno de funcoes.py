def soma3(x = 0, y = 0, z = 0):
    res = x + y + z
    return res
# Programa Principal
retornado = soma3(1,2,3)
print(retornado)

#Forma simplificada
print(soma3(2,2))

# Outra forma de retornar os valores da função e posso colocar varias variaveis
retornado1 = soma3(1,2,3)
retornado2 = soma3(1,2)
retornado3 = soma3(1)
retornado4 = soma3(1)
print('O resultados das variavies:{} {} {} {}'.format(retornado1,retornado2,retornado3,retornado4))