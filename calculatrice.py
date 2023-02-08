import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os

root = Tk()
root.title("Calculatrice - Christopher CORNET")
root.geometry("550x370")
root.iconbitmap("calculatrice.ico")

nb_entry = Entry(root, width=50, borderwidth=4, justify='center')
nb_entry.grid(row=0, column=0, columnspan=5, padx=15, pady=15)

# Clique bouton
def click_NB_OP(btn):
    nb_entry.insert(tk.END, btn)

# Efface l'Entry
def clear_entry():
    nb_entry.delete(0, tk.END)

# Efface le dernier nombre/opérateur
def remove():
    nb_entry.delete(len(nb_entry.get())-1,END)

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

# Historique
def history():
    history_window = Toplevel(root)
    history_window.title("Historique des calculs")
    history_window.iconbitmap("calculatrice.ico")
    history_window.geometry("350x270")

    filename = open("calculation_history.txt", 'r')
    filename_read = filename.read()

    calculation_history = Label(history_window, text=filename_read, font=('Times New Roman', 12, 'bold'))
    calculation_history.grid()

# Efface l'historique
def clear_history():
    os.remove("calculation_history.txt")

# Résultat
def result():
    file_history = open("calculation_history.txt", "a")
    file_history.write("{}\n".format(nb_entry.get()))
    file_history.close()
    try:
        nb = str(eval(nb_entry.get()))
        nb_entry.delete(0, tk.END)
        nb_entry.insert(0, nb)
    except:
        messagebox.showerror("Erreur", "Erreur de calcul.")
    file_history = open("calculation_history.txt", "a")
    file_history.write("{}\n".format(nb_entry.get()))
    file_history.close()

# Nombres
b1 = Button(root, text=1, padx=40, pady=20, bg="#8E8EE5", activebackground='#7A7AC6', command=lambda: click_NB_OP(1))
b2 = Button(root, text=2, padx=40, pady=20, bg="#8E8EE5", activebackground='#7A7AC6', command=lambda: click_NB_OP(2))
b3 = Button(root, text=3, padx=40, pady=20, bg="#8E8EE5", activebackground='#7A7AC6', command=lambda: click_NB_OP(3))
b4 = Button(root, text=4, padx=40, pady=20, bg="#7A7AC5", activebackground='#7373BB', command=lambda: click_NB_OP(4))
b5 = Button(root, text=5, padx=40, pady=20, bg="#7A7AC5", activebackground='#7373BB', command=lambda: click_NB_OP(5))
b6 = Button(root, text=6, padx=40, pady=20, bg="#7A7AC5", activebackground='#7373BB', command=lambda: click_NB_OP(6))
b7 = Button(root, text=7, padx=40, pady=20, bg="#6666CD", activebackground='#6161C2', command=lambda: click_NB_OP(7))
b8 = Button(root, text=8, padx=40, pady=20, bg="#6666CD", activebackground='#6161C2', command=lambda: click_NB_OP(8))
b9 = Button(root, text=9, padx=40, pady=20, bg="#6666CD", activebackground='#6161C2', command=lambda: click_NB_OP(9))
b0 = Button(root, text=0, padx=40, pady=20, bg="#9898F5", activebackground='#FFFF72', command=lambda: click_NB_OP(0))

# Opérateurs
add = Button(root, text="+", padx=40, pady=20, bg="#AFE961", activebackground="#A5DD5B", command=lambda: click_NB_OP("+"))
subtract = Button(root, text="-", padx=40, pady=20, bg="#AFE961", activebackground="#A5DD5B", command=lambda: click_NB_OP("-"))
multiply = Button(root, text="×", padx=40, pady=20, bg="#AFE961", activebackground="#A5DD5B", command=lambda: click_NB_OP("*"))
divide = Button(root, text="÷", padx=40, pady=20, bg="#AFE961", activebackground="#A5DD5B", command=lambda: click_NB_OP("/"))
comma = Button(root, text=".", padx=40, pady=20, bg="#AFE961", activebackground="#A5DD5B", command=lambda: click_NB_OP("."))
square_root = Button(root, text="√x", padx=40, pady=20, bg="#AFE961", activebackground="#A5DD5B", command=square_root_func)
square = Button(root, text="x²", padx=40, pady=20, bg="#AFE961", activebackground="#A5DD5B", command=square_func)
delete = Button(root, text="⌦", padx=40, pady=20, bg="#FF3636", activebackground="#E83131", command=remove)
equal = Button(root, text="=", padx=40, pady=20, bg="#FF3636", activebackground="#E83131", command=result)

# Effacer
clear = Button(root, text="Clear", padx=30, pady=20, bg="#FF3636", activebackground="#E83131", command=clear_entry)

# Historique
history_btn = Button(root, text="Historique", padx=20, pady=20, bg="#FABF3F", activebackground="#EBB43D", command=history)

# Effacer l'historique
del_history_btn = Button(root, text="Supprimer l'historique", padx=10, pady=20, bg="#FF3636", activebackground="#E83131", command=clear_history)

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

add.grid(row=1, column=3)
subtract.grid(row=2, column=3)
multiply.grid(row=3, column=3)
divide.grid(row=4, column=3)
comma.grid(row=4, column=0)
equal.grid(row=5, column=3)

clear.grid(row=5, column=0)
square_root.grid(row=4, column=2)
square.grid(row=5, column=1)
delete.grid(row=5, column=2)

history_btn.grid(row=1, column=4)
del_history_btn.grid(row=2, column=4)

root.mainloop()