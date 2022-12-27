#---------------------------------------------------------------------------------------
# CriarTabelaBD.py
#
# Este arquivo define a Engine do Banco de Dados conectando a um servidor.
# Aqui também são definidas a classe e suas ligações com a tabela no banco de dados. 
#---------------------------------------------------------------------------------------


#[Importações]--------------------------------------------
import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker


#[Criando Engine]------------------------------------------
engine = sqlalchemy.create_engine("mysql+mysqlconnector://root@localhost/alugabike")
# Criando a base de dados
Base = declarative_base()
# Criando sessão no banco de dados
SessaoBD = sessionmaker(bind=engine)


#[Definindo Tabela no BD]------------------------------
class Clientes(Base):
    __tablename__ = 'cliente'
    cpf = Column(String(20), nullable=False, primary_key=True)
    nome = Column(String(50))
    email = Column(String(50))
    telefone = Column(String(20))
    tipo = Column(String(20))
    bicicleta = Column(String(30))

#[Criando tabela no Banco de Dados]-------------------------
Base.metadata.create_all(engine)
