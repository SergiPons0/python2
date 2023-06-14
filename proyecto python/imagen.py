import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def cargar_imagen_desde_url(url):
    response = requests.get(url)
    imagen = Image.open(BytesIO(response.content))
    return imagen

def mostrar_imagen():
    url_imagen = entrada_url.get()
    imagen = cargar_imagen_desde_url(url_imagen)
    imagen = imagen.resize((300, 300))  # Ajusta el tamaño de la imagen si es necesario
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta_imagen.configure(image=imagen_tk)
    etiqueta_imagen.image = imagen_tk

ventana = tk.Tk()
ventana.title("Imagen de Internet")

# Crear una etiqueta para mostrar la imagen
etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack(pady=10)

# Crear una entrada de texto para la URL de la imagen
entrada_url = tk.Entry(ventana)
entrada_url.pack(pady=10)

# Crear un botón para cargar la imagen
boton_cargar = tk.Button(ventana, text="Cargar imagen", command=mostrar_imagen)
boton_cargar.pack(pady=10)

ventana.mainloop()

