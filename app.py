import os

restaurantes = [{'nome': 'Pizza', 'categoria': 'Italiana', 'ativo': False},
                {'nome': 'Sushi', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Hamburguer', 'categoria': 'Americana', 'ativo': True}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input('Digite a categoria do restaurante que deseja cadastrar: ')
    dados_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    for restaurante in restaurantes:
        #print(f'- {restaurante}')
        #print(f'- {restaurante["nome"]}')
        nomerestaurante = restaurante['nome']
        categorarestaurante = restaurante['categoria']
        ativorestaurante = restaurante['ativo']
        print(f'- {nomerestaurante} | {categorarestaurante}| {ativorestaurante}')        

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
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
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()