from datetime import datetime

def main():

    print("--- SISTEMA DE CHAMADOS | HELPDESK ---")

    solicitante = input("Digite o seu nome: ")
    setor = input("Digite o setor solicitante: ")

    total_chamados = 0
    op = ""
    sair = "nao"

    while op != "7" and sair == "nao":
        print("\n======================")
        print("SELECIONE SUA OPÇÃO:")
        print("1 - Hardware")
        print("2 - Software")
        print("3 - Redes e Internet")
        print("4 - Acesso e Permissões")
        print("5 - Outros")
        print("6 - Solicitar novamente os dados")
        print("7 - Sair")
        print("======================")

        op = input("Digite sua opção: ")

        if op == "1":
            categoria = "Hardware"
        elif op == "2":
            categoria = "Software"
        elif op == "3":
            categoria = "Redes e Internet"
        elif op == "4":
            categoria = "Acesso e Permissões"
        elif op == "5":
            categoria = "Outros"
        else:
            categoria = ""

        if categoria != "":
            descricao = input("Descreva brevemente o problema: ")
            total_chamados = total_chamados + 1
            data_abertura = datetime.now().strftime("%d/%m/%Y %H:%M")

            print("\n--- Chamado Registrado com Sucesso! ---")
            print("Solicitante:", solicitante, "(" + setor + ")")
            print("Categoria:", categoria)
            print("Descrição:", descricao)
            print("Aberto em:", data_abertura)
            print("Status: Aberto")

            while True:
                continua = input("\nDeseja abrir outro chamado (s/n)? ").upper()
                if continua == "S" or continua == "SIM":
                    break
                elif continua == "N" or continua == "NAO" or continua == "NÃO":
                    sair = "sim"
                    op = "7"
                    break
                else:
                    print("Entrada inválida! Responda S ou N.")

        elif op == "6":
            solicitante = input("Digite o seu nome: ")
            setor = input("Digite o setor solicitante: ")

        elif op == "7":
            pass

        else:
            print("Opção inválida! Digite um número de 1 a 7.")

    print("\nFIM DO PROGRAMA!")
    print("Chamados abertos:", total_chamados)


if __name__ == "__main__":
    main()
