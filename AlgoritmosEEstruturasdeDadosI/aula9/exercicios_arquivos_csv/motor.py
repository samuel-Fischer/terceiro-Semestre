import csv
accidnts = []

def carrega_dados():
    with open('motor2.csv', mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for linha in csv_reader:
            accidnts.append(linha)

def titulo(texto, sublinhado="-"):
    print()
    print(texto)
    print(sublinhado*40)

def sobre_ano():
    titulo("Nº Acidentes por ano")
    dicionario = {}

    for accidnt in accidnts:
        ano = dicionario.get(accidnt['CRASH DATE'][-4:], None)

        if ano == None:
            dicionario[accidnt['CRASH DATE'][-4:]] = 1
        else:
            dicionario[accidnt['CRASH DATE'][-4:]] = ano + 1

    lista = sorted(dicionario.items(), key=lambda dic : dic[1], reverse=True)
    
    print("\nAno                       Nº de Acidentes")
    for (ano, num) in lista:
        print(f"{ano:30} {num}")
        

def sobre_bairro():
    titulo("Nº Acidentes por Bairro")
    dicionario = {}
    outros = 0

    for accidnt in accidnts:
        bairro = dicionario.get(accidnt['BOROUGH'], None)

        if accidnt['BOROUGH'] != "":
            if bairro == None:
                dicionario[accidnt['BOROUGH']] = 1
            else:
                dicionario[accidnt['BOROUGH']] = bairro + 1
        else:
            outros += 1

    lista = sorted(dicionario.items(), key=lambda dic : dic[1], reverse=True)

    print("\nBairro                     Nº de Acidentes")
    for (bairro, num) in lista:
        print(f"{bairro:30} {num}")
    print(f"Outros {'':24}{outros}")

def sobre_classe():
    titulo("Nº Acidentes: Bikes, Ônibus e Sedans")
    bikes = 0
    onibus = 0
    sedans = 0
    outros = 0

    for accidnt in accidnts:
        if accidnt['VEHICLE TYPE CODE 1'] == "Bike":
            bikes += 1
        elif accidnt['VEHICLE TYPE CODE 1'] == "Bus":
            onibus += 1
        elif accidnt['VEHICLE TYPE CODE 1'] == "Sedan":
            sedans += 1
        elif accidnt['VEHICLE TYPE CODE 1'] != "":
            outros += 1

        if accidnt['VEHICLE TYPE CODE 2'] == "Bike":
            bikes += 1
        elif accidnt['VEHICLE TYPE CODE 2'] == "Bus":
            onibus += 1
        elif accidnt['VEHICLE TYPE CODE 2'] == "Sedan":
            sedans += 1
        elif accidnt['VEHICLE TYPE CODE 2'] != "":
            outros += 1

        if accidnt['VEHICLE TYPE CODE 3'] == "Bike":
            bikes += 1
        elif accidnt['VEHICLE TYPE CODE 3'] == "Bus":
            onibus += 1
        elif accidnt['VEHICLE TYPE CODE 3'] == "Sedan":
            sedans += 1
        elif accidnt['VEHICLE TYPE CODE 3'] != "":
            outros += 1

        if accidnt['VEHICLE TYPE CODE 4'] == "Bike":
            bikes += 1
        elif accidnt['VEHICLE TYPE CODE 4'] == "Bus":
            onibus += 1
        elif accidnt['VEHICLE TYPE CODE 4'] == "Sedan":
            sedans += 1
        elif accidnt['VEHICLE TYPE CODE 4'] != "":
            outros += 1
        
        if accidnt['VEHICLE TYPE CODE 5'] == "Bike":
            bikes += 1
        elif accidnt['VEHICLE TYPE CODE 5'] == "Bus":
            onibus += 1
        elif accidnt['VEHICLE TYPE CODE 5'] == "Sedan":
            sedans += 1
        elif accidnt['VEHICLE TYPE CODE 5'] != "":
            outros += 1
        
    print(f"Bikes: {bikes}")
    print(f"Ônibus: {onibus}")
    print(f"Sedans: {sedans}")
    print(f"Outros: {outros}")


def sobre_pessoas():
    num_pessoas_feridas = 0
    num_pessoas_mortas = 0
    num_pedestres_feridos = 0
    num_pedestres_mortos = 0
    num_ciclistas_feridos = 0
    num_ciclistas_mortos = 0
    num_motoristas_feridos = 0
    num_motoristas_mortos = 0
    num_pessoas_envolvidas = 0

    for accidnt in accidnts:
        num_pessoas_feridas += int(accidnt['NUMBER OF PERSONS INJURED'])
        num_pessoas_mortas += int(accidnt['NUMBER OF PERSONS KILLED'])
        num_pedestres_feridos += int(accidnt['NUMBER OF PEDESTRIANS INJURED'])
        num_pedestres_mortos += int(accidnt['NUMBER OF PEDESTRIANS KILLED'])
        num_ciclistas_feridos += int(accidnt['NUMBER OF CYCLIST INJURED'])
        num_ciclistas_mortos += int(accidnt['NUMBER OF CYCLIST KILLED'])
        num_motoristas_feridos += int(accidnt['NUMBER OF MOTORIST INJURED'])
        num_motoristas_mortos += int(accidnt['NUMBER OF MOTORIST KILLED'])
        num_pessoas_envolvidas += int(accidnt['NUMBER OF PERSONS INJURED']) + int(accidnt['NUMBER OF PERSONS KILLED'])

    print(f"Nº de pessoas envolvidas: {num_pessoas_envolvidas}")
    print(f"Nº de pessoas feridas: {num_pessoas_feridas}")
    print(f"Nº de pessoas mortas: {num_pessoas_mortas}")
    print(f"\nNº de pedestres feridos: {num_pedestres_feridos}")
    print(f"Nº de pedestres mortos: {num_pedestres_mortos}")
    print(f"\nNº de ciclistas feridos: {num_ciclistas_feridos}")
    print(f"Nº de ciclistas mortos: {num_ciclistas_mortos}")
    print(f"\nNº de motoristas feridos: {num_motoristas_feridos}")
    print(f"Nº de motoristas mortos: {num_motoristas_mortos}")



carrega_dados()

while True:
    titulo("Estatísticas: Passageiros do Titanic")    
    print("1. Nº Acidentes por ano")
    print("2. Nº Acidentes agrupados por bairro")
    print("3. Nº Acidentes Bikes, Ônibus e Sedans")
    print("4. Nº Acidentes envolvendo pessoas")
    print("5. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        sobre_ano()
    elif opcao == 2:
        sobre_bairro()
    elif opcao == 3:
        sobre_classe()
    elif opcao == 4:
        sobre_pessoas()
    else: 
        break
