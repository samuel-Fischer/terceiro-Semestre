# Arquivo .csv utilizado: https://www.kaggle.com/datasets/kaggle/us-baby-names?resource=download&select=StateNames.csv

import csv
babys = []

def loaded_data():
    with open('StateNames.csv', mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for linha in csv_reader:
            babys.append(linha)

def title(texto, sublinhado="-"):
    print()
    print(texto)
    print(sublinhado*40)

def general():
    title("Dados Gerais")
    dictionary_year = {}
    dictionary_state = {}
    babyF = 0
    babyM = 0

    for baby in babys:
        year = dictionary_year.get(baby['Year'], None)
        state = dictionary_state.get(baby['State'], None)

        if baby['Gender'] == 'F':
            babyF += 1
        else:
            babyM += 1

        if year == None:
            dictionary_year[baby['Year']] = 1
        else:
            dictionary_year[baby['Year']] = year + 1
        
        if state == None:
            dictionary_state[baby['State']] = 1
        else:
            dictionary_state[baby['State']] = state + 1

    list_year = sorted(dictionary_year.items(), key=lambda dic : dic[1], reverse=True)
    list_state = sorted(dictionary_state.items(), key=lambda dic : dic[1], reverse=True)

    print(f"Total de Bebês: {len(babys)}")
    print(f"Nº de bebês Masculinos: {babyM}")
    print(f"Nº de bebês Femininos: {babyF}")

    years = [list_year[i][:4] for i in range(len(list_year))]
    smallest = min(years)
    larger = max(years)

    print(f"\nNumero de bebês de {smallest[0]} a {larger[0]}:")
    print("Ano   Nº de Bebês")
    for (year, num) in list_year:
        print(f"{year:10} {num}")

    print(f"\nNumero de bebês por Estado({len(dictionary_state)}):")
    print("Estado   Nº de Bebês")
    for (state, num) in list_state:
        print(f"{state:^6} {num}")

def compare():
    title("Comparar Nomes")
    name1 = input("Nome 1: ")
    name2 = input("Nome 2: ")
    cont1 = 0
    cont2 = 0

    for baby in babys:
        if baby['Name'].upper() == name1.upper():
            cont1 += 1
        elif baby['Name'].upper() == name2.upper():
            cont2 += 1
        
      
    print(f"\n{name1}: {cont1}")
    print(f"{name2}: {cont2}")
        
def frequency_names():
    dictionary = {}

    for baby in babys:
        name = dictionary.get(baby['Name'], None)

        if name == None:
            dictionary[baby['Name']] = 1
        else:
            dictionary[baby['Name']] = name + 1

    title("Nº de Bebês por Nome")
    lista = sorted(dictionary.items(), key=lambda dic : dic[1], reverse=True)[:20]
    print("\n Nº - Nome                       Nº de Bebês")
    for i, (name, num) in enumerate(lista, start=1):
        print(f"{i:3} - {name:30} {num}")
        
def info_name():
    title("Informações por Nome")
    name = input("Nome: ")
    cont1 = 0
    dictionary_year = {}
    dictionary_state = {}

    for baby in babys:
        year = dictionary_year.get(baby['Year'], None)
        state = dictionary_state.get(baby['State'], None)

        if baby['Name'].upper() == name.upper():
            cont1 += 1

            if year == None:
                dictionary_year[baby['Year']] = 1
            else:
                dictionary_year[baby['Year']] = year + 1
        
            if state == None:
                dictionary_state[baby['State']] = 1
            else:
                dictionary_state[baby['State']] = state + 1
    
    list_year = sorted(dictionary_year.items(), key=lambda dic : dic[1], reverse=True)[:5]
    list_state = sorted(dictionary_state.items(), key=lambda dic : dic[1], reverse=True)[:5]


    print(f"\nInformações sobre {name}.")
    print(f"Casos com o nome: {cont1}")
    print(f"\nFrequência por ano:")
    for i, (year, num) in enumerate(list_year, start=1):
        print(f"{i:3}ª - {year:10} {num}")
    print(f"\nFrequência por estado:")
    for i, (state, num) in enumerate(list_state, start=1):
        print(f"{i:3}ª - {state:12} {num}")


loaded_data()
while True:
    title("Nomes de Bebês")    
    print("1. Dados Gerais")
    print("2. Comparar Nomes")
    print("3. Frequência de Nomes")
    print("4. Informações por Nome")
    opcao = int(input("Opção: "))
    if opcao == 1:
        general()
    elif opcao == 2:
        compare()
    elif opcao == 3:
        frequency_names()
    elif opcao == 4:
        info_name()
    else: 
        break
