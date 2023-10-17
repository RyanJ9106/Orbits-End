import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

#Variables
HP = 3
HPtext = (f"HP - {HP}/3")
XP = 0
XPtext = (f"XP - {XP}/10")

class CustomApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title and default size/position
        self.setWindowTitle("GUI")
        self.setGeometry(100, 100, 500, 300)

        # Create a main vertical layout
        main_layout = QVBoxLayout()

        # Top Section for the Console Display and Stats
        top_info_layout = QHBoxLayout()

        # Console Display label with frame and center alignment
        self.console_label = QLabel("Console Display", self)
        self.console_label.setAlignment(Qt.AlignCenter)
        self.console_label.setFrameShape(QFrame.Panel)
        self.console_label.setFrameShadow(QFrame.Sunken)
        top_info_layout.addWidget(self.console_label, 1)  # Add to top layout with stretch factor 1

        # Vertical layout for HP and XP stats
        stats_layout = QVBoxLayout()

        # HP label with custom font
        self.hp_label = QLabel(HPtext, self)
        self.hp_label.setFont(QFont("Arial", 14, QFont.Bold))
        stats_layout.addWidget(self.hp_label)

        # XP label with custom font
        self.xp_label = QLabel(XPtext, self)
        self.xp_label.setFont(QFont("Arial", 14, QFont.Bold))
        stats_layout.addWidget(self.xp_label)

        # Add stats layout to the top layout with no stretch (default is 0)
        top_info_layout.addLayout(stats_layout, 0)
        main_layout.addLayout(top_info_layout)  # Add top layout to the main layout

        # Bottom Section for buttons
        bottom_layout = QHBoxLayout()

        # Move button
        self.move_button = QPushButton("Move", self)
        bottom_layout.addWidget(self.move_button)

        # Interact button
        self.interact_button = QPushButton("Interact", self)
        bottom_layout.addWidget(self.interact_button)

        # Inventory button
        self.inventory_button = QPushButton("Inventory", self)
        bottom_layout.addWidget(self.inventory_button)

        # Add bottom layout to the main layout
        main_layout.addLayout(bottom_layout)

        # Set the main layout for the window
        self.setLayout(main_layout)

# Standard boilerplate code to run the app
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create an instance of the application
    window = CustomApp()          # Create an instance of our custom app window
    window.show()                 # Display the window
    sys.exit(app.exec())         # Start the application event loop