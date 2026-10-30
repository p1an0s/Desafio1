
def descontos(serDescontado, valorCompra):
    valor = valorCompra * (serDescontado / 100)
    return valor


continuar = 1

resumoDia = []
comprasFeitas = 0

totalBruto = []
totalDescontos = 0
numDescontos = 0
totalFinal = []

while continuar != 0:
    print("--- Digite o valor da compra em Reais: ---")
    valor_Compra = float(input())

    while valor_Compra < 0:
        print("Valor inválido. Digite um valor positivo:")
        valor_Compra = float(input())

    totalBruto.append(valor_Compra)

    print("--- Digite a idade do cliente ---")
    idadeCliente = int(input())

    while idadeCliente < 0:
        print("Idade inválida. Por favor, insira uma idade válida.")
        idadeCliente = int(input())

    comprasFeitas += 1
    valorFinal = valor_Compra

    match idadeCliente:
        case idade if idade >= 65:
            desconto = descontos(20, valor_Compra)
            valorFinal -= desconto
            numDescontos += 1

            if valorFinal > 100:
                desconto = descontos(10, valorFinal)
                valorFinal -= desconto
                numDescontos += 1

        case idade if idade < 65:
            if valor_Compra > 100:
                desconto = descontos(10, valor_Compra)
                valorFinal -= desconto
                numDescontos += 1

    totalFinal.append(valorFinal)

    print(f"Valor final: R$ {valorFinal:.2f}")

    print("=== Digite 1 para continuar ou 0 para sair ===")
    continuar = int(input())

resumoDia.append(comprasFeitas)
totalDescontos = numDescontos

print("\n===== RESUMO DO DIA =====")
print(f"Compras realizadas: {comprasFeitas}")
print(f"Total bruto: R$ {sum(totalBruto):.2f}")
print(f"Descontos aplicados até agora: {numDescontos}")
print(f"Total final das compras: R$ {sum(totalFinal):.2f}")
print(f"Resumo das compras: {resumoDia}")
