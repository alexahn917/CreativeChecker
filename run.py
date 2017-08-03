import sys
from UI.ui import Ui_MainWindow as UI
from PyQt5 import QtWidgets
from Utils.verify import *
from Utils.resize import *
from subprocess import call
import zipfile
import shutil

class CreativeChecker(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CreativeChecker, self).__init__(parent)
        self.ui = UI()
        self.ui.setupUi(self)
        self.set_up_backend()

    def set_up_backend(self):
        self.ui.btn_checker_zip.clicked.connect(self.on_click_checker_zip)
        self.ui.btn_checker_img.clicked.connect(self.on_click_checker_img)
        self.ui.btn_checker_resize.clicked.connect(self.on_click_resize)


    def on_click_checker_zip(self):
        self.ui.result_txt_box.setText("")
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Select a .zip file", "","All Files (*);;Python Files (*.py)", options=options)
        if is_valid_zip_file(fileName):
            dirPath = str.join("/", fileName.split("/")[:-1])
            tempPath = dirPath + '/temp'
            zip_ref = zipfile.ZipFile(fileName, 'r')
            zip_ref.extractall(tempPath)
            zip_ref.close()
            error_msg = ""
            if len(os.listdir(tempPath)) is 1:
                tempPath = dirPath + "/temp/" + os.listdir(tempPath)[0]
            try:
                error_msg = verify_images_in_dir(tempPath)
            except:
                self.pop_up_message("Error occurred while verifying images in the selected zip file")
            shutil.rmtree(dirPath + "/temp")
            self.ui.result_txt_box.setText(self.clean_up_error_msg(error_msg))
        elif not fileName:
            pass
        else:
            self.pop_up_message("Not a zip file")

    def on_click_checker_img(self):
        self.ui.result_txt_box.setText("")
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileNames, _ = QtWidgets.QFileDialog.getOpenFileNames(self,"Select image(s)", "","All Files (*);;Python Files (*.py)", options=options)
        error_msg = ""
        for fileName in fileNames:
            if is_valid_image_file(fileName):
                try:
                    error_msg += verify_image(fileName)
                except:
                    self.pop_up_message("Error occurred while verifying image [%s]" %fileName)
                    pass
            else:
                error_msg += "[%s] is not an image file\n" %path_leaf(fileName)
        self.ui.result_txt_box.setText(self.clean_up_error_msg(error_msg))

    def on_click_resize(self):
        self.ui.result_txt_box.setText("")
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        dirPath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', options=options)
        error_msg = ""
        if dirPath:
            try:
                error_msg = resize(dirPath)
                targetDirectory = dirPath
                call(["open", targetDirectory])
            except:
                self.pop_up_message("Error occurred while resizing images in the selected directory")
        self.ui.result_txt_box.setText(error_msg)

    def pop_up_message(self, msg):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setIcon(QtWidgets.QMessageBox.Warning)
        msgbox.setText(msg)
        msgbox.setWindowTitle("Error")
        msgbox.exec_()

    def clean_up_error_msg(self, msg):
        if not msg:
            return ""
        error = "<Invalid Creatives>\n\n"
        ok = "<Valid Creatives>\n\n"
        for line in msg.split('\n'):
            if "OK" in line:
                ok += line + "\n"
            else:
                error += line + "\n"
        return error + ok

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = CreativeChecker()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()