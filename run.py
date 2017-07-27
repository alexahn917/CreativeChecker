import sys
from ui import Ui_MainWindow as UI
from PyQt5 import QtWidgets
from verify import *
import zipfile
import shutil

class CreativeChecker(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CreativeChecker, self).__init__(parent)
        self.ui = UI()
        self.ui.setupUi(self)
        self.set_up_backend()

    def set_up_backend(self):
        self.ui.btn_checker_zip.clicked.connect(self.on_checker_click_zip)
        self.ui.btn_checker_jpeg.clicked.connect(self.on_checker_click_jpeg)

    def on_checker_click_zip(self):
        self.ui.result_txt_box.setText("")
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if is_valid_zip_file(fileName):
            zip_ref = zipfile.ZipFile(fileName, 'r')
            zip_ref.extractall('temp')
            zip_ref.close()
            error_msg = verify_images_in_dir('temp')
            shutil.rmtree('temp')
            self.ui.result_txt_box.setText(error_msg)
        elif not fileName:
            pass
        else:
            self.pop_up_message("Not a zip file")

    def on_checker_click_jpeg(self):
        self.ui.result_txt_box.setText("")
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileNames, _ = QtWidgets.QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        error_msg = ""
        for fileName in fileNames:
            if is_valid_image_file(fileName):
                error_msg += verify_image(fileName)
        self.ui.result_txt_box.setText(error_msg)

    def pop_up_message(self, msg):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setIcon(QtWidgets.QMessageBox.Warning)
        msgbox.setText(msg)
        msgbox.setWindowTitle("Error")
        msgbox.exec_()


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = CreativeChecker()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()