import tkinter as tk
from tkinter import ttk
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class tela_principal:
    def __init__(self, tela):
        self.tela = tela
        self.tela.title(f'{self.tela}')
        self.tela.geometry('560x227')
    def tabela(self):
        table_dt = dados_tabela()
        qtd_linhas = table_dt["qtd_linhas"]
        linhas = table_dt["linhas"]
        tabela = ttk.Treeview(tela)
        tabela['columns'] = table_dt["colunas"]
        tabela.column('#0', width=0, stretch=tk.NO)
        tabela.heading('#0', text='', anchor=tk.W)
        for c in tabela["columns"]:
        
            tabela.column(c, anchor=tk.W, width=150)
            tabela.heading(c, text=c, anchor=tk.W)

        for i in range(qtd_linhas):
            if i % 2 == 0:
                tabela.insert(parent='', index=i, values=linhas[i], tags=('evenrow',))
            else:
                tabela.insert(parent='', index=i, values=linhas[i], tags=('oddrow',))


        tabela.pack(side="left")
    def botões(self):

        funcoes = {"adicionar": adicionar,
                   "deletar": deletar,
                    "editar": editar,
                    "pesquisar": pesquisar}
        botoes = ["adicionar","deletar","editar","pesquisar"]
        for botao in botoes:
            add_btn = tk.Button(self.tela, text=botao, command=funcoes[botao])
            add_btn.pack(side="top")

        def adicionar():
            ...
        def deletar():
            ...
        def editar():
            ...
        def pesquisar():
            ...
    
 

            
        
class tela_add():
    def __init__():
            ...
    def criar_input(telae, nome):
        linha = tk.Frame(telae)
        linha.pack(pady=5)
        label = tk.Label(linha, text=nome, fg="black")
        label.pack(side="left")
        input = nome = tk.Entry(linha)
        input.pack(side="left")
        return input



def dados_tabela():
    db = mysql.connector.connect(host=os.getenv("HOST"), user=os.getenv("USER"), password=os.getenv("PASSWORD"), database=os.getenv("DATABASE"))
    cursor = db.cursor()
    query = ("SELECT * FROM new_schema.new_table"
                     "")
    
    cursor.execute(query)
    results = cursor.fetchall()

    colunas = cursor.column_names
    qtd_colunas = len(colunas)
    qtd_linhas = len(results)
    dados_tabela = {"colunas": colunas,
                    "qtd_colunas": qtd_colunas,
                    "qtd_linhas": qtd_linhas,
                    "linhas": results}
    cursor.close()
    return dados_tabela


tela = tk.Tk()
tela_principal.tabela(tela)
tela.mainloop()


