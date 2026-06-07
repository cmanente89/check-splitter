import tkinter as tk
from tkinter import ttk, messagebox

class CheckSplitterGUI:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        
        self.root.title("Check Splitter 💵")
        self.root.geometry("500x600")
        self.root.configure(bg="#f5f6fa")
        
        # Estilo para las pestañas
        style = ttk.Style()
        style.configure("TNotebook", background="#f5f6fa")
        style.configure("TNotebook.Tab", font=("Arial", 11))

        # Creación del contenedor de pestañas (Notebook)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Crear los contenedores para cada pestaña
        self.tab_simple = tk.Frame(self.notebook, bg="#f5f6fa")
        self.tab_advanced = tk.Frame(self.notebook, bg="#f5f6fa")
        
        # Añadir las pestañas al Notebook
        self.notebook.add(self.tab_simple, text=" Simple Split ")
        self.notebook.add(self.tab_advanced, text=" Advanced Split (By Diner) ")
        
        # Inicializar los componentes de cada pestaña
        self.build_simple_tab()
        self.build_advanced_tab()

    # ==========================================
    # PESTAÑA 1: DIVISIÓN SIMPLE
    # ==========================================
    def build_simple_tab(self):
        # Título
        lbl_title = tk.Label(self.tab_simple, text="Simple Bill Splitter", font=("Arial", 16, "bold"), bg="#f5f6fa", fg="#2c3e50")
        lbl_title.pack(pady=20)
        
        # Monto Total
        lbl_total = tk.Label(self.tab_simple, text="Total Bill Amount ($):", font=("Arial", 11), bg="#f5f6fa")
        lbl_total.pack(pady=2)
        self.entry_simple_total = tk.Entry(self.tab_simple, font=("Arial", 11), justify="center")
        self.entry_simple_total.pack(pady=5)
        
        # Cantidad de personas
        lbl_diners = tk.Label(self.tab_simple, text="Number of Diners:", font=("Arial", 11), bg="#f5f6fa")
        lbl_diners.pack(pady=2)
        self.entry_simple_diners = tk.Entry(self.tab_simple, font=("Arial", 11), justify="center")
        self.entry_simple_diners.pack(pady=5)
        
        # Botón Calcular
        btn_calc = tk.Button(self.tab_simple, text="Calculate", font=("Arial", 11, "bold"), bg="#2ecc71", fg="white", padx=10, pady=5, command=self.calculate_simple)
        btn_calc.pack(pady=20)
        
        # Resultado
        self.lbl_simple_result = tk.Label(self.tab_simple, text="Enter values to calculate", font=("Arial", 12, "italic"), bg="#f5f6fa", fg="#7f8c8d")
        self.lbl_simple_result.pack(pady=20)

    def calculate_simple(self):
        try:
            total = float(self.entry_simple_total.get())
            diners_count = int(self.entry_simple_diners.get())
            
            if diners_count <= 0:
                messagebox.showerror("Error", "Diners must be greater than 0.")
                return
                
            amount_per_person = total / diners_count
            self.lbl_simple_result.config(
                text=f"Each person pays:\n${amount_per_person:.2f}", 
                font=("Arial", 14, "bold"), 
                fg="#27ae60"
            )
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers.")

    # ==========================================
    # PESTAÑA 2: DIVISIÓN AVANZADA (Marcador de posición por ahora)
    # ==========================================
    def build_advanced_tab(self):
        lbl_title = tk.Label(self.tab_advanced, text="Advanced Split (Item by Item)", font=("Arial", 16, "bold"), bg="#f5f6fa", fg="#2c3e50")
        lbl_title.pack(pady=20)
        
        lbl_coming_soon = tk.Label(self.tab_advanced, text="Here we will wire our diners list and item loader!", font=("Arial", 11, "italic"), bg="#f5f6fa", fg="#7f8c8d")
        lbl_coming_soon.pack(pady=50)