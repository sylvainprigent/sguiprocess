from qtpy.QtCore import QObject, QThread, Signal
from qtpy.QtWidgets import QWidget, QVBoxLayout, QPushButton

from sguiprocess.widgets import SObserverGui

class SPlugin(QObject):
    """Worker interface for plugin

    """
    finished = Signal()
    progress = Signal(int)
    log = Signal(str)

    def __init__(self):
        self.observer = SObserverGui()
        self.widget = None
        # connect observer to Qt signals
        self.init_ui()
        
    def widget(self) -> QWidget():
        return self.widget

    def init_ui():
        raise NotImplementedError()

    def state(self) -> dict:    
        #{'name': 'SPlugin', 'inputs': [], 'parameters': {}, 'outputs': []} 
        raise NotImplementedError()   

    def run(self):
        raise NotImplementedError()


class SPluginWidget(QWidget):
    """SPluginWidget

    Main widget for a S plugin. A plugin is a widget to setup
    the parameters and exec the plugin

    """
    def __init__(self, worker: SPlugin):
        self.name = 'SPlugin'
        self.worker = worker
        self.thread = QThread()  
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.progress.connect(self.reportProgress)
        self.worker.progress.connect(self.reportLog)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(self.worker.widget())

        run_btn = QPushButton('Run')
        layout.addWidget(run_btn)

        logWidget = SLogWidget()
        layout.addWidget(logWidget)
        self.setLayout(layout)

    def run(self):
        self.thread.start()
