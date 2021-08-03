from qtpy.QtCore import QObject, QThread, Signal
from qtpy.QtWidgets import QWidget, QVBoxLayout, QPushButton

from sguiprocess.observer import SObserverGui
from sguiprocess.widgets import SLogWidget


class SPlugin(QObject):
    """Worker interface for plugin

    """
    finished = Signal()
    progress = Signal(int)
    log = Signal(str)

    def __init__(self):
        super().__init__()
        self._widget = None
        # connect observer to Qt signals
        self.init_ui()

    def widget(self):
        return self._widget

    def init_ui(self):
        raise NotImplementedError()

    def state(self) -> dict:
        # {'name': 'SPlugin', 'inputs': [], 'parameters': {}, 'outputs': []}
        raise NotImplementedError()

    def run(self):
        raise NotImplementedError()


class SPluginWidget(QWidget):
    """SPluginWidget

    Main widget for a S plugin. A plugin is a widget to setup
    the parameters and exec the plugin

    """

    def __init__(self, worker: SPlugin):
        super().__init__()
        # thread
        self.worker = worker
        self.thread = QThread()
        self.worker.moveToThread(self.thread)

        # GUI
        self.log_widget = SLogWidget()
        self.initUI()

        # connect
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.progress.connect(self.log_widget.set_progress)
        self.worker.log.connect(self.log_widget.add_log)

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(self.worker.widget())

        run_btn = QPushButton('Run')
        run_btn.released.connect(self.run)
        layout.addWidget(run_btn)

        layout.addWidget(self.log_widget)
        self.setLayout(layout)

    def run(self):
        self.thread.start()
