import os

restaurantes = [{'nome': 'Pizza', 'categoria': 'Italiana', 'ativo': False},
                {'nome': 'Sushi', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Hamburguer', 'categoria': 'Americana', 'ativo': True}]

def exibir_nome_do_programa():
    '''Essa função é responsável por exibir o nome do programa'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    '''Essa função é responsável por exibir as opções do menu'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função é responsável por finalizar o programa'''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    '''Essa função é responsável por voltar ao menu principal 
    '''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    '''Essa função é responsável por exibir uma mensagem de opção inválida'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função é responsável por exibir um subtítulo'''
    os.system('cls')
    linha = '-' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    inputs     nome_do_restaurante: string
                categoria_do_restaurante: string
    outputs    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input('Digite a categoria do restaurante que deseja cadastrar: ')
    dados_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes cadastrados
    inputs     restaurantes: lista de dicionários
    outputs    '''
    exibir_subtitulo('Listando restaurantes')

    print(f'Nome do restaurante'.ljust(22) + '|' + 'Categoria'.ljust(22) + '|' + 'Ativo')
    for restaurante in restaurantes:
        #print(f'- {restaurante}')
        #print(f'- {restaurante["nome"]}')
        nomerestaurante = restaurante['nome']
        categorarestaurante = restaurante['categoria']
        ativorestaurante = restaurante['ativo']
        print(f'- {nomerestaurante}'.ljust(20) + '|' + f'{categorarestaurante}'.ljust(20) + '|' + f'{ativorestaurante}')

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    '''Essa função é responsável por ativar ou desativar um restaurante
    
    inputs     nome_do_restaurante: string
    outputs    estado: string
    '''
    exibir_subtitulo('Ativando ou desativando um restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja ativar ou desativar: ')
    for restaurante in restaurantes:
        if restaurante['nome'].lower() == nome_do_restaurante.lower():
            restaurante['ativo'] = not restaurante['ativo']
            estado = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'O restaurante {restaurante["nome"]} foi {estado} com sucesso!')
            break
    else:
        print(f'Não foi encontrado um restaurante com o nome {nome_do_restaurante}.')
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função é responsável por escolher a opção do menu
    inputs     opcao_escolhida: int
    outputs   '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Essa função é responsável por iniciar o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()