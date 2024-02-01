import customtkinter
from tkinter import *
import tkinter
from tkinter import ttk
def gui():
    customtkinter.set_appearance_mode("dark")
    root = customtkinter.CTk()
    root.geometry('800x600')
    root.title("Clientes IE")
    root.resizable(False,False)
    frm = customtkinter.CTkFrame(root, height= 300)
    frm.grid(column=0, sticky=tkinter.E + tkinter.W)
    root.grid_columnconfigure(0,weight=1)
    customtkinter.CTkLabel(frm, text=f"Insira o nome do cliente").grid(column=0, row=0)
    clienteentry = customtkinter.CTkEntry(frm, width= 450).grid(column = 0, row = 1)
    customtkinter.CTkLabel(frm, text=f"Insira o cod do cliente").grid(column=0, row=2)
    clientecod = customtkinter.CTkEntry(frm, width= 450).grid(column = 0, row = 3)
    global btcount
    root.mainloop()
if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   
   gui()