import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer.
        uic.loadUi("sign_raw_transaction.ui", self)

        # Create the event handlers
        # button handler
        self.pushbutton_generate.clicked.connect(self.generateTX)

        # Input method for networkid
        self.radiobutton_networkid_textbox.clicked.connect(self.setNetworkIDField)
        self.radiobutton_networkid_dropdown.clicked.connect(self.setNetworkIDField)

        # Input method for private key
        self.radiobutton_keystore.clicked.connect(self.setKeyField)
        self.radiobutton_key.clicked.connect(self.setKeyField)

        # Insert file dialog manually
        self.pushbutton_browse.clicked.connect(self.browse)

        # Input method for private key
        #self.radiobutton_key.clicked.connect(self.set

        self.show()

    def browse(self):
        self.textbox_keystore.setText(QFileDialog().\
          getOpenFileName(None, "Select keystore file", "", "JSON (*.json)")[0])

    def setNetworkIDField(self):
        textbox = self.radiobutton_networkid_textbox.isChecked()
        self.combobox_networkid.setEnabled(not textbox)
        self.textbox_networkid.setEnabled(textbox)

    def setKeyField(self):
        # TODO
        pass

    def generateTX(self):
        self.textbrowser_result.insertPlainText("Did it work?")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
