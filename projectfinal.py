import tkinter as tk

balance = 0
history = []

window = tk.Tk()
window.title("Banking Simulator")
window.geometry("400x450")

title = tk.Label(window, text="BANKING SIMULATOR",
                 font=("Arial", 20))
title.pack(pady=20)

balance_label = tk.Label(window, text="Balance: €0.00",
                         font=("Arial", 16))
balance_label.pack(pady=10)

amount = tk.Entry(window)
amount.pack(pady=10)

message = tk.Label(window, text="Welcome!")
message.pack(pady=10)

#function for update balance
def update_balance():
    balance_label.config(text=f"Balance: €{balance:.2f}") 


def deposit():
    global balance

    money = float(amount.get())

    if money > 0:
        balance += money
        history.append(f"Deposited €{money:.2f}")
        update_balance()
        message.config(text="Deposit successful!")
    else:
        message.config(text="Amount must be greater than 0.")


def withdraw():
    global balance

    money = float(amount.get())

    if money <= 0:
        message.config(text="Amount must be greater than 0.")

    elif money > balance:
        message.config(text="Insufficient funds!")

    else:
        balance -= money
        history.append(f"Withdrew €{money:.2f}")
        update_balance()
        message.config(text="Withdrawal successful!")


def show_history():
    if len(history) == 0:
        message.config(text="No transactions yet.")
    else:
        message.config(text="\n".join(history))


tk.Button(window, text="Deposit",
          width=20, command=deposit).pack(pady=5)

tk.Button(window, text="Withdraw",
          width=20, command=withdraw).pack(pady=5)

tk.Button(window, text="Transaction History",
          width=20, command=show_history).pack(pady=5)

tk.Button(window, text="Exit",
          width=20, command=window.destroy).pack(pady=5)

window.mainloop()
