# Documento base para a criação das tabelas. É o arquivo em que se encontra o banco de dados.

from sqlalchemy.orm import DeclarativeBase # ORM é o módulo que contém as classes

class Base(DeclarativeBase): # DeclarativeBase é a classe-mãe da classe Base. Assim, Base traz todas as suas características.
    pass