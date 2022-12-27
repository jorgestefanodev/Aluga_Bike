# ----------------------------------------------------
# regras_de_negocio.py.py
# 
# Este arquivo contém as regras de negócio da aplicação, ou  seja, as funções que executam as # operações escolhidas pelo usuário na interface.
# As funções trabalham instanciando classes do BD e acionando métodos do SQLAlchemy para #  
# manipular dados armazenados.
# ----------------------------------------------------


#[Importações]----------------------------------------
from CriarTabelaBD import Clientes, SessaoBD
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk


#[Funções]---------------------------------------------

def incluir_cliente(cpf:str, nome:str, email:str, telefone:str, tipo:str):
    '''Cadastra o cliente no Banco de Dados'''
    try:
        # Instanciando contato
        cliente = Clientes(cpf = cpf, nome = nome, email = email, telefone = telefone, tipo = tipo, bicicleta = 'Nenhuma')
        # Criando sessão no banco de dados
        sessao = SessaoBD()
        # Inserindo novo cliente no Banco de Dados
        sessao.add(cliente)
        sessao.commit()
        messagebox.showinfo (title='Confirmação Banco de Dados', message='Cliente adicionado com sucesso!')
    except:
         messagebox.showerror(title='Erro Banco de Dados', message='Erro ao adicionar cliente!')


def alterar_cliente(cpf:str, nome:str, email:str, telefone:str, tipo:str):
    '''Altera os dados do cliente no Banco de Dados'''
    try:
        # Criando uma sessao no banco de dados
        sessao = SessaoBD()
        # Recuperar o contato no banco de dados
        cliente = sessao.query(Clientes).filter_by(cpf=cpf).first()
        # Alterando dados do cliente
        cliente.nome = nome
        cliente.email = email
        cliente.telefone = telefone
        cliente.tipo = tipo
        sessao.commit()
        messagebox.showinfo (title='Alteração de Cadastro', message='Dados alterado com sucesso!')
    except:
        messagebox.showerror(title='Alteração de Cadastro', message='Erro ao alterar dados do cliente!')


def excluir_cliente(cpf:str):
    '''Exclui cliente do Banco de Dados'''
    try: 
        # Criando sessão no banco de dados
        sessao = SessaoBD()
        # Recuperandoo o contato no Banco de Dados
        cliente = sessao.query(Clientes).filter_by(cpf=cpf).first() 
        # Excluindo o contato recuperado
        sessao.delete(cliente)
        sessao.commit()
        messagebox.showinfo (title='Exclusão de Cliente', message='Cliente excluido com sucesso!')
    except:
         messagebox.showerror(title='Exclusão de Cliente', message= 'Erro ao excluir cliente!')


    try:
        global tree
        # criando uma sessão no banco de dados
        sessao = SessaoBD()
        # recuperando todos os contatos do banco de dados em uma lista
        clientes = sessao.query(Clientes)
        for resp in clientes:
            tree.insert('', tk.END, values=(resp.cpf, resp.nome, resp.tipo, resp.bicicleta))
    except:
        messagebox.showerror(title='Erro Listagem', message='Não foi possivel listar clientes')  


def aluguel(cpf:str, bicicleta:str):
    '''Aluga uma bibicleta alterando de Nenhuma para um modelo de bicicleta pre-cadastrada'''
    global cliente
    try:
        # Criando uma sessao no banco de dados
        sessao = SessaoBD()
        # Recuperar o contato no banco de dados
        cliente = sessao.query(Clientes).filter_by(cpf=cpf).first()
        # Alterando dados do cliente
        cliente.bicicleta = bicicleta
        sessao.commit()
        messagebox.showinfo (title='Aluguel de Bike', message='Bike alugada com sucesso')
    except:
         messagebox.showerror(title='Erro Aluguel', message='Não foi possivel alugar a bike!')        
         

def devolucao(cpf:str, bicicleta:str):
    '''Devolve a bicicleta alterando de um modelo para Nenhuma'''
    global cliente
    try:
        # Criando uma sessao no banco de dados
        sessao = SessaoBD()
        # Recuperar o contato no banco de dados
        cliente = sessao.query(Clientes).filter_by(cpf=cpf).first()
        # Alterando dados do cliente
        cliente.bicicleta = bicicleta
        sessao.commit()
        messagebox.showinfo (title='Devolução de Bike', message='Bike devolvida com sucesso')
    except:
         messagebox.showerror(title='Erro Devolução', message='Erro na devolução da bike!')     