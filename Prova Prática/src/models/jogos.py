# Importação dos módulos necessários
from models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float

# Criação da classe Jogos que herda da classe Base
class Jogos(Base):
    __tablename__ = 'Jogos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    plataforma = Column(String)
    preço = Column(Float)
    quantidade = Column(Integer)

    def __repr__(self):
        return f"Jogos(id={self.id}, id={self.id}, nome={self.nome}, plataforma={self.plataforma}, preço={self.preço}, quantidade={self.quantidade})"
