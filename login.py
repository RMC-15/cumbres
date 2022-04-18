import tkinter as tk
from tkinter import ttk, messagebox

import variables
from usuario import Usuario
from usuario_dao import UsuarioDAO

class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.geometry('300x130')
        self.controller.title('Login')
        self.controller.resizable(0, 0)

        self.controller.rowconfigure(0, weight=1)
        self.controller.rowconfigure(1, weight=1)
        self.controller.rowconfigure(2, weight=2)
        self.controller.columnconfigure(0, weight=1)
        self.controller.columnconfigure(1, weight=3)

        self._crear_componentes()

    def _crear_componentes(self):
        offset = 250

        imagen = tk.PhotoImage(file='python-logo.png')
        def mostrar_titulo():
            messagebox.showinfo('Más info...', f'Hecho con python... {imagen.cget("file")}')
        boton_imagen = ttk.Button(self, image=imagen, command=mostrar_titulo, cursor='hand2')
        boton_imagen.grid(row=0, column=1)

        label_user = tk.Label(self, text='Usuario:')
        label_user.grid(row=1, column=1, sticky='WE', padx=offset)

        label_pass = tk.Label(self, text='Password:')
        label_pass.grid(row=3, column=1, sticky='WE', padx=offset)

        self.in_user = ttk.Entry(self, width=30, justify=tk.CENTER)
        self.in_user.grid(row=2, column=1, padx=offset, sticky='WE', pady=5)

        self.in_pass = ttk.Entry(self, width=30, justify=tk.CENTER, show='*')
        self.in_pass.grid(row=4, column=1, padx=offset, sticky='WE', pady=5)

        button_log = ttk.Button(self, text='Login', command=self._evaluar, cursor='hand2')
        button_log.grid(row=5, column=1, sticky='WE', padx=offset, pady=10)

    def _evaluar(self):
        def search_db():
            usuario = Usuario(username=self.in_user.get())
            usuarios = UsuarioDAO.login(usuario)
            for usuario in usuarios:
                _, user, password = usuario[0], usuario[1], usuario[2]
                if self.in_user.get() == user:
                    variables.userp = user
                    if self.in_pass.get() == password:
                        messagebox.showinfo('Entrando...', 'Accediendo')
                        self.controller.show_frame("Cumbres")
                        return
                    messagebox.showwarning('Warning', 'Contraseña errónea')
            messagebox.showwarning('Warning', 'Verifica datos ingresados')
        if self.in_user.get() == '':
            messagebox.showwarning('Falta usuario', 'Ingresa un Usuario')
        elif self.in_pass.get() == '':
            messagebox.showwarning('Falta usuario', 'Ingresa una contraseña')
        else:
            search_db()

if __name__ == '__main__':
    login_ventana = Login()
    login_ventana.mainloop()