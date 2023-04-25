# 5. Que receba os parâmetros: idade, nome e cidade, sendo destes apenas a idade como obrigatório.
# Exiba os dados informados e a mensagem de você é maior ou menor de idade.
# Para os testes, faça chamadas a essa função usando os parâmetros nomeados. 

def mostra_dados(idade, nome="", cidade=""):
  if nome != "":
    print(f"Nome: {nome}")
  if cidade != "":
    print(f"Cidade: {cidade}")
  if idade >= 18:
    print("Você é maior de idade")
  else:
    print("Você é menor de idade")