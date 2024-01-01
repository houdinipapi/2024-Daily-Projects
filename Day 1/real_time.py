import tkinter as tk
import time


def update_clock():
    # Get the current time in the format HH:MM:SS
    current_time = time.strftime("%H:%M:%S")

    # Update the text of the clock label with the current time
    clock_label.config(text=current_time)

    # Schedule the update_clock function to be called after 1000 milliseconds (1 second)
    clock_label.after(1000, update_clock)


# Create the main application window
app = tk.Tk()
app.title("Python Clock")

# Create a label widget to display the clock
clock_label = tk.Label(app, text="", font=("Helvetica", 50))
clock_label.pack()

# Initial call to update_clock to start the clock
update_clock()

# Start the Tknter event loop
app.mainloop()