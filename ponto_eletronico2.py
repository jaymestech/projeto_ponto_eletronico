#PONTO ELETRONICO VERSÃO 2: POR: JAYMES SOARES RIBEIRO
#IMPORTANTE :
#INSTALAR EM SUA MAQUINA AS BIBLIOTECAS:
#TABULATE : pip install tabulate
#LOCATE: pip install locate





import datetime
import json
from tabulate import tabulate
import locale


locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

# Caminho do arquivo JSON
arquivo_dados = 'dados_funcionarios.json'

# Lista para armazenar os funcionários
funcionarios = []

# Carregar dados de um arquivo JSON
def carregar_dados():
    try:
        with open(arquivo_dados, 'r') as file:
            dados = json.load(file)
            # Converter strings de volta em objetos datetime
            for funcionario in dados:
                if funcionario["horario_entrada"]:
                    funcionario["horario_entrada"] = datetime.datetime.fromisoformat(funcionario["horario_entrada"])
                if funcionario["horario_saida"]:
                    funcionario["horario_saida"] = datetime.datetime.fromisoformat(funcionario["horario_saida"])
            return dados
    except FileNotFoundError:
        return []
    
# Carregar dados dos funcionários ao iniciar o programa
funcionarios = carregar_dados()
    
# Salvar dados em um arquivo JSON
def salvar_dados(dados):
    # Converta os objetos datetime de volta para strings em formato ISO
    for funcionario in dados:
        if funcionario["horario_entrada"] and isinstance(funcionario["horario_entrada"], datetime.datetime):
            funcionario["horario_entrada"] = funcionario["horario_entrada"].isoformat()
        if funcionario["horario_saida"] and isinstance(funcionario["horario_saida"], datetime.datetime):
            funcionario["horario_saida"] = funcionario["horario_saida"].isoformat()

    # Salve os dados no arquivo
    with open(arquivo_dados, 'w') as file:
        json.dump(dados, file, indent=4)

# Função para adicionar um funcionário
def adicionar_funcionario(nome, cpf):
    # Verificar se já existe um funcionário com o mesmo CPF
    for funcionario in funcionarios:
        if funcionario["cpf"] == cpf:
            return False
    
    # Criar um novo funcionário e adicionar à lista
    funcionario = {"nome": nome, "cpf": cpf, "horario_entrada": None, "horario_saida": None}
    funcionarios.append(funcionario)
    return True

# Função para remover um funcionário
def remover_funcionario(nome):
    for funcionario in funcionarios:
        if funcionario["nome"] == nome:
            funcionarios.remove(funcionario)
            return True
    return False

# Função para atualizar os dados de um funcionário
def atualizar_funcionario(nome, novo_cpf):
    for funcionario in funcionarios:
        if funcionario["nome"] == nome:
            funcionario["cpf"] = novo_cpf
            return True
    return False

# Função para registrar o horário de entrada de um funcionário
def registrar_entrada(nome, horario_entrada):
    for funcionario in funcionarios:
        if funcionario["nome"] == nome:
            funcionario["horario_entrada"] = horario_entrada
            return True
    return False

# Função para registrar o horário de saída de um funcionário
def registrar_saida(nome, horario_saida):
    for funcionario in funcionarios:
        if funcionario["nome"] == nome:
            funcionario["horario_saida"] = horario_saida
            return True
    return False

# Função para filtrar funcionários por nome ou CPF
def filtrar_funcionario(consulta):
    resultado = []
    for funcionario in funcionarios:
        if consulta in funcionario["nome"] or consulta in funcionario["cpf"]:
            resultado.append(funcionario)
    return resultado

# Função para zerar os registros de ponto
def zerar_registros():
    for funcionario in funcionarios:
        funcionario["horario_entrada"] = None
        funcionario["horario_saida"] = None

## Função para exibir os funcionários
def exibir_funcionarios(lista_funcionarios):
    headers = ["Nome", "CPF", "Horário de Entrada", "Horário de Saída", "Tempo de Expediente"]
    table_data = []
    # Dentro da função exibir_funcionarios()
    for funcionario in lista_funcionarios:
        horario_entrada = ""
        horario_saida = ""
        duracao = ""
        if funcionario["horario_entrada"]:
            horario_entrada = funcionario["horario_entrada"].strftime("%d-%m-%Y %H:%M:%S")
        if funcionario["horario_saida"]:
            horario_saida = funcionario["horario_saida"].strftime("%d-%m-%Y %H:%M:%S")
            if funcionario["horario_entrada"]:
                duracao = funcionario["horario_saida"] - funcionario["horario_entrada"]
                dias, segundos = duracao.days, duracao.seconds
                horas = segundos // 3600
                minutos = (segundos % 3600) // 60
                segundos = (segundos % 60)
                duracao = f"{dias}d {horas}h {minutos}m {segundos}s"
        table_data.append([funcionario["nome"], funcionario["cpf"], horario_entrada, horario_saida, duracao])


    if not table_data:
        print("Nenhum funcionário foi cadastrado ainda. Por favor, cadastre um funcionário.")
    else:
        print(tabulate(table_data, headers, tablefmt="grid"))




def converter_horario(data_horario):
    formatos = ["%d-%m-%Y %H:%M:%S", "%d/%m/%Y %H:%M:%S", "%d-%m-%Y %H:%M", "%d/%m/%Y %H:%M"]
    for formato in formatos:
        try:
            return datetime.datetime.strptime(data_horario, formato)
        except ValueError:
            pass
    return None

def limpar_entrada_data(data_entrada):
    # Permite apenas números e os caracteres '/' e '-'
    caracteres_permitidos = set("0123456789/-: ")
    return ''.join(c for c in data_entrada if c in caracteres_permitidos).strip()

def exibir_mensagem(texto):
    print(tabulate([[texto]], tablefmt="grid"))

# Menu principal do programa
while True:
    print("""\n>>> Bem-vindo ao Sistema de Funcionários da Empresa! <<<
1 - Cadastrar Funcionário
2 - Remover Funcionário
3 - Atualizar Funcionário
4 - Visualizar Todos os Funcionários
5 - Filtrar Funcionários
6 - Registrar Entrada
7 - Registrar Saída
8 - Zerar Registros de Ponto
9 - Salvar Dados
10 - Sair""")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do funcionário: ")
        cpf = input("Digite o CPF do funcionário: ")
        if adicionar_funcionario(nome, cpf):
            exibir_mensagem("Funcionário cadastrado com sucesso!")
        else:
            exibir_mensagem("CPF já cadastrado!")

    elif opcao == "2":
        nome = input("Digite o nome do funcionário: ")
        if remover_funcionario(nome):
            exibir_mensagem("Funcionário removido com sucesso!")
        else:
            exibir_mensagem("Funcionário não encontrado!")

    elif opcao == "3":
        nome = input("Digite o nome do funcionário: ")
        novo_cpf = input("Digite o novo CPF do funcionário: ")
        if atualizar_funcionario(nome, novo_cpf):
            exibir_mensagem("Funcionário atualizado com sucesso!")
        else:
            exibir_mensagem("Funcionário não encontrado!")

    elif opcao == "4":
        exibir_funcionarios(funcionarios)

    elif opcao == "5":
        consulta = input("Digite o nome ou CPF do funcionário para filtrar: ")
        filtrados = filtrar_funcionario(consulta)
        exibir_funcionarios(filtrados)

    elif opcao == "6":
        nome = input("Digite o nome do funcionário: ")

        # Verifica se o nome do funcionário existe
        existe_funcionario = False
        for funcionario in funcionarios:
            if funcionario["nome"] == nome:
                existe_funcionario = True
                break

        # Se o funcionário existir, procede com o registro do horário
        if existe_funcionario:
            horario_entrada = input("Digite a data e horário de entrada (formato DD-MM-AAAA HH:MM:SS ou DD/MM/AAAA HH:MM:SS): ")
            horario_entrada = limpar_entrada_data(horario_entrada)
            horario = converter_horario(horario_entrada)
            if horario:
                if registrar_entrada(nome, horario):
                    exibir_mensagem("Horário de entrada registrado com sucesso!")
                    exibir_funcionarios(funcionarios)
                else:
                    exibir_mensagem("Funcionário não encontrado!")
            else:
                exibir_mensagem("Formato de data/horário inválido!")
        else:
            exibir_mensagem("Funcionário não encontrado. Por favor, tente novamente.")

    elif opcao == "7":
        nome = input("Digite o nome do funcionário: ")

        # Verifica se o nome do funcionário existe
        existe_funcionario = False
        for funcionario in funcionarios:
            if funcionario["nome"] == nome:
                existe_funcionario = True
                break

        # Se o funcionário existir, procede com o registro do horário
        if existe_funcionario:
            horario_saida = input("Digite a data e horário de saída (formato DD-MM-AAAA HH:MM:SS): ")
            horario_saida = limpar_entrada_data(horario_saida)
            horario = converter_horario(horario_saida)
            if horario:
                if registrar_saida(nome, horario):
                    exibir_mensagem("Horário de saída registrado com sucesso!")
                else:
                    exibir_mensagem("Funcionário não encontrado!")
            else:
                exibir_mensagem("Formato de data/horário inválido!")
        else:
            exibir_mensagem("Funcionário não encontrado. Por favor, tente novamente.")
            

    elif opcao == "8":
        zerar_registros()
        exibir_mensagem("Registros de ponto zerados com sucesso!")

   # Opção para salvar os dados manualmente
    elif opcao == "9":
        salvar_dados(funcionarios)
        exibir_mensagem("Dados salvos com sucesso!")

    # Opção para sair do programa
    elif opcao == "10":
        # Salvar os dados dos funcionários em um arquivo JSON antes de sair
        salvar_dados(funcionarios)
        exibir_mensagem("Saindo...")
        break