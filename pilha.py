lista_pilha = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def menu_pilha():

  opt = '' 
  opt = int(input(" [1]-Remover elemento [2]- Adicionar elemento: "))
  if opt == 1:
    sub_pilha()
  if opt == 2:
    add_pilha()
  
def sub_pilha():
  
  print(lista_pilha)
  opt = input("Deseja ultimo o primeiro elemento? [s] ou [n]")
  if opt == 's': 
    lista_pilha.pop(-1)
    print(lista_pilha)
  elif opt == 'n':
    menu_pilha()
  if len(lista_pilha) == 0: 
    print("lista vazia!")
    menu_pilha()
  else:
    sub_pilha()

def add_pilha():

  print(lista_pilha)
  elemento = input("Digite o valor do elemento para adicionar ou escreva sair:")
  if elemento == 'sair':
    print(lista_pilha)
    menu_pilha()
  else:
    elemento = int(elemento)
    lista_pilha.append(elemento)
    add_pilha()
  
menu_pilha()

  
