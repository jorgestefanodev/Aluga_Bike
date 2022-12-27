#[Importações]------------------------------
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Design import *


#[Programa Principal (Login)]
# Contém a tela de Login, criação de novo usuário e função para altenticação de senha

def Login():
    # Janela principal
    janela = tk.Tk()
    janela.geometry('330x500+600+200')
    janela.title("App Bike Store")
    janela.configure(background ='white')
    janela.resizable(width=False , height=False)
    icone = PhotoImage(file ='D:\Infinity School\Pyhon_\Projeto Modulo\logomarca\logoLaranja.png')
    janela.iconphoto(False, icone)
    
    
    # Frame Logomarca
    img = PhotoImage(file='logomarca\logonew.png')
    logo = Label(janela, image=img, width=100, height=100, bg='white')
    logo.place(x=115, y=12)

    label_logo = Label(janela, text='Aluga Bike', bg='white', fg='#02245B')
    label_logo.config(font=('Helvetica', 16))
    label_logo.place(x=116, y=110)


    # Frame Login
    frame_login = Frame(janela, width=270, height=200, bg='#F55D08')
    frame_login.place(x=30, y=160)


    # Label e Entrys Usuário
    label_usuario = Label(text='Usuário', fg='white', bg='#F55D08')
    label_usuario.config(font=('Arial', 12))
    label_usuario.place(x=58, y=180)

    entry_usuario = Entry(janela, width=23, font=('Arial', 12))
    entry_usuario.config(borderwidth=2, highlightthickness=1, highlightcolor='#02245B')
    entry_usuario.place(x=60, y=210)


    # Label e Entrys Usuário Senha
    label_senha = Label(text='Senha', fg='white', bg='#F55D08')
    label_senha.config(font=('Arial', 12))
    label_senha.place(x=58, y=260)

    entry_senha = Entry(janela, show='*', width=23, font=('Arial', 12))
    entry_senha.config(borderwidth=2, highlightthickness=1, highlightcolor='#02245B')
    entry_senha.place(x=60, y=290)

    # Autenticação Login    
    def Acessar(event=None):
        arqsenhas = {"admin":"admin"}
        usuario_informado = entry_usuario.get()
        senha_informada = entry_senha.get()
        if (usuario_informado in arqsenhas):
            if(arqsenhas[usuario_informado] == senha_informada):
                messagebox.showinfo('Autenticação', 'Usuário autenticado com sucesso!')
                janela.destroy()
                Menu()
            else: 
                messagebox.showerror('Autenticação', "Usuário ou Senha incorretos")
        else: 
            messagebox.showerror('Autenticação', "Usuário ou Senha incorretos")
                

    # Confirma login com botão Enter ----------------------------------------------        
    janela.bind('<Return>', Acessar)


    # Botão Entrar ------------------------------------------------------------
    bt_entrar = tk.Button(text='Entrar', width=22, bg="#02245B", fg='white', command=Acessar)
    bt_entrar.config(font=('Arial', 11))
    bt_entrar.place(x=62, y=390)


    # by --------------------------------------------------------------------
    by_label = Label(text='By Stefano Carvalho - 2022', bg='white')
    by_label.place(x=98, y=440)
    by_label.config(font=('Arial', 8))

    
    # Barra final --------------------------------------------------------------
    frameBarra = Frame(janela, width=330, height=15, bg='#02245B')
    frameBarra.place(x=0, y=485)
   

    # Janela Loop  
    janela.mainloop()


if __name__ == '__main__':
    login = Login()      