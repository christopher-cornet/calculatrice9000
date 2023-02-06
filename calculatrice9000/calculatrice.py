import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os

root = Tk()
root.title("Calculatrice - Christopher CORNET")
root.geometry('383x367')

nb_entry = Entry(root, width=35, borderwidth=5, justify='center')
nb_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Clique bouton
def click_btn(btn):
    nb_entry.insert(tk.END, btn)

# Efface l'Entry
def clear_entry():
    nb_entry.delete(0, tk.END)

# Racine carrée
def square_root_func():
    squareRoot = float(nb_entry.get())**(1/2)
    nb_entry.delete(0, tk.END)
    nb_entry.insert(0, squareRoot)

# Calcul carré
def square_func():
    square = float(nb_entry.get())*float(nb_entry.get())
    nb_entry.delete(0, tk.END)
    nb_entry.insert(0, square)

# Résultat
def result():
    try:
        nb = str(eval(nb_entry.get()))
        nb_entry.delete(0, tk.END)
        nb_entry.insert(0, nb)
    except:
        messagebox.showinfo("Erreur", "Erreur de syntaxe.")

# Nombres
b1 = Button(root, text=1, padx=40, pady=20, bg="#8E8EE5", activebackground='#7A7AC6', command=lambda: click_btn(1))
b2 = Button(root, text=2, padx=40, pady=20, bg="#8E8EE5", activebackground='#7A7AC6', command=lambda: click_btn(2))
b3 = Button(root, text=3, padx=40, pady=20, bg="#8E8EE5", activebackground='#7A7AC6', command=lambda: click_btn(3))
b4 = Button(root, text=4, padx=40, pady=20, bg="#7A7AC5", activebackground='#7373BB', command=lambda: click_btn(4))
b5 = Button(root, text=5, padx=40, pady=20, bg="#7A7AC5", activebackground='#7373BB', command=lambda: click_btn(5))
b6 = Button(root, text=6, padx=40, pady=20, bg="#7A7AC5", activebackground='#7373BB', command=lambda: click_btn(6))
b7 = Button(root, text=7, padx=40, pady=20, bg="#6666CD", activebackground='#6161C2', command=lambda: click_btn(7))
b8 = Button(root, text=8, padx=40, pady=20, bg="#6666CD", activebackground='#6161C2', command=lambda: click_btn(8))
b9 = Button(root, text=9, padx=40, pady=20, bg="#6666CD", activebackground='#6161C2', command=lambda: click_btn(9))
b0 = Button(root, text=0, padx=40, pady=20, bg="#9898F5", activebackground='#FFFF72', command=lambda: click_btn(0))

# Opérateurs
add = Button(root, text='+', padx=40, pady=20, bg="#AFE961", activebackground='#A5DD5B', command=lambda: click_btn('+'))
subtract = Button(root, text='-', padx=40, pady=20, bg="#AFE961", activebackground='#A5DD5B', command=lambda: click_btn('-'))
multiply = Button(root, text='*', padx=40, pady=20, bg="#AFE961", activebackground='#A5DD5B', command=lambda: click_btn('*'))
divide = Button(root, text='/', padx=40, pady=20, bg="#AFE961", activebackground='#A5DD5B', command=lambda: click_btn('/'))
comma = Button(root, text='.', padx=40, pady=20, bg="#AFE961", activebackground='#A5DD5B', command=lambda: click_btn('.'))
square_root = Button(root, text='√x', padx=40, pady=20, bg="#AFE961", activebackground='#A5DD5B', command=square_root_func)
square = Button(root, text='x²', padx=40, pady=20, bg="#AFE961", activebackground='#A5DD5B', command=square_func)
equal = Button(root, text='=', padx=40, pady=20, bg="#FF3636", activebackground='#E83131', command=result)

# Effacer
clear = Button(root, text='Clear', padx=30, pady=20, bg="#FF3636", activebackground='#E83131', command=clear_entry)

# Afficher dans l'interface graphique
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b0.grid(row=4, column=1)

add.grid(row=1,column=3)
subtract.grid(row=2,column=3)
multiply.grid(row=3,column=3)
divide.grid(row=4,column=3)
comma.grid(row=4,column=0)
equal.grid(row=5,column=3)

clear.grid(row=5,column=0)
square_root.grid(row=4,column=2)
square.grid(row=5,column=1)

root.mainloop()