# NAME: AIGBEDION SAMUEL
# MAT. NUMBER: ENG2403492

import tkinter as tk
from tkinter import messagebox
def login():
 username = entry_username.get()
 password = entry_password.get()

 # Example check (replace with your own logic)
 if username == "AIGBEDION SAMUEL" and password == "ENG2403492":
 messagebox.showinfo("Login Successful", f"Welcome, {username}!")
 else:
 messagebox.showerror("Login Failed", "Invalid username or password")
# Create main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x180")
# Username label and entry
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)
# Password label and entry
