import datetime


funcionarios = []

def cadastrar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    cpf = input("Digite o CPF do funcionário: ")

    for funcionario in funcionarios:
        if funcionario['cpf'] == cpf:
            print("CPF já cadastrado.")
            return False

    funcionario = {'nome': nome, 'cpf': cpf, 'abertura_ponto': None, 'fechamento_ponto': None}
    funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso.")
    return True

def remover_funcionario():
    cpf = input("Digite o CPF do funcionário a ser removido: ")

    for funcionario in funcionarios:
        if funcionario['cpf'] == cpf:
            funcionarios.remove(funcionario)
            print("Funcionário removido com sucesso.")
            return True

    print("Funcionário não encontrado.")
    return False

def atualizar_funcionario():
    cpf = input("Digite o CPF do funcionário a ser atualizado: ")

    for funcionario in funcionarios:
        if funcionario['cpf'] == cpf:
            nome = input("Digite o novo nome do funcionário: ")
            funcionario['nome'] = nome
            print("Dados do funcionário atualizados com sucesso.")
            return True

    print("Funcionário não encontrado.")
    return False

def abrir_ponto():
    cpf = input("Digite o CPF do funcionário para abrir o ponto: ")

    for funcionario in funcionarios:
        if funcionario['cpf'] == cpf:
            if funcionario['abertura_ponto'] is not None:
                print("Ponto já aberto para esse funcionário.")
                return False
            else:
                funcionario['abertura_ponto'] = datetime.now()
                print("Ponto aberto com sucesso.")
                return True

    print("Funcionário não encontrado.")
    return False

def fechar_ponto():
    cpf = input("Digite o CPF do funcionário para fechar o ponto: ")

    for funcionario in funcionarios:
        if funcionario['cpf'] == cpf:
            if funcionario['fechamento_ponto'] is not None:
                print("Ponto já fechado para esse funcionário.")
                return False
            else:
                funcionario['fechamento_ponto'] = datetime.now()
                print("Ponto fechado com sucesso.")
                return True

    print("Funcionário não encontrado.")
    return False

def filtrar_funcionarios():
    filtro = input("Digite o nome ou CPF do funcionário a ser filtrado: ")

    resultados = []
    for funcionario in funcionarios:
        if filtro.lower() in funcionario['nome'].lower() or filtro == funcionario['cpf']:
            resultados.append(funcionario)

    if resultados:
        print("Funcionários encontrados:")
        for funcionario in resultados:
            print(f"Nome: {funcionario['nome']}, CPF: {funcionario['cpf']}")
    else:
        print("Nenhum funcionário encontrado.")

def zerar_pontos():
    for funcionario in funcionarios:
        funcionario['abertura_ponto'] = None
        funcionario['fechamento_ponto'] = None

while True:
    print("\nBem-vindo ao Sistema de Funcionários da Empresa!")
    print("1 - Cadastrar Funcionário")
    print("2 - Remover Funcionário")
    print("3 - Atualizar Funcionário")
    print("4 - Visualizar Todos os Funcionários")
    print("5 - Filtrar Funcionários")
    print("6 - Abrir Ponto Eletrônico")
    print("7 - Fechar Ponto Eletrônico")
    print("8 - Zerar Ponto Eletrônico")
    print("9 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_funcionario()
    elif opcao == '2':
        remover_funcionario()
    elif opcao == '3':
        atualizar_funcionario()
    elif opcao == '4':
        print("Lista de Funcionários:")
        for funcionario in funcionarios:
            print(f"Nome: {funcionario['nome']}, CPF: {funcionario['cpf']}")
    elif opcao == '5':
        filtrar_funcionarios()
    elif opcao == '6':
        abrir_ponto()
    elif opcao == '7':
        fechar_ponto()
    elif opcao == '8':
        zerar_pontos()
    elif opcao == '9':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Digite novamente.")

