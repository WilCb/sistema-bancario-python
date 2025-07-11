import os
import datetime
import textwrap
from typing import Dict, List, Any
from validate_docbr import CPF

cpf = CPF()

"""
Nova função: Criar Usuário(Cliente)
informações: nome, data de nascimento, cpf e endereço(logradouro, n° - bairro - cidade/estado(sigla))
CPF: Somente com o número, não podendo ter o mesmo CPF já cadastrado anteriormente.
"""


def menu() -> str:
    limparTela()
    menu: str = f"""\n
    {"="*10} MENU {"="*10}
    [ d ]\tDepositar
    [ s ]\tSacar
    [ e ]\tExtrato
    [ nc ]\tNova conta
    [ lc ]\tListar contas
    [ nu ]\tNovo Usuário
    [ lu ]\tListar Usuários
    [ q ]\tSair
    => """

    return input(textwrap.dedent(menu)).lower().strip()


def limparTela() -> None:
    """
    Limpa o terminal, tanto no windows quando no linux.
    """
    os.system("cls" if os.name == "nt" else "clear")


def criar_usuario(lista: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    limparTela()
    print(f"{"=" * 10} Nova conta {"=" * 10}")
    nome: str = input("Nome: ")
    data_nascimento: int = int(
        input("Data de Nascimento(Somente número, ex: DDMMYYYY): ")
    )
    meu_cpf: str = input("CPF: ")
    # cpf_sem_mascara: str = meu_cpf.replace(
    #     '.', '').replace('-', '')
    # cpf_validacao: bool = cpf.validate(cpf_sem_mascara)
    cpf_encontrado: bool = False

    for usuario in lista:
        if meu_cpf in usuario['cpf']:
            cpf_encontrado = True
            break

    if cpf_encontrado:
        raise ValueError("CPF já cadastrado!")

    # elif not cpf_validacao:
    #     raise ValueError("CPF inválido!")

    logradouro: str = input("Logradouro: ")
    numero: str = input("Número: ")
    bairro: str = input("Bairro: ")
    cidade: str = input("Cidade: ")
    estado: str = input("Estado(Apenas sigla, ex: AL): ")
    endereco: Dict[str, str] = {
        "logradouro": logradouro,
        "numero": numero,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado,
    }

    novo_usuario: Dict[str, Any] = {
        "nome": nome,
        "data_nascimento": str(data_nascimento),
        "cpf": meu_cpf,
        "endereco": endereco
    }

    lista.append(novo_usuario)
    return lista


def listar_usuarios(dados: Dict[str, Any]) -> None:
    limparTela()
    if not dados:
        raise ValueError("Lista de usuário vazia")

    print("Lista de Clientes")
    for usuario in dados:
        cliente_cpf = cpf.mask(usuario['cpf'])
        print(f"""
                Nome: {usuario["nome"]}
                Data de Nascimento: {usuario['data_nascimento']}
                CPF: {cliente_cpf}
                Endereço: {usuario['endereco']['logradouro']}, {usuario['endereco']['numero']} - {usuario['endereco']['bairro']} - {usuario['endereco']['cidade']}/{usuario['endereco']['estado']}
        """)

        print('=-' * 30)

    input("Pressione Enter para voltar")


def exibe_mensagem_e_volta_menu(mensagem: str) -> None:
    limparTela()
    print(f"{mensagem}\n")
    input("Pressione Enter para voltar...")


def depositar(deposito: float, extrato: List[str], contas: List[Dict[str, Any]]) -> None:
    """
    Adiciona o valor de depósito ao saldo.

    Args:
        saldo (float): Saldo atual.
        deposito (float): Valor a ser depositado.

    Returns:
        float: Novo saldo após depósito.
    """
    buscar_conta = int(input("Número da conta: "))

    for conta in contas:
        if buscar_conta == conta["conta_corrente"]:    
            if deposito <= 0:
                raise ValueError("O valor do deposito não pode ser 0 ou negativo!")
            else:
                conta["saldo"] += deposito
                data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                extrato.append(
                    f"Depósito realizado de R$ {deposito:.2f} às {data_atual}"
                )


def sacar(saldo: float, saque: float, limite: int, extrato: List[str], contas: List[Dict[str, Any]]) -> None:

    buscar_conta = int(input("Número da conta: "))

    for conta in contas:
        if buscar_conta == conta["conta_corrente"]:    
            if conta["saldo"] < saque:
                raise ValueError(
                    f"O valor do saque excedeu seu saldo atual de R$ {saldo:.2f}!"
                )

            elif saque <= 0:
                raise ValueError("O valor do saque não pode ser menor ou igual a 0!")

            elif conta["saques"] >= 3:
                raise ValueError("Excedeu o saque diario permitido!")

            elif saque > limite:
                raise ValueError(f"Saque excedeu o limite permitido de R$ {limite}!")

            else:
                conta["saldo"] -= saque
                conta["saques"] += 1
                data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                extrato.append(f"Saque realizado de R$ {saque:.2f} às {data_atual}")


def exibir_extrato(extrato: List[str], saldo: float, limite: int, contas: List[Dict[str, Any]]) -> None:
    buscar_conta = int(input("Número da conta: "))

    for conta in contas:
        if conta["conta_corrente"] == buscar_conta:
            print("="*30)
            print("       EXTRATO BANCÁRIO       ")
            print("="*30)

            if not extrato:
                print("Nenhuma movimentação realizada.")
            else:
                for i in extrato:
                    print(i)

            print("-"*30)
            print(f"Saldo atual: R$ {conta["saldo"]:.2f}")
            print(f"Saques realizados: {conta["saques"]}/{limite}")
            print("="*30)
            input("Pressione Enter para voltar...")


def criar_conta(agencia: str, dados_conta: List[Dict[str, str]], dados_usuarios: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    limparTela()
    print("Criar conta corrente")

    cpf_usuario = input("Informe um CPF cadastrado: ").strip()
    cpf_encontrado = False

    for usuario in dados_usuarios:
        if cpf_usuario == usuario['cpf']:
            cpf_encontrado = True
            break

    if not cpf_encontrado:
        raise ValueError("CPF não encontrado!")

    if dados_conta:
        numero_conta_inicial = max(
            conta["conta_corrente"] for conta in dados_conta
        ) + 1
    else:
        numero_conta_inicial = 1

    conta_corrente = {
        "conta_corrente": numero_conta_inicial,
        "agencia": agencia,
        "cpf_vinculado": cpf_usuario,
        "saldo": 0.0,
        "saques": 0,
    }

    dados_conta.append(conta_corrente)
    return dados_conta


def listar_contas(dados: List[Dict[str, str]]) -> None:
    limparTela()
    print("Lista de contas cadastradas")
    for conta in dados:
        print(f"""
        CPF: {conta['cpf_vinculado']}
        Agência: {conta['agencia']}
        Conta corrente: {conta['conta_corrente']}
        Saldo: {conta["saldo"]:.2f}
        """)

    input("Enter para voltar...")


def main():
    LIMITE_SAQUE: int = int(3)
    AGENCIA: str = str("0001")

    saldo: float = float(0.0)
    limite: float = float(500.0)
    extrato: List[str] = []
    # numero_saques: int = int(0)
    usuarios: List[Dict[str, Any]] = []
    contas: List[Dict[str, str]] = []

    while True:
        opcao = menu()
        match opcao:
            case "d":
                try:
                    deposito: float = float(
                        input("Valor do deposito: ")
                    )
                    depositar(deposito, extrato, contas)
                except ValueError as e:
                    exibe_mensagem_e_volta_menu(
                        f"Erro: {e}. Pressione Enter para voltar")
            case "s":
                try:
                    saque: float = float(input("Valor do saque: R$ ").strip())
                    sacar(saldo, saque, limite, extrato, contas)
                except ValueError as e:
                    exibe_mensagem_e_volta_menu(
                        f"Erro: {e}. Pressione Enter para voltar"
                    )
            case "e":
                exibir_extrato(extrato, saldo, LIMITE_SAQUE, contas)
            case "nc":
                try:
                    criar_conta(AGENCIA, contas, usuarios)
                except ValueError as e:
                    exibe_mensagem_e_volta_menu(
                        f"Erro: {e}. Pressione Enter para voltar")
            case "lc":
                listar_contas(contas)
            case "nu":
                try:
                    criar_usuario(usuarios)
                except ValueError as e:
                    exibe_mensagem_e_volta_menu(
                        f"Erro: {e}. Pressione Enter para voltar")
            case "lu":
                listar_usuarios(usuarios)
            case "q":
                limparTela()
                print("Sistema finalizado. Obrigado por utilizar nossos serviços!")
                break
            case _:
                input("Opção inválida!")


if __name__ == '__main__':
    main()
