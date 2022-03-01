def validaCNPJ(CNPJ):
  #CNPJ tem 14 posições de 0 a 13
  cnpj = []

  #Lista Primeiro Digito
  primeiroDigito = [5,4,3,2,9,8,7,6,5,4,3,2]
  segundoDigito  = [6,5,4,3,2,9,8,7,6,5,4,3,2]
  
 # Um laço que percorrer a variável CNPJ e tranforma para inteiro e coloca esses valores no vetor cnpj
  for n in CNPJ:
    cnpj.append(int(n))

 # Variável tam está recebendo o tamanho da lista cnpj
  tam = len(cnpj)

 # Verifica se tam é maior que o número permitido em um CNPJ
  if tam > 14:
    quit('CNPJ Inválido')

  #Está fazendo a multiplicação das Listas CNPJ e primeiraConta
  pd = list(map(lambda x,y: x*y ,cnpj,primeiroDigito))
  
  #Está somando todos as posições das duas listas, e calculando o resto da divisão por 11
  somaPD = sum(pd) % 11


  if somaPD < 2:
    somaPD = 0
  else:
    somaPD = 11 - somaPD

  if somaPD == cnpj[12]:
    sd = list(map(lambda x,y: x*y,cnpj,segundoDigito))
    somaSD = sum(sd) % 11

    if somaSD < 2:
      somaSD = 0
    else:
      somaSD = 11 - somaSD

    if somaSD == cnpj[13]:
      print("CNPJ Válido")
    else:
      print("CNPJ Inválido")
    
  else:
    print("CNPJ Inválido")



CNPJ = input("Digite o CNPJ: ")
validaCNPJ(CNPJ)