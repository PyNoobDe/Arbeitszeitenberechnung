import sys
from qtpy import QtWidgets, QtGui, QtCore

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow()
window.setGeometry(900, 450, 420, 190)
window.setWindowTitle("Berechnung Arbeitszeit")
icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap("python.ico"))
window.setWindowIcon(icon)

#Eingabefeld - Arbeitsbeginn1
eingabefeld_arbeitsbeginn1 = QtWidgets.QTimeEdit(window)
eingabefeld_arbeitsbeginn1.setGeometry(120, 10, 60, 30)
arbeitsbeginn_label1 = QtWidgets.QLabel(window)
arbeitsbeginn_label1.setGeometry(10, 10, 90, 30)
arbeitsbeginn_label1.setText("Arbeitsbeginn 1:")

#Eingabefeld - Arbeitsende1
eingabefeld_arbeitsende1 = QtWidgets.QTimeEdit(window)
eingabefeld_arbeitsende1.setGeometry(120, 40, 60, 30)
arbeitsende_label1 = QtWidgets.QLabel(window)
arbeitsende_label1.setGeometry(10, 40, 90, 30)
arbeitsende_label1.setText("Arbeitsende:")

#Eingabefeld - Arbeitsbeginn2
eingabefeld_arbeitsbeginn2 = QtWidgets.QTimeEdit(window)
eingabefeld_arbeitsbeginn2.setGeometry(350, 10, 60, 30)
arbeitsbeginn_label2 = QtWidgets.QLabel(window)
arbeitsbeginn_label2.setGeometry(240, 10, 90, 30)
arbeitsbeginn_label2.setText("Arbeitsbeginn 2:")

#Eingabefeld - Arbeitsende2
eingabefeld_arbeitsende2 = QtWidgets.QTimeEdit(window)
eingabefeld_arbeitsende2.setGeometry(350, 40, 60, 30)
arbeitsende_label2 = QtWidgets.QLabel(window)
arbeitsende_label2.setGeometry(240, 40, 90, 30)
arbeitsende_label2.setText("Arbeitsende 2:")


#Ergebnisfeld - Arbeitszeit
ergebnisfeld_arbeitszeit = QtWidgets.QLabel(window)
ergebnisfeld_arbeitszeit.setGeometry(130, 70, 60, 30)
arbeitszeit_label = QtWidgets.QLabel(window)
arbeitszeit_label.setGeometry(10, 70, 90, 30)
arbeitszeit_label.setText("Arbeitszeit:")


#Ergebnisfeld - Arbeitszeit abzgl. Pause
abzgl_pause = QtWidgets.QLabel(window)
abzgl_pause.setGeometry(130, 100, 90, 30)
abzgl_pause_label = QtWidgets.QLabel(window)
abzgl_pause_label.setGeometry(10, 100, 90, 30)
abzgl_pause_label.setText("abzgl. Pause:")


def berechne_arbeitszeit():
    start_zeit1 = eingabefeld_arbeitsbeginn1.time()
    end_zeit1 = eingabefeld_arbeitsende1.time()
    start_zeit2 = eingabefeld_arbeitsbeginn2.time()
    end_zeit2 = eingabefeld_arbeitsende2.time()

    arbeitszeit = start_zeit1.secsTo(end_zeit1) / 3600.0 + start_zeit2.secsTo(end_zeit2) / 3600.0
    arbeitszeit = round(arbeitszeit, 2)
    ergebnisfeld_arbeitszeit.setText(str(arbeitszeit))
    if arbeitszeit > 5.99:
        arbeitszeit_abzgl_pause = arbeitszeit-0.5
        arbeitszeit_abzgl_pause = round(arbeitszeit_abzgl_pause, 2)
        abzgl_pause.setText(str(arbeitszeit_abzgl_pause))

#Enter-Taste löst die Berechnung aus // ESC-Taste beendet das Programm
def keyPressEvent(event):
    if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
        berechne_arbeitszeit()
    elif event.key() == QtCore.Qt.Key.Key_Escape:
        program_quit()
    else:
        super(QtWidgets.QMainWindow, window).keyPressEvent(event)


window.keyPressEvent = keyPressEvent

#Button - Quit
button_quit = QtWidgets.QPushButton(window)
button_quit.setText("Programm beenden")
button_quit.setGeometry(150, 150, 120, 30)

def program_quit():
    sys.exit(app.exec())
button_quit.clicked.connect(program_quit)
window.show()
sys.exit(app.exec())
