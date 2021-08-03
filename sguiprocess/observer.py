from qtpy.QtCore import QObject, Signal


class SObserverGui(QObject):
    finished_signal = Signal()
    progress_signal = Signal(int)
    log_signal = Signal(str)

    def __init__(self):
        super().__init__()

    def progress(self, value):
        self.progress_signal(value)

    def log(self, value):
        self.log_sginal(value)  

    def finished(self, value):
        self.finished_signal(value)
