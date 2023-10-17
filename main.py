import sys
import io
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame, QTextEdit
from PySide6.QtGui import QFont, QTextCursor
from PySide6.QtCore import Qt, QTimer

class OutputRedirector(io.StringIO):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    def write(self, s):
        super().write(s)
        self.callback(s)

class CustomApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI")
        self.setGeometry(100, 100, 500, 300)

        main_layout = QVBoxLayout()

        top_info_layout = QHBoxLayout()

        self.console_label = QTextEdit(self)  # Using QTextEdit for multiline text
        self.console_label.setReadOnly(True)  # Making it read-only
        self.console_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        top_info_layout.addWidget(self.console_label, 1)

        stats_layout = QVBoxLayout()

        self.hp_label = QLabel("HP - 3/3", self)
        self.hp_label.setFont(QFont("Arial", 14, QFont.Bold))
        stats_layout.addWidget(self.hp_label)

        self.xp_label = QLabel("XP - 0/10", self)
        self.xp_label.setFont(QFont("Arial", 14, QFont.Bold))
        stats_layout.addWidget(self.xp_label)

        top_info_layout.addLayout(stats_layout, 0)
        main_layout.addLayout(top_info_layout)

        bottom_layout = QHBoxLayout()

        self.move_button = QPushButton("Move", self)
        bottom_layout.addWidget(self.move_button)

        self.interact_button = QPushButton("Interact", self)
        bottom_layout.addWidget(self.interact_button)

        self.inventory_button = QPushButton("Inventory", self)
        bottom_layout.addWidget(self.inventory_button)

        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

        # Redirecting stdout to the console_label
        sys.stdout = OutputRedirector(self.update_console)

        # For demonstration purposes: A timer to print something every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.demo_output)
        self.timer.start(1000)

    def update_console(self, text):
        self.console_label.moveCursor(QTextCursor.End)  # Move cursor to end
        self.console_label.insertPlainText(text)          # Insert text at cursor position
        self.console_label.moveCursor(QTextCursor.End)  # Ensure latest text is visible

    def demo_output(self):
        print("Updating console...")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CustomApp()
    window.show()
    sys.exit(app.exec())
