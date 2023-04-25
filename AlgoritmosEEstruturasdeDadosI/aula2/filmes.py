# 2. Que apresente um menu com as opções:
# 1. Incluir Filme
# 2. Listar Filmes
# 3. Listar os Filmes em Ordem Alfabética
# 4. Remover um Filme
# 5. Sair

filmes = []

def incluir():
    print("")
    print("inclusão de Filmes")
    print("-"*30)
    x = input("Título do Filme: ")
    filmes.append(x)

def listar():
    print("")
    print("Listagem de filmes")
    print("-"*30)
    for i, filme in enumerate(filmes, start=1):
      print(f"{i} - {filme}")
      
def listar_ordem():
    print("")
    print("Listagem de filmes em Ordem")
    print("-"*30)
    filmes2 = sorted(filmes)
    for i, filme in enumerate(filmes2, start=1):
        print(f"{i} - {filme}")
        
def remover():
    listar()
    num = int(input("Qual filme remover? (0, para sair):" ))
    if num == 0:
        return
    elif num > len(filmes):
        print("Erro... Informe um número existente na lista")
    else:
        filmes.pop(num-1)
        print("Ok. Filme removido.")

while True:
    print("Cadastro de Filmes")
    print("-"*30)
    print("1. Incluir Filme")
    print("2. Listar Filme")
    print("3. Listar em ordem")
    print("4. Remover Filme")
    print("5. Sair")
    opcao = int(input("Opção: "))
    if opcao == 1:
        incluir()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        listar_ordem()      
    elif opcao == 4:
        remover()
    elif opcao == 5:
        break