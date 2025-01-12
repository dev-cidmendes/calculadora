import os #importa a biblioteca 'OS'.

def soma(numero,numero2):
  print('{}+{}={}' .format(numero,numero2,numero+numero2)) #função que faz a soma dos números

def sub(numero,numero2):
  print('{}-{}={}' .format(numero,numero2,numero-numero2)) #função que faz a subtração dos números

def mult(numero,numero2):
  print('{}x{}={}' .format(numero,numero2,numero*numero2)) #função que faz a multiplicação dos números

def div(numero,numero2):
  print('{}/{}={}' .format(numero,numero2,numero/numero2)) #função que faz a divisão dos números

#função que exibe o menu da calculadora na tela do usuário
def menu():
  linha()
  print('         CALCULADORA         ')
  linha()
  print('1 - SOMA')
  print()
  print('2 - SUBTRAÇÃO')
  print()
  print('3 - MULTIPLICAÇÃO')
  print()
  print('4 - DIVISÃO')      

def linha():
  print('=============================') #função que imprime uma linha divisória na tela

def limpa_terminal(): #função que limpa o terminal ao fim da operação
 sistema = os.name
 if sistema == 'nt':
  os.system('cls')

while True: #loop que exibe o código na tela enquanto o usário desejar continuar
  menu()

  linha()

#condição para selecionar a operação
  opcao = int(input('Digite o número da operação:'))
  print()
  if opcao == 1:
    print('selecionado: SOMA')
  elif opcao == 2:
    print('selecionado: SUBTRAÇÃO')
  elif opcao == 3:
    print('selecionado: MULTIPLICAÇÃO')
  elif opcao == 4:
    print('selecionado: DIVISÃO')
  else:
    print('OPÇÃO INVÁLIDA')
    continue

  linha()
#variaveis que recebem os números do usuário
  n1usuario = int(input('Digite um número:'))
  print()
  n2usuario = int(input('Digite outro número:'))

  linha()
#condição que imprime a operação selecionada
  if opcao == 1:
    soma(n1usuario,n2usuario)
  elif opcao == 2:
    sub(n1usuario,n2usuario)
  elif opcao == 3:
    mult(n1usuario,n2usuario)
  elif opcao == 4:
    div(n1usuario,n2usuario)


  linha()

  continuar = input('REALIZAR OUTRA OPERAÇÃO? (S/N)').lower().upper() # limpa o terminal e reinicia a calculadora
  limpa_terminal()

  if continuar != 'S': #encerra a calculadora e limpa o terminal caso o usuário não queira continuar 
    limpa_terminal()
    break
