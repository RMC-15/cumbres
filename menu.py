import time

import variables
from usuario_dao import UsuarioDAO
from servicio_dao import ServicioDAO
from junta_dao import JuntasDAO
from usuario import Usuario
from servicio import Servicio
from juntas import Juntas
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext


class Cumbres(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.screen = controller
        self.screen.geometry('680x400+400+120')
        self.screen.title('Cumbres')
        self.screen.resizable(0, 1)

        self._tabs()

    def _com_tab1(self, tabulador):
        label1 = ttk.Label(tabulador, text='Pendientes')
        label1.grid(row=0, column=0, sticky='NS', pady=15)
        def actualizar():
            juntas = JuntasDAO.seleccionar()
            self.scroll = scrolledtext.ScrolledText(tabulador, width=80, height=10, wrap=tk.WORD)
            datec = time.strftime('20%y-%m-%d')
            showj = []
            for junta in juntas:
                datej = str(junta[2])
                if datej == datec:
                    asunto = junta[1]
                    showj.append(asunto)
                    showj.append(datej)
                    showj.append(',')
            showj = str(showj).replace(',', '\n')
            showj = showj.replace("'", "")
            showj = showj.replace("[", "")
            showj = showj.replace("]", "")
            self.scroll.insert(tk.INSERT, showj)
            self.scroll.grid(row=1, column=0, padx=10)
            self.scroll.config(state=tk.DISABLED)
        actualizar()
        boton_act = ttk.Button(tabulador, text='Actualizar', command=actualizar, cursor='hand2')
        boton_act.grid(row=2, column=0, sticky='E', padx=15, pady=10)

    def _com_tab2(self, tabulador):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Búsqueda de usuarios
        busqueda = tk.StringVar(value='')
        search_label = ttk.Label(tabulador, text='Buscar personal')
        search_label.grid(row=0, column=1, sticky='NS', pady=15)
        search_entry = ttk.Entry(tabulador, width=40, textvariable=busqueda)
        search_entry.grid(row=1, column=0, columnspan=3, sticky='W', padx=10)

        # Agregar usuarios
        name = tk.StringVar(value='')
        password = tk.StringVar(value='')
        add_label = ttk.Label(tabulador, text='Agregar un trabajador')
        add_label.grid(row=3, column=1, sticky='NS', pady=20)
        add_nom_label = ttk.Label(tabulador, text='Ingresa el usuario del nuevo trabajador')
        add_nom_label.grid(row=4, column=0, sticky='W', padx=10)
        add_pass_label = ttk.Label(tabulador, text='Ingresa la contraseña del nuevo trabajador')
        add_pass_label.grid(row=4, column=2, sticky='E', padx=25)
        add_nom_entry = ttk.Entry(tabulador, width=40)
        add_nom_entry.grid(row=5, column=0, sticky='W', padx=10)
        add_pass_entry = ttk.Entry(tabulador, width=40)
        add_pass_entry.grid(row=5, column=2, sticky='E', padx=25)

        # Editar usuarios
        mod_label = ttk.Label(tabulador, text='Modificar un trabajador')
        mod_label.grid(row=7, column=1, sticky='NS', pady=20)
        mod_id_label = ttk.Label(tabulador, text='Ingresa el número de trabajador')
        mod_id_label.grid(row=8, column=0, sticky='W', padx=10)
        mod_id_entry = ttk.Entry(tabulador, width=10)
        mod_id_entry.grid(row=9, column=0, sticky='W', padx=10, pady=5)
        mod_nom_label = ttk.Label(tabulador, text='Ingresa el nuevo nombre del trabajador')
        mod_nom_label.grid(row=10, column=0, sticky='W', padx=10, pady=5)
        mod_pass_label = ttk.Label(tabulador, text='Ingresa la nueva contraseña del trabajador')
        mod_pass_label.grid(row=10, column=2, sticky='E', padx=25)
        mod_nom_entry = ttk.Entry(tabulador, width=40)
        mod_nom_entry.grid(row=11, column=0, sticky='W', padx=10)
        mod_pass_entry = ttk.Entry(tabulador, width=40)
        mod_pass_entry.grid(row=11, column=2, sticky='W', padx=25)

        # Eliminar usuarios
        del_label = ttk.Label(tabulador, text='Eliminar un trabajador')
        del_label.grid(row=13, column=1, sticky='NS', pady=15)
        del_id_label = ttk.Label(tabulador, text='Ingresa el ID del trabajador')
        del_id_label.grid(row=14, column=0, sticky='W', padx=10)
        del_id_entry = ttk.Entry(tabulador, width=10)
        del_id_entry.grid(row=15, column=0, sticky='W', padx=10)

        def search():
            persona = Usuario(username=busqueda.get())
            if busqueda.get() == '':
                messagebox.showwarning('Falta usuario', 'Debes ingresar el nombre del trabajador o ingresa la palabra "Todos"')
            elif busqueda.get() == 'Todos':
                select_user()
            else:
                search = UsuarioDAO.buscar(persona)
                if search == []:
                    messagebox.showinfo('Sin resultados', 'No se ha encontrado ningún resultado')
                else:
                    self.scroll = scrolledtext.ScrolledText(tabulador, width=28, height=5, wrap=tk.WORD)
                    self.scroll.insert(tk.INSERT, search)
                    self.scroll.grid(row=2, column=0, padx=10)
                    self.scroll.config(state=tk.DISABLED)

        def select_user():
            usuarios = UsuarioDAO.seleccionar()
            self.scroll = scrolledtext.ScrolledText(tabulador, width=28, height=5, wrap=tk.WORD)
            self.scroll.insert(tk.INSERT, usuarios)
            self.scroll.grid(row=2, column=0, padx=10)
            self.scroll.config(state=tk.DISABLED)

        def add():
            add_user = add_nom_entry.get()
            add_pass = add_pass_entry.get()
            if add_user == '':
                messagebox.showwarning('Falta nombre de usuario', 'Debes agregar el nombre de usuario')
            elif add_pass == '':
                messagebox.showwarning('Falta la contraseña del trabajador', 'Debes agregar la contraseña del usuario')
            else:
                usuario = Usuario(username=add_user, password=add_pass)
                usuarios_agregados = UsuarioDAO.insertar(usuario)
                messagebox.showinfo('Añadido', f'Se han agregado {usuarios_agregados} usuarios')

        def mod_user():
            if mod_id_entry.get() == '':
                messagebox.showwarning('Falta ID', 'Debes agregar el número de trabajador')
            elif mod_nom_entry.get() == '':
                messagebox.showwarning('Falta Nombre', 'Debes agregar el nuevo nombre de trabajador')
            elif mod_pass_entry.get() == '':
                messagebox.showwarning('Falta Password', 'Debes agregar la nueva contraseña de trabajador')
            else:
                id = int(mod_id_entry.get())
                usuario = Usuario(id, mod_nom_entry.get(), mod_pass_entry.get())
                usuarios_modificados = UsuarioDAO.actualizar(usuario)
                messagebox.showinfo('Usuarios editados', f'Se han editado {usuarios_modificados} usuarios')

        def del_user():
            if del_id_entry.get() == '':
                messagebox.showwarning('Falta ID', 'Debes agregar el número de trabajador')
            else:
                id = int(del_id_entry.get())
                usuario = Usuario(id_usuario=id)
                usuarios_eliminados = UsuarioDAO.eliminar(usuario)
                messagebox.showinfo('Usuarios eliminados', f'Se han eliminado {usuarios_eliminados} usuarios')

        search_button = ttk.Button(tabulador, text='Buscar', command=search, cursor='hand2')
        search_button.grid(row=1, column=1, sticky='NS', padx=10)
        add_button = ttk.Button(tabulador, text='Agregar', command=add, cursor='hand2')
        add_button.grid(row=6, column=1, sticky='NS', pady=5)
        mod_button = ttk.Button(tabulador, text='Editar', command=mod_user, cursor='hand2')
        mod_button.grid(row=12, column=1, sticky='NS', pady=5)
        del_button = ttk.Button(tabulador, text='Eliminar', command=del_user, cursor='hand2')
        del_button.grid(row=15, column=0)
        #select_button = ttk.Button(tabulador, text='Buscar personal', command=select_user)
        #select_button.grid(row=16, column=0, sticky='E')

    def _com_tab3(self, tabulador):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Búsqueda de servicio
        search_label = ttk.Label(tabulador, text='Buscar Servicio')
        search_label.grid(row=0, column=1, sticky='NS', pady=15)
        search_entry = ttk.Entry(tabulador, width=40)
        search_entry.grid(row=1, column=0, columnspan=3, sticky='W', padx=10)

        # Agregar servicios
        add_label = ttk.Label(tabulador, text='Agregar un servicio')
        add_label.grid(row=3, column=1, sticky='NS', pady=20)
        add_nom_label = ttk.Label(tabulador, text='Ingresa el nuevo servicio')
        add_nom_label.grid(row=4, column=0, sticky='W', padx=10)
        add_pass_label = ttk.Label(tabulador, text='Ingresa el proceso del nuevo servicio')
        add_pass_label.grid(row=4, column=2, sticky='E', padx=25)
        add_note_label = ttk.Label(tabulador, text='Ingresa los detalles del servicio')
        add_note_label.grid(row=6, column=0, sticky='W', padx=10)
        add_nom_entry = ttk.Entry(tabulador, width=40)
        add_nom_entry.grid(row=5, column=0, sticky='W', padx=10)
        add_pass_entry = ttk.Entry(tabulador, width=40)
        add_pass_entry.grid(row=5, column=2, sticky='E', padx=25)
        add_note_entry = ttk.Entry(tabulador, width=40)
        add_note_entry.grid(row=7, column=0, sticky='W', padx=10)

        # Editar usuarios
        mod_label = ttk.Label(tabulador, text='Modificar un servicio')
        mod_label.grid(row=8, column=1, sticky='NS', pady=20)
        mod_id_label = ttk.Label(tabulador, text='Ingresa el número de servicio')
        mod_id_label.grid(row=9, column=0, sticky='W', padx=10)
        mod_id_entry = ttk.Entry(tabulador, width=10)
        mod_id_entry.grid(row=10, column=0, sticky='W', padx=10, pady=5)
        mod_nom_label = ttk.Label(tabulador, text='Ingresa el nuevo servicio')
        mod_nom_label.grid(row=11, column=0, sticky='W', padx=10, pady=5)
        mod_pass_label = ttk.Label(tabulador, text='Ingresa el proceso del nuevo servicio')
        mod_pass_label.grid(row=11, column=2, sticky='E', padx=25)
        mod_note_label = ttk.Label(tabulador, text='Ingresa los detalles del nuevo servicio')
        mod_note_label.grid(row=13, column=0, sticky='W', padx=10)
        mod_nom_entry = ttk.Entry(tabulador, width=40)
        mod_nom_entry.grid(row=12, column=0, sticky='W', padx=10)
        mod_pass_entry = ttk.Entry(tabulador, width=40)
        mod_pass_entry.grid(row=12, column=2, sticky='W', padx=25)
        mod_note_entry = ttk.Entry(tabulador, width=40)
        mod_note_entry.grid(row=14, column=0, sticky='W', padx=10)

        # Eliminar usuarios
        del_label = ttk.Label(tabulador, text='Eliminar un servicio')
        del_label.grid(row=15, column=1, sticky='NS', pady=15)
        del_id_label = ttk.Label(tabulador, text='Ingresa el ID del servicio')
        del_id_label.grid(row=16, column=0, sticky='W', padx=10)
        del_id_entry = ttk.Entry(tabulador, width=10)
        del_id_entry.grid(row=17, column=0, sticky='W', padx=10)

        def search():
            servicio = Servicio(nombre_servicio=search_entry.get())
            if search_entry.get() == '':
                messagebox.showwarning('Falta servicio', 'Debes ingresar el servicio o ingresa la palabra "Todos"')
            elif search_entry.get() == 'Todos':
                select_service()
            else:
                search = ServicioDAO.buscar(servicio)
                if search == []:
                    messagebox.showinfo('Sin resultados', 'No se ha encontrado ningún resultado')
                else:
                    self.scroll = scrolledtext.ScrolledText(tabulador, width=28, height=5, wrap=tk.WORD)
                    self.scroll.insert(tk.INSERT, search)
                    self.scroll.grid(row=2, column=0, padx=10)
                    self.scroll.config(state=tk.DISABLED)

        def select_service():
            servicios = ServicioDAO.seleccionar()
            self.scroll = scrolledtext.ScrolledText(tabulador, width=28, height=5, wrap=tk.WORD)
            self.scroll.insert(tk.INSERT, servicios)
            self.scroll.grid(row=2, column=0, padx=10)
            self.scroll.config(state=tk.DISABLED)

        def add():
            add_user = add_nom_entry.get()
            add_pass = add_pass_entry.get()
            add_note = add_note_entry.get()
            if add_user == '':
                messagebox.showwarning('Falta servicio', 'Debes agregar el servicio')
            elif add_pass == '':
                messagebox.showwarning('Falta el proceso del servicio', 'Debes agregar el proceso del servicio')
            else:
                if add_note == '':
                    messagebox.showinfo('Faltan detalles', 'Si desea agregar detalles puede modificar el proceso')
                servicio = Servicio(nombre_servicio=add_user, proceso=add_pass, notas=add_note)
                servicios_agregados = ServicioDAO.insertar(servicio)
                messagebox.showinfo('Añadido', f'Se han agregado {servicios_agregados} servicio')

        def mod_service():
            if mod_id_entry.get() == '':
                messagebox.showwarning('Falta ID', 'Debes agregar el número de servicio')
            elif mod_nom_entry.get() == '':
                messagebox.showwarning('Falta Servicio', 'Debes agregar el nuevo servicio')
            elif mod_pass_entry.get() == '':
                messagebox.showwarning('Falta Proceso', 'Debes agregar el nuevo proceso del servicio')
            else:
                if mod_note_entry == '':
                    messagebox.showinfo('Faltan detalles', 'Si desea agregar detalles puede modificar el proceso')
                id = int(mod_id_entry.get())
                servicio = Servicio(id, mod_nom_entry.get(), mod_pass_entry.get(), mod_note_entry.get())
                servicios_modificados = ServicioDAO.actualizar(servicio)
                messagebox.showinfo('Servicios editados', f'Se ha editado {servicios_modificados} servicio')

        def del_service():
            if del_id_entry.get() == '':
                messagebox.showwarning('Falta ID', 'Debes agregar el número de servicio')
            else:
                id = int(del_id_entry.get())
                servicio = Servicio(id_servicios=id)
                servicios_eliminados = ServicioDAO.eliminar(servicio)
                messagebox.showinfo('Servicios eliminados', f'Se han eliminado {servicios_eliminados} servicio')

        search_button = ttk.Button(tabulador, text='Buscar', command=search, cursor='hand2')
        search_button.grid(row=1, column=1, sticky='NS', padx=10)
        add_button = ttk.Button(tabulador, text='Agregar', command=add, cursor='hand2')
        add_button.grid(row=7, column=1, sticky='NS', pady=5)
        mod_button = ttk.Button(tabulador, text='Editar', command=mod_service, cursor='hand2')
        mod_button.grid(row=14, column=1, sticky='NS', pady=5)
        del_button = ttk.Button(tabulador, text='Eliminar', command=del_service, cursor='hand2')
        del_button.grid(row=17, column=0)

    def _com_tab4(self, tabulador):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Búsqueda de juntas
        search = tk.StringVar(value='')
        search_label = ttk.Label(tabulador, text='Buscar junta')
        search_label.grid(row=0, column=1, sticky='NS', pady=15)
        search_entry = ttk.Entry(tabulador, width=40, textvariable=search)
        search_entry.grid(row=1, column=0, columnspan=3, sticky='W', padx=10)

        # Agregar juntas
        add_label = ttk.Label(tabulador, text='Agregar junta')
        add_label.grid(row=3, column=1, sticky='NS', pady=20)
        add_nom_label = ttk.Label(tabulador, text='Ingresa asunto de junta')
        add_nom_label.grid(row=4, column=0, sticky='W', padx=10)
        add_pass_label = ttk.Label(tabulador, text='Ingresa la fecha programada (dd/mm/aaaa)')
        add_pass_label.grid(row=4, column=2, sticky='E', padx=25)
        add_nom_entry = ttk.Entry(tabulador, width=40)
        add_nom_entry.grid(row=5, column=0, sticky='W', padx=10)
        add_pass_entry = ttk.Entry(tabulador, width=40)
        add_pass_entry.grid(row=5, column=2, sticky='E', padx=25)

        # Editar juntas
        mod_label = ttk.Label(tabulador, text='Modificar una junta')
        mod_label.grid(row=7, column=1, sticky='NS', pady=20)
        mod_id_label = ttk.Label(tabulador, text='Ingresa el folio de junta')
        mod_id_label.grid(row=8, column=0, sticky='W', padx=10)
        mod_id_entry = ttk.Entry(tabulador, width=10)
        mod_id_entry.grid(row=9, column=0, sticky='W', padx=10, pady=5)
        mod_nom_label = ttk.Label(tabulador, text='Ingresa el nuevo asunto de junta')
        mod_nom_label.grid(row=10, column=0, sticky='W', padx=10, pady=5)
        mod_pass_label = ttk.Label(tabulador, text='Ingresa la nueva fecha programada')
        mod_pass_label.grid(row=10, column=2, sticky='E', padx=25)
        mod_nom_entry = ttk.Entry(tabulador, width=40)
        mod_nom_entry.grid(row=11, column=0, sticky='W', padx=10)
        mod_pass_entry = ttk.Entry(tabulador, width=40)
        mod_pass_entry.grid(row=11, column=2, sticky='W', padx=25)

        # Eliminar juntas
        del_label = ttk.Label(tabulador, text='Eliminar junta')
        del_label.grid(row=13, column=1, sticky='NS', pady=15)
        del_id_label = ttk.Label(tabulador, text='Ingresa el folio de la junta')
        del_id_label.grid(row=14, column=0, sticky='W', padx=10)
        del_id_entry = ttk.Entry(tabulador, width=10)
        del_id_entry.grid(row=15, column=0, sticky='W', padx=10)

        def search():
            juntas = Juntas(junta=search_entry.get())
            if search_entry.get() == '':
                messagebox.showwarning('Falta asunto', 'Debes ingresar el asunto de una junta o ingresa la palabra "Todas"')
            elif search_entry.get() == 'Todas':
                select_junta()
            else:
                search = JuntasDAO.buscar(juntas)
                if search == []:
                    messagebox.showinfo('Sin resultados', 'No se ha encontrado ningúna junta')
                else:
                    self.scroll = scrolledtext.ScrolledText(tabulador, width=28, height=5, wrap=tk.WORD)
                    self.scroll.insert(tk.INSERT, search)
                    self.scroll.grid(row=2, column=0, padx=10)
                    self.scroll.config(state=tk.DISABLED)

        def select_junta():
            juntas = JuntasDAO.seleccionar()
            self.scroll = scrolledtext.ScrolledText(tabulador, width=28, height=5, wrap=tk.WORD)
            self.scroll.insert(tk.INSERT, juntas)
            self.scroll.grid(row=2, column=0, padx=10)
            self.scroll.config(state=tk.DISABLED)

        def add():
            add_junta = add_nom_entry.get()
            add_fecha = add_pass_entry.get()
            if add_junta == '':
                messagebox.showwarning('Falta asunto de junta', 'Debes agregar un asunto de junta')
            elif add_fecha == '':
                messagebox.showwarning('Falta fecha', 'Debes agregar la fecha programada')
            else:
                junta = Juntas(junta=add_junta, fecha_junta=add_fecha)
                juntas_agregadas = JuntasDAO.insertar(junta)
                messagebox.showinfo('Añadido', f'Se han agregado {juntas_agregadas} juntas')

        def mod_junta():
            if mod_id_entry.get() == '':
                messagebox.showwarning('Falta Folio', 'Debes agregar el folio de la junta')
            elif mod_nom_entry.get() == '':
                messagebox.showwarning('Falta Asunto', 'Debes agregar el nuevo asunto de la junta')
            elif mod_pass_entry.get() == '':
                messagebox.showwarning('Falta Fecha', 'Debes agregar la nueva fecha programada')
            else:
                fol = int(mod_id_entry.get())
                junta = Juntas(fol, mod_nom_entry.get(), mod_pass_entry.get())
                juntas_modificadas = JuntasDAO.actualizar(junta)
                messagebox.showinfo('Juntas editadas', f'Se han editado {juntas_modificadas} juntas')

        def del_junta():
            if del_id_entry.get() == '':
                messagebox.showwarning('Falta Folio', 'Debes agregar el folio de la junta')
            else:
                fol = int(del_id_entry.get())
                junta = Juntas(id_junta=fol)
                juntas_eliminadas = JuntasDAO.eliminar(junta)
                messagebox.showinfo('Juntas eliminadas', f'Se han eliminado {juntas_eliminadas} juntas')

        search_button = ttk.Button(tabulador, text='Buscar', command=search, cursor='hand2')
        search_button.grid(row=1, column=1, sticky='NS', padx=10)
        add_button = ttk.Button(tabulador, text='Agregar', command=add, cursor='hand2')
        add_button.grid(row=6, column=1, sticky='NS', pady=5)
        mod_button = ttk.Button(tabulador, text='Editar', command=mod_junta, cursor='hand2')
        mod_button.grid(row=12, column=1, sticky='NS', pady=5)
        del_button = ttk.Button(tabulador, text='Eliminar', command=del_junta, cursor='hand2')
        del_button.grid(row=15, column=0)

    def _tabs(self):
        menu = ttk.Notebook(self)
        date = time.strftime('%d/%m/20%y')
        tab1 = ttk.LabelFrame(menu, text=f'Hoy {date} tienes:')
        menu.add(tab1, text=f'Bienvenida...')
        print(variables.userp)
        menu.pack(fill='both')
        self._com_tab1(tab1)
        tab2 = ttk.Frame(menu)
        menu.add(tab2, text='Personal')
        self._com_tab2(tab2)
        tab3 = ttk.Frame(menu)
        menu.add(tab3, text='Servicios')
        self._com_tab3(tab3)
        tab4 = ttk.Frame(menu)
        menu.add(tab4, text='Juntas')
        self._com_tab4(tab4)

if __name__ == '__main__':
    screen = Cumbres()
    screen.mainloop()