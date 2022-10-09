from PySide2.QtWidgets import *


""""""
from view.ui_ViewQt import Ui_Form
from model.Lexico import lexico
from model.lexicoAux import lexicoAux
from model.semantico import semantico


class Compilador(QWidget, Ui_Form):
      def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.cargarPushButton.clicked.connect(self.AbrirBuscador)
            self.pushButton.clicked.connect(self.Lexicon)
            self.pushButtonSemantico.clicked.connect(self.Semantico)

      def AbrirBuscador(self):
            dlg = QFileDialog()
            if dlg.exec_():
                  filename = dlg.selectedFiles()
                  f = open(filename[0], "r")

            with f:
                  data = f.read().strip()
                  if data:
                        self.TxtPlainTextEdit.setPlainText(data + "\n")

      def Lexicon(self):
            self.LexplainTextEdit.setPlainText("")
            datos = self.TxtPlainTextEdit.toPlainText().strip()
            resultadoLexico = lexico(datos)
            self.LexplainTextEdit.setPlainText("Analizando lexico")
            cadena = ""
            for lex in resultadoLexico:
                  cadena += lex + "\n"
            self.LexplainTextEdit.setPlainText(cadena)

      def Semantico(self):
            print("SEMANTICO")
            self.semanticoTextEdit.setPlainText("")
            datos = self.TxtPlainTextEdit.toPlainText().strip()
            lexicoAux(datos)
            resultadoSemantico = semantico(datos)
            if len(resultadoSemantico) == 0:
                  self.semanticoTextEdit.setPlainText("TODO OK")
            else:      
                  cadena = ''
                  for item in resultadoSemantico:
                        cadena += item + "\n"
                  self.semanticoTextEdit.setPlainText(cadena)
            
      

      def Limpiar(self):
            self.LexplainTextEdit.setPlainText("")
            self.TxtPlainTextEdit.setPlainText("")
