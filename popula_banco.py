import sqlite3

# Produtos para popular
produtos = [
    (1, 'Pen Drive 32GB Sandisk', 10, 49.9),
    (2, 'Notebook Dell Inspiron 15', 5, 3899.9),
    (3, 'Smart TV LG 50 polegadas', 3, 2799.0),
    (4, 'Fone de Ouvido Bluetooth JBL', 20, 249.9),
    (5, 'Mouse Logitech M170', 15, 79.9),
    (6, 'Teclado Mecânico Redragon', 10, 229.9),
    (7, 'Caixa de Som JBL Flip 5', 8, 599.99),
    (8, "Monitor LG 24''", 6, 849.9),
    (9, 'Carregador Turbo USB-C', 25, 59.9),
    (10, 'Cabo HDMI 2.0 2m', 30, 29.9)
]

# Conectar ao banco de dados (ele será criado caso não exista)
conn = sqlite3.connect('mercado.db')
cursor = conn.cursor()

# Criar a tabela produtos (caso não exista)
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    estoque INTEGER NOT NULL,
    preco REAL NOT NULL
)
''')

# Limpar tabela produtos antes de inserir
cursor.execute('DELETE FROM produtos')

# Inserir os produtos
cursor.executemany('INSERT INTO produtos (id, nome, estoque, preco) VALUES (?, ?, ?, ?)', produtos)

# Confirmar as mudanças e fechar a conexão
conn.commit()
conn.close()

print("Banco populado com sucesso!")
