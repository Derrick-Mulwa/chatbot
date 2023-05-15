import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QLabel, QScrollArea
from PyQt5.QtCore import Qt


class ScrollAreaApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scroll Area Application")

        # Create a scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Create a widget to hold the frame
        frame_widget = QWidget()
        frame_widget.setStyleSheet("background-color: #E0E0E0; padding: 10px;")

        # Create a vertical layout for the frame widget
        frame_layout = QVBoxLayout(frame_widget)
        frame_layout.setAlignment(Qt.AlignBottom)

        # Set the frame widget as the widget for the scroll area
        scroll_area.setWidget(frame_widget)

        # Create a main layout for the central widget
        main_layout = QVBoxLayout()

        # Create a text edit and a button
        text_edit = QTextEdit()
        button = QPushButton("Add Label")
        button.clicked.connect(lambda: self.add_label(frame_layout, text_edit.toPlainText()))

        # Add the text edit and button to the main layout
        main_layout.addWidget(text_edit)
        main_layout.addWidget(button)

        # Create a central widget and set the main layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        # Create a layout for the main window
        window_layout = QVBoxLayout()
        window_layout.addWidget(scroll_area)
        window_layout.addWidget(central_widget)

        # Set the main window layout
        main_widget = QWidget()
        main_widget.setLayout(window_layout)
        self.setCentralWidget(main_widget)
        self.i = 1

    def add_label(self, layout, text):
        if (self.i % 2) != 0:
            label = QLabel(text)
            label.setStyleSheet("background-color: #FFFFFF; padding: 6px; border-radius: 4px;")
            label.setWordWrap(True)
            label.setMaximumWidth(300)
            label.setFixedSize(label.sizeHint())
            # label.setAlignment(Qt.AlignRight)
            layout.addWidget(label, 0, Qt.AlignRight)
        else:
            label = QLabel(text)
            label.setStyleSheet("background-color: #FFFFFF; padding: 6px; border-radius: 4px;")
            label.setWordWrap(True)
            label.setMaximumWidth(300)
            label.setFixedSize(label.sizeHint())
            # label.setAlignment(Qt.AlignRight)
            layout.addWidget(label, 0, Qt.AlignLeft)

        self.i += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScrollAreaApplication()
    window.setGeometry(400, 200, 400, 600)
    window.show()
    sys.exit(app.exec_())
