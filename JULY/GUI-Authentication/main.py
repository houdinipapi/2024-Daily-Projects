import tkinter as tk
from tkinter import simpledialog, messagebox


def validate_age():
    age = simpledialog.askinteger("Age Validation", "Enter the user's age:")
    if age is None:
        return
    if age <= 0:
        messagebox.showerror("Error", "Age must be a positive number.")
    elif age <= 17:
        messagebox.showinfo("Result", f"Underage. Age difference from 18: {18 - age}")
    elif 18 <= age <= 25:
        messagebox.showinfo("Result", "Eligible to drive.")
    else:
        messagebox.showinfo("Result", f"Too old. Age difference from 25: {age - 25}")


def find_string_length():
    user_string = simpledialog.askstring("String Length", "Enter a string:")
    if user_string is not None:
        messagebox.showinfo("Result", f"Length of the string: {len(user_string)}")


def find_biggest_number():
    numbers = []
    for i in range(4):
        number = simpledialog.askfloat("Biggest Number", f"Enter number {i + 1}:")
        if number is None:
            return
        numbers.append(number)

    messagebox.showinfo("Result", f"The biggest number is: {max(numbers)}")


def check_number():
    number = simpledialog.askinteger("Number Check", "Enter a number:")
    if number is None:
        return
    if number > 0 and number % 2 == 0:
        messagebox.showinfo("Result", "Positive and even number.")
    elif number > 0 and number % 2 != 0:
        messagebox.showinfo("Result", "Positive and odd number.")
    elif number < 0 and number % 2 == 0:
        messagebox.showinfo("Result", "Negative and even number.")
    elif number < 0 and number % 2 != 0:
        messagebox.showinfo("Result", "Negative and odd number.")
    else:
        messagebox.showinfo("Result", "The number is zero, which is even.")


def check_shape():
    length = simpledialog.askfloat("Shape Check", "Enter the length:")
    width = simpledialog.askfloat("Shape Check", "Enter the width:")
    if length is None or width is None:
        return
    if length == width:
        messagebox.showinfo("Result", "It is a square.")
    else:
        messagebox.showinfo("Result", "It is a rectangle.")


def admin_operations():
    admin_win = tk.Toplevel(root)
    admin_win.title("Admin Operations")

    tk.Button(admin_win, text="Validate a user's eligibility to drive", command=validate_age).pack(pady=5)
    tk.Button(admin_win, text="Find the length of any string", command=find_string_length).pack(pady=5)
    tk.Button(admin_win, text="Exit", command=admin_win.destroy).pack(pady=5)


def user_operations():
    user_win = tk.Toplevel(root)
    user_win.title("User Operations")

    tk.Button(user_win, text="Find the biggest of 4 numbers", command=find_biggest_number).pack(pady=5)
    tk.Button(
        user_win,
        text="Check if a number is positive & even, positive & odd, negative & even, or negative & odd",
        command=check_number,
    ).pack(pady=5)
    tk.Button(user_win, text="Check if a shape is a square or rectangle", command=check_shape).pack(pady=5)
    tk.Button(user_win, text="Exit", command=user_win.destroy).pack(pady=5)


def login_as_user():
    pin=simpledialog.askstring("User Login", "Enter the user pin:", show="*")
    if pin is None:
        return
    if pin == "2222":
        user_operations()
    else:
        messagebox.showerror("Error", "Invalid user pin.")

def login_as_admin():
    pin = simpledialog.askstring("Admin Login", "Enter the admin pin:", show="*")
    if pin is None:
        return
    if pin == "1111":
        admin_operations()
    else:
        messagebox.showerror("Error", "Invalid admin pin.")


def main_menu():
    main_win = tk.Toplevel(root)
    main_win.title("Login")

    tk.Button(main_win, text="Login as User", command=login_as_user).pack(pady=5)
    tk.Button(main_win, text="Login as Admin", command=login_as_admin).pack(pady=5)
    tk.Button(main_win, text="Exit", command=exit_program).pack(pady=5)


def exit_program():
    root.quit()
    root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    main_menu()
    root.mainloop()
