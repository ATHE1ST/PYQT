import sys
import os

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout

class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.yazı_alanı = QTextEdit()

        self.temizle = QPushButton("Temizle")
        self.ac = QPushButton("Aç")
        self.kaydet = QPushButton("Kaydet")

        h_box = QHBoxLayout()

        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        v_box = QVBoxLayout()

        v_box.addWidget(self.yazı_alanı)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle("Notepad")
        self.temizle.clicked.connect(self.yaziyi_temizle)
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)

        self.show()

    def yaziyi_temizle(self):
        self.yazı_alanı.clear()


    def dosya_ac(self):

        dosya_ismi = QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("Masaüstü"))
        print(dosya_ismi)

        with open(dosya_ismi[0],"r") as file:
            self.yazı_alanı.setText(file.read())


    def dosya_kaydet(self):

        dosya_ismi = QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))

        with open(dosya_ismi[0],"w") as file:
            file.write(self.yazı_alanı.toPlainText())


app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())