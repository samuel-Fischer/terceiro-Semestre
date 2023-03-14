# 5. Elaborar um programa para simular um parquímetro, o qual leia o valor de
# moedas depositado em um terminal de estacionamento rotativo. O programa deve
# informar o tempo de permanência do veículo no local e o troco (se existir). Se o
# valor for inferior ao tempo mínimo, exiba a mensagem: “Valor Insuficiente”.
# Considerar os valores/tempos do quadro ao lado (o máximo é 120 min):

valor = float(input("Valor: "))

if valor >= 3:
  print(f"Tempo de Permanência: 120min")
  print(f"Seu Troco é R$ {(valor - 3):.2f}.")
elif valor >=1.75:
  print(f"Tempo de Permanência: 60min")
  print(f"Seu Troco é R$ {(valor - 1.75):.2f}.")
elif valor >=1:
  print(f"Tempo de Permanência: 30min")
  print(f"Seu Troco é R$ {(valor - 1):.2f}.")
else:
  print(f"Valor Insuficiente")
  print(f"Seu Troco é R$ {valor:.2f}.")