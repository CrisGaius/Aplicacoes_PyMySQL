from tkinter import *
from tkinter import messagebox
from datetime import datetime
import pymysql

def pega_parametro():
    if e_codigo.get() != '' and e_nome.get() != '' and e_qtdEstoque.get() != '':
        codigo = e_codigo.get()
        nome = e_nome.get().title()
        qtd_estoque = e_qtdEstoque.get()
        dataEhora = datetime.now()

        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='pwd',
                                     database='dbname',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection:
            with connection.cursor() as cursor:
                insert_elements = "INSERT INTO produtos (CodigoDoProduto, NomeDoProduto, QuantidadeEmEstoque, DataDoCadastro) VALUES (%s, %s, %s, %s)"
                cursor.execute(insert_elements, (codigo, nome, qtd_estoque, dataEhora))
                connection.commit()
        messagebox.showinfo('SUCESSO!', 'PRODUTO CADASTRADO COM SUCESSO!')
    else:
        messagebox.showerror('ERRO!', 'NEM TODOS OS CAMPOS FORAM PREENCHIDOS!')

janela = Tk()
janela.title('Cadastro de produtos')
janela.geometry('314x227')
janela['background'] = '#e5eaf5'
janela.resizable(width=0, height=0)
photo = PhotoImage(file='C:\\Users\\crist\\Desktop\\PyMySQL\\icon\\logo_unibra.png')
janela.wm_iconphoto(False, photo)

l_cadastro = Label(janela, text='CADASTRO DE PRODUTOS', font=('Ivy 8 bold', 15), justify=CENTER)
l_cadastro.pack()
l_cadastro.config(bg='#e5eaf5')

l_codigo = Label(janela, text='Código do produto *', font=('Ivy 8 bold'))
l_codigo.place(x=12, y=30)
l_codigo.config(bg='#e5eaf5')
e_codigo = Entry(janela, bd=2, font=('Calibri', 12), width=35)
e_codigo.place(x=14, y=50)

l_nome = Label(janela, text='Nome do produto *', font=('Ivy 8 bold'))
l_nome.place(x=12, y=80)
l_nome.config(bg='#e5eaf5')
e_nome = Entry(janela, bd='2', font=('Calibri', 12), width=35)
e_nome.place(x=14, y=100)

l_qtdEstoque = Label(janela, text='Quantidade em estoque *', font=('Ivy 8 bold'))
l_qtdEstoque.place(x=12, y=130)
l_qtdEstoque.config(bg='#e5eaf5')
e_qtdEstoque = Entry(janela, bd='2', font=('Calibri', 12), width=35)
e_qtdEstoque.place(x=14, y=150)

b_submit = Button(janela, text='Enviar', font=('Ivy 8 bold'), bd=2, command=pega_parametro)
b_submit.place(x=14, y=185)

janela.mainloop()