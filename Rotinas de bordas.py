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
def borda(s1):
    tam = len(s1)
    if tam:
        print('|', '—' * tam, '|')
        print('|',s1,'|')
        print('|', '—' * tam, '|')
#Programa Principal
borda('menu')
borda('alessandro')

