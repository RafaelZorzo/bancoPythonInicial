menu = """ 
        MENU
1 - Extrato
2 - Saque
3 - Depósito
4 - Sair


"""
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3
saldo = 0
listaDepositos = []
listaSaques = []
limite = 500

while True:
    print(menu)
    opcao = int(input())
    match opcao:
        case 1:
            if extrato == "":
                print("Não foram realizadas movimentações")
            else:
                print(extrato)
        case 2:
                if(saldo == 0):
                     print("Não será possível sacar o dinheiro por falta de saldo")
                elif (numero_de_saques == LIMITE_DE_SAQUES):
                     print("Não será possível sacar o dinheiro, limite de saques atingindo.")
                else:
                    valor_saque = float(input("Informe o valor do saque\nR$"))
                    while (valor_saque  > 500) or (valor_saque >saldo) or (valor_saque  < 0):
                        valor_saque  = float(input("Informe um valor válido de saque\nR$")) 
                    print(f"Saque de R$ {valor_saque:.2f} feito com sucesso.")
                    saldo -= valor_saque
                    print(f"Saldo atual: R$ {saldo:.2f}")
                    numero_de_saques += 1 
                    print(f"Você possui {LIMITE_DE_SAQUES - numero_de_saques} saques restantes hoje")
                    extrato += f"Saque de R${valor_saque:.2f}\n"
        case 3:
                valor_deposito = float(input("Qual valor positivo será o depósito? \nR$"))
                while(valor_deposito < 0):
                     valor_deposito = float(input("Qual valor positivo será o depósito?\nR$"))
                print(f"Depósito de R$ {valor_deposito:.2f} feito com sucesso.")
                saldo += valor_deposito
                print(f"Saldo atual: R$ {saldo:.2f}")
                extrato += f"Depósito de R${valor_deposito:.2f}\n"
        case 4:
            break
        case default:
              print("Selecione a opção desejada")
        