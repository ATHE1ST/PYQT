import sys
import sqlite3
from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()
        self.baglanti_kur()
        self.init_ui()
        self.baglanti_ekle()

    def baglanti_kur(self):
        con = sqlite3.connect("yenidatabase.db")
        self.cursor = con.cursor()
        self.cursor.execute("create table if not exists isimler(İsim TEXT,Parola TEXT)")
        con.commit()


    def init_ui(self):

        self.kullanıcı_adi = QtWidgets.QLineEdit("Adınız...")
        self.parola = QtWidgets.QLineEdit("")
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş")
        self.yazi_alani = QtWidgets.QLabel("")
        self.kayit = QtWidgets.QPushButton("Kayıt Ol")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanıcı_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.giris)
        v_box.addWidget(self.kayit)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()


        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("Kullanıcı Girişi")
        self.giris.clicked.connect(self.login)
        self.kayit.clicked.connect(self.baglanti_ekle)

        self.show()

    def login(self):
        adi = self.kullanıcı_adi.text()
        par = self.parola.text()

        self.cursor.execute("Select * From isimler where İsim = ? and Parola = ? ", (adi, par))
        data = self.cursor.fetchall()

        if len(data) == 0:
            self.yazi_alani.setText("Hatalı Kullanıcı Adı veya Parola\nLütfen Yeniden Deneyiniz")
        else:
            self.yazi_alani.setText("Giriş Başarılı\nHoşgeldin " + adi)

    def baglanti_ekle(self):

        con = sqlite3.connect("yenidatabase.db")
        self.cursor = con.cursor()

        isim = self.kullanıcı_adi.text()
        parol = self.parola.text()

        self.cursor.execute("insert into isimler Values(?,?)", (isim,parol))
        self.yazi_alani.setText("Kayıt Başarı ile tamamlandı.")
        con.commit()


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())


