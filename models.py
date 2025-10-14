from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    estoque = Column(Integer)
    preco = Column(Float)

    def __repr__(self):
        return f"<Produto(id={self.id}, nome='{self.nome}', estoque={self.estoque}, preco={self.preco})>"

# Conexão com o banco de dados SQLite
engine = create_engine('sqlite:///mercado.db')
Session = sessionmaker(bind=engine)

# Cria a tabela produtos caso não exista
Base.metadata.create_all(engine)
