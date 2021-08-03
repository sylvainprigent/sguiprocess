import sys
import time
from qtpy.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout, QLabel

from sguiprocess.plugin import SPlugin, SPluginWidget

# create a new plugin
class SDemoPlugin(SPlugin):
    def __init__(self):
        super().__init__()

    def init_ui(self):
        self._widget = QWidget()
        layout = QGridLayout()
        self.name_parameter = QLineEdit()
        layout.addWidget(QLabel('What is your name:'), 0, 0)
        layout.addWidget(self.name_parameter, 0, 1)
        self._widget.setLayout(layout)

    def state(self) -> dict:
        return {'name': 'SDemoPlugin', 'inputs': [],
                'parameters': {'your_name': self.name_parameter.text()},
                'outputs': []}

    def run(self):
        name = self.state()['parameters']['your_name']
        self.log.emit('Hello ' + name)
        self.log.emit('The progress bar will move slowly ')
        for i in range(100+1):
            time.sleep(1)
            self.progress.emit(i)


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)

    # load the settings
    plugin = SPluginWidget(SDemoPlugin())
    plugin.show()

    #w = SLogWidget()
    #w.set_progress(50)
    #w.add_log('Hello')
    #w.show()

    # Run the main Qt loop
    sys.exit(app.exec_())