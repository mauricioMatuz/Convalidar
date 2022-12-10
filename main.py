
from PySide2.QtWidgets import QApplication
from controller.ViewQtController import Compilador

if __name__ == '__main__':
      app =QApplication()
      windows = Compilador()
      windows.show()
      app.exec_()
#! encontro fallas :C for solo imprimir