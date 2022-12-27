# Aluga_Bike
App criado em Python, interface com TKINTER e banco de dados SQLAlchemy

##

Projeto desenvolvido para testar conhecimentos adquiridos no Curso de Dev Full Stack
da Infinity School.

Tem as seguintes funcionalidades:

- Login
- Cadastro de Novo Cliente
- Alteração de dados do cliente
- Lista todos os clientes cadastrados
- Exclui cliente atráves do CPF
- Alugar (altera o status nos dados do cliente: nenhuma bike para o nome da bike alugada)
- Devolver (altera o status nos dados do cliente: Alguma bike para nenhuma)
- Acompanhamento (Lista todos os clientes com bike alugada)
- Exclui cliente atráves do CPF


- Possui um Banco de Dados MYSQL, utilizando o SQLALCHEMY com uma tabela:		
	- Clientes (Cpf, nome, email e telefone, tipo de cliente(mensalista ou avulso e bicicleta)

Como usuar o app:
- Instalar um servidor (Wampserver ou Xamp, etc e executar)
- Instalar as dependências com  pip install -r requirements.txt
- Executar o arquivo criando_BD.py para criar o Banco de dados
- Executar o arquivo CriarTabelaBD.py para criar a tabela Clientes
- Executar o arquivo app.py (arquivo principal)
- Usar login: admin e senha: admin
