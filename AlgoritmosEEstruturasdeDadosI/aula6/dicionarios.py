import csv
import os
apostadores = []


def obter_dados_do_arquivo():
    # se o arquivo não existe, retorna
    if not os.path.isfile("apostas.csv"):
        return

    # abre o arquivo para leitura
    with open("apostas.csv", "r") as arq:
        # lê todas as linhas do arquivo (carregando em um vetor)
        linhas = arq.readlines()

        for linha in linhas:
            # separa a linha em elementos de vetor, a cada ";"
            partes = linha.split(";")
            apostadores.append(partes[0])


def salvar_dados_no_arquivo():
    # abre o arquivo para gravação (sobrepõe os dados)
    with open("apostas.csv", "w") as arq:
        for apostador in zip(apostadores):
            arq.write(f"{apostador},\n")


def incluir():
    nome = input("nome: ")
    clube = input("clube: ")
    valor = float(input("valor: "))
    apostadores.append({"nome": nome, "clube": clube, "valor": valor})


def listar_apostadores():
    listar = sorted(apostadores, key=lambda apostador: apostador['nome'])

    print()
    print("Lista de Apostadores")
    print("-"*30)
    for a in listar:
        print(f"{a['nome']} - {a['clube']} - {a['valor']}")


def listar_valores():
    listar = sorted(apostadores, key=lambda apostador: apostador['valor'])

    print()
    print("Lista de Apostadores")
    print("-"*30)
    for a in listar:
        print(f"{a['nome']} - {a['clube']} - {a['valor']}")


def pesq():
    pesq = input("Por qual clube você está pesquisando: ")
    listar = sorted(apostadores, key=lambda apostadore: apostadore['clube'])

    print()
    print("Lista de Apostadores")
    print("-"*30)
    for a in listar:
        if a['clube'] == pesq:
            print(f"{a['nome']} - {a['clube']} - {a['valor']}")


def resumo1():
    pass

def resumo2():
    pass


obter_dados_do_arquivo()

while True:
    print("==== Apostas.com ====")
    print("1. Adicionar apostador.")
    print("2. Listar por ordem de nome.")
    print("3. Listar por ordem de valor.")
    print("4. Pesquisa por clube.")
    print("5. Resumo: Clube e Numero de apostas.")
    print("6. Resumo: Clube e R$ apostado.")
    print("7. Para finalizar.")
    opt = int(input("O que você deseja fazer: "))

    if opt == 1:
        incluir()
    elif opt == 2:
        listar_apostadores()
    elif opt == 3:
        listar_valores()
    elif opt == 4:
        pesq()
    elif opt == 5:
        resumo1()
    elif opt == 6:
        resumo2()
    else:
        salvar_dados_no_arquivo()
        break
