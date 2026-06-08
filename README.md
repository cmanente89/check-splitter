Check Splitter 💵
A smart, desktop-based utility built in Python using Tkinter to easily calculate and split restaurant bills, group expenses, or shared event costs. Developed as a final project for Stanford's Code in Place.

The application implements a clean Model-View-Controller (MVC) software architecture to separate calculation logic from the graphical user interface.

🚀 Features
1. Simple Split Mode
Fast and straightforward calculation.

Input the total bill and the number of diners to get an even split instantly.

Built-in keyboard shortcuts (press Enter to jump between fields and calculate).

2. Advanced Split Mode (By Diner)
Item-by-Item Breakdown: Load each expense with a custom description (e.g., "Drinks", "Pizza") and its cost.

Smart Assignment: Use dynamic checkboxes to select exactly who shared each specific item (perfect for separating costs like alcohol or desserts).

Global Tip Selector: Dynamically apply 0%, 10%, 15%, or 20% tip to the table and see individual subtotals and grand totals update in real-time.

Live Gastronomic Ticket Summary: Features a beautifully aligned, text-based live invoice overview showing loaded item history and individual totals.

🛠️ Project Structure
main.py: The application entry point that initializes the Tkinter loop and wires the system.

diners_model.py: Core backend containing math equations, data structures (lists of dictionaries), and calculation logic.

gui.py: Frontend architecture containing layout management, widgets, tabs, and event bindings.

test_model.py: Automated unit testing suite ensuring database logic stability.

📦 Installation & Setup
Clone the repository:
git clone https://github.com/cmanente89/check-splitter.git
cd check-splitter

Create and activate a virtual environment (Recommended):
python3 -m venv venv

On Windows:
.\Scripts\activate

On macOS/Linux:
source venv/bin/activate

Run the Application:
Tkinter is bundled with standard Python installations. Run the app directly using:
python main.py

🧪 Running Tests
This project includes robust automated test coverages. To run the suite and verify logic consistency, execute:
python test_model.py