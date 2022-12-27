#[Importações]--------------------------------------------------
import tkinter as tk 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
from regras_de_negocio import excluir_cliente, incluir_cliente, aluguel, devolucao, alterar_cliente
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from CriarTabelaBD import Clientes
# ---------------------------------------------------------------


#[Funções referente a parte gráfica com TKINTER] ----------------

def Menu():
    '''Contém a tela do Menu com todos os botões  que dão acesso as funcionalidades do App'''

    # Janela prinipal -----------------------------------------------------
    janelaMenu = tk.Tk()
    janelaMenu.geometry('330x500+100+200')
    janelaMenu.title("App Bike Store")
    janelaMenu.configure(background ='white')
    janelaMenu.resizable(width=False , height=False)
    icone = PhotoImage(file ='D:\Infinity School\Pyhon_\Projeto Modulo\logomarca\logoLaranja.png')
    janelaMenu.iconphoto(False, icone)


    # Frame e Label Logomarca ----------------------------------------------
    img = PhotoImage(file='logomarca\logonew.png')
    logo = Label(janelaMenu, image=img, width=100, height=100, bg='white')
    logo.place(x=115, y=12)

    label_logo = Label(janelaMenu, text='Aluga Bike', bg='white', fg='#02245B')
    label_logo.config(font=('Helvetica', 16))
    label_logo.place(x=116, y=110)


    # Botões ------------------------------------------------
    bt_incluir = tk.Button(text='Incluir Cliente / Alterar', width=23, bg="#F55D08", fg='white', command=Cadastro_Cliente)
    bt_incluir.config(font=('Arial', 11)) 
    bt_incluir.place(x=58, y=170)

    bt_lista_usuario = tk.Button(text='Listar Cliente', width=23, bg="#F55D08", fg='white', command=Lista_Cliente)
    bt_lista_usuario.config(font=('Arial', 11))
    bt_lista_usuario.place(x=58, y=210)

    bt_excluir_usuario = tk.Button(text='Excluir Cliente', width=23, bg="#F55D08", fg='white', command=Excluir)
    bt_excluir_usuario.config(font=('Arial', 11))
    bt_excluir_usuario.place(x=58, y=250)

    bt_retirada = tk.Button(text='Alugar', width=23, bg="#F55D08", fg='white', command=Retirada)
    bt_retirada.config(font=('Arial', 11))
    bt_retirada.place(x=58, y=290)

    bt_devolucao = tk.Button(text='Devolver', width=23, bg="#F55D08", fg='white', command=Devolucao)
    bt_devolucao.config(font=('Arial', 11))
    bt_devolucao.place(x=58, y=330)

    bt_acompanhamento = tk.Button(text='Acompanhamento', width=23, bg="#F55D08", fg='white', command=Acompanhamento)
    bt_acompanhamento.config(font=('Arial', 11))
    bt_acompanhamento.place(x=58, y=370)


    # by --------------------------------------------------------------------
    by_label = Label(text='By Stefano Carvalho - 2022', bg='white')
    by_label.place(x=98, y=430)
    by_label.config(font=('Arial', 8))


    #Barra final ------------------------------------------------------------
    frameBarra = Frame(janelaMenu, width=330, height=15, bg='#02245B')
    frameBarra.place(x=0, y=485)


    # Loop 
    janelaMenu.mainloop()
   
def Cadastro_Cliente():
    '''Contém a parte gráfica da tela de Cadastro e Alteração de cadastro de clentes. Bem como função para capturar os dados digitados  nas entries e enviar ao Banco de Dados'''

    # Janela principal -----------------------------------------------------
    janelaCadastro = tk.Toplevel()
    janelaCadastro.geometry('600x360+500+200')
    janelaCadastro.title("App Bike Store")
    janelaCadastro.configure(background ='white')
    janelaCadastro.resizable(width=False , height=False)
    icone = PhotoImage(file ='D:\Infinity School\Pyhon_\Projeto Modulo\logomarca\logoLaranja.png')
    janelaCadastro.iconphoto(False, icone)


    # Frame Logomarca ------------------------------------------------------
    img = PhotoImage(file='logomarca\logonew.png')
    logo = Label(janelaCadastro, image=img, width=100, height=100, bg='white')
    logo.place(x=20, y=10)

    label_logo = Label(janelaCadastro, text='Aluga Bike', bg='white', fg='#02245B')
    label_logo.config(font=('Helvetica', 16))
    label_logo.place(x=20, y=105)


    # Frame Titulo ----------------------------------------------------------
    frame_titulo = Frame(janelaCadastro, bg='#F55D08', width=430, height=55)
    frame_titulo.place(x=140, y=35)


    # Label Cadastro de Clientes --------------------------------------------
    label_cadastro = Label(janelaCadastro, text='Cadastrar / Alterar Cliente', bg='#F55D08', fg='white')
    label_cadastro.config(font=('Helvetica', 16))
    label_cadastro.place(x=240, y=47)

 
    # Label e Entry CPF ------------------------------------------------------------
    label_cpf = Label(janelaCadastro, text='CPF:', bg='white', fg='#02245B')
    label_cpf.config(font=('Helvetica', 13))
    label_cpf.place(x=20, y=150)

    entry_cpf = Entry(janelaCadastro, width=20, font=('Arial', 12))
    entry_cpf.config(borderwidth=2, highlightthickness=1, highlightcolor='#02245B')
    entry_cpf.place(x=75, y=150)
   
    
    # Label e Entry Telefone ------------------------------------------------------------
    label_telefone = Label(janelaCadastro, text='Telefone:', bg='white', fg='#02245B')
    label_telefone.config(font=('Helvetica', 13))
    label_telefone.place(x=280, y=150)

    entry_telefone = Entry(janelaCadastro, width=23, font=('Arial', 12))
    entry_telefone.config(borderwidth=2, highlightthickness=1, highlightcolor='#02245B')
    entry_telefone.place(x=360, y=150)
    
    
    # Label e Entry Nome ------------------------------------------------------------
    label_nome = Label(janelaCadastro, text='Nome:', bg='white', fg='#02245B')
    label_nome.config(font=('Helvetica', 13))
    label_nome.place(x=20, y=190)

    entry_nome = Entry(janelaCadastro, width=55, font=('Arial', 12))
    entry_nome.config(borderwidth=2, highlightthickness=1, highlightcolor='#02245B')
    entry_nome.place(x=75, y=190)
    
    
    # Label e Entry Email ------------------------------------------------------------
    label_email = Label(janelaCadastro, text='Email:', bg='white', fg='#02245B')
    label_email.config(font=('Helvetica', 13))
    label_email.place(x=20, y=230)

    entry_email = Entry(janelaCadastro, width=55, font=('Arial', 12))
    entry_email.config(borderwidth=2, highlightthickness=1, highlightcolor='#02245B')
    entry_email.place(x=75, y=230)
    
    
    # Label Tipo---------------------------------------------------------------
    label_tipo = Label(janelaCadastro, text='Tipo:', bg='white', fg='#02245B')
    label_tipo.config(font=('Helvetica', 13))
    label_tipo.place(x=20, y=280)


    # Criando Combobox ---------------------------------------------------------
    lista_tipo = ['Avulso', 'Mensalista']
    
    cb_tipo = ttk.Combobox(janelaCadastro, value = lista_tipo)
    cb_tipo.set('Opções')
    cb_tipo.place(x=75, y=282)

    
    # ----------------------------------------------------------------
    def clear():
        '''Limpa todas as entries após clicar no botão confirmar'''
        entry_cpf.delete(0, END)
        entry_nome.delete(0, END)
        entry_email.delete(0, END)
        entry_telefone.delete(0, END)
        

    # ----------------------------------------------------------------------------
    def get():
        '''resgata os dados das entries e envia para função INCLUIR_CLIENTE,
        que enviará os dados para o Banco de Dados no arquivo regras_de_negocio.py'''
        cpf = entry_cpf.get()
        nome = entry_nome.get()
        email = entry_email.get()
        telefone = entry_telefone.get()
        tipo = cb_tipo.get()
        #print(cpf, nome, email, telefone, tipo)
        incluir_cliente(cpf, nome, email, telefone, tipo)
        clear()
        
   
    # -----------------------------------------------------------------------------------
    def get_alterar():
        '''Captura dados das entries e enviar para função ALTERAR_CLIENTE,
        que envia para Banco de Dados no arquivo regras_de_negocio.py'''
        cpf = entry_cpf.get()
        nome = entry_nome.get()
        email = entry_email.get()
        telefone = entry_telefone.get()
        tipo = cb_tipo.get()
        print(cpf, nome, email, telefone, tipo)
        alterar_cliente(cpf, nome, email, telefone, tipo)
        clear()


    # Botão Cancelar e e Confirmar ------------------------------------------------------------
    bt_cancelar = tk.Button(janelaCadastro, text='Cancelar', width=16, bg="#02245B", fg='white', command=clear)
    bt_cancelar.config(font=('Arial', 10))
    bt_cancelar.place(x=290, y=268)
     
  
    bt_confirmar = tk.Button(janelaCadastro, text='Confirmar', width=16, bg="#02245B", fg='white', command=get)
    bt_confirmar.config(font=('Arial', 10))
    bt_confirmar.place(x=441, y=268)

   
    bt_alterar = tk.Button(janelaCadastro, text='Alterar', width=35, bg="#02245B", fg='white', command=get_alterar)
    bt_alterar.config(font=('Arial', 10))
    bt_alterar.place(x=290, y=300)

    #Barra final -----------------------------------------------------------
    frameBarra = Frame(janelaCadastro, width=600, height=16, bg='#02245B')
    frameBarra.place(x=0, y=345)

    # Loop  
    janelaCadastro.mainloop()

def Lista_Cliente():
    '''Lista todos os clientes cadastrados no App. Independente se está 
    com bicicleta alugada'''

    # Janela principal -----------------------------------------------------
    janelaListagem = tk.Toplevel()
    janelaListagem.geometry('900x645+460+52')
    janelaListagem.title("App Bike Store")
    janelaListagem.configure(background ='white')
    janelaListagem.resizable(width=False , height=False)
    icone = PhotoImage(file ='D:\Infinity School\Pyhon_\Projeto Modulo\logomarca\logoLaranja.png')
    janelaListagem.iconphoto(False, icone)


    # Frame Logomarca ------------------------------------------------------
    img = PhotoImage(file='logomarca\logonew.png')
    logo = Label(janelaListagem, image=img, width=100, height=100, bg='white')
    logo.place(x=20, y=10)

    label_logo = Label(janelaListagem, text='Aluga Bike', bg='white', fg='#02245B')
    label_logo.config(font=('Helvetica', 16))
    label_logo.place(x=20, y=105)


    # Frame Titulo ----------------------------------------------------------
    frame_titulo = Frame(janelaListagem, bg='#F55D08', width=740, height=75)
    frame_titulo.place(x=140, y=35)


    # Label Acompanhamento --------------------------------------------
    label_listagem = Label(janelaListagem, text='Listagem de todos os clientes', bg='#F55D08', fg='white')
    label_listagem.config(font=('Helvetica', 18))
    label_listagem.place(x=350, y=57)


    # Treeview ---------------------------------------------------------
    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font=('Helvetica', 11), height=11)
    
    # Configurações da Treeview ----------------------------------------
    estilo.configure('Treeview',
    backgroud='white',
    foreground='black',
    rowheight=25,
    fieldbackground='white',
    font=('Helvetica', 11))

    # Colunas Treeview -------------------------------------------------
    columns = ('nome', 'cpf', 'telefone', 'tipo', 'bicicleta')

    tree = ttk.Treeview(janelaListagem, columns=columns, show='headings', height=11)
    
    # Configurações de cores para as linhas da treeview. Se a linha for impar, cor branca
    # se par, cor azul. 
    # -----------------------------------------------------------------------------------
    tree.tag_configure('impar', background='white')
    tree.tag_configure('par', background='#B0C4DE')

  
    # Nomes e tamanho das colunas da Treeview ----------------------------------
    tree.column("nome", width=263)
    tree.column("cpf", width=150)
    tree.column("telefone", width=160)
    tree.column("tipo", width=145)
    tree.column("bicicleta", width=130)
    # Cabeçalhos Treeview -------------------------------------------------------
    tree.heading('nome', text='Nome do Cliente')
    tree.heading('cpf', text='CPF')
    tree.heading('telefone', text='Telefone')
    tree.heading('tipo', text='Tipo')
    tree.heading('bicicleta', text='Bicicleta')
    # Posicão Treeview ----------------------------------------------------------
    tree.place(x=25, y=180)


    # Inserindo Scrollbar -------------------------------------------------------
    scroll_bar = Scrollbar(janelaListagem)
    scroll_bar.pack(side = 'right', fill = 'y')
    tree.config(yscrollcommand = scroll_bar.set)
    scroll_bar.config(command = tree.yview)


    # Conecta ao Banco de dados e traz como resultado todos os clientes cadastrados no App,
    # monstrando na treeview
    # ------------------------------------------------------------------------------------
    engine = sqlalchemy.create_engine("mysql+mysqlconnector://root@localhost/alugabike")
    SessaoBD = sessionmaker(bind=engine)
    # criando uma sessão no banco de dados
    sessao = SessaoBD()
    # recuperando os clientes do banco de dados
    cliente = sessao.query(Clientes)
    global count
    count=0
    # Lista todos os clientes na treeview
    # Contém a seguinte lógica: Se o contador for par a linha na treeview será azul, senão # 
    # branca
    for resp in cliente:
        if count % 2 == 0:
            tree.insert('', tk.END, values=(resp.nome,resp.cpf,resp.telefone,resp.tipo,resp.bicicleta), tags=('par'))
        else:
            tree.insert('', tk.END, values=(resp.nome,resp.cpf,resp.telefone,resp.tipo,resp.bicicleta), tags=('impar'))
        count += 1
       

    # by -------------------------------------------------------------------
    by_label = Label(janelaListagem, text='By Stefano Carvalho - 2022', bg='white')
    by_label.place(x=370, y=565)
    by_label.config(font=('Arial', 8))


    #Barra final -----------------------------------------------------------
    frameBarra = Frame(janelaListagem, width=885, height=25, bg='#02245B')
    frameBarra.place(x=0, y=620)


    # Loop  
    janelaListagem.mainloop()

def Excluir():
    '''Exclui cliente do BD'''
    # Janela principal -----------------------------------------------------
    janelaExcluir = tk.Toplevel()
    janelaExcluir.geometry('330x500+530+200')
    janelaExcluir.title("App Bike Store")
    janelaExcluir.configure(background ='white')
    janelaExcluir.resizable(width=False , height=False)
    icone = PhotoImage(file ='D:\Infinity School\Pyhon_\Projeto Modulo\logomarca\logoLaranja.png')
    janelaExcluir.iconphoto(False, icone)


    # Frame Logomarca ------------------------------------------------------
    img = PhotoImage(file='logomarca\logonew.png')
    logo = Label(janelaExcluir, image=img, width=100, height=100, bg='white')
    logo.place(x=115, y=12)

    label_logo = Label(janelaExcluir, text='Aluga Bike', bg='white', fg='#02245B')
    label_logo.config(font=('Helvetica', 16))
    label_logo.place(x=116, y=110)


    # Label Cliente --------------------------------------------------------
    frame_label = Frame(janelaExcluir, width=290, height=1, bg='#02245B')
    frame_label.place(x=20, y=165)

    label_cliente = Label(janelaExcluir, text='Excluir Cliente', bg='white', fg='#F55D08')
    label_cliente.config(font=('Helvetica', 16))
    label_cliente.place(x=98, y=170)

    frame_label = Frame(janelaExcluir, width=290, height=1, bg='#02245B')
    frame_label.place(x=20, y=205)


    # Frame CPF ------------------------------------------------------------
    frame_cpf = Frame(janelaExcluir, width=290, height=150, bg='#F55D08')
    frame_cpf.place(x=20, y=230 )


    # Label e Entry CPF ----------------------------------------------------
    label_cpf = Label(janelaExcluir, text='CPF:', bg='#F55D08', fg='white')
    label_cpf.config(font=('Arial', 12))
    label_cpf.place(x=58, y=250)

    entry_cpf = Entry(janelaExcluir, width=23, font=('Arial', 12))
    entry_cpf.config(borderwidth=2)
    entry_cpf.place(x=60, y=280)

   
    # -----------------------------------------------
    def clear_entryCpf():
        '''limpa entry após exclusão do cliente'''
        entry_cpf.delete(0, END)


    # ----------------------------------------------------------------------
    def get_cpf(event=None):
        '''resgata cpf digitado na entry e por ultimo limpa as entries'''
        getCpf = entry_cpf.get()
        excluir_cliente(getCpf)
        clear_entryCpf()


    # Pressiona botao com a tecla ENTER
    janelaExcluir.bind('<Return>', get_cpf)


    # Botão consultar ------------------------------------------------------
    bt_excluir = tk.Button(janelaExcluir, text='Excluir', width=24, bg="#02245B", fg='white', command=get_cpf)
    bt_excluir.config(font=('Arial', 10))
    bt_excluir.place(x=65, y=330)


    # by -------------------------------------------------------------------
    by_label = Label(janelaExcluir, text='By Stefano Carvalho - 2022', bg='white')
    by_label.place(x=92, y=420)
    by_label.config(font=('Arial', 8))


    #Barra final -----------------------------------------------------------
    frameBarra = Frame(janelaExcluir, width=330, height=15, bg='#02245B')
    frameBarra.place(x=0, y=485)

    # Loop  
    janelaExcluir.mainloop()

def Retirada():
    '''Referente ao aluguel da bike. Ao escolher qual bike o cliente alugará, insere nos dados do cliente qual bike ele alugou'''
    # Janela principal -----------------------------------------------------
    janelaRetirada = tk.Toplevel()
    janelaRetirada.geometry('330x500+530+200')
    janelaRetirada.title("App Bike Store")
    janelaRetirada.configure(background ='white')
    janelaRetirada.resizable(width=False , height=False)
    icone = PhotoImage(file ='D:\Infinity School\Pyhon_\Projeto Modulo\logomarca\logoLaranja.png')
    janelaRetirada.iconphoto(False, icone)

    # Frame Logomarca ------------------------------------------------------
    img = PhotoImage(file='logomarca\logonew.png')
    logo = Label(janelaRetirada, image=img, width=100, height=100, bg='white')
    logo.place(x=115, y=12)

    label_logo = Label(janelaRetirada, text='Aluga Bike', bg='white', fg='#02245B')
    label_logo.config(font=('Helvetica', 16))
    label_logo.place(x=116, y=110)


    # Label Cliente --------------------------------------------------------
    frame_label = Frame(janelaRetirada, width=290, height=1, bg='#02245B')
    frame_label.place(x=20, y=160)

    label_retirada = Label(janelaRetirada, text='Aluguel', bg='white', fg='#F55D08')
    label_retirada.config(font=('Helvetica', 16))
    label_retirada.place(x=130, y=165)

    frame_label = Frame(janelaRetirada, width=290, height=1, bg='#02245B')
    frame_label.place(x=20, y=200)


    # Frame Retirada ----------------------------------------------------------
    frame_retirada = Frame(janelaRetirada, width=290, height=160, bg='#F55D08')
    frame_retirada.place(x=20, y=215)


    # Label e Entrys Usuário e Senha ---------------------------------------------

    # CPF ---------------------------------------------------------------
    label_cpf = Label(janelaRetirada, text='CPF:', fg='white', bg='#F55D08')
    label_cpf.config(font=('Arial', 12))
    label_cpf.place(x=58, y=230)

    entry_cpf = Entry(janelaRetirada, width=23, font=('Arial', 12))
    entry_cpf.config(borderwidth=2, highlightthickness=1, highlightcolor='#02245B')
    entry_cpf.place(x=60, y=255)

    
    # Label Bicicleta ------------------------------------------------------------------
    label_bicicleta = Label(janelaRetirada, text='Bicicleta:', fg='white', bg='#F55D08')
    label_bicicleta.config(font=('Arial', 12))
    label_bicicleta.place(x=58, y=300)

    
    # Cadastro das Bicicletas ------------------------------
    bicicletas = ['Nenhuma', 'Caloi', 'Sense', 'Oggi', 'Specialized', 'Cannondale', 'Trek']

    # Combobox ---------------------------------
    cb_bicicleta = ttk.Combobox(janelaRetirada, width=22, font=('Helvetica', 12), value = bicicletas)
    cb_bicicleta.set( 'Bicicletas')
    cb_bicicleta.place(x=60, y=325)

    # Gets Combobox -------------------------------------------
    def clear():
        '''limpa a entry cpf'''
        entry_cpf.delete(0, END)

    
    # -----------------------------------------------------------------------
    def get_cpf_retirada(event=None):
        '''captura os dados da entry cpf e bicileta e envia para função # 
        ALTERAR_BICICLETA, no arquivo regras_de_negócio.py'''
        cpf = entry_cpf.get()
        bicicleta = cb_bicicleta.get()
        aluguel(cpf, bicicleta)
        clear()


    # Pressiona botao com a tecla ENTER
    janelaRetirada.bind('<Return>', get_cpf_retirada)


    # Botão Confirmar ------------------------------------------------------------
    bt_alugar = tk.Button(janelaRetirada, text='Alugar', width=22, bg="#02245B", fg='white', command=get_cpf_retirada)
    bt_alugar.config(font=('Arial', 11))
    bt_alugar.place(x=64, y=390)


    # by -------------------------------------------------------------------
    by_label = Label(janelaRetirada, text='By Stefano Carvalho - 2022', bg='white')
    by_label.place(x=95, y=450)
    by_label.config(font=('Arial', 8))


    #Barra final -----------------------------------------------------------
    frameBarra = Frame(janelaRetirada, width=330, height=15, bg='#02245B')
    frameBarra.place(x=0, y=485)


    # Loop  
    janelaRetirada.mainloop()

def Devolucao():
    '''Referente a devolução da bicicleta alterando nos dados do cliente o nome da bike para nenhuma'''
    # Janela principal -----------------------------------------------------
    janelaDevolucao = tk.Toplevel()
    janelaDevolucao.geometry('330x500+530+200')
    janelaDevolucao.title("App Bike Store")
    janelaDevolucao.configure(background ='white')
    janelaDevolucao.resizable(width=False , height=False)
    icone = PhotoImage(file ='D:\Infinity School\Pyhon_\Projeto Modulo\logomarca\logoLaranja.png')
    janelaDevolucao.iconphoto(False, icone)

    # Frame Logomarca ------------------------------------------------------
    img = PhotoImage(file='logomarca\logonew.png')
    logo = Label(janelaDevolucao, image=img, width=100, height=100, bg='white')
    logo.place(x=115, y=12)

    label_logo = Label(janelaDevolucao, text='Aluga Bike', bg='white', fg='#02245B')
    label_logo.config(font=('Helvetica', 16))
    label_logo.place(x=116, y=110)


    # Label Devolução --------------------------------------------------------
    frame_label = Frame(janelaDevolucao, width=290, height=1, bg='#02245B')
    frame_label.place(x=20, y=160)

    label_logo = Label(janelaDevolucao, text='Devolução', bg='white', fg='#F55D08')
    label_logo.config(font=('Helvetica', 16))
    label_logo.place(x=115, y=165)

    frame_label = Frame(janelaDevolucao, width=290, height=1, bg='#02245B')
    frame_label.place(x=20, y=200)


    # Frame Retirada ----------------------------------------------------------
    frame_devolucao = Frame(janelaDevolucao, width=290, height=160, bg='#F55D08')
    frame_devolucao.place(x=20, y=215)


    # Label e Entrys Devolução ---------------------------------------------

    # Bicicleta ------------------------------------------------------------------
    label_cpf = Label(janelaDevolucao, text='CPF:', fg='white', bg='#F55D08')
    label_cpf.config(font=('Arial', 12))
    label_cpf.place(x=58, y=237)

    entry_cpf = Entry(janelaDevolucao, width=23, font=('Arial', 12))
    entry_cpf.config(borderwidth=2, highlightthickness=1, highlightcolor='#02245B')
    entry_cpf.place(x=60, y=265)


    # Cadastro das Bicicletas ------------------------------
    bicicletas = ['Nenhuma', 'Caloi', 'Sense', 'Oggi', 'Specialized', 'Cannondale', 'Trek']

    # Combobox ---------------------------------
    cb_bicicleta = ttk.Combobox(janelaDevolucao, width=22, font=('Helvetica', 12), value = bicicletas)
    cb_bicicleta.set( 'Bicicletas')
    cb_bicicleta.place(x=60, y=318)


    # --------------------------------------
    def clear():
        '''Limpa a entry cpf'''
        entry_cpf.delete(0, END)


    # -------------------------------------------
    def get_cpf_devolucao(event=None):
        '''Captura os dados da entry cpf e da combobox'''
        cpf = entry_cpf.get()
        bicicleta = cb_bicicleta.get()
        devolucao(cpf, bicicleta)
        clear()
       

    # Pressiona botao com a tecla ENTER
    janelaDevolucao.bind('<Return>', get_cpf_devolucao)


    # Botão Confirmar ------------------------------------------------------------
    bt_devolver = tk.Button(janelaDevolucao, text='Devolver', width=22, bg="#02245B", fg='white', command=get_cpf_devolucao)
    bt_devolver.config(font=('Arial', 11))
    bt_devolver.place(x=64, y=390)


    # by -------------------------------------------------------------------
    by_label = Label(janelaDevolucao, text='By Stefano Carvalho - 2022', bg='white')
    by_label.place(x=97, y=433)
    by_label.config(font=('Arial', 8))


    #Barra final -----------------------------------------------------------
    frameBarra = Frame(janelaDevolucao, width=330, height=15, bg='#02245B')
    frameBarra.place(x=0, y=485)


    # Loop  
    janelaDevolucao.mainloop()

def Acompanhamento():
    '''Acompanha o status do aluguel: Mostrando em uma treeview apenas os clientes que estão com bike alugada'''
    # Janela principal -----------------------------------------------------
    janelaAcompanhamento = tk.Toplevel()
    janelaAcompanhamento.geometry('900x645+460+52')
    janelaAcompanhamento.title("App Bike Store")
    janelaAcompanhamento.configure(background ='white')
    janelaAcompanhamento.resizable(width=False , height=False)
    icone = PhotoImage(file ='D:\Infinity School\Pyhon_\Projeto Modulo\logomarca\logoLaranja.png')
    janelaAcompanhamento.iconphoto(False, icone)

    # Frame Logomarca ------------------------------------------------------
    img = PhotoImage(file='logomarca\logonew.png')
    logo = Label(janelaAcompanhamento, image=img, width=100, height=100, bg='white')
    logo.place(x=20, y=10)

    label_logo = Label(janelaAcompanhamento, text='Aluga Bike', bg='white', fg='#02245B')
    label_logo.config(font=('Helvetica', 16))
    label_logo.place(x=20, y=105)


    # Frame Titulo ----------------------------------------------------------
    frame_titulo = Frame(janelaAcompanhamento, bg='#F55D08', width=740, height=75)
    frame_titulo.place(x=140, y=35)


    # Label Acompanhamento --------------------------------------------
    label_acompanhamento = Label(janelaAcompanhamento, text='Acompanhamento', bg='#F55D08', fg='white')
    label_acompanhamento.config(font=('Helvetica', 16))
    label_acompanhamento.place(x=420, y=57)


    # Janela Treeview -----------------------------------
    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font=('Helvetica', 11),  height=11)

    # Configurações da Treeview -------------------------
    estilo.configure('Treeview',
    backgroud='white',
    foreground='black',
    rowheight=25,
    fieldbackground='white',
    font=('Helvetica', 11))

    # Colunas Treeview -----------------------------------
    columns = ('nome', 'cpf', 'telefone', 'tipo', 'bicicleta')
    global tree
    tree = ttk.Treeview(janelaAcompanhamento, columns=columns, show='headings', height=11)

    # Configuração de cor das linhas da treeview ----------
    tree.tag_configure('impar', background='white')
    tree.tag_configure('par', background='#B0C4DE')

    # Nomes e tamanho da Treeview---------------------------
    tree.column("nome", width=252)
    tree.column("cpf", width=160)
    tree.column("telefone", width=155)
    tree.column("tipo", width=150)
    tree.column("bicicleta", width=130)
    # Cabeçalhos Treeview ----------------------------------
    tree.heading('nome', text='Nome do Cliente')
    tree.heading('cpf', text='CPF')
    tree.heading('telefone', text='Telefone')
    tree.heading('tipo', text='Tipo')
    tree.heading('bicicleta', text='Bicicleta')
    # Posicão Treeview
    tree.place(x=25, y=180)

    # Inserindo Scrollbar -----------------------------------
    scroll_bar = Scrollbar(janelaAcompanhamento)
    scroll_bar.pack(side = 'right', fill = 'y')
    tree.config(yscrollcommand = scroll_bar.set)
    scroll_bar.config(command = tree.yview)


    # Conecta ao banco de dados e traz como resultado todos os clientes cadastrados no APP
    # ------------------------------------------------------------------------------------
    engine = sqlalchemy.create_engine("mysql+mysqlconnector://root@localhost/alugabike")
    SessaoBD = sessionmaker(bind=engine)
    # criando uma sessão no banco de dados
    sessao = SessaoBD()
    # recuperando o contato do banco de dados
    cliente = sessao.query(Clientes)
    global count
    count=0
    # Recebe resultado da pesquisa a cima e lista na treeview apenas clientes com bicicletas alugadas para acompanhamento. A lógica além de listar apenas clientes com bicicletas, analisa se linha da treeview é par ou impar. Se par, cor azul se impar, branca
    for resp in cliente:
        if (count % 2 == 0) and (resp.bicicleta != 'Nenhuma'):
                tree.insert('', tk.END, values=(resp.nome,resp.cpf,resp.telefone,resp.tipo,resp.bicicleta), tags='par')
        elif (count % 2 != 0) and (resp.bicicleta != 'Nenhuma'):
            tree.insert('', tk.END, values=(resp.nome,resp.cpf,resp.telefone,resp.tipo,resp.bicicleta), tags='impar')
        count += 1


    # Botão Fechar ---------------------------------------------------------
    bt_fechar = tk.Button(text='Fechar', width=16, bg="#02245B", fg='white')
    bt_fechar.config(font=('Arial', 11))
    bt_fechar.place(x=719, y=550)


    # by -------------------------------------------------------------------
    by_label = Label(janelaAcompanhamento, text='By Stefano Carvalho - 2022', bg='white')
    by_label.place(x=360, y=550)
    by_label.config(font=('Arial', 8))


    #Barra final -----------------------------------------------------------
    frameBarra = Frame(janelaAcompanhamento, width=900, height=25, bg='#02245B')
    frameBarra.place(x=0, y=620)


    # Loop  
    janelaAcompanhamento.mainloop()
