import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def cargar_imagen_desde_url(url):
    response = requests.get(url)
    imagen = Image.open(BytesIO(response.content))
    return imagen

ventana = tk.Tk()
ventana.title("Ventana con imagen")

url_imagen = "https://media.gq.com.mx/photos/5ffb662e9274cd36fe35683c/16:9/w_2560%2Cc_limit/messi-cerveza-goles-porteros.jpg"  # Reemplaza con la URL de la imagen que desees mostrar

imagen = cargar_imagen_desde_url(url_imagen)
imagen_tk = ImageTk.PhotoImage(imagen)

label = tk.Label(ventana, image=imagen_tk)
label.pack()

ventana.mainloop()
