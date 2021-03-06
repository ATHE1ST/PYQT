import sys
import os

from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow,QVBoxLayout,QHBoxLayout,QPushButton,QLabel,QTextEdit

class Menu(QMainWindow):
    def __init__(self):

        super().__init__()


        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")
        duzenle = menubar.addMenu("Düzenle")

        dosya_ac = QAction("Dosya Aç",self)
        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet = QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")

        cıkıs = QAction("Çıkış",self)
        cıkıs.setShortcut("Ctrl+Q")

        sil_ara = duzenle.addMenu("Sil ve Ara")

        sil = QAction("Sil",self)
        sil.setShortcut("Ctrl+D")

        ara = QAction("Ara",self)
        ara.setShortcut("Ctrl+F")


        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cıkıs)

        sil_ara.addAction(sil)
        sil_ara.addAction(ara)


        self.setWindowTitle("Menüler")
        self.show()






app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())