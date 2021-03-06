import sys

from PyQt5 import QtWidgets,QtGui

def pencere():

    app = QtWidgets.QApplication([sys.argv])

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 1")

    etiket1 = QtWidgets.QLabel(pencere)
    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("jaguar.jpg"))


    etiket1.setText("Yazmak İyidir")
    etiket1.move(500,30)


    pencere.setGeometry(0,30,2000,1000)

    pencere.show()

    sys.exit(app.exec_())

pencere()