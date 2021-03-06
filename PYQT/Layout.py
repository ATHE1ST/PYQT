import sys

from PyQt5 import QtWidgets,QtGui

uygulamam = QtWidgets.QApplication(sys.argv)
pencere = QtWidgets.QWidget()
etiket = QtWidgets.QLabel("Python dersleri")
buton = QtWidgets.QPushButton("Tamam")
buton2 = QtWidgets.QPushButton("Çık")


h_box = QtWidgets.QHBoxLayout()
h_box.addStretch()
h_box.addWidget(buton)
h_box.addWidget(buton2)


v_box = QtWidgets.QVBoxLayout()
v_box.addStretch()
v_box.addLayout(h_box)


pencere.setLayout(v_box)
pencere.setWindowTitle("Programım")
pencere.setGeometry(100,100,500,500)
pencere.show()

sys.exit(uygulamam.exec_())



