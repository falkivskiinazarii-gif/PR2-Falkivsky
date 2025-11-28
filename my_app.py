import tkinter as tk
from tkinter import messagebox

# Курси валют
RATES = {
    "USD": 41.50,
    "EUR": 44.20,
    "PLN": 10.50
}

# --- ОСЬ ВОНА, ПОТРІБНА ФУНКЦІЯ ---
def calculate_exchange(amount, rate):
    """Функція повертає результат множення суми на курс."""
    if rate is None:
        raise TypeError("Rate cannot be None")
    return amount * rate

# --- Інтерфейс ---
def convert_currency():
    try:
        amount = entry_amount.get()
        amount = float(amount)
        
        try:
            selected_index = listbox_currency.curselection()[0]
            selected_currency = listbox_currency.get(selected_index)
            
            rate = RATES[selected_currency]
            
            # Виклик функції розрахунку
            result = calculate_exchange(amount, rate)
            
            label_result.config(text=f"Result: {result:.2f} UAH")
            
        except IndexError:
            messagebox.showwarning("Warning", "Оберіть валюту зі списку!")
            return
            
    except ValueError:
        messagebox.showerror("Error", "Будь ласка, введіть число!")
        return

# --- Запуск ---
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Best Converter FINAL")
    root.geometry("300x300")
    root.configure(bg="white")

    label_instruction = tk.Label(root, text="Enter amount in UAH:", bg="white", fg="black")
    label_instruction.pack(pady=10)

    entry_amount = tk.Entry(root)
    entry_amount.pack(pady=5)

    label_currency = tk.Label(root, text="Select currency:", bg="white", fg="black")
    label_currency.pack()

    listbox_currency = tk.Listbox(root, height=3)
    for currency in RATES:
        listbox_currency.insert(tk.END, currency)
    listbox_currency.pack()

    btn_convert = tk.Button(root, text="Convert", command=convert_currency, bg="red", fg="white")
    btn_convert.pack(pady=20)

    label_result = tk.Label(root, text="Result: 0.00", bg="white", fg="black", font=("Arial", 12, "bold"))
    label_result.pack()

    root.mainloop()