

class CheckSplitterModel:
    def __init__(self):
        self.diners = []
        self.items_history = []  # Almacena diccionarios con {"desc": str, "amount": float, "shared_by": list}
        self.global_tip_percentage = 10.0  # Propina base de la mesa

    def set_global_tip(self, percentage):
        """Updates the tip percentage for all diners at the table."""
        self.global_tip_percentage = float(percentage)
        for diner in self.diners:
            diner["tip_percentage"] = self.global_tip_percentage

    def add_diner(self, name):
        """Adds a new diner to the table."""
        for diner in self.diners:
            if diner["name"].lower() == name.lower():
                return False, f"Diner '{name}' already exists."
        
        new_diner = {
            "name": name,
            "subtotal": 0.0,
            "tip_percentage": self.global_tip_percentage
        }
        self.diners.append(new_diner)
        return True, f"{name} added."

    def load_item(self, description, amount, friends_sharing):
        """Splits an item cost among selected friends and records it in history."""
        if not description:
            return False, "Item description cannot be empty."
        if not friends_sharing:
            return False, "No friends selected for this item."

        split_amount = amount / len(friends_sharing)
        
        # Guardamos en el historial global
        self.items_history.append({
            "desc": description,
            "amount": amount,
            "shared_by": friends_sharing
        })

        # Sumamos al subtotal de cada comensal implicado
        for name in friends_sharing:
            for diner in self.diners:
                if diner["name"].lower() == name.lower():
                    diner["subtotal"] += split_amount
                    break
        return True, f"'{description}' loaded successfully."

    def get_results(self):
        """Returns the calculated totals and the history breakdown."""
        results = []
        grand_total = 0
        for diner in self.diners:
            tip_amount = diner["subtotal"] * (diner["tip_percentage"] / 100)
            total_to_pay = diner["subtotal"] + tip_amount
            grand_total += total_to_pay
            
            results.append({
                "name": diner["name"],
                "subtotal": diner["subtotal"],
                "tip": tip_amount,
                "total": total_to_pay
            })
        return results, grand_total, self.items_history