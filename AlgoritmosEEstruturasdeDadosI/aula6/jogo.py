NUM_LINHAS = 6
NUM_COLUNAS = 7

jogo = []

def cria_jogo():
  for i in range(NUM_LINHAS):
    jogo.append([])
    for _ in range (NUM_COLUNAS):
      jogo[i].append(" ")

def mostra_jogo():
  print()
  for i, linha in enumerate(jogo, start=1):
    print(f"{i} |" , end="")
    for casa in linha:
      print(f" {casa} ", end="")
    print("|")
  print("  +---------------------+")
  print("    1  2  3  4  5  6  7")

def linha_disponivel(coluna):
  disponivel = -1
  for i in range(NUM_LINHAS-1, -1, -1):
    if jogo[i][coluna] == " ":
      disponivel = i
      break
  return disponivel

def vencedor(simbolo):
  for l in range(NUM_LINHAS):
    for c in range(NUM_COLUNAS-3):
      if jogo [l][c]==simbolo and jogo [l][c+1]==simbolo and jogo [l][c+2]==simbolo and jogo [l][c+3]==simbolo:
        return True

  for l in range(NUM_LINHAS-3):
    for c in range(NUM_COLUNAS):
      if jogo [l][c]==simbolo and jogo [l+1][c]==simbolo and jogo [l+2][c]==simbolo and jogo [l+3][c]==simbolo:
        return True

  for l in range(NUM_LINHAS-3):
    for c in range(NUM_COLUNAS-3):
      if jogo [l][c]==simbolo and jogo [l+1][c+1]==simbolo and jogo [l+2][c+2]==simbolo and jogo [l+3][c+3]==simbolo:
        return True

  for l in range(NUM_LINHAS-1, NUM_COLUNAS-3, -1):
    for c in range(NUM_COLUNAS-3):
      if jogo [l][c]==simbolo and jogo [l-1][c+1]==simbolo and jogo [l-2][c+2]==simbolo and jogo [l-3][c+3]==simbolo:
        return True

cria_jogo()
mostra_jogo()

print("\nJogo Connect")
print("="*40)
print("informe um numero: ")

contador = 1

while True:
  jogador = "X" if contador % 2 == 1 else "O"

  coluna = int(input(f"\nJogador '{jogador}', informe a coluna: "))

  if coluna == 0 or coluna > NUM_COLUNAS:
    break

  linha = linha_disponivel(coluna-1)
  if linha == -1:
    print("coluna está cheia...")
  else:
    jogo[linha][coluna-1] = jogador
    contador += 1

  mostra_jogo()

  if vencedor(jogador):
    print()
    print("*"*40)
    print(f"Parabens Jogador '{jogador}': você é o vencedor!")
    print("*"*40)
    break
  
  if contador == NUM_LINHAS*NUM_COLUNAS:
    print()
    print("*"*40)
    print(f"Ah... Deu Empate")
    print("*"*40)
    break