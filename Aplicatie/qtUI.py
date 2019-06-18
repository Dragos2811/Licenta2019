from PySide2 import QtWidgets
import glob
import os
from PyQt5 import QtCore
from PyQt5 import QtMultimedia as M
import main
class MyQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.getMusicians()
        self.generareBtn.clicked.connect(self.generare)
       # self.url = QtCore.QUrl.fromLocalFile(os.path.abspath('byron.mp3'))
        self.url = QtCore.QUrl.fromLocalFile(os.path.abspath('byron.mp3'))
        print(self.url)
        self.content = M.QMediaContent(self.url)
        self.player = M.QMediaPlayer()
        self.player.setMedia(self.content)
        self.playBtn.pressed.connect(self.play)
        self.pauseBtn.pressed.connect(self.pause)
    def play(self):
        print("play")
        self.player.play()
    def pause(self):
        self.player.pause()
    def generare(self):
        #predict.create_midi(predict.get_notes())
        print("generare")
    def getMusicians(self):
        path = 'D:\\Dropbox\\licenta\\practice\\Proiect\\models'
        files = [os.path.basename(f).split(".")[0] for f in glob.glob(path + "**/*.hdf5")]
        self.comboBox.clear()
        for f in files:
            self.comboBox.addItem(f)




if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()