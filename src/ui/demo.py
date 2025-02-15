# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\ui\demo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtMultimediaWidgets, QtWidgets, QtMultimedia
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from pipeline import exercise_map
import pathlib
#from .form import FormWindow




class ExerciseDemoWindow(object):
    def __init__(self, recordWindowReference) -> None:
        self.recordWindowReference = recordWindowReference
        
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rootLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.rootLayout.setContentsMargins(24, -1, 24, -1)
        self.rootLayout.setObjectName("rootLayout")

        self.MainWindow.setWindowIcon(QtGui.QIcon('favicon.png'))

        self.exerciseTypeLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.exerciseTypeLabel.sizePolicy().hasHeightForWidth()
        )
        self.exerciseTypeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.exerciseTypeLabel.setFont(font)
        self.exerciseTypeLabel.setStyleSheet(
            "background: rgba(0, 0, 0, 0.5);\n" "color: white;\n" ""
        )
        self.exerciseTypeLabel.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop
        )
        self.exerciseTypeLabel.setWordWrap(True)
        self.exerciseTypeLabel.setObjectName("exerciseTypeLabel")
        self.rootLayout.addWidget(self.exerciseTypeLabel)

        self.videoWidget = QtMultimediaWidgets.QVideoWidget(self.centralwidget)
        self.mediaPlayer = QtMultimedia.QMediaPlayer(
            None, QtMultimedia.QMediaPlayer.VideoSurface
        )
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(
            self.videoWidget.sizePolicy().hasHeightForWidth()
        )
        self.videoWidget.setSizePolicy(sizePolicy)
        self.videoWidget.stackUnder(self.exerciseTypeLabel)
        self.rootLayout.addWidget(self.videoWidget)
        
        #back button
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setStyleSheet(
            """
            border-width: 5px;
            border-color: #000000;
            border-radius: 5px;
            background: #0a0a23;
            color: #FEFEFE;
            padding: 10px 20px;
            font-size: 12px;
            font-weight: bold;
            """
        )
        font = QtGui.QFont()
        font.setPointSize(16)
        self.backButton.setFont(font)
        sizePolicy.setHeightForWidth(
            self.backButton.sizePolicy().hasHeightForWidth()
        )
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setMinimumSize(QtCore.QSize(0, 0))
        self.rootLayout.addWidget(self.backButton, 0, QtCore.Qt.AlignHCenter)
        #end of back button
        
        #next button
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setStyleSheet(
            """
            border-width: 5px;
            border-color: #000000;
            border-radius: 5px;
            background: #0a0a23;
            color: #FEFEFE;
            padding: 10px 20px;
            font-size: 12px;
            font-weight: bold;
            """
        )

        #styling 
        self.MainWindow.setStyleSheet(
            """            
            background-color: #4d47b2;
            border-radius: 10px;
            color: #FFFFFF;
            font-family: Arial, Helvetica, sans-serif;
            """
        )

        font = QtGui.QFont()
        font.setPointSize(16)
        self.nextButton.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.nextButton.sizePolicy().hasHeightForWidth()
        )
        self.nextButton.setSizePolicy(sizePolicy)
        self.nextButton.setMinimumSize(QtCore.QSize(0, 0))
        self.rootLayout.addWidget(self.nextButton, 0, QtCore.Qt.AlignHCenter)
        self.rootLayout.setStretch(0, 0)
        self.rootLayout.setStretch(1, 4)
        self.rootLayout.setStretch(2, 1)


        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

        self.exercise_type = None
        self.state = None
        self.mediaPlayer.stateChanged.connect(self.handle_media_state_changed)
        self.nextButton.clicked.connect(self.handle_next_button_clicked)

        #set form here
        '''self.formWindowContainer = QtWidgets.QMainWindow()
        self.formWindow = FormWindow(self)
        self.formWindow.setupUi(self.formWindowContainer)'''

    def set_state(self, state):
        self.state = state

    def set_exercise_type(self, exercise_type):
        self.exercise_type = exercise_type
        self.exerciseTypeLabel.setText(
            "A professional trainer performing {}".format(self.exercise_type),
        )
        self.play_exercise_video_file()

    def play_exercise_video_file(self):
        if self.exercise_type is None or not isinstance(
            self.exercise_type, str
        ):
            return

        exercise_type_short = exercise_map[self.exercise_type]
        filepath = str(
            pathlib.Path(".")
            .absolute()
            .joinpath(
                "src",
                "ui",
                "videos",
                "{}_expert.avi".format(exercise_type_short),
            )
        )
        self.mediaPlayer.setMedia(
            QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(filepath))
        )
        self.mediaPlayer.play()

    def handle_media_state_changed(self, state):
        # continuous loop
        if self.mediaPlayer.state() == QtMultimedia.QMediaPlayer.StoppedState:
            self.play_exercise_video_file()
    
    # handle next button
    def handle_next_button_clicked(self):
        self.recordWindowReference.set_state(self.state)
        self.recordWindowReference.MainWindow.show()
        self.MainWindow.close()

    # handle back button
    def handle_back_button_clicked(self):
        self.form

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Exercise Demo"))
        self.exerciseTypeLabel.setText(_translate("MainWindow", "",))
        self.nextButton.setText(_translate("MainWindow", "Next"))
        self.backButton.setText(_translate("MainWindow", "Back"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ExerciseDemoWindow(None)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
