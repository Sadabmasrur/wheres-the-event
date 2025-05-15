import tkinter as tk

def check_strength():
    pwd = password_entry.get()
    length = len(pwd)

    if length == 0:
        result_label.config(text="Enter a password.")
    elif length < 5:
        result_label.config(text="Strength: Very Weak")
    elif length < 8:
        result_label.config(text="Strength: Weak")
    elif length < 12:
        result_label.config(text="Strength: Medium")
    else:
        result_label.config(text="Strength: Strong")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")
root.resizable(False, False)

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
password_entry = tk.Entry(root, show="*", width=25)
password_entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=check_strength, bg="#2196F3", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=5)

root.mainloop()
