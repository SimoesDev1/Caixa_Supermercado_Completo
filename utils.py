from models import Produto, Session

def carregar_produtos(session):
    return session.query(Produto).all()

def buscar_produto(session, id_produto):
    return session.query(Produto).filter_by(id=id_produto).first()

def iniciar_atendimento(session, cliente_id):
    itens = []
    total = 0.0
    print(f"\n Iniciando atendimento - Cliente {cliente_id}")

    while True:
        id_input = input("Digite o ID do produto (ou 'fim' para encerrar): ")
        if id_input.lower() == 'fim':
            break

        try:
            id_produto = int(id_input)
            produto = buscar_produto(session, id_produto)

            if not produto:
                print(" Erro: produto não cadastrado.")
                continue

            qtd = int(input("Digite a quantidade: "))
            if qtd <= 0:
                print(" Erro: quantidade deve ser maior que zero.")
                continue

            if qtd > produto.estoque:
                print(" Erro: estoque insuficiente.")
                continue

            produto.estoque -= qtd  # Baixa no estoque
            preco_total = qtd * produto.preco
            item = [produto.id, produto.nome, qtd, produto.preco, preco_total]
            itens.append(item)
            total += preco_total

        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")
            continue

    gerar_nota_fiscal(itens, cliente_id)
    return itens, total

def gerar_nota_fiscal(itens, cliente_id):
    print(f"\n Nota Fiscal - Cliente {cliente_id}")
    print("{:<5} {:<30} {:<8} {:<10} {:<10}".format("ID", "Produto", "Qtd", "Preço", "Total"))

    for item in itens:
        print("{:<5} {:<30} {:<8} {:<10.2f} {:<10.2f}".format(*item))

    total = sum(item[4] for item in itens)
    print(f"\nTotal da compra: R$ {total:.2f}")

def resumo_final(clientes, total_vendas, session):
    print("\n Resumo Final do Caixa")
    print("\nClientes atendidos:")
    for cliente in clientes:
        print(f"Cliente {cliente[0]} - Total: R$ {cliente[1]:.2f}")

    print(f"\n Total de vendas: R$ {total_vendas:.2f}")

    print("\n Produtos sem estoque:")
    produtos = session.query(Produto).filter_by(estoque=0).all()
    for p in produtos:
        print(f"{p.id} - {p.nome}")
