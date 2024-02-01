import customtkinter
from tkinter import *
import tkinter
import tkinter.messagebox
import sqlite3
from tkinter import ttk
def gui():
    def enviar(nome, cod, IE):
        con = sqlite3.connect("dados.db")
        cur = con.cursor()
        try:
            cur.execute("CREATE TABLE cliente(nome, cod UNIQUE, IE)")
        except Exception:
            pass
        
        try:
            cur.execute("INSERT INTO cliente VALUES(?,?,?)", (nome,cod,IE))
            con.commit()
            print(cur.execute("Select * from cliente").fetchall())
        except sqlite3.IntegrityError:
            tkinter.messagebox.showinfo(message=f"NÃO INSERIDO NA DB, COD {cod} JA EXISTE NO BANCO DE DADOS")
        
    
    customtkinter.set_appearance_mode("dark")
    root = customtkinter.CTk()
    root.geometry('500x300')
    root.title("Clientes IE")
    root.resizable(False,False)
    frm = customtkinter.CTkFrame(root, height= 300)
    frm.grid(column=0, sticky=tkinter.E + tkinter.W)
    root.grid_columnconfigure(0,weight=1)
    customtkinter.CTkLabel(frm, text=f"Insira o nome do cliente").grid(column=0, row=0)
    clienteentry = customtkinter.CTkEntry(frm, width= 450)
    clienteentry.grid(column = 0, row = 1)
    customtkinter.CTkLabel(frm, text=f"Insira o cod do cliente").grid(column=0, row=2)
    clientecod = customtkinter.CTkEntry(frm, width= 450)
    clientecod.grid(column = 0, row = 3)
    customtkinter.CTkLabel(frm, text=f"Insira o num da IE do cliente").grid(column=0, row=4)
    clienteIE = customtkinter.CTkEntry(frm, width= 450)
    clienteIE.grid(column = 0, row = 5)
    customtkinter.CTkButton(frm, text="Enviar", command=lambda: enviar(clienteentry.get(), clientecod.get(), clienteIE.get())).grid(column = 0, row =6)
    
    root.mainloop()
if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   
   gui()