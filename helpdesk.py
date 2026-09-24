def main():
    print("--- SISTEMA DE CHAMADOS | HELPDESK ---")

    # 1. Coleta de dados básicos do usuário
    solicitante = input("Digite o seu nome: ").strip()
    setor = input("Digite o seu setor: ").strip()

    # 2. Definição das opções de problemas (como strings textuais)
    opcoes_problema = ["Hardware", "Software", "Redes e Internet", "Acessos e Permissões"]

    # 3. Exibição das opções para o usuário escolher por número
    print("\nSelecione o tipo de problema:")
    for indice, tipo in enumerate(opcoes_problema, start=1):
        print(f"[{indice}] - {tipo}")

    # 4. Captura e validação da escolha do usuário
    try:
        escolha = int(input("\nDigite o número da opção desejada: "))
        # Ajusta o índice (ex: se o usuário digitar 1, pegamos o índice 0 da lista)
        tipo_selecionado = opcoes_problema[escolha - 1]
    except (ValueError, IndexError):
        print("Opção inválida! O chamado será categorizado como 'Outros'.")
        tipo_selecionado = "Outros"

    descricao = input("Descreva brevemente o problema: ").strip()

    # 5. Agrupando todas as variáveis do chamado em um Dicionário
    # Isso organiza os dados e facilita para salvar em arquivos depois!
    chamado = {
        "solicitante": solicitante,
        "setor": setor,
        "categoria": tipo_selecionado,
        "descricao": descricao,
        "status": "Aberto"
    }

    # Exibe o chamado final na tela para o usuário ver
    print("\n--- Chamado Registrado com Sucesso! ---")
    print(f"Solicitante: {chamado['solicitante']} ({chamado['setor']})")
    print(f"Categoria: {chamado['categoria']}")
    print(f"Descrição: {chamado['descricao']}")
    print(f"Status: {chamado['status']}")


if __name__ == "__main__":
    main()