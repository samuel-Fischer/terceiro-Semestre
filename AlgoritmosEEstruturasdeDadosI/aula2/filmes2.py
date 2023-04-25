# 2. Que apresente um menu com as opções:
# 1. Incluir Filme
# 2. Listar Filmes
# 3. Listar os Filmes em Ordem Alfabética
# 4. Remover um Filme
# 5. Sair
filmes = []

def incluir():
  filme = input("\nQual filme você deseja incluir? ")
  filmes.append(filme)

def listar():
  for i, filme in enumerate(filmes, start=1):
    print(f"{i} - {filme}")

def listarOrdemA():
  filmes2 = sorted(filmes)
  for i, filme in enumerate(filmes2, start=1):
    print(f"{i} - {filme}")

def remover():
  listar()
  num = int(input("Qual o numero do filme você deseja remover?"))
  if num == 0:
    return
  elif num > len(filmes):
    print("Erro... Não temos este numero na lista.")
  else:
    filme_removido = filmes.pop(num-1)
    print("O segundo filme da lista era", filme_removido)

while True:
  print("\nSISTEMA PARA FILMES.")
  print("1. Incluir Filme.")
  print("2. Listar Filmes")
  print("3. Listar os filmes em ordem Alfábetica.")
  print("4. Remover um Filme.")
  print("5. Sair.")

  opt = int(input("\nEscolhe uma opção: "))
  print("-"*30)
  if opt == 1:
    incluir()
  elif opt == 2:
    listar()
  elif opt == 3:
    listarOrdemA()
  elif opt == 4:
    remover()
  else:
    break