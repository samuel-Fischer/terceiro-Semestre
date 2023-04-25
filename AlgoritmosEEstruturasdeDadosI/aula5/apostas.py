import csv

# Define as listas de apostas
apostadores = []
palpites = []
valores = []

# Carrega os dados do arquivo CSV
with open('apostas.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        apostadores.append(linha[0])
        palpites.append(linha[1])
        valores.append(float(linha[2]))

# Define a função para cadastrar uma nova aposta
def cadastrar_aposta():
    nome = input("Digite o nome do apostador: ")
    palpite = input("Digite o palpite (no formato 2x1): ")
    valor = float(input("Digite o valor da aposta: "))
    while not (len(palpite) == 3 and palpite[1] == 'x' and palpite[0:1].isdigit() and palpite[2:3].isdigit()):
        palpite = input("Palpite inválido. Digite o palpite novamente (no formato 2x1): ")
    apostadores.append(nome)
    palpites.append(palpite)
    valores.append(valor)
    print("Aposta cadastrada com sucesso!")

# Define a função para listar todas as apostas
def listar_apostas():
    for i in range(len(apostadores)):
        print(apostadores[i], palpites[i], valores[i])

# Define a função para listar o resultado
def listar_resultado():
    caxias = int(input("Digite o número de gols do Caxias: "))
    gremio = int(input("Digite o número de gols do Grêmio: "))
    resultado = str(caxias) + "x" + str(gremio)
    total_apostado = 0
    total_premiado = 0
    for i in range(len(apostadores)):
        if palpites[i] == resultado:
            total_apostado += valores[i]
            total_premiado += valores[i] * 2.0
    print("Resultado:", resultado)
    print("Total apostado:", total_apostado)
    print("Total premiado:", total_premiado)

# Define a função para exibir o total de apostas
def total_apostas():
    print("Total de apostas:", len(apostadores))
    print("Total apostado:", sum(valores))

# Define a função para exibir as apostas por resultado
def apostas_por_resultado():
    caxias = int(input("Digite o número de gols do Caxias: "))
    gremio = int(input("Digite o número de gols do Grêmio: "))
    resultado = str(caxias) + "x" + str(gremio)
    total_apostado = 0
    total_premiado = 0
    for i in range(len(apostadores)):
        if palpites[i] == resultado:
            print(apostadores[i], valores[i])
            total_apostado += valores[i]
            total_premiado += valores[i] * 2.0
    print("Total apostado:", total_apostado)
    print("Total premiado:", total_premiado)

# Define a função para exibir o resultado e a premiação
def resultado_e_premiacao():
    caxias = int(input("Digite o número de gols do Caxias: "))
    gremio = int(input("Digite o número de gols do Grêmio: "))
    resultado = str(caxias) + "x" + str(gremio)
    total_apostado = 0
    total_premiado = 0
    for i in range(len(apostadores)):
        if palpites[i] == resultado:
            total_apostado += valores[i]
            total_premiado += valores[i] * 2.0
    print("Resultado:", resultado)
    print("Total apostado:", total_apostado)
    print("Total premiado:", total_premiado)

# Define o loop principal do programa
while True:
    # Exibe o menu
    print("\n---- MENU ----")
    print(" AvenidasBet – Controle de Apostas")
    print(" Caxias x Grêmio (Final do Gauchão 2023)")
    print("==============================================")
    print("1. Cadastrar Aposta")
    print("2. Listar Apostas")
    print("3. Listar Resultado")
    print("4. Total de Apostas")
    print("5. Apostas por Resultado")
    print("6. Resultado e Premiação")
    print("7. Finalizar")

    # Lê a opção escolhida pelo usuário
    opcao = int(input("Escolha uma opção: "))

        # Executa a opção escolhida pelo usuário
    if opcao == 1:
        cadastrar_aposta()
    elif opcao == 2:
        listar_apostas()
    elif opcao == 3:
        listar_resultado()
    elif opcao == 4:
        total_apostas()
    elif opcao == 5:
        apostas_por_resultado()
    elif opcao == 6:
        resultado_e_premiacao()
    elif opcao == 7:
        break
    else:
        print("Opção inválida. Tente novamente.")
print("Programa finalizado.")