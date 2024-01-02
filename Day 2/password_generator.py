import random
import string
import tkinter as tk


# Function to generate a random password of given length
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password


# Function to handle password generation and update the GUI
def generate_password_interface():
    password_length = int(entry_length.get())
    if password_length < 6:
        label_result.config(text="Password length should be at least 6 characters.")
    else:
        generated_password = generate_password(password_length)
        label_result.config(text="Generated Password: " + generated_password)


# Create the main Tkinter window
root = tk.Tk()
root.title("Password Generator")

# Label to prompt the user for the desired password length
label_length = tk.Label(root, text="Enter the desired password length: ")
label_length.pack()

# Entry widget for user input (password length)
entry_length = tk.Entry(root)
entry_length.pack()

# Button to trigger password generation
button_generate = tk.Button(
    root, text="Generate Password", command=generate_password_interface
)
button_generate.pack()

# Label to display the result or error message
label_result = tk.Label(root, text="")
label_result.pack()

# Start the Tkinter event loop
root.mainloop()
