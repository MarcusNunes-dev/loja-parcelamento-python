print('Boas vindas à loja do Marcus Vinicius da Silva Nunes!') #Mensagem de boas vindas da loja

valorDoPedido = float(input('Digite o valor do pedido: ')) #Comando para que seja inserido o valor do pedido
quantidadeParcelas = int(input('Digite a quantidade de parcelas: ')) #Comando para que seja inserido a quantidade de parcelas

if quantidadeParcelas < 4:
    juros = 0 / 100 # Juros não é aplicado
elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = 4 / 100 # Juros aplicado de 4%
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = 8 / 100 # Juros aplicado de 8%
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    juros = 16 / 100 # Juros aplicado de 16%
else:
    juros = 32 / 100 # Juros aplicado de 32%


valorDaParcela = (valorDoPedido * (1 + juros) / quantidadeParcelas)
#Cálculo para se obter o valor da parcela, onde se multiplica o valor do pedido pelo juros (caso se aplique) e divide pela quantidade de parcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas
#Cálculo para se obter o valor total parcelado (valor final), onde se multiplica o valor da parcela (já com juros aplicado caso tenha) pela quantidade de parcelas selecionada

print(f'O valor da parcela é: R$ {valorDaParcela:.2f}') #Saída de console para o valor da parcela
print(f'O valor total parcelado é de: R$ {valorTotalParcelado:.2f}') #Saída de console para a o valor final total
