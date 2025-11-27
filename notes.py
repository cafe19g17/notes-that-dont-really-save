import os
import platform

notes = []


def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def anotacoes():
    clear_terminal()
    print("'/' ler notas  |  '+' criar nota  |  '-' apagar nota  |  '*' apagar tudo")
    print("")

    option = input("opção: ")

    match option:
        case "/":
            clear_terminal()

            if notes == []:
                print("")
                print("Não há nenhuma nota aqui!")
                print("")

                comeback_to_menu = input("pressione 'f' para voltar para o menu: ")

                if comeback_to_menu == "f":
                    anotacoes()
            else:
                clear_terminal()

                for nota_lida in notes:
                    print("")
                    print(f"{nota_lida}")

                print("")
                print("")
                print("")
                comeback_to_menu = input("pressione 'f' para voltar para o menu: ")

                if comeback_to_menu == "f":
                    anotacoes()
        case "+":
            clear_terminal()
            print("")
            note = input("Nota: ")
            notes.append(note)
            print("")

            comeback_to_menu = input("pressione 'f' para voltar para o menu: ")

            if comeback_to_menu == "f":
                anotacoes()
        case "-":
            clear_terminal()
            notes.pop(0)
            print("Uma nota foi deletada!")
            print("")

            comeback_to_menu = input("pressione 'f' para voltar para o menu: ")

            if comeback_to_menu == "f":
                anotacoes()
        case "*":
            clear_terminal()
            notes.clear()
            print("Todas as notas foram deletadas!")
            print("")

            comeback_to_menu = input("pressione 'f' para voltar para o menu: ")

            if comeback_to_menu == "f":
                anotacoes()

    print("")
    print("")


clear_terminal()
anotacoes()
