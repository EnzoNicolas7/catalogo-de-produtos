import tkinter as tk
from tkinter import ttk
import mysql.connector

def save():
    lista.append(input.get())


def add_produto():
    
    tela_add = tk.Toplevel()
    tela.title('adicionar produto')

    

    #fazer fução que cria input ja com label do lado, e coloca os inputs numa lista ou dicionario, depois pega os dados de todos inputs das lista
    
    class input:
        def __init__(self, nome:str, tela):
            self.nome = nome
            self.tela = tela
        def criar_input(self):
            linha = tk.Frame(self.tela)
            linha.pack(pady=5)
            label = tk.Label(linha, text=self.nome, fg="black")
            label.pack(side="left")
            input = self.nome = tk.Entry(linha)
            input.pack(side="left")
            
            
            
    lista = []
    for c in colunas[1:]:
        
    produto = input("produto", tela_add)
    produto.criar_input()
    preco = input("preço", tela_add)
    preco.criar_input()
    
    salvar = tk.Button(tela_add, text="confirmar", command=save)
    salvar.pack(side="left")
    cancelar = tk.Button(tela_add, text="cancelar")
    cancelar.pack(side="left")
    

   #produto(nome, preco, linhas)



def atualizar_tabela():
    table = ttk.Treeview(tela)
    
    table['columns'] = colunas
    table.column('#0', width=0, stretch=tk.NO)
    table.heading('#0', text='', anchor=tk.W)
    for c in table["columns"]:
        
        table.column(c, anchor=tk.W, width=150)
        table.heading(c, text=c, anchor=tk.W)

    for i in range(linhas):
        if i % 2 == 0:
            table.insert(parent='', index=i, values=results[i], tags=('evenrow',))
        else:
            table.insert(parent='', index=i, values=results[i], tags=('oddrow',))


    table.pack(side="left")

    #cursor.execute("INSERT INTO new_table (id, nome, descricao)VALUES(id, nome, preco)")

#pegando dados da tabela mysql
db = mysql.connector.connect(host="localhost", user="root", password="Japaa2222", database="new_schema")
cursor = db.cursor()

query = ("SELECT * FROM new_schema.new_table"
         "")
cursor.execute(query)

results = cursor.fetchall()
colunas = cursor.column_names
cursor.close()

qtd_colunas = len(colunas)


linhas = len(results)


print(f"colunas: {colunas} quantidade de colunas: {qtd_colunas} linhas: {linhas}\n dados da tabela: {results}")

# criando tela inicial
tela = tk.Tk()
tela.title('Catalogo de Produtos')
tela.geometry('560x227')
atualizar_tabela()

add_btn = tk.Button(tela, text="adicionar produto", command=add_produto)
add_btn.pack(side="top")
tela.mainloop()




