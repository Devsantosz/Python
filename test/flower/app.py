import tkinter as tk


janela = tk.Tk()
janela.title("FLOWERS")
janela.geometry("400x400")
janela.configure(bg="#57006d")

container = tk.Frame(
    janela,
    width=300,
    height=200,
    bg="#d60707"
)
container.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(container, text="Usuário").grid(row=0, column=0, sticky="e")
tk.Entry(container).grid(row=0, column=1)

tk.Label(container, text="Senha").grid(row=1, column=0, sticky="e")
tk.Entry(container, show="*").grid(row=1, column=1)


janela.mainloop()