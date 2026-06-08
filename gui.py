
import tkinter as tk
from tkinter import ttk, messagebox

class CheckSplitterGUI:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        
        self.root.title("Check Splitter 💵")
        self.root.geometry("650x700")  # Ventana más ancha para evitar saltos de línea
        self.root.configure(bg="#f5f6fa")
        
        # Estilo para las pestañas
        style = ttk.Style()
        style.configure("TNotebook", background="#f5f6fa")
        style.configure("TNotebook.Tab", font=("Arial", 11))

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.tab_simple = tk.Frame(self.notebook, bg="#f5f6fa")
        self.tab_advanced = tk.Frame(self.notebook, bg="#f5f6fa")
        
        self.notebook.add(self.tab_simple, text=" Simple Split ")
        self.notebook.add(self.tab_advanced, text=" Advanced Split (By Diner) ")
        
        self.build_simple_tab()
        self.build_advanced_tab()

    # ==========================================
    # PESTAÑA 1: DIVISIÓN SIMPLE
    # ==========================================
    def build_simple_tab(self):
        lbl_title = tk.Label(self.tab_simple, text="Simple Bill Splitter", font=("Arial", 16, "bold"), bg="#f5f6fa", fg="#2c3e50")
        lbl_title.pack(pady=20)
        
        lbl_total = tk.Label(self.tab_simple, text="Total Bill Amount ($):", font=("Arial", 11), bg="#f5f6fa")
        lbl_total.pack(pady=2)
        self.entry_simple_total = tk.Entry(self.tab_simple, font=("Arial", 11), justify="center")
        self.entry_simple_total.pack(pady=5)
        
        lbl_diners = tk.Label(self.tab_simple, text="Number of Diners:", font=("Arial", 11), bg="#f5f6fa")
        lbl_diners.pack(pady=2)
        self.entry_simple_diners = tk.Entry(self.tab_simple, font=("Arial", 11), justify="center")
        self.entry_simple_diners.pack(pady=5)
        
        # Atajos de Enter en Pestaña Simple
        self.entry_simple_total.bind("<Return>", lambda event: self.entry_simple_diners.focus())
        self.entry_simple_diners.bind("<Return>", lambda event: self.calculate_simple())

        btn_calc = tk.Button(self.tab_simple, text="Calculate", font=("Arial", 11, "bold"), bg="#2ecc71", fg="white", padx=10, pady=5, command=self.calculate_simple)
        btn_calc.pack(pady=20)
        
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
    # PESTAÑA 2: DIVISIÓN AVANZADA
    # ==========================================
    def build_advanced_tab(self):
        # --- SECCIÓN 1: AGREGAR COMENSALES ---
        frame_diners = tk.LabelFrame(self.tab_advanced, text=" 1. Add Diners to the Table ", font=("Arial", 10, "bold"), bg="#f5f6fa", fg="#2c3e50")
        frame_diners.pack(fill="x", padx=15, pady=5)

        self.entry_diner_name = tk.Entry(frame_diners, font=("Arial", 11))
        self.entry_diner_name.pack(side="left", padx=10, pady=10, expand=True, fill="x")
        self.entry_diner_name.bind("<Return>", lambda event: self.gui_add_diner())  # Enter para agregar amigo

        btn_add_diner = tk.Button(frame_diners, text="Add Diner", font=("Arial", 10, "bold"), bg="#3498db", fg="white", command=self.gui_add_diner)
        btn_add_diner.pack(side="right", padx=10, pady=10)

        # --- SECCIÓN NUEVA: CONFIGURACIÓN DE TIP GLOBAL ---
        frame_tip = tk.LabelFrame(self.tab_advanced, text=" Tip Settings ", font=("Arial", 10, "bold"), bg="#f5f6fa", fg="#2c3e50")
        frame_tip.pack(fill="x", padx=15, pady=5)
        
        lbl_tip_desc = tk.Label(frame_tip, text="Select Tip Percentage for the table:", font=("Arial", 10), bg="#f5f6fa")
        lbl_tip_desc.pack(side="left", padx=10, pady=5)
        
        self.tip_var = tk.StringVar(value="10")
        self.combo_tip = ttk.Combobox(frame_tip, textvariable=self.tip_var, values=["0", "10", "15", "20"], width=5, state="readonly")
        self.combo_tip.pack(side="left", padx=5, pady=5)
        self.combo_tip.bind("<<ComboboxSelected>>", self.gui_change_tip)

        # --- SECCIÓN 2: CARGAR ÍTEMS ---
        frame_items = tk.LabelFrame(self.tab_advanced, text=" 2. Load Item & Assign Sharing ", font=("Arial", 10, "bold"), bg="#f5f6fa", fg="#2c3e50")
        frame_items.pack(fill="x", padx=15, pady=5)

        lbl_item_desc = tk.Label(frame_items, text="Item Description (e.g., Drinks, Pizza):", font=("Arial", 10), bg="#f5f6fa")
        lbl_item_desc.pack(anchor="w", padx=10, pady=2)
        self.entry_item_desc = tk.Entry(frame_items, font=("Arial", 11))
        self.entry_item_desc.pack(fill="x", padx=10, pady=2)
        self.entry_item_desc.bind("<Return>", lambda event: self.entry_item_amount.focus())  # Enter salta al monto

        lbl_item_amount = tk.Label(frame_items, text="Item Amount ($):", font=("Arial", 10), bg="#f5f6fa")
        lbl_item_amount.pack(anchor="w", padx=10, pady=2)
        self.entry_item_amount = tk.Entry(frame_items, font=("Arial", 11))
        self.entry_item_amount.pack(fill="x", padx=10, pady=2)
        self.entry_item_amount.bind("<Return>", lambda event: self.gui_load_item())  # Enter carga el ítem

        lbl_share = tk.Label(frame_items, text="Who shared this item?", font=("Arial", 10), bg="#f5f6fa")
        lbl_share.pack(anchor="w", padx=10, pady=3)
        
        self.frame_checkboxes = tk.Frame(frame_items, bg="#f5f6fa")
        self.frame_checkboxes.pack(fill="x", padx=10, pady=3)
        
        self.diner_checkbox_vars = {}

        # Botón único corregido
        btn_load_item = tk.Button(frame_items, text="Load Item", font=("Arial", 10, "bold"), bg="#e67e22", fg="white", command=self.gui_load_item)
        btn_load_item.pack(fill="x", padx=10, pady=10)

        # --- SECCIÓN 3: RESUMEN EN VIVO ---
        frame_summary = tk.LabelFrame(self.tab_advanced, text=" 3. Live Bill Summary ", font=("Arial", 10, "bold"), bg="#f5f6fa", fg="#2c3e50")
        frame_summary.pack(fill="both", expand=True, padx=15, pady=5)

        # Cambiamos a una altura mayor y barra de scroll por si la cuenta es larga
        self.txt_summary = tk.Text(frame_summary, font=("Courier", 10), height=14, bg="white", state="disabled")
        self.txt_summary.pack(fill="both", expand=True, padx=10, pady=10)

    # ==========================================
    # FUNCIONES DE CONTROL
    # ==========================================
    def gui_add_diner(self):
        name = self.entry_diner_name.get().strip()
        if not name:
            messagebox.showwarning("Warning", "Diner name cannot be empty.")
            return

        success, message = self.model.add_diner(name)
        if success:
            self.entry_diner_name.delete(0, tk.END)
            self.update_checkboxes()
            self.update_live_summary()
        else:
            messagebox.showerror("Error", message)

    def gui_change_tip(self, event=None):
        percentage = self.combo_tip.get()
        self.model.set_global_tip(percentage)
        self.update_live_summary()

    def update_checkboxes(self):
        for widget in self.frame_checkboxes.winfo_children():
            widget.destroy()
        
        self.diner_checkbox_vars.clear()

        for diner in self.model.diners:
            name = diner["name"]
            var = tk.BooleanVar(value=True)
            self.diner_checkbox_vars[name] = var
            
            cb = tk.Checkbutton(self.frame_checkboxes, text=name, variable=var, font=("Arial", 10), bg="#f5f6fa")
            cb.pack(side="left", padx=5)

    def gui_load_item(self):
        description = self.entry_item_desc.get().strip()
        if not description:
            messagebox.showwarning("Warning", "Please enter an item description.")
            return

        try:
            amount = float(self.entry_item_amount.get())
            if amount <= 0:
                messagebox.showwarning("Warning", "Amount must be greater than 0.")
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")
            return

        friends_sharing = [name for name, var in self.diner_checkbox_vars.items() if var.get()]
        
        success, message = self.model.load_item(description, amount, friends_sharing)
        if success:
            self.entry_item_desc.delete(0, tk.END)
            self.entry_item_amount.delete(0, tk.END)
            self.entry_item_desc.focus()  # Devuelve el foco arriba para seguir cargando ágilmente
            self.update_live_summary()
        else:
            messagebox.showerror("Error", message)

    def update_live_summary(self):
        results, grand_total, history = self.model.get_results()
        
        self.txt_summary.config(state="normal")
        self.txt_summary.delete("1.0", tk.END)
        
        if not results:
            self.txt_summary.insert(tk.END, "No diners added yet.")
            self.txt_summary.config(state="disabled")
            return

        summary_text = ""

        # --- BLOQUE A: HISTORIAL DE ÍTEMS ---
        if history:
            summary_text += "--- LOADED ITEMS HISTORY ---\n"
            for item in history:
                shared_str = ", ".join(item['shared_by'])
                summary_text += f" • {item['desc']:<15} ${item['amount']:>8.2f}  [Shared by: {shared_str}]\n"
            summary_text += "\n"

        # --- BLOQUE B: TOTALES POR PERSONA ---
        summary_text += "--- INDIVIDUAL TOTALS ---\n"
        tip_label = f"Tip ({int(self.model.global_tip_percentage)}%)"
        summary_text += f"{'Diner':<15} | {'Subtotal':<11} | {tip_label:<10} | {'Total':<11}\n"
        summary_text += "-" * 60 + "\n"
        
        for r in results:
            summary_text += f"{r['name']:<15} | ${r['subtotal']:<10.2f} | ${r['tip']:<9.2f} | ${r['total']:<10.2f}\n"
            
        summary_text += "-" * 60 + "\n"
        summary_text += f"{'GRAND TOTAL COLLECTED:':<43} ${grand_total:.2f}\n"
        
        self.txt_summary.insert(tk.END, summary_text)
        self.txt_summary.config(state="disabled")