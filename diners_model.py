class CheckSplitterModel:
    def __init__(self):
        self.diners = []

    def add_diner(self, name):
        """Adds a new diner to the table."""
        for diner in self.diners:
            if diner["name"].lower() == name.lower():
                return False, f"Diner '{name}' already exists."
        
        new_diner = {
            "name": name,
            "subtotal": 0.0,
            "tip_percentage": 10.0
        }
        self.diners.append(new_diner)
        return True, f"{name} added."

    def load_item(self, amount, friends_sharing):
        """Splits an item cost among selected friends."""
        if not friends_sharing:
            return False, "No friends selected for this item."

        split_amount = amount / len(friends_sharing)
        
        for name in friends_sharing:
            for diner in self.diners:
                if diner["name"].lower() == name.lower():
                    diner["subtotal"] += split_amount
                    break
        return True, "Item loaded successfully."

    def get_results(self):
        """Returns the calculated totals for all diners."""
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
        return results, grand_total