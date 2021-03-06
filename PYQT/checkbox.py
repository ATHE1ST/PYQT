import sys

from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.checkbox = QCheckBox("Ünal Pc'mi hackleyebilir mi?")
        self.yazı_alanı = QLabel("")
        self.buton = QPushButton("Tıkla")

        v_box = QVBoxLayout()

        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.setWindowTitle("Check box")

        self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.yazı_alanı))

        self.show()

    def click(self,checkbox,yazı_alanı):
        if checkbox:
            self.yazı_alanı.setText("BOKUMU HACKLER!!!")
        else:
            self.yazı_alanı.setText("BENCEDE SİKTİRSİN!!!")


app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())