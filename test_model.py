import unittest
from diners_model import CheckSplitterModel

class TestCheckSplitterModel(unittest.TestCase):

    def setUp(self):
        """Este método se ejecuta antes de cada test. Resetea el escenario."""
        self.model = CheckSplitterModel()

    def test_add_diner(self):
        """Verifica que se agreguen comensales y no permita duplicados."""
        # Agregar comensal nuevo
        success, _ = self.model.add_diner("Carlos")
        self.assertTrue(success)
        self.assertEqual(len(self.model.diners), 1)

        # Intentar agregar duplicado (mismo nombre, distinta mayúscula)
        success, _ = self.model.add_diner("carlos")
        self.assertFalse(success)
        self.assertEqual(len(self.model.diners), 1)

    def test_load_item_split(self):
        """Verifica que un gasto se divida equitativamente entre los seleccionados."""
        self.model.add_diner("Carlos")
        self.model.add_diner("Milagros")
        self.model.add_diner("Lisa")

        # Cargar un ítem de $3000 compartido solo por Carlos y Milagros
        success, _ = self.model.load_item("Drinks", 3000, ["Carlos", "Milagros"])
        self.assertTrue(success)

        # Carlos y Milagros deberían tener $1500 cada uno. Lisa $0.
        results, _, _ = self.model.get_results()
        
        for r in results:
            if r["name"] in ["Carlos", "Milagros"]:
                self.assertEqual(r["subtotal"], 1500.0)
            if r["name"] == "Lisa":
                self.assertEqual(r["subtotal"], 0.0)

    def test_global_tip_calculation(self):
        """Verifica que el cambio de propina aplique correctamente a los totales."""
        self.model.add_diner("Carlos")
        self.model.load_item("Pizza", 1000, ["Carlos"])
        
        # Cambiamos la propina al 20%
        self.model.set_global_tip(20)
        results, grand_total, _ = self.model.get_results()
        
        # Subtotal: 1000, Propina (20%): 200, Total: 1200
        self.assertEqual(results[0]["tip"], 200.0)
        self.assertEqual(results[0]["total"], 1200.0)
        self.assertEqual(grand_total, 1200.0)

if __name__ == "__main__":
    unittest.main()