# Import necessary modules
import sys
from PyQt5.QtWidgets import *
from PyQt5 import *

# the Converter class
class Converter(QWidget):
    # Constructor for the Converter class
    def __init__(self):
        super().__init__()

        # Initialize the user interface
        self.initUI()

    # Function to initialize the user interface
    def initUI(self):
        # Set the window title and geometry
        self.setWindowTitle('Temperature Converter')
        self.setGeometry(300, 300, 300, 200)

        # Create input fields for Celsius and Fahrenheit
        self.celcius_input = QLineEdit()
        self.fahrenheit_input = QLineEdit()

        # Create a button to convert Celsius to Fahrenheit
        self.convert_btn = QPushButton('Convert')
        self.convert_btn.clicked.connect(self.convert)

        # Create a button to reset the input fields and result label
        self.reset_btn = QPushButton('Reset')
        self.reset_btn.clicked.connect(self.reset)

        # Create a label to display the result
        self.result_label = QLabel()

        # Create a grid layout and add the widgets
        layout = QGridLayout()
        layout.addWidget(QLabel('Celsius:'), 0, 0)
        layout.addWidget(self.celcius_input, 0, 1)
        layout.addWidget(QLabel('Fahrenheit:'), 1, 0)
        layout.addWidget(self.fahrenheit_input, 1, 1)
        layout.addWidget(self.convert_btn, 2, 1)
        layout.addWidget(self.reset_btn, 2, 2)
        layout.addWidget(self.result_label, 3, 0, 1, 2)

        # Set the layout for the window
        self.setLayout(layout)

    # Function to convert Celsius to Fahrenheit or vice versa
    def convert(self):
        try:
            # Check if the Celsius input field is not empty
            if self.celcius_input.text():
                # Convert Celsius to Fahrenheit
                celcius = float(self.celcius_input.text())
                fahrenheit = (celcius * 9/5) + 32
                self.result_label.setText(f"{celcius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")
                self.fahrenheit_input.clear()
            # Check if the Fahrenheit input field is not empty
            elif self.fahrenheit_input.text():
                # Convert Fahrenheit to Celsius
                fahrenheit = float(self.fahrenheit_input.text())
                celcius = (fahrenheit - 32) * 5/9
                self.result_label.setText(f"{fahrenheit} degrees Fahrenheit is equal to {celcius} degrees Celsius")
                self.celcius_input.clear()
        except ValueError:
            # Display a warning message box if the input is not a valid number
            QMessageBox.warning(self, 'Invalid Input', 'Please enter a valid number.')

    # Function to reset the input fields and result label
    def reset(self):
        self.celcius_input.clear()
        self.fahrenheit_input.clear()
        self.result_label.clear()

# Create the main application
if __name__ == '__main__':
    # Create a QApplication object
    app = QApplication(sys.argv)

    # Create a Converter object
    converter = Converter()

    # Show the Converter window
    converter.show()

    # Start the event loop
    sys.exit(app.exec_())