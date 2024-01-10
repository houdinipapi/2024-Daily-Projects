# Import necessary modules
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QApplication,  # Import QApplication for creating and running the application
    QWidget,  # Import QWidget for creating the main window
    QPushButton,  # Import QPushButton for creating clickable buttons
    QVBoxLayout,  # Import QVBoxLayout for creating a vertical layout
    QHBoxLayout,  # Import QHBoxLayout for creating a horizontal layout
    QLabel,  # Import QLabel for displaying text
)


class TicTacToeGame(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set window title and position/size
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(100, 100, 300, 300)

        # Initialize game variables
        self.board = [" "] * 9
        self.current_player = "X"
        self.buttons = []

        # Create 9 buttons and add them to the board list
        for i in range(9):
            button = QPushButton("", self)
            button.setFont(button.font())
            button.clicked.connect(lambda _, i=i: self.make_move(i))
            self.buttons.append(button)

        # Create a reset button
        self.reset_button = QPushButton("Reset", self)
        self.reset_button.clicked.connect(self.reset_game)

        # Create a vertical layout and add the buttons to it
        layout = QVBoxLayout()
        grid_layout = [self.buttons[i : i + 3] for i in range(0, 9, 3)]

        for row in grid_layout:
            row_layout = QHBoxLayout()
            for button in row:
                row_layout.addWidget(button)
            layout.addLayout(row_layout)

        # Add the reset button to the layout
        layout.addWidget(self.reset_button)
        self.setLayout(layout)

        # Initialize the UI
        self.update_ui()

    def make_move(self, index):
        # Check if the space is empty
        if self.board[index] == " ":
            # Make the move and update the UI
            self.board[index] = self.current_player
            self.update_ui()
            winner = self.check_winner()
            if winner:
                self.show_winner(winner)
            else:
                # Switch player
                self.current_player = "0" if self.current_player == "X" else "X"

    def update_ui(self):
        # Update the text of each button with the corresponding board value
        for i in range(9):
            self.buttons[i].setText(self.board[i])

    def check_winner(self):
        # List of winning combinations
        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        # Check each combination for a winner
        for combo in winning_combinations:
            if (
                self.board[combo[0]]
                == self.board[combo[1]]
                == self.board[combo[2]]
                != " "
            ):
                return self.board[combo[0]]
        # Check if there's a tie
        if " " not in self.board:
            return "Tie"
        # No winner yet
        return None

    def show_winner(self, winner):
        # Create a label with the winner message
        message = f"Winner: {winner}" if winner != "Tie" else "It's a Tie!"
        winner_label = QLabel(message, self)
        winner_label.setAlignment(QtCore.Qt.AlignCenter)
        winner_label.setFont(winner_label.font())
        # Add the label to the layout
        self.layout().addWidget(winner_label)

    def reset_game(self):
        # Reset game variables and update the UI
        self.board = [" "] * 9
        self.current_player = "X"
        self.update_ui()
        # Remove the winner label if it exists
        winner_label = self.findChild(QLabel)
        if winner_label:
            winner_label.deleteLater()


if __name__ == "__main__":
    # Create the application and the main window
    app = QApplication(sys.argv)
    ex = TicTacToeGame()
    ex.show()
    # Start the event loop and exit when it's done
    sys.exit(app.exec_())
