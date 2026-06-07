import tkinter as tk
from diners_model import CheckSplitterModel
from gui import CheckSplitterGUI

def main():
    # 1. Creamos la ventana base de Tkinter
    root = tk.Tk()
    
    # 2. Inicializamos el modelo (el cerebro)
    model = CheckSplitterModel()
    
    # 3. Inicializamos la interfaz gráfica pasándole la ventana y el modelo
    app = CheckSplitterGUI(root, model)
    
    # 4. Encendemos el bucle de la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()