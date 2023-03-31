# Importação dos módulos SQLAlchemy necessários
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

# Importação dos módulos criados
from models.base import Base
from models.jogos import Jogos

# Criação de sessão para uso do ORM
engine = create_engine("sqlite:///jogos.db", echo=True)

Session = sessionmaker(bind=engine) 
session = Session()

# Criação das tabelas através da engine instanciada
Base.metadata.create_all(engine)

# Armazenamento dos dados referentes aos jogos que serão inseridos na tabela
dead_space_remake = Jogos(
    nome="Dead Space Remake",
    plataforma="PS5",
    preço="350.00",
    quantidade="10",
)
forspoken = Jogos(
    nome="Forspoken",
    plataforma="PC",
    preço="299.00",
    quantidade="8",
)
dead_island_two = Jogos(
    nome="Dead Island 2",
    plataforma="PS5",
    preço="350.00",
    quantidade="10",
)
hogwarts_legacy = Jogos(
    nome="Hogwarts Legacy",
    plataforma="PC",
    preço="219.00",
    quantidade="7",
)
wild_hearts = Jogos(
    nome="Wild Hearts",
    plataforma="Xbox Series",
    preço="350.00",
    quantidade="7",
)
resident_evil_four = Jogos(
    nome="Resident Evil 4",
    plataforma="PS5",
    preço="289.00",
    quantidade="10",
)
the_legend_of_zelda = Jogos(
    nome="The Legend of Zelda: Tears of the Kingdom",
    plataforma="Switch",
    preço="359.00",
    quantidade="10",
)

# Inserção dos dados na tabela "jogos.db"
session.add_all([dead_space_remake, forspoken, dead_island_two, hogwarts_legacy, wild_hearts, resident_evil_four, the_legend_of_zelda])
session.commit()

# Query para visualização dos dados inseridos na tabela "jogos.db"
historico = select(Jogos).where(Jogos.nome.in_(["Dead Space Remake","Forspoken","Dead Island 2","Hogwarts Legacy","Wild Hearts","Resident Evil 4","The Legend of Zelda: Tears of the Kingdom"]))

for registro in session.scalars(historico):
    print(registro)