import json
import requests
from bs4 import BeautifulSoup
from titulo import titulo

jogadores = []

def carregar_jogadores():
    url = "https://ge.globo.com/futebol/brasileirao-serie-a/"

    req = requests.get(url)

    # Faz um "parser" (conversão) da página para análise
    html = BeautifulSoup(req.content, "html.parser")

    artilheiros = html.find_all("div", class_="ranking-item-wrapper")

    for artilheiro in artilheiros:
        nome = artilheiro.find("div", class_="jogador-nome").string
        posicao = artilheiro.find("div", class_="jogador-posicao").string
        gols = artilheiro.find("div", class_="jogador-gols").string
        fotos = artilheiro.find_all("img")
        clube = fotos[1]["alt"]

        jogadores.append({"nome": nome, "posicao": posicao, "gols": gols, "clube": clube})


def listar():
    titulo("Listagem dos Artilheiros")
    print("\nNome do Jogador....: Clube.........: Posição............: Gols")
    print("-"*62)
    for jogador in jogadores:
        nome = jogador["nome"]
        clube = jogador["clube"]
        posicao = jogador["posicao"]
        gols = jogador["gols"]
        print(f"{nome:20} {clube:15} {posicao:20}  {gols}")


def listar_ordem():
    titulo("Listagem dos Artilheiros por Ordem de Nome")
    jogadores2 = sorted(jogadores, key=lambda jogador: jogador["nome"])
    print("\nNome do Jogador....: Clube.........: Posição............: Gols")
    print("-"*62)
    for jogador in jogadores2:
        nome = jogador["nome"]
        clube = jogador["clube"]
        posicao = jogador["posicao"]
        gols = jogador["gols"]
        print(f"{nome:20} {clube:15} {posicao:20}  {gols}")


def agrupar_clube():
    titulo("Artilheiros por Clube")
    dicionario = {}
    for jogador in jogadores:
        # Busca a palavra (chave). Se não existir: None
        chave = dicionario.get(jogador["clube"], None)
        if chave == None:
            # Não existe, adiciona com o nome do jogador
            dicionario[jogador["clube"]] = jogador["nome"]
        else:
            # Se existe, adiciona mais ", " e o nome deste jogador
            dicionario[jogador["clube"]] = chave + ", " + jogador["nome"]
    
    ordenados = sorted(dicionario.items(), key=lambda c : c[0])

    # Para obter chave e valor
    for (clube, jogador) in ordenados:
        print(f"{clube}: {jogador}")


carregar_jogadores()

# imprimir a resposta em formato JSON
resposta_json = json.dumps(jogadores, indent=4)
# print(resposta_json)
with open("exemplo.json", "w", encoding="utf-8") as arquivo:
    json.dump(jogadores, arquivo, indent=4, ensure_ascii=False)

while True:
    titulo("Goleadores do Brasileirão 2023")
    print("1. Listar Goleadores")
    print("2. Goleadores em Ordem de Nome")
    print("3. Goleadores por Clube")
    print("4. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        listar()
    elif opcao == 2:
        listar_ordem()
    elif opcao == 3:
        agrupar_clube()
    elif opcao == 4:
        break
