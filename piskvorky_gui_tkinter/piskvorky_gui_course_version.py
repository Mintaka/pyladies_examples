""" 
Rozpracovaná verze GUI pro 1D piškvorky, tak jak jsme s ní končili na 
lekci Pyladies 7.5.2019

Na ni navazuje propracovanější verze.
"""


from tkinter import Tk, ttk, RIGHT, LEFT, X, Y, Frame, SUNKEN, StringVar

def test():
    print("test ", int(velikost_hry.get()))

root = Tk()

label = ttk.Label(root, text="1D piškvorky")
label.pack()

button = ttk.Button(root, text="Nová hra", command=test)
button.pack()

label = ttk.Label(root, text="Velikost hry")
label.pack()

velikost_hry = StringVar()
entry = ttk.Entry(root,  width=3, textvariable=velikost_hry)
entry.pack()
velikost_hry.set("7")

print("obsah pole:", entry.get())

label2 = ttk.Label(root, text="Klikněte na pole, na které chce hrát.")
label2.pack()

button = ttk.Button(root, text="Konec hry", command=exit)
button.pack()

frame1 = Frame(height=2, bd=1, relief=SUNKEN).pack(fill=X, padx=5, pady=5)

for i in range(3):
    button_gen = ttk.Button(frame1, text="Generované tlačítko "+str(i))
    button_gen.pack(padx=5, pady=50, side=LEFT)

root.mainloop()
