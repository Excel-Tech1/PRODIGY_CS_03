import re
from tkinter import *
from tkinter import messagebox

# Function to check password complexity
def check_password_complexity(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one number."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."
    return True, "Password is strong!"

# Function to validate the password when the button is clicked
def validate_password():
    password = password_entry.get()
    is_valid, message = check_password_complexity(password)
    messagebox.showinfo("Password Check", message)

# Initialize the GUI window
root = Tk()
root.title("Password Complexity Checker")
root.geometry("400x300")
root.configure(bg="lightgray")

# Widgets
Label(root, text="Enter Password:", bg="lightgray", font=("Arial", 14)).pack(pady=20)
password_entry = Entry(root, show="*", width=30, font=("Arial", 12))
password_entry.pack(pady=10)

check_button = Button(root, text="Check Password", command=validate_password, bg="blue", fg="white")
check_button.pack(pady=20)

# Run the GUI main loop
root.mainloop()
