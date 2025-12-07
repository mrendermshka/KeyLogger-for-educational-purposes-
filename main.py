import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QHBoxLayout

app = QApplication([])
window = QWidget()
window.setWindowTitle("OPENER")
label = QLabel("Файл не вибрано")
button = QPushButton("Файлікі?❤")

def choose_file():
    path = QFileDialog.getOpenFileName(window, "Єлісей шукає файл", "", "Усі файли (*)")
    if path:
        print(path)
        with open(path[0], "r", encoding="utf-8") as f:
            label.setText(f.read())
    else:
       label.setText("Файл не вибрано")


layout = QHBoxLayout()
layout.addWidget(label)
layout.addWidget(button)
button.clicked.connect(choose_file)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())