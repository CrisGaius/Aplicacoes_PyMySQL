from time import sleep
from emoji import emojize
from datetime import datetime
import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='pwd',
                             database='dbname',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:

        print('-=' * 15)
        print(' ' * 10, 'CADASTRO')
        print('-=' * 15, '\n')

        opcao = 0
        qtdClientes = 1
        qtdFuncionarios = 1
        qtdProdutos = 1

        while True:
            print(emojize('''MENU
[1] PARA CADASTRAR CLIENTES :department_store:
[2] PARA CADASTRAR FUNCIONÁRIOS :man:
[3] PARA CADASTRAR PRODUTOS :package:
[4] PARA IR PARA O PROGRAMA DE CONSULTA :magnifying_glass_tilted_left:'''))
            opcao = int(input('Digite a opção desejada: '))

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
                opcao = int(input('Digite a opção desejada: '))

            if opcao == 1:
                print('')
                print('-' * 86)
                nomeCliente = str(input(f'Digite o nome da {qtdClientes}ª empresa: ')).strip().title()
                pais = str(input(f'Digite o país da {qtdClientes}ª empresa: ')).strip().title()
                codCliente = int(input(f'Digite o código da {qtdClientes}ª empresa: '))
                dataDoCadastro = datetime.now()

                insert_clientes = "INSERT INTO clientes (CodigoDoCliente, NomeDaEmpresa, Pais, DataDoCadastro) VALUES (%s, %s, %s, %s)"
                cursor.execute(insert_clientes, (codCliente, nomeCliente, pais, dataDoCadastro))
                connection.commit()

                print(emojize(f'\033[32m{qtdClientes}ª EMPRESA CADASTRADA!\033[m :check_mark_button:'))
                print('-' * 86)
                print('')

                qtdClientes += 1

            elif opcao == 2:
                print('')
                print('-' * 86)
                nomeFunc = str(input(f'Digite o nome do {qtdFuncionarios}º funcionário: ')).strip().title()
                codFunc = int(input(f'Digite o código do {qtdFuncionarios}º funcionário: '))
                dataDoCadastro = datetime.now()

                insert_funcionarios = "INSERT INTO funcionarios (CodigoDoFuncionario, Nome, DataDoCadastro) VALUES (%s, %s, %s)"
                cursor.execute(insert_funcionarios, (codFunc, nomeFunc, dataDoCadastro))
                connection.commit()

                print(emojize(f'\033[32m{qtdFuncionarios}º FUNCIONÁRIO CADASTRADO!\033[m :check_mark_button:'))
                print('-' * 86)
                print('')

                qtdFuncionarios += 1

            elif opcao == 3:
                print('')
                print('-' * 86)
                nomeProd = str(input(f'Digite o nome do {qtdProdutos}º produto: ')).strip().title()
                qtdEstoque = int(input(f'Digite a quantidade de {nomeProd} em estoque: '))
                codigoDoProduto = int(input(f'Digite o código do {qtdProdutos}º produto: '))
                dataDoCadastro = datetime.now()

                insert_produtos = "INSERT INTO Produtos (CodigoDoProduto, NomeDoProduto, QuantidadeEmEstoque, DataDoCadastro) VALUES (%s, %s, %s, %s)"
                cursor.execute(insert_produtos, (codigoDoProduto, nomeProd, qtdEstoque, dataDoCadastro))
                connection.commit()

                print(emojize(f'\033[32m{qtdProdutos}º PRODUTO CADASTRADO!\033[m :check_mark_button:'))
                print('-' * 86)
                print('')

                qtdProdutos += 1
                
            else:
                break

        print('\nINDO PARA O PROGRAMA DE CONSULTA', end='')

        for i in range(3):
            print('.', end='')
            sleep(1)

        print('')
        print('')

        print('-=' * 15)
        print(' ' * 10, 'CONSULTA')
        print('-=' * 15, '\n')

        opcao = 0

        while True:
            print(emojize('''MENU
[1] PARA CONSULTAR CLIENTES :department_store:
[2] PARA CONSULTAR FUNCIONÁRIOS :man:
[3] PARA CONSULTAR PRODUTOS :package:
[0] PARA SAIR :stop_sign:'''))
            opcao = int(input('Digite a opção desejada: '))

            while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 0:
                opcao = int(input('Digite a opção desejada: '))

            if opcao == 1:
                select_clientes = "SELECT * FROM clientes"
                cursor.execute(select_clientes)
                result = cursor.fetchall()

                print('')
                print('-' * 140)

                for i in range(len(result)):
                    print(f'\033[32mCódigo do cliente: {result[i]["CodigoDoCliente"]} | Nome da empresa: {result[i]["NomeDaEmpresa"]} | País: {result[i]["Pais"]} | Data do cadastro: {result[i]["DataDoCadastro"]}\033[m')
                
                print('-' * 140)
                print('')
                
            elif opcao == 2:
                select_funcionarios = "SELECT * FROM funcionarios"
                cursor.execute(select_funcionarios)
                result = cursor.fetchall()

                print('')
                print('-' * 140)

                for i in range(len(result)):
                    print(f'\033[32mCódigo do funcionário: {result[i]["CodigoDoFuncionario"]} | Nome: {result[i]["Nome"]} | Data do cadastro: {result[i]["DataDoCadastro"]}\033[m')

                print('-' * 140)
                print('')

            elif opcao == 3:
                select_produtos = "SELECT * FROM produtos"
                cursor.execute(select_produtos)
                result = cursor.fetchall()

                print('')
                print('-' * 140)

                for i in range(len(result)):
                     print(f'\033[32mCódigo do produto: {result[i]["CodigoDoProduto"]} | Nome do produto: {result[i]["NomeDoProduto"]} | Quantidade em estoque: {result[i]["QuantidadeEmEstoque"]} | Data do cadastro: {result[i]["DataDoCadastro"]}\033[m')

                print('-' * 140)
                print('')
                
            else:
                break

        print('\nSAINDO DO PROGRAMA DE CONSULTA', end='')

        for i in range(3):
            print('.', end='')
            sleep(1)