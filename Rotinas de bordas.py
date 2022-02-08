""""

def formato(s1):
    tam = len(s1)
    if tam:
        print('|', '—' * tam, '|')
        print('|', '—' * tam, '|')
        print()
        print('|', '—' * tam, '|')
        print('|', '—' * tam, '|')
#Programa Principal
s1 = input('digite seu nome')
print('{}{} '.format(s1,formato))"""
###################################################################
def borda(s1): # O s1 vai ser uma string
    tam = len(s1)# Pego o tamanho da string com len
    if tam: # Caso a  string form menor que 0 fica como False
            # Se a string tem mais do que 0 retorna TRUE e impriome na tela
        print('|', '—' * tam, '|')
        print('|',s1,'|')
        print('|', '—' * tam, '|')
#Programa Principal
borda('menu')
borda('alessandro')

