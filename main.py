import sys

from PyQt5.QtWidgets import QApplication

from scripts.welcome import Welcome

if __name__ == '__main__':
    from PyQt5 import QtCore, QtWidgets

    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    ex = Welcome()
    ex.show()
    sys.exit(app.exec_())