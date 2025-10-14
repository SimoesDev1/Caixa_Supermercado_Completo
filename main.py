from utils import carregar_produtos, iniciar_atendimento, resumo_final
from models import Session

def main():
    session = Session()
    clientes = []
    total_vendas = 0.0
    cliente_id = 1

    print(" Caixa aberto.")

    while True:
        print("\n1 - Iniciar atendimento")
        print("2 - Fechar caixa")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            _, total_cliente = iniciar_atendimento(session, cliente_id)
            clientes.append([cliente_id, total_cliente])
            total_vendas += total_cliente
            cliente_id += 1
        elif opcao == "2":
            session.commit()
            resumo_final(clientes, total_vendas, session)
            session.close()
            print(" Caixa fechado.")
            break
        else:
            print(" Opção inválida.")

if __name__ == "__main__":
    main()
