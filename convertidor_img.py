import os
import platform
import subprocess
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image

# Asegúrate de que tkinterdnd2 está instalado
try:
    from tkinterdnd2 import TkinterDnD, DND_FILES
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "tkinterdnd2"])
    from tkinterdnd2 import TkinterDnD, DND_FILES

# Variables globales
ruta_entrada = ""

# Función para manejar archivos arrastrados
def manejar_arrastrar(archivo):
    global ruta_entrada
    ruta_entrada = archivo.strip().replace("{", "").replace("}", "")
    ruta_entrada = os.path.normpath(ruta_entrada)  # Ajusta la ruta para cualquier SO

    if os.path.exists(ruta_entrada):
        drop_area.config(text=f"Archivo seleccionado:\n{ruta_entrada}")
    else:
        ruta_entrada = ""
        messagebox.showerror("Error", "La ruta del archivo no existe o no es válida.")

# Función para seleccionar un archivo manualmente
def seleccionar_archivo():
    global ruta_entrada
    ruta_entrada = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Todos los archivos de imagen", "*.png *.jpg *.jpeg *.bmp *.gif *.webp *.tiff")]
    )
    if ruta_entrada:
        ruta_entrada = os.path.normpath(ruta_entrada)
        drop_area.config(text=f"Archivo seleccionado:\n{ruta_entrada}")

# Función para convertir la imagen
def convertir_imagen():
    global ruta_entrada
    formato_salida = formato_salida_seleccionado.get()

    if not ruta_entrada:
        messagebox.showerror("Error", "Por favor selecciona o arrastra una imagen.")
        return
    if not formato_salida:
        messagebox.showerror("Error", "Por favor selecciona un formato de salida.")
        return

    try:
        if not os.path.exists(ruta_entrada):
            messagebox.showerror("Error", "La ruta del archivo no existe.")
            return

        ruta_salida = filedialog.asksaveasfilename(
            title="Guardar como",
            defaultextension=f".{formato_salida.lower()}",
            filetypes=[(f"Archivos {formato_salida.upper()}", f"*.{formato_salida.lower()}")]
        )

        if not ruta_salida:
            return

        imagen = Image.open(ruta_entrada)

        # Convertir al modo RGB si la imagen tiene canal alfa y se guarda en JPEG
        if formato_salida.upper() == "JPEG" and imagen.mode == "RGBA":
            imagen = imagen.convert("RGB")

        # Guardar imagen
        imagen.save(ruta_salida, format=formato_salida.upper())

        messagebox.showinfo("Éxito", f"Imagen convertida a {formato_salida.upper()} y guardada correctamente.")

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo convertir la imagen: {e}")

# Configurar ventana principal
ventana = TkinterDnD.Tk()
ventana.title("Conversor de Imágenes")
ventana.geometry("500x400")
ventana.resizable(False, False)
ventana.configure(bg="#f4f4f4")

# Encabezado
encabezado = tk.Label(
    ventana, text="EASY CONVERT",
    font=("Helvetica", 16, "bold"), bg="#f4f4f4", fg="#333"
)
encabezado.pack(pady=10)

# Área de arrastrar archivos
drop_area = tk.Label(
    ventana, text="Arrastra aquí tu imagen\n(o haz clic para seleccionar)",
    font=("Helvetica", 12), bg="#90e0ef", fg="#023e8a", relief="groove", width=50, height=5
)
drop_area.pack(pady=20)
drop_area.drop_target_register(DND_FILES)
drop_area.dnd_bind('<<Drop>>', lambda event: manejar_arrastrar(event.data))
drop_area.bind("<Button-1>", lambda event: seleccionar_archivo())

# Selección de formato
etiqueta_salida = tk.Label(
    ventana, text="Selecciona el formato de salida:", font=("Helvetica", 12), bg="#f4f4f4"
)
etiqueta_salida.pack(pady=10)

formatos = ["JPEG", "PNG", "BMP", "GIF", "WEBP", "TIFF"]
formato_salida_seleccionado = ttk.Combobox(ventana, values=formatos, state="readonly")
formato_salida_seleccionado.pack(pady=5)

# Botón de conversión
boton_convertir = tk.Button(
    ventana, text="Convertir Imagen", command=convertir_imagen,
    font=("Helvetica", 12), bg="#0e6d18", fg="white", relief="raised", borderwidth=2
)
boton_convertir.pack(pady=20)

ventana.iconbitmap("C:/xampp/htdocs/Python/logoconverter.ico")
# Inicia el bucle principal
ventana.mainloop()
