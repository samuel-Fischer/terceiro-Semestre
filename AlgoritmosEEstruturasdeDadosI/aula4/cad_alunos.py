import os

# declara os vetores globais
alunos = []
idades = []
cursos = []

def ler_arquivo():
  # se o arquivo não existe, retorna
  if not os.path.isfile("alunos.txt"):
    return
  
  # abre o arquivo para leitura
  with open("alunos.txt", "r") as arq:
    linhas = arq.readlines()

    for linha in linhas:
      # separa a linha em elementos de vetor, a cada ";"
      partes = linha.split(";")
      alunos.append(partes[0])
      idades.append(int(partes[1]))
      cursos.append(partes[2][0:-1])    
    # print(alunos)
    # print(idades)
    # print(cursos)

def salva_arquivo():
  # abre o arquivo para gravação (sobrepõe os dados)
  with open("alunos.txt", "w") as arq:
    
    for nome, idade, curso in zip(alunos, idades, cursos):
      arq.write(f"{nome};{idade};{curso}\n")

def titulo(texto, sublinhado="-"):
  print()
  print(texto)
  print(sublinhado*30)

def cadastrar():
  titulo("Inclusão de Aluno")
  nome = input("Nome do Aluno: ")
  idade = int(input("Idade: "))
  curso = input("Curso: ")
  alunos.append(nome)
  idades.append(idade)
  cursos.append(curso)
  print("Ok! Aluno cadastrado com sucesso")

def listar():
  titulo("Lista de Alunos Cadastrados")
  print("Nº Nome do Aluno....... Idade Curso.....")
  for x, (nome, idade, curso) in enumerate(zip(alunos, idades, cursos), start=1):
    print(f"{x:2} {nome:20}  {idade:3}  {curso}")

def pesquisar():
  titulo("Pesquisa por Nome")

  pesq = input("Nome do Aluno (ou parte do nome): ")

  print("Nº Nome do Aluno....... Idade Curso.....")
  
  for x, (nome, idade, curso) in enumerate(zip(alunos, idades, cursos), start=1):
    if pesq.upper() in nome.upper():
      print(f"{x:2} {nome:20}  {idade:3}  {curso}")

def excluir():
  # lista os alunos para o usuário ver o nº
  listar() 

  titulo("Exclusão de Aluno")
  num = int(input("Nº do Aluno a Excluir: "))

  if num <= 0 or num > len(alunos):
    print("Número inválido")
    return
  
  # num-1, pois no vetor inicia em 0 (e, na listagem, em 1)
  alunos.pop(num-1)
  idades.pop(num-1)
  cursos.pop(num-1)

def resumo():
  titulo("Resumo do Cadastro")

  num = len(alunos)
  soma = sum(idades)
  media = soma / num

  print(f"Nº de Alunos: {num}")
  print(f"Média de Idades: {media:4.1f}")

# ao iniciar o programa, carrega os dados salvos no arquivo
ler_arquivo()

while True:
  titulo("Cadastro de Alunos", "=")
  print("1. Cadastrar Aluno")
  print("2. Listar os Alunos")
  print("3. Pesquisar por Nome")
  print("4. Excluir")
  print("5. Resumo (Nº de Alunos e Média de Idade)")
  print("6. Finalizar")
  opcao = int(input("Opção: "))
  if opcao == 1:
    cadastrar()
  elif opcao == 2:
    listar()
  elif opcao == 3:
    pesquisar()
  elif opcao == 4:
    excluir()
  elif opcao == 5:
    resumo()
  else:
    # ao finalizar o programa, salva os dados no arquivo
    salva_arquivo()
    break