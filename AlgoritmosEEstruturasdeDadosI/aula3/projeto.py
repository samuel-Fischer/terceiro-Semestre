import csv

# Define as listas de alunos
nomes = []
idades = []
cursos = []

# Carrega os dados do arquivo CSV
with open('alunos.csv', 'r') as arquivo:
    leitor = arquivo.readlines()
    for linha in leitor:
        partes = linha.split(";")
        nomes.append(partes[0])
        idades.append(int(partes[1]))
        cursos.append(partes[2])

# Define a função para cadastrar um novo aluno
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    curso = input("Digite o curso do aluno: ")
    nomes.append(nome)
    idades.append(idade)
    cursos.append(curso)
    print("Aluno cadastrado com sucesso!")

# Define a função para listar todos os alunos
def listar_alunos():
    for i in range(len(nomes)):
        print(nomes[i], idades[i], cursos[i])

# Define a função para pesquisar um aluno pelo nome
def pesquisar_aluno():
    nome_pesquisa = input("Digite o nome do aluno para pesquisar: ")
    indice = nomes.index(nome_pesquisa)
    print(nomes[indice], idades[indice], cursos[indice])

# Define a função para excluir um aluno pelo nome
def excluir_aluno():
    nome_exclusao = input("Digite o nome do aluno para excluir: ")
    indice = nomes.index(nome_exclusao)
    nomes.pop(indice)
    idades.pop(indice)
    cursos.pop(indice)
    print("Aluno excluído com sucesso!")

# Define a função para exibir um resumo do número de alunos e média de idade
def resumo_alunos():
    total_alunos = len(nomes)
    media_idade = sum(idades) / total_alunos
    print("Total de alunos:", total_alunos)
    print("Média de idade:", media_idade)

# Define o loop principal do programa
while True:
    # Exibe o menu
    print("\n---- MENU ----")
    print("1. Cadastrar Aluno")
    print("2. Listar os Alunos")
    print("3. Pesquisar por Nome")
    print("4. Excluir")
    print("5. Resumo (Nº de Alunos e Média de Idade)")
    print("6. Finalizar")

    # Lê a opção escolhida pelo usuário
    opcao = int(input("Escolha uma opção: "))

    # Executa a opção escolhida pelo usuário
    if opcao == 1:
        cadastrar_aluno()
    elif opcao == 2:
        listar_alunos()
    elif opcao == 3:
        pesquisar_aluno()
    elif opcao == 4:
        excluir_aluno()
    elif opcao == 5:
        resumo_alunos()
    elif opcao == 6:
        # Salva os dados no arquivo CSV e finaliza o programa
        with open('alunos.csv', 'w', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            for i in range(len(nomes)):
                linha = [nomes[i], idades[i], cursos[i]]
                escritor.writerow(linha)
        break
    else:
        print("Opção inválida. Tente novamente.")