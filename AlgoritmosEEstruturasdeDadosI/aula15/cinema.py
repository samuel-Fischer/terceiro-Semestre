import requests
from bs4 import BeautifulSoup
from titulo import titulo

pelotas = []
portoAlegre = []

def carregar_jogadores():
    urlpel = "https://www.cineflix.com.br/cinema/pelotas/"
    urlpoa = "https://www.cineflix.com.br/cinema/porto-alegre/"

    reqpel = requests.get(urlpel)
    reqpoa = requests.get(urlpoa)

    htmlpel = BeautifulSoup(reqpel.content, "html.parser")
    htmlpoa = BeautifulSoup(reqpoa.content, "html.parser")

    filmespel = htmlpel.find_all("tr", class_="prog_line")
    filmespoa = htmlpoa.find_all("tr", class_="prog_line")

    for filme in filmespel:
        titulo_element = filme.find("div", class_="title")
        tit = titulo_element.text.strip()  
        tdidioma = filme.find("td", class_="idioma")
        idioma = tdidioma.find("span", class_="show_tooltip").string
        clasifi = filme.find("i", class_="show_tooltip").get("title")

        pelotas.append({"titulo": tit, "idioma": idioma, "clasificacao": clasifi})


    for filme in filmespoa:
        titulo_element = filme.find("div", class_="title")
        tit = titulo_element.text.strip()  
        tdidioma = filme.find("td", class_="idioma")
        idioma = tdidioma.find("span", class_="show_tooltip").string
        clasifi = filme.find("i", class_="show_tooltip").get("title")

        portoAlegre.append({"titulo": tit, "idioma": idioma, "clasificacao": clasifi})

carregar_jogadores()

def listar_pelotas():
    titulo("Listagem dos Filmes em Pelotas")
    print("\nTitulo do Filme.........................: Idioma.......: Classificação....:")
    print("-"*62)
    for filme in pelotas:
        tit = filme["titulo"]
        idioma = filme["idioma"]
        clasificacao = filme["clasificacao"]
        print(f"{tit:40} {idioma:15} {clasificacao:20}")

def listar_poa():
    titulo("Listagem dos Filmes em Porto Alegre")
    print("\nTitulo do Filme.........................: Idioma.......: Classificação....:")
    print("-"*62)
    for filme in portoAlegre:
        tit = filme["titulo"]
        idioma = filme["idioma"]
        clasificacao = filme["clasificacao"]
        print(f"{tit:40} {idioma:15} {clasificacao:20}")

# Exclusivos de cada cidade

# def exclusivos():
#     exclusivos = pelotas or portoAlegre
#     titulo("Listagem dos Filmes exclusivos")
#     print("\nTitulo do Filme.........................: Idioma.......: Classificação....:")
#     print("-"*62)
#     for i in exclusivos:
#         for i["titulo"] ^ i
#         tit = i["titulo"]
#         idioma = i["idioma"]
#         clasificacao = i["clasificacao"]
#         print(f"{tit:40} {idioma:15} {clasificacao:20}")

# exclusivos()