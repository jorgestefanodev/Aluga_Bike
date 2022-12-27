# Importações -----------------------------------------------
from sqlalchemy_utils import create_database, database_exists

# Cria Banco de Dados caso não exista -----------------------
url = "mysql+mysqlconnector://root@localhost/alugabike"
if not database_exists(url): create_database(url)
