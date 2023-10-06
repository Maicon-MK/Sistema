import customtkinter
import tkinter as tk

windows = tk.Tk()

width = 800
height = 500

windows.geometry(f'{width}x{height}')

@classmethod
def adcionar():
    ""
@classmethod
def remover():
    ""
@classmethod
def mostrar():
    ""
@classmethod
def sortear():
    ""

title = customtkinter.CTkLabel(windows , text='Sistema de gestão de pessoas')
title.pack(pady=10, padx=10)

name = customtkinter.CTkLabel(windows, text='Nome')
name.pack(pady=5,padx=5)
name = customtkinter.CTkEntry(windows,placeholder_text='Digite um nome' )
name.pack(pady=5, padx=5)


local = customtkinter.CTkLabel(windows, text='Onde mora ')
local.pack(pady=5,padx=5)
local = customtkinter.CTkEntry(windows,placeholder_text='Digite o endereço' )
local.pack(pady=5, padx=5)

btn_adcionar = customtkinter.CTkButton(windows,text="Adcionar")
btn_adcionar.pack(pady=5, padx=5)

btn_remover = customtkinter.CTkButton(windows,text="Remover")
btn_remover.pack(pady=5, padx=5)

btn_mostrar = customtkinter.CTkButton(windows,text="Mostra")
btn_mostrar.pack(pady=5, padx=5)

btn_sortear = customtkinter.CTkButton(windows,text="Sortear")
btn_sortear.pack(pady=5, padx=5)


windows.mainloop()