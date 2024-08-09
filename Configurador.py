import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import yaml
import os

CONFIG_FILE = 'config.yaml'

def set_style():
    style = ttk.Style()
    """
    Configura un estilo moderno para los widgets de ttk.
    """
    style.theme_use('clam')  # Usar 'clam' como tema base

    # Configuración de estilo para botones
    style.configure('TButton',
                    font=('Segoe UI', 9, 'bold'),  # Tamaño de fuente reducido
                    foreground='#ffffff',
                    background='#0078D7',
                    borderwidth=0,
                    focuscolor='none',
                    padding=5)  # Acolchado reducido
    style.map('TButton',
            background=[('active', '#005A9E'), ('pressed', '#004578')],
            foreground=[('disabled', '#888888')])

    # Configuración de estilo para cuadros de texto
    style.configure('TEntry',
                    font=('Segoe UI', 10),
                    foreground='#333333',
                    fieldbackground='#ffffff',
                    bordercolor='#cccccc',
                    borderwidth=1,
                    focusthickness=2,
                    focuscolor='#0078D7',
                    padding=5)

    # Configuración de estilo para etiquetas
    style.configure('TLabel',
                    font=('Segoe UI', 10),
                    foreground='#333333',
                    background='#f7f7f7')

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {'configurations': [], 'wait_time': 10}  # Valor por defecto si no existe el archivo
    with open(CONFIG_FILE, 'r') as file:
        return yaml.safe_load(file)

def add_row(folder="", filename="", extension=""):
    # Permite al usuario seleccionar un directorio si no se proporciona uno
    if not folder:
        folder = filedialog.askdirectory(title="Seleccione la carpeta de origen")
        if not folder:
            messagebox.showerror("Error", "La carpeta es un campo obligatorio.")
            return
    # Inserta una nueva fila en la tabla con los valores proporcionados o por defecto
    table.insert("", "end", values=(folder, filename, extension))

def save_config():
    # Recopila los datos de todas las filas de la tabla
    rows = table.get_children()
    config_data = []
    for row in rows:
        folder, filename, extension = table.item(row, 'values')
        config_data.append({
            'folder': folder,
            'filename': filename if filename else '*',
            'extension': extension if extension else '*',
        })
    
    # Guarda la configuración en un archivo YAML
    config = {
        'configurations': config_data,
        'wait_time': wait_time_var.get()
    }
    
    with open(CONFIG_FILE, 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
    
    messagebox.showinfo("Información", "Configuración guardada exitosamente en config.yaml")

def on_double_click(event):
    # Verifica si hay algún elemento seleccionado
    selected_items = table.selection()
    if not selected_items:
        return  # No hay ninguna fila seleccionada, salir de la función

    item = selected_items[0]
    column = table.identify_column(event.x)
    
    # Define la columna y fila del elemento
    x, y, width, height = table.bbox(item, column)
    
    # Define el índice de la columna basado en la identificación de la columna
    column_index = int(column.replace('#', '')) - 1

    # Crea un Entry en el lugar del elemento para permitir la edición
    entry_edit = tk.Entry(root)
    entry_edit.place(x=x + 10, y=y + 30, width=width)
    
    # Inicializa el Entry con el valor actual del elemento
    current_value = table.item(item, 'values')[column_index]
    entry_edit.insert(0, current_value)

    # Define qué hacer cuando se completa la edición
    def on_entry_edit(event):
        # Actualiza el valor del elemento con el nuevo valor ingresado
        new_value = entry_edit.get()
        current_values = list(table.item(item, 'values'))
        current_values[column_index] = new_value
        table.item(item, values=current_values)
        # Elimina el Entry una vez se termina de editar
        entry_edit.destroy()

    # Liga la función a la tecla Enter, para aplicar la edición
    entry_edit.bind('<Return>', on_entry_edit)
    entry_edit.focus()

def load_initial_data():
    # Carga las configuraciones existentes al inicio
    config = load_config()
    configurations = config.get('configurations', [])
    wait_time = config.get('wait_time', 10)
    
    for conf in configurations:
        add_row(conf['folder'], conf['filename'], conf['extension'])
    
    wait_time_var.set(wait_time)

# Crear la ventana principal
root = tk.Tk()
root.title("Configuración de Archivos")

# Establecer tamaño inicial y tamaño mínimo
root.geometry("800x400")  # Tamaño inicial: 800x600 píxeles
root.minsize(650, 400)    # Tamaño mínimo: 600x400 píxeles

# Aplicar estilo moderno
set_style()

# Tabla para ingresar datos
table = ttk.Treeview(root, columns=("Carpeta", "Nombre del Archivo", "Extensión"), show="headings")
table.heading("Carpeta", text="Carpeta")
table.heading("Nombre del Archivo", text="Nombre del Archivo")
table.heading("Extensión", text="Extensión")
table.pack(fill=tk.BOTH, expand=True)

# Frame para contener los controles
control_frame = ttk.Frame(root)
control_frame.pack(fill=tk.X)

# Botón para añadir filas
add_row_button = ttk.Button(control_frame, text="Añadir Fila", command=add_row)
add_row_button.pack(side=tk.LEFT, padx=5, pady=5)

# Variable para el tiempo de espera
wait_time_var = tk.IntVar()
wait_time_selector_label = ttk.Label(control_frame, text="Tiempo de Espera (segundos)")
wait_time_selector_label.pack(side=tk.LEFT, padx=5)

wait_time_selector = ttk.Spinbox(control_frame, from_=1, to=60, textvariable=wait_time_var, width=5)
wait_time_selector.pack(side=tk.LEFT, padx=5)

# Botón para guardar configuración
save_button = ttk.Button(control_frame, text="Guardar Configuración", command=save_config)
save_button.pack(side=tk.LEFT, padx=5)

# Cargar los datos iniciales
load_initial_data()

# Ejecutar la aplicación
root.mainloop()