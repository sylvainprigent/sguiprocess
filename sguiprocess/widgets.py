from qtpy.QtWidgets import QWidget, QProgressBar, QVBoxLayout, QTextEdit


class SLogWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.progress_bar = QProgressBar()
        self.log_area = QTextEdit()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.log_area)
        self.setLayout(layout)

    def set_advanced(self, mode: bool):
        if mode:
            self.log_area.setVisible(True)
        else:
            self.log_area.setVisible(False)

    def set_progress(self, value: int):
        self.progress_bar.setValue(value)

    def add_log(self, value: str):
        self.log_area.append(value)

    def clear_log(self):
        self.log_area.clear()


