def maior_menor(anos):
    if anos < 18:
        return True
    else:
         return False

anos = int(input('Qual é a sua Idade ?\n'))
    
if maior_menor(anos):
      print('Essa Pessoa é Menor de Idade')
else:
      print('Essa Pessoa é Maior de Idade')
