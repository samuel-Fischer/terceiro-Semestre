# Listas
nomes = []

# Tuplas
bairros = ()

# Dicionários
alunos = {}
alunos = dict()

# exemplos de dicionários
contatos = {"Ana": "99101-0203",
            "Bianca": "99108-0706",
            "Carlos": "98430-4050",
            "Débora": "98118-1920",}

print("Buscar contatos: " + f"{contatos}")
print("Buscar por 'Bianca': " + contatos['Bianca'])

# alterar o direcionário
contatos.update({"Eduardo": "99988-7766"})
contatos["Fernanda"] = "984830201"

print("Buscar contatos (atualizada): " + f"{contatos}")

# formas de percorrer um dicionário
## para obter as chaves:
print ()
print("Lista de Clientes")
print("-"*30)
for nome in contatos.keys():
  print(nome)

## para obter as valor:
print ()
print("Lista de Fones")
print("-"*30)
for fone in contatos.values():
  print(fone)

## para obter as chaves e valor:
print ()
print("Lista de Clientes e Fones")
print("-"*30)
for (nome, fone) in contatos.items():
  print(f"{nome} - {fone}")

# Exempo de aplicação
## Vetor de dicionários
clientes = [{"nome": "Luis Carlos", "idade": 23},
            {"nome": "Ana Maria", "idade": 32},
            {"nome": "Simone Santos", "idade": 28},
            {"nome": "Bianca Costa", "idade": 40},
            {"nome": "Zilmar Cardoso", "idade": 30}]

print ()
print("Lista de Clientes")
print("-"*30)
for cliente in clientes:
  print(f"{cliente['nome']} - {cliente['idade']} anos")

""" para classificar os elementos utilizados a palavra 
reservada lambda que permite criar funções anonimas Python """
clientes2 = sorted(clientes, key=lambda cliente: cliente['nome'])

print ()
print("Lista de Clientes - em ordem de Nome")
print("-"*30)
for cliente in clientes2:
  print(f"{cliente['nome']} - {cliente['idade']} anos")

# Classifica (ordena) pelo atributo idade
clientes3 = sorted(clientes, key=lambda cliente: cliente['idade'])

print ()
print("Lista de Clientes - em ordem de Idade")
print("-"*30)
for cliente in clientes3:
  print(f"{cliente['nome']} - {cliente['idade']} anos")
  