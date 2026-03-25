import os
import subprocess


def introducao():
    print('============= Sabor Express ===============')


def opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')


def finalizar_app():
    subprocess.call('cls', shell=True)
    print('Encerrando o Aplicativo\n')


def reboot_app():
    print("Opção inválida")
    input("Digite uma tecla para retornar ao menu inicial")
    main()


def escolher_opcao():
    try:
        selected_choice = int(input('Escolha uma opção: '))
        # selected_choice = int(selected_choice)

        # print(selected_choice == 1)
        # print(type(selected_choice))
        # print(type(1))

        if selected_choice == 1:
            print('Cadastrar Restaurante: ')
        elif selected_choice == 2:
            print('Listar Restaurante')
        elif selected_choice == 3:
            print('Ativar Restaurante')
        elif selected_choice == 4:
            finalizar_app()
        else:
            reboot_app()
    except:
        reboot_app()


def main():
    subprocess.call('cls', shell=True)
    introducao()
    opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
