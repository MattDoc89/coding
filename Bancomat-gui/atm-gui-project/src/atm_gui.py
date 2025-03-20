from tkinter import Tk, Label, Button, Entry, StringVar, messagebox

class ATMApp:
    def __init__(self, master):
        self.master = master
        master.title("ATM Machine")

        self.balance = 500  # Initial balance

        self.balance_var = StringVar()
        self.balance_var.set(f"Balance: {self.balance:.2f}€")

        self.label = Label(master, text="Welcome to the ATM")
        self.label.pack()

        self.balance_label = Label(master, textvariable=self.balance_var)
        self.balance_label.pack()

        self.deposit_entry = Entry(master)
        self.deposit_entry.pack()
        self.deposit_button = Button(master, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        self.withdraw_entry = Entry(master)
        self.withdraw_entry.pack()
        self.withdraw_button = Button(master, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()

        self.exit_button = Button(master, text="Exit", command=master.quit)
        self.exit_button.pack()

    def deposit(self):
        try:
            amount = float(self.deposit_entry.get())
            if amount > 0:
                self.balance += amount
                self.balance_var.set(f"Balance: {self.balance:.2f}€")
                messagebox.showinfo("Success", f"Deposited: {amount:.2f}€")
            else:
                messagebox.showerror("Error", "Please enter a valid amount.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def withdraw(self):
        try:
            amount = float(self.withdraw_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Please enter a valid amount.")
            elif amount > self.balance:
                messagebox.showerror("Error", "Insufficient balance!")
            else:
                self.balance -= amount
                self.balance_var.set(f"Balance: {self.balance:.2f}€")
                messagebox.showinfo("Success", f"Withdrawn: {amount:.2f}€")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

if __name__ == "__main__":
    root = Tk()
    atm_app = ATMApp(root)
    root.mainloop()