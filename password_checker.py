import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    # Minimum length requirement
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    # Check for presence of uppercase, lowercase, and numeric characters
    if not re.search(r'[A-Z]', password) or \
       not re.search(r'[a-z]', password) or \
       not re.search(r'\d', password):
        return "Weak: Password must include uppercase, lowercase, and numeric characters."

    # Check for presence of special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Password must include special characters."

    # Check for common patterns or dictionary words
    common_patterns = ["123456", "password", "qwerty", "abc123", "admin"]
    if any(pattern in password.lower() for pattern in common_patterns):
        return "Weak: Password contains a common pattern or dictionary word."

    return "Strong: Password meets the minimum strength requirements."

def check_password():
    password = entry.get()
    result = check_password_strength(password)
    messagebox.showinfo("Password Strength", result)

# Create the main window
window = tk.Tk()
window.title("Password Strength Checker")

# Create the label
label = tk.Label(window, text="Enter your password:")
label.pack()

# Create the entry field
entry = tk.Entry(window, show="*")
entry.pack()

# Create the button
button = tk.Button(window, text="Check", command=check_password)
button.pack()

# Run the main loop
window.mainloop()
