# Sistema de Ponto de Venda (PDV) - Nível 1

## 1. O que o código faz

O programa consiste em um sistema de Ponto de Venda (PDV) desenvolvido em Python. Seu objetivo é registrar as compras realizadas durante o dia, calcular descontos de acordo com a idade do cliente e o valor da compra, apresentar o valor final de cada operação e gerar um resumo diário com a quantidade de compras, o total bruto, o número de descontos aplicados e o valor total após os descontos.

## 2. Como ele faz

O programa funciona seguindo as seguintes etapas:

1. Inicializa as variáveis responsáveis por armazenar os valores das compras, os totais e a quantidade de descontos aplicados.
2. Solicita ao usuário o valor da compra e verifica se ele é válido, impedindo a utilização de valores negativos.
3. Solicita a idade do cliente e verifica se ela é válida, impedindo idades negativas.
4. Verifica a idade do cliente para determinar qual desconto será aplicado:
   - **Clientes com 65 anos ou mais:** recebem 20% de desconto sobre o valor da compra.
   - **Clientes com menos de 65 anos:** recebem 10% de desconto caso o valor da compra seja superior a R$ 100,00.
5. Para clientes com 65 anos ou mais, depois de aplicar o primeiro desconto, o programa verifica se o valor restante ainda é superior a R$ 100,00. Caso seja, aplica mais 10% de desconto sobre esse valor.
6. Armazena os valores das compras e seus respectivos resultados em listas para realizar os cálculos do resumo.
7. Exibe o valor final da compra após a aplicação dos descontos.
8. Pergunta ao usuário se deseja registrar outra compra ou encerrar o programa.
9. Quando o usuário decide encerrar, o programa apresenta um resumo do dia contendo:
   - Quantidade de compras realizadas.
   - Total bruto das compras.
   - Quantidade de descontos aplicados.
   - Total final das compras após os descontos.
   - Lista com a quantidade de compras registradas.

## 3. Como rodar

Para executar o programa, é necessário ter o Python instalado no computador.

Abra o terminal dentro da pasta `nivel_1` e execute o seguinte comando:

```bash
python pdv.py
```