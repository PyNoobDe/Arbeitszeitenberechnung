import sys  # Importiere das Modul sys

from qtpy import QtWidgets, QtGui, QtCore  # Importiere die Klassen QtWidgets, QtGui und QtCore aus dem Modul qtpy

app = QtWidgets.QApplication(sys.argv)  # Erstelle eine QApplication mit den Kommandozeilenargumenten

window = QtWidgets.QMainWindow()  # Erstelle ein Hauptfenster (QMainWindow)

window.setGeometry(900, 450, 420, 190)  # Setze die Position und Größe des Fensters
window.setWindowTitle("Berechnung Arbeitszeit")  # Setze den Fenstertitel

icon = QtGui.QIcon()  # Erstelle ein Icon-Objekt
icon.addPixmap(QtGui.QPixmap("python.ico"))  # Füge ein Pixmap zum Icon hinzu
window.setWindowIcon(icon)  # Setze das Icon für das Fenster

eingabefeld_arbeitsbeginn1 = QtWidgets.QTimeEdit(window)  # Erstelle ein Eingabefeld für die Arbeitsbeginnzeit 1
eingabefeld_arbeitsbeginn1.setGeometry(120, 10, 60, 30)  # Setze die Position und Größe des Eingabefelds
arbeitsbeginn_label1 = QtWidgets.QLabel(window)  # Erstelle ein Beschriftungsfeld für den Arbeitsbeginn 1
arbeitsbeginn_label1.setGeometry(10, 10, 90, 30)  # Setze die Position und Größe des Beschriftungsfelds
arbeitsbeginn_label1.setText("Arbeitsbeginn 1:")  # Setze den Text des Beschriftungsfelds

#Eingabefeld - Arbeitsende1
eingabefeld_arbeitsende1 = QtWidgets.QTimeEdit(window) # Erstelle ein Eingabefeld für die Arbeitsendezeit 1
eingabefeld_arbeitsende1.setGeometry(120, 40, 60, 30) # Setze die Position und Größe des Eingabefelds
arbeitsende_label1 = QtWidgets.QLabel(window) # Erstelle ein Beschriftungsfeld für das Arbeitsende 1
arbeitsende_label1.setGeometry(10, 40, 90, 30) # Setze die Position und Größe des Beschriftungsfelds
arbeitsende_label1.setText("Arbeitsende:") # Setze den Text des Beschriftungsfelds

#Eingabefeld - Arbeitsbeginn2
eingabefeld_arbeitsbeginn2 = QtWidgets.QTimeEdit(window) # Erstelle ein Eingabefeld für die Arbeitsbeginnzeit 2
eingabefeld_arbeitsbeginn2.setGeometry(350, 10, 60, 30) # Setze die Position und Größe des Eingabefelds
arbeitsbeginn_label2 = QtWidgets.QLabel(window) # Erstelle ein Beschriftungsfeld für den Arbeitsbeginn 2
arbeitsbeginn_label2.setGeometry(240, 10, 90, 30) # Setze die Position und Größe des Beschriftungsfelds
arbeitsbeginn_label2.setText("Arbeitsbeginn 2:") # Setze den Text des Beschriftungsfelds

#Eingabefeld - Arbeitsende2
eingabefeld_arbeitsende2 = QtWidgets.QTimeEdit(window) # Erstelle ein Eingabefeld für die Arbeitsendezeit 2
eingabefeld_arbeitsende2.setGeometry(350, 40, 60, 30) # Setze die Position und Größe des Eingabefelds
arbeitsende_label2 = QtWidgets.QLabel(window) # Erstelle ein Beschriftungsfeld für das Arbeitsende 2
arbeitsende_label2.setGeometry(240, 40, 90, 30) # Setze die Position und Größe des Beschriftungsfelds
arbeitsende_label2.setText("Arbeitsende 2:") # Setze den Text des Beschriftungsfelds

ergebnisfeld_arbeitszeit = QtWidgets.QLabel(window)  # Erstelle ein Beschriftungsfeld für die Arbeitszeit
ergebnisfeld_arbeitszeit.setGeometry(130, 70, 60, 30)  # Setze die Position und Größe des Beschriftungsfelds
arbeitszeit_label = QtWidgets.QLabel(window)  # Erstelle ein Beschriftungsfeld für das Label "Arbeitszeit"
arbeitszeit_label.setGeometry(10, 70, 90, 30)  # Setze die Position und Größe des Beschriftungsfelds
arbeitszeit_label.setText("Arbeitszeit:")  # Setze den Text des Beschriftungsfelds

abzgl_pause = QtWidgets.QLabel(window)  # Erstelle ein Beschriftungsfeld für die abzüglich Pause
abzgl_pause.setGeometry(130, 100, 90, 30)  # Setze die Position und Größe des Beschriftungsfelds
abzgl_pause_label = QtWidgets.QLabel(window)  # Erstelle ein Beschriftungsfeld für das Label "abzgl. Pause"
abzgl_pause_label.setGeometry(10, 100, 90, 30)  # Setze die Position und Größe des Beschriftungsfelds
abzgl_pause_label.setText("abzgl. Pause:")  # Setze den Text des Beschriftungsfelds

def berechne_arbeitszeit():  # Definiere die Funktion "berechne_arbeitszeit"
    start_zeit1 = eingabefeld_arbeitsbeginn1.time()  # Hole die Arbeitsbeginnzeit 1 aus dem Eingabefeld
    end_zeit1 = eingabefeld_arbeitsende1.time()  # Hole die Arbeitsendzeit 1 aus dem Eingabefeld
    start_zeit2 = eingabefeld_arbeitsbeginn2.time()  # Hole die Arbeitsbeginnzeit 2 aus dem Eingabefeld
    end_zeit2 = eingabefeld_arbeitsende2.time()  # Hole die Arbeitsendzeit 2 aus dem Eingabefeld

    arbeitszeit = start_zeit1.secsTo(end_zeit1) / 3600.0 + start_zeit2.secsTo(end_zeit2) / 3600.0
    # Berechne die Arbeitszeit in Stunden (Differenz zwischen Start- und Endzeit für beide Zeiträume)
    arbeitszeit = round(arbeitszeit, 2)  # Runde die Arbeitszeit auf 2 Nachkommastellen
    ergebnisfeld_arbeitszeit.setText(str(arbeitszeit))  # Setze die berechnete Arbeitszeit als Text in das Beschriftungsfeld

    if arbeitszeit > 5.99:  # Wenn die Arbeitszeit größer als 5.99 Stunden ist
        arbeitszeit_abzgl_pause = arbeitszeit - 0.5  # Ziehe 0.5 Stunden für die Pause ab
        arbeitszeit_abzgl_pause = round(arbeitszeit_abzgl_pause, 2)  # Runde die bereinigte Arbeitszeit auf 2 Nachkommastellen
        abzgl_pause.setText(str(arbeitszeit_abzgl_pause))  # Setze die bereinigte Arbeitszeit als Text in das Beschriftungsfeld

def keyPressEvent(event):  # Definiere die Funktion "keyPressEvent"
    if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
        berechne_arbeitszeit()  # Wenn die Enter-Taste gedrückt wird, rufe die Funktion "berechne_arbeitszeit" auf
    elif event.key() == QtCore.Qt.Key.Key_Escape:
        program_quit()  # Wenn die Escape-Taste gedrückt wird, rufe die Funktion "program_quit" auf
    else:
        super(QtWidgets.QMainWindow, window).keyPressEvent(event)

window.keyPressEvent = keyPressEvent  # Setze die Funktion "keyPressEvent" als Handler für Tastatureingaben im Fenster

button_quit = QtWidgets.QPushButton(window)  # Erstelle einen Button für das Beenden des Programms
button_quit.setText("Programm beenden")  # Setze den Text des Buttons
button_quit.setGeometry(150, 150, 120, 30)  # Setze die Position und Größe des Buttons

def program_quit():  # Definiere die Funktion "program_quit"
    sys.exit(app.exec())  # Beende das Programm

button_quit.clicked.connect(program_quit)  # Verbinde den Button-Klick mit der Funktion "program_quit"
window.show()  # Zeige das Fenster an
sys.exit(app.exec())  # Starte die Qt-Anwendung und beende das Programm nach dem Schließen des Fensters
