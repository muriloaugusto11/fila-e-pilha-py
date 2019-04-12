lista_fila = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def menu_fila():

  opt = '' 
  opt = int(input(" [1]-Remover elemento [2]- Adicionar elemento: "))
  if opt == 1:
    sub_fila()
  if opt == 2:
    add_fila()
  
def sub_fila():
  
  print(lista_fila)
  opt = input("Deseja apagar o primeiro elemento? [s] ou [n]")
  if opt == 's': 
    lista_fila.pop(0)
    print(lista_fila)
  elif opt == 'n':
    menu_fila()
  if len(lista_fila) == 0: 
    print("lista vazia!")
    menu_fila()
  else:
    sub_fila()

def add_fila():

  print(lista_fila)
  elemento = input("Digite o valor do elemento para adicionar ou escreva sair:")
  if elemento == 'sair':
    print(lista_fila)
    menu_fila()
  else:
    elemento = int(elemento)
    lista_fila.append(elemento)
    add_fila()
  
menu_fila()
