import os
import datetime


def limparTela():
    os.system("cls" if os.name == "nt" else "clear")


def exibe_mensagem_e_volta_menu(mensagem):
    print(mensagem)
    input("Pressione Enter para voltar...")


def depositar(saldo, deposito) -> float:
    """
    Adiciona o valor de depósito ao saldo.

    Args:
        saldo (float): Saldo atual.
        deposito (float): Valor a ser depositado.

    Returns:
        float: Novo saldo após depósito.
    """

    if deposito <= 0:
        raise ValueError("O valor do deposito não pode ser 0 ou negativo!")
    else:
        saldo += deposito
        return saldo


def sacar(saldo, saque) -> float:
    if saldo < saque or saque <= 0:
        raise ValueError(
            "verifique se tem saldo disponível, se não excedeu o saque diario ou se o valor do saque não é menor ou igual a 0!")
    else:
        saldo -= saque
        return saldo


def exibir_extrato(extrato, saldo, limite, numero_saque):
    print("="*30)
    print("       EXTRATO BANCÁRIO       ")
    print("="*30)

    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for i in extrato:
            print(i)

    print("-"*30)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print(f"Saques realizados: {numero_saque}/{limite}")
    print("="*30)
    input("Pressione Enter para voltar...")


def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saque = 0
    LIMITE_SAQUE = 3
    menu = """

MENU:

[ d ] - Depositar
[ s ] - Sacar
[ e ] - Extrato
[ q ] - Sair
                     
=> """

    while True:
        limparTela()

        opcao = input(menu).lower()
        match opcao:
            case "d":
                try:
                    limparTela()
                    valor_deposito = float(
                        input("Informe o valor a depositar: R$"))
                    saldo = depositar(saldo, valor_deposito)

                    data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                    extrato.append(
                        f"Depósito realizado de R$ {valor_deposito:.2f} às {data_atual}")
                except ValueError as e:
                    exibe_mensagem_e_volta_menu(f"Erro na operação: {e}")
            case "s":
                try:
                    limparTela()
                    if saldo <= 0:
                        exibe_mensagem_e_volta_menu(
                            "Sem saldo disponível para sacar.")
                        continue

                    valor_saque = float(
                        input("Digite o valor que deseja sacar: R$ "))
                    if numero_saque == LIMITE_SAQUE:
                        exibe_mensagem_e_volta_menu("Saque diário excedido")
                    elif valor_saque <= 0:
                        exibe_mensagem_e_volta_menu(
                            "Valor de saque inválido. Deve ser maior que zero.")
                    elif valor_saque > saldo:
                        exibe_mensagem_e_volta_menu("Saldo insuficiente.")
                    elif valor_saque > limite:
                        exibe_mensagem_e_volta_menu(
                            "Valor acima do limite permitido (R$ 500.00).")
                    else:
                        saldo = sacar(saldo, valor_saque)
                        numero_saque += 1

                        data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                        extrato.append(
                            f"Saque realizado de R$ {valor_saque:.2f} às {data_atual}")

                        exibe_mensagem_e_volta_menu(
                            f"Saque realizado de R$ {valor_saque:.2f}\nSaldo Atual: {saldo:.2f}\nSaques disponíveis hoje: {LIMITE_SAQUE - numero_saque}")

                except ValueError as e:
                    exibe_mensagem_e_volta_menu(f"Erro na operação: {e}")
            case "e":
                limparTela()
                exibir_extrato(extrato, saldo, LIMITE_SAQUE, numero_saque)
            case "q":
                limparTela()
                print("Sistema finalizado. Obrigado por utilizar nossos serviços!")
                break
            case _:
                limparTela()
                input("Opção inválida... Pressione Enter")


if __name__ == '__main__':
    main()
