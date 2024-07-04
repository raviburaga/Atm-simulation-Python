import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json
import os

class ATM:
    def __init__(self, master):
        self.master = master
        master.title("ATM")
        master.geometry("600x400")  # Set window size

        self.master.configure(bg="lightblue")  # Set background color

        self.data_file = "accounts.json"
        self.accounts = self.load_data()

        self.current_card = None

        # Initial Login Screen
        self.login_frame = tk.Frame(master, bg="lightblue")
        self.card_number_label = tk.Label(self.login_frame, text="Card Number:", bg="lightblue", font=("Helvetica", 14))
        self.card_number_label.grid(row=0, column=0, padx=10, pady=10)
        self.card_number_entry = tk.Entry(self.login_frame, font=("Helvetica", 14))
        self.card_number_entry.grid(row=0, column=1, padx=10, pady=10)

        self.pin_label = tk.Label(self.login_frame, text="PIN:", bg="lightblue", font=("Helvetica", 14))
        self.pin_label.grid(row=1, column=0, padx=10, pady=10)
        self.pin_entry = tk.Entry(self.login_frame, show="*", font=("Helvetica", 14))
        self.pin_entry.grid(row=1, column=1, padx=10, pady=10)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.validate_credentials, font=("Helvetica", 14))
        self.login_button.grid(row=2, column=1, padx=10, pady=10)

        self.exit_button = tk.Button(self.login_frame, text="Exit", command=master.quit, font=("Helvetica", 14))
        self.exit_button.grid(row=3, column=1, padx=10, pady=10)

        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.create_main_menu()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                return json.load(file)
        else:
            return {
                "1234": {"pin": "1111", "balance": 0, "transactions": []},
                "5678": {"pin": "2222", "balance": 0, "transactions": []},
                "9012": {"pin": "3333", "balance": 0, "transactions": []}
            }

    def save_data(self):
        with open(self.data_file, "w") as file:
            json.dump(self.accounts, file, indent=4)

    def validate_credentials(self):
        card_number = self.card_number_entry.get()
        pin = self.pin_entry.get()
        if card_number in self.accounts and self.accounts[card_number]["pin"] == pin:
            self.current_card = card_number
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid card number or PIN")

    def create_main_menu(self):
        # Banking Services Menu
        self.main_menu_frame = tk.Frame(self.master, bg="lightblue")
        self.deposit_button = tk.Button(self.main_menu_frame, text="Deposit", command=self.show_deposit, font=("Helvetica", 14))
        self.withdraw_button = tk.Button(self.main_menu_frame, text="Withdraw", command=self.show_withdraw, font=("Helvetica", 14))
        self.check_balance_button = tk.Button(self.main_menu_frame, text="Check Balance", command=self.show_balance, font=("Helvetica", 14))
        self.transactions_button = tk.Button(self.main_menu_frame, text="Transactions", command=self.show_transactions, font=("Helvetica", 14))
        self.logout_button = tk.Button(self.main_menu_frame, text="Logout", command=self.logout, font=("Helvetica", 14))

        self.deposit_button.grid(row=0, column=0, padx=10, pady=10)
        self.withdraw_button.grid(row=0, column=1, padx=10, pady=10)
        self.check_balance_button.grid(row=0, column=2, padx=10, pady=10)
        self.transactions_button.grid(row=1, column=0, padx=10, pady=10)
        self.logout_button.grid(row=1, column=1, padx=10, pady=10)

        self.create_deposit_screen()
        self.create_withdraw_screen()
        self.create_balance_screen()
        self.create_transactions_screen()

    def show_main_menu(self):
        self.login_frame.place_forget()
        self.main_menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def logout(self):
        self.main_menu_frame.place_forget()
        self.card_number_entry.delete(0, tk.END)
        self.pin_entry.delete(0, tk.END)
        self.current_card = None
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def create_deposit_screen(self):
        # Deposit Screen
        self.deposit_frame = tk.Frame(self.master, bg="lightblue")
        self.amount_label_deposit = tk.Label(self.deposit_frame, text="Amount:", bg="lightblue", font=("Helvetica", 14))
        self.amount_label_deposit.grid(row=0, column=0, padx=10, pady=10)
        self.amount_entry_deposit = tk.Entry(self.deposit_frame, font=("Helvetica", 14))
        self.amount_entry_deposit.grid(row=0, column=1, padx=10, pady=10)
        self.deposit_confirm_button = tk.Button(self.deposit_frame, text="Confirm", command=self.deposit, font=("Helvetica", 14))
        self.deposit_confirm_button.grid(row=1, column=1, padx=10, pady=10)
        self.back_button_deposit = tk.Button(self.deposit_frame, text="Back", command=self.show_main_menu_from_deposit, font=("Helvetica", 14))
        self.back_button_deposit.grid(row=2, column=1, padx=10, pady=10)

    def create_withdraw_screen(self):
        # Withdraw Screen
        self.withdraw_frame = tk.Frame(self.master, bg="lightblue")
        self.amount_label_withdraw = tk.Label(self.withdraw_frame, text="Amount:", bg="lightblue", font=("Helvetica", 14))
        self.amount_label_withdraw.grid(row=0, column=0, padx=10, pady=10)
        self.amount_entry_withdraw = tk.Entry(self.withdraw_frame, font=("Helvetica", 14))
        self.amount_entry_withdraw.grid(row=0, column=1, padx=10, pady=10)
        self.withdraw_confirm_button = tk.Button(self.withdraw_frame, text="Confirm", command=self.withdraw, font=("Helvetica", 14))
        self.withdraw_confirm_button.grid(row=1, column=1, padx=10, pady=10)
        self.back_button_withdraw = tk.Button(self.withdraw_frame, text="Back", command=self.show_main_menu_from_withdraw, font=("Helvetica", 14))
        self.back_button_withdraw.grid(row=2, column=1, padx=10, pady=10)

    def create_balance_screen(self):
        # Check Balance Screen
        self.balance_frame = tk.Frame(self.master, bg="lightblue")
        self.balance_label = tk.Label(self.balance_frame, text="", bg="lightblue", font=("Helvetica", 14))
        self.balance_label.grid(row=0, column=0, padx=10, pady=10)
        self.back_button_balance = tk.Button(self.balance_frame, text="Back", command=self.show_main_menu_from_balance, font=("Helvetica", 14))
        self.back_button_balance.grid(row=1, column=0, padx=10, pady=10)

    def create_transactions_screen(self):
        # Transactions Screen
        self.transactions_frame = tk.Frame(self.master, bg="lightblue")
        self.transactions_text = tk.Text(self.transactions_frame, width=60, height=10, font=("Helvetica", 14))
        self.transactions_text.grid(row=0, column=0, padx=10, pady=10)
        self.back_button_transactions = tk.Button(self.transactions_frame, text="Back", command=self.show_main_menu_from_transactions, font=("Helvetica", 14))
        self.back_button_transactions.grid(row=1, column=0, padx=10, pady=10)

    def show_deposit(self):
        self.main_menu_frame.place_forget()
        self.deposit_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_withdraw(self):
        self.main_menu_frame.place_forget()
        self.withdraw_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_balance(self):
        self.balance_label.config(text=f"Current balance: ${self.accounts[self.current_card]['balance']:.2f}")
        self.main_menu_frame.place_forget()
        self.balance_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_transactions(self):
        self.transactions_text.delete("1.0", tk.END)
        transactions = self.accounts[self.current_card]["transactions"]
        if transactions:
            for transaction in transactions:
                self.transactions_text.insert(tk.END, f"{transaction}\n")
        else:
            self.transactions_text.insert(tk.END, "No transactions yet.")
        self.main_menu_frame.place_forget()
        self.transactions_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_main_menu_from_deposit(self):
        self.deposit_frame.place_forget()
        self.main_menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_main_menu_from_withdraw(self):
        self.withdraw_frame.place_forget()
        self.main_menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_main_menu_from_balance(self):
        self.balance_frame.place_forget()
        self.main_menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_main_menu_from_transactions(self):
        self.transactions_frame.place_forget()
        self.main_menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def deposit(self):
        try:
            amount = float(self.amount_entry_deposit.get())
            if amount <= 0:
                messagebox.showerror("Error", "Please enter a positive amount")
            else:
                self.accounts[self.current_card]["balance"] += amount
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.accounts[self.current_card]["transactions"].append(f"{timestamp} - Deposited ${amount:.2f}")
                self.save_data()
                messagebox.showinfo("Deposit", f"Deposited ${amount:.2f}. New balance: ${self.accounts[self.current_card]['balance']:.2f}")
                self.amount_entry_deposit.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")

    def withdraw(self):
        try:
            amount = float(self.amount_entry_withdraw.get())
            if amount <= 0:
                messagebox.showerror("Error", "Please enter a positive amount")
            elif amount > self.accounts[self.current_card]["balance"]:
                messagebox.showerror("Error", "Insufficient funds")
            else:
                self.accounts[self.current_card]["balance"] -= amount
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.accounts[self.current_card]["transactions"].append(f"{timestamp} - Withdrew ${amount:.2f}")
                self.save_data()
                messagebox.showinfo("Withdrawal", f"Withdrew ${amount:.2f}. New balance: ${self.accounts[self.current_card]['balance']:.2f}")
                self.amount_entry_withdraw.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")

    def mainloop(self):
        self.master.mainloop()

# Creating and running the ATM application
root = tk.Tk()
atm = ATM(root)
atm.mainloop()
