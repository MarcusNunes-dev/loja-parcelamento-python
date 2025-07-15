# 💳 Loja com Cálculo de Parcelamento

Este projeto simula o sistema de pagamento parcelado de uma loja, com aplicação de juros conforme a quantidade de parcelas.

## 🚀 Como funciona

O usuário informa:
- O **valor do pedido**
- A **quantidade de parcelas**

O programa calcula o valor de cada parcela e o valor total a ser pago, aplicando as regras de juros abaixo:

| Parcelas             | Juros Aplicado |
|----------------------|----------------|
| Até 3 parcelas       | 0%             |
| De 4 a 5 parcelas    | 4%             |
| De 6 a 8 parcelas    | 8%             |
| De 9 a 12 parcelas   | 16%            |
| 13 parcelas ou mais  | 32%            |

## 📌 Exemplo de uso

```bash
Digite o valor do pedido: 1000
Digite a quantidade de parcelas: 6
O valor da parcela é: R$ 180.00
O valor total parcelado é de: R$ 1080.00
🛠️ Tecnologias
Python 3.x

👨‍💻 Autor
Marcus Vinicius da Silva Nunes
GitHub - MarcusNunes-dev
