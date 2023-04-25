import os 

patrimonio = []
dataAq = []
valorE = []

def ler_arquivo():
  # se o arquivo não existe, retorna
  if not os.path.isfile("patrimonio.txt"):
    return
  
  # abre o arquivo para leitura
  with open("patrimonio.txt", "r") as arq:
    linhas = arq.readlines()

    for linha in linhas:
      # separa a linha em elementos de vetor, a cada ";"
      partes = linha.split(";")
      patrimonio.append(partes[0])
      dataAq.append(partes[1])
      valorE.append(float(partes[2][0:-1]))
      
def salva_arquivo():
  with open("patrimonio.txt", "w") as arq:

    for Patrimonio, DataAq, ValorE in zip(patrimonio, dataAq, valorE):
      arq.write(f"{Patrimonio};{DataAq};{ValorE}\n")

def titulo(texto, sublinhado="-"):
  print()
  print(texto)
  print(sublinhado*30)
  
def cadastrar():
  titulo("Inclusão de Patrimonio")
  Patrimonio = input("Nome do Patrimonio: ")

  while True:
    data = input("Data da Aquisição: ")
    if len(data) != 10:
      print("Erro. Formato inválido. informe no formato DD/MM/AAAA")
      continue
    
    if data[2] != "/" or data[5] != "/":
      print("prencha com as duas /")
      continue


    # separa em elementos de vetor a partir da ocorrência do x
    partes = data.split("/")
    

    if len(partes) != 3:
      print("Erro. Formato inválido.")
      continue                        # volta ao início da repetição

    # strip(): retira os espaços em branco
    dia = partes[0].strip()  
    mes = partes[1].strip()
    ano = partes[2].strip()

    # isdigit(): retorna verdadeiro se for dígito numérico
    if not dia.isdigit() or not mes.isdigit() or not ano.isdigit():    
      print("Erro. Informe apenas números no placar")
      continue                        # volta ao início do while

    break   # sai da repetição


  valor = (float(input("valor do Item: ")))
  patrimonio.append(Patrimonio)
  dataAq.append(data)
  valorE.append(valor)
  print("Ok! Item cadastrado com sucesso")

def listar():
  titulo("Listagem de patromônio")

  print("Patrimônios.........  Data:         Valor R$:")

  for patr, dat, val in zip(patrimonio, dataAq, valorE):
    print(f"{patr:20}  {dat:^12}  {val:9.2f}")

def pesquisar():
  titulo("Pesquisa por Ano de Aquisição")
  ano = input("Informe o ano desejado (AAAA): ")
  resultados = []
  for i, data in enumerate(dataAq):
    if ano in data:
      resultados.append((patrimonio[i], data, valorE[i]))

  if resultados:
    print(f"Patrimônios adquiridos no ano de {ano}:")
    print("Patrimônios.........  Data:         Valor R$:")
    for patr, dat, val in resultados:
      print(f"{patr:20}  {dat:^12}  {val:9.2f}")
  else:
    print(f"Nenhum patrimônio encontrado para o ano de {ano}")


def alterar():
  valor = int(input("Em quantos % você quer aumentar os valores dos patrimônios? "))
  for i in range(len(patrimonio)):
    valorE[i] = valorE[i] * (1 + valor/100)

  print(f"Todos os patrimonios receberam um acrecimo de {valor}%")

ler_arquivo()

while True:
  titulo("Cadastro de Patrimônio", "=") 
  print("1. Cadastrar Patrimônio")
  print("2. Listar Patrimônios")
  print("3. Pesquisar por aquisição")
  print("4. Alterar o preço de todos os patrimônios em %")
  print("5. Finalizar")
  opcao = int(input("Opção: "))
  if opcao == 1:
    cadastrar()
  elif opcao == 2:
    listar()
  elif opcao == 3:
    pesquisar()
  elif opcao == 4:
    alterar()
  else:
    salva_arquivo()
    break