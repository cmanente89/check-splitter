import tkinter as tk

def probar_tkinter():
    # Creamos la ventana principal
    ventana = tk.Tk()
    ventana.title("Check Splitter - Prueba")
    ventana.geometry("300x200")

    # Añadimos una etiqueta de texto
    etiqueta = tk.Label(ventana, text="¡Todo listo para arrancar!", font=("Arial", 14))
    etiqueta.pack(pady=50)

    # Iniciamos el bucle de la interfaz
    ventana.mainloop()

if __name__ == "__main__":
    probar_tkinter()