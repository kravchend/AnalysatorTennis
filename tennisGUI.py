from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QPainter, QColor
import sys
from modulTennis import *
import os


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class Ui_tennis(object):
    def setupUi(self, tennis):
        self.tennis = tennis
        tennis.setObjectName("tennis")
        tennis.setEnabled(True)
        tennis.setFixedSize(1400, 670)
        tennis.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        tennis.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.offset = None

        self.centralwidget = QtWidgets.QWidget(tennis)
        self.centralwidget.setStyleSheet("background: transparent;")
        self.centralwidget.setObjectName("centralwidget")
        tennis.setCentralWidget(self.centralwidget)
        self.add_shadow_effect(self.centralwidget, x_offset=20, y_offset=25, blur_radius=30)

        self.gradient_background = QtWidgets.QLabel(self.centralwidget)
        self.gradient_background.setGeometry(QtCore.QRect(0, 0, 1400, 670))
        self.gradient_background.setStyleSheet("background-color: rgba(25, 36, 40, 0.92); border: 3px solid #164147;")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 12, 661, 40))
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET") 
        font.setPointSize(23)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.add_shadow_effect(self.label, x_offset=6, y_offset=6, blur_radius=25)
        self.p1_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.p1_1.setGeometry(QtCore.QRect(190, 161, 100, 30))
        self.p1_1.setStyleSheet("background-color: rgb(14, 30, 40); font-size: 24px;")
        self.p1_1.setObjectName("p1_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(137, 41, 250, 31))
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.add_shadow_effect(self.label_2, x_offset=6, y_offset=6, blur_radius=25)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(548, 41, 245, 31))
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.add_shadow_effect(self.label_3, x_offset=6, y_offset=6, blur_radius=25)
        self.name_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.name_1.setGeometry(QtCore.QRect(52, 85, 358, 32))
        self.name_1.setStyleSheet("background-color: rgb(14, 30, 40); font-size: 20px;")
        self.name_1.setAlignment(QtCore.Qt.AlignCenter)
        self.name_1.setObjectName("name_1")
        self.name_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.name_2.setGeometry(QtCore.QRect(465, 85, 360, 32))
        self.name_2.setStyleSheet("background-color: rgb(14, 30, 40); font-size: 20px;")
        self.name_2.setAlignment(QtCore.Qt.AlignCenter)
        self.name_2.setObjectName("name_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(135, 122, 275, 30))
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_4.setObjectName("label_4")
        self.add_shadow_effect(self.label_4, x_offset=6, y_offset=6, blur_radius=25)
        self.p1_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.p1_2.setGeometry(QtCore.QRect(600, 161, 100, 30))
        self.p1_2.setStyleSheet("background-color: rgb(14, 30, 40); font-size: 24px;")
        self.p1_2.setWrapping(False)
        self.p1_2.setObjectName("p1_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(545, 122, 276, 30))
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_5.setObjectName("label_5")
        self.add_shadow_effect(self.label_5, x_offset=6, y_offset=6, blur_radius=25)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 198, 281, 30))
        self.label_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_6.setObjectName("label_6")
        self.add_shadow_effect(self.label_6, x_offset=6, y_offset=6, blur_radius=25)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(547, 198, 291, 30))
        self.label_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_7.setObjectName("label_7")
        self.add_shadow_effect(self.label_7, x_offset=6, y_offset=6, blur_radius=25)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(535, 275, 280, 30))
        self.label_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_8.setObjectName("label_8")
        self.add_shadow_effect(self.label_8, x_offset=6, y_offset=6, blur_radius=25)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(123, 275, 280, 30))
        self.label_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_9.setLineWidth(-1)
        self.label_9.setObjectName("label_9")
        self.add_shadow_effect(self.label_9, x_offset=6, y_offset=6, blur_radius=25)
        self.p2_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.p2_2.setGeometry(QtCore.QRect(600, 239, 100, 30))
        self.p2_2.setStyleSheet("background-color: rgb(14, 30, 40); font-size: 24px;")
        self.p2_2.setObjectName("p2_2")
        self.p2_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.p2_1.setGeometry(QtCore.QRect(190, 239, 100, 30))
        self.p2_1.setStyleSheet("background-color: rgb(14, 30, 40); font-size: 24px;")
        self.p2_1.setObjectName("p2_1")
        self.p3_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.p3_2.setGeometry(QtCore.QRect(600, 317, 100, 30))
        self.p3_2.setStyleSheet("background-color: rgb(14, 30, 40); font-size: 24px;")
        self.p3_2.setObjectName("p3_2")
        self.p3_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.p3_1.setGeometry(QtCore.QRect(190, 317, 100, 30))
        self.p3_1.setStyleSheet("background-color: rgb(14, 30, 40); font-size: 24px;")
        self.p3_1.setObjectName("p3_1")

        self.game_Winnerlicht = QtWidgets.QLabel(self.centralwidget)
        self.game_Winnerlicht.setGeometry(QtCore.QRect(179, 464, 535, 50))
        self.game_Winnerlicht.setStyleSheet("background-color: rgb(57, 57, 57);")
        self.game_Winnerlicht.setObjectName("game_Winnerlicht")
        self.licht_effect(self.game_Winnerlicht, x_offset=0, y_offset=-7, blur_radius=45)

        self.game_WinnerLinks = QtWidgets.QLabel(self.centralwidget)
        self.game_WinnerLinks.setGeometry(QtCore.QRect(175, 462, 545, 50))
        self.game_WinnerLinks.setStyleSheet("background-color: rgb(57, 57, 57);")
        self.game_WinnerLinks.setObjectName("game_WinnerLinks")
        self.add_shadow_effect(self.game_WinnerLinks, x_offset=-11, y_offset=0, blur_radius=60)

        self.game_WinnerRecht = QtWidgets.QLabel(self.centralwidget)
        self.game_WinnerRecht.setGeometry(QtCore.QRect(175, 462, 545, 50))
        self.game_WinnerRecht.setStyleSheet("background-color: rgb(57, 57, 57);")
        self.game_WinnerRecht.setObjectName("game_WinnerRecht")
        self.add_shadow_effect(self.game_WinnerRecht, x_offset=12, y_offset=0, blur_radius=60)

        self.game_WinnerRamka = QtWidgets.QLabel(self.centralwidget)
        self.game_WinnerRamka.setGeometry(QtCore.QRect(175, 462, 545, 50))
        self.game_WinnerRamka.setStyleSheet("background-color: rgb(0, 0, 0); font-size: 20px;")
        self.game_WinnerRamka.setFrameShape(QtWidgets.QFrame.Box)
        self.game_WinnerRamka.setFrameShadow(QtWidgets.QFrame.Raised)
        self.game_WinnerRamka.setLineWidth(5)
        self.game_WinnerRamka.setMidLineWidth(2)
        self.game_WinnerRamka.setObjectName("game_WinnerRamka")
        self.apply_3d_borders(self.game_WinnerRamka)
        self.add_shadow_effect(self.game_WinnerRamka, x_offset=0, y_offset=15, blur_radius=60)

        self.game_Winner = QtWidgets.QLabel(self.centralwidget)
        self.game_Winner.setGeometry(QtCore.QRect(183, 470, 529, 33))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(20)
        self.game_Winner.setFont(font)
        self.game_Winner.setToolTip("")
        self.game_Winner.setToolTipDuration(-1)
        self.game_Winner.setStyleSheet("background-color: rgb(14, 30, 40);")
        self.game_Winner.setObjectName("game_Winner")
        self.game_Winner.setScaledContents(True)
        self.game_Winner.setWordWrap(False)
        self.game_Winner.setIndent(-1)
        self.game_Winner.setOpenExternalLinks(False)
        self.game_Winner.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.game_Winner.setAlignment(QtCore.Qt.AlignCenter)
        self.game_Winner.setWordWrap(True)
        self.game_Winner.setMargin(0)
        self.game_Winner.setIndent(0)

        self.pushBut_Game = QtWidgets.QPushButton(self.centralwidget)
        self.pushBut_Game.setGeometry(QtCore.QRect(205, 595, 115, 50))
        self.pushBut_Game.setIcon(
            QIcon(resource_path("/Users/dmitriykravchenko/Documents/Programirovanie/Tennis/images/game.png")))
        self.pushBut_Game.setIconSize(QtCore.QSize(440, 105)) 
        self.pushBut_Game.setObjectName("pushBut_Game")
        self.pushBut_Game.setStyleSheet("border-radius: 25px; border: 0px solid red;")
        self.add_shadow_effect(self.pushBut_Game, x_offset=6, y_offset=6, blur_radius=25)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(50, 468, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(24)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_11.setFont(font)
        self.label_11.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_11.setAcceptDrops(False)
        self.label_11.setToolTipDuration(-1)
        self.label_11.setStatusTip("")
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "")
        self.label_11.setLineWidth(0)
        self.label_11.setScaledContents(False)
        self.label_11.setWordWrap(False)
        self.label_11.setIndent(-1)
        self.label_11.setOpenExternalLinks(False)
        self.label_11.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_11.setObjectName("label_11")
        self.add_shadow_effect(self.label_11, x_offset=6, y_offset=6, blur_radius=25)

        self.final_Storielicht = QtWidgets.QLabel(self.centralwidget)
        self.final_Storielicht.setGeometry(QtCore.QRect(179, 533, 535, 50))
        self.final_Storielicht.setStyleSheet("background-color: rgb(57, 57, 57);")
        self.final_Storielicht.setObjectName("final_Storielicht")
        self.licht_effect(self.final_Storielicht, x_offset=0, y_offset=-7, blur_radius=45)

        self.final_StorieLinks = QtWidgets.QLabel(self.centralwidget)
        self.final_StorieLinks.setGeometry(QtCore.QRect(175, 530, 545, 50))
        self.final_StorieLinks.setStyleSheet("background-color: rgb(57, 57, 57);")
        self.final_StorieLinks.setObjectName("final_Storied")
        self.add_shadow_effect(self.final_StorieLinks, x_offset=-11, y_offset=0, blur_radius=60)

        self.final_StorieRecht = QtWidgets.QLabel(self.centralwidget)
        self.final_StorieRecht.setGeometry(QtCore.QRect(175, 530, 545, 50))
        self.final_StorieRecht.setStyleSheet("background-color: rgb(57, 57, 57);")
        self.final_StorieRecht.setObjectName("final_Storied")
        self.add_shadow_effect(self.final_StorieRecht, x_offset=12, y_offset=0, blur_radius=60)

        self.final_labelRamka = QtWidgets.QLabel(self.centralwidget)
        self.final_labelRamka.setGeometry(QtCore.QRect(175, 530, 545, 50))
        self.final_labelRamka.setStyleSheet("background-color: rgb(0, 0, 0); font-size: 20px;")
        self.final_labelRamka.setFrameShape(QtWidgets.QFrame.Box)
        self.final_labelRamka.setFrameShadow(QtWidgets.QFrame.Raised)
        self.final_labelRamka.setLineWidth(5)
        self.final_labelRamka.setMidLineWidth(2)
        self.final_labelRamka.setObjectName("final_labelRamka")
        self.apply_3d_borders(self.final_labelRamka)
        self.add_shadow_effect(self.final_labelRamka, x_offset=0, y_offset=13, blur_radius=60)

        self.final_Storie = QtWidgets.QLabel(self.centralwidget)
        self.final_Storie.setGeometry(QtCore.QRect(183, 538, 529, 33))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(20)
        self.final_Storie.setFont(font)
        self.final_Storie.setToolTip("")
        self.final_Storie.setToolTipDuration(-1)
        self.final_Storie.setStyleSheet("background-color: rgb(14, 30, 40);")
        self.final_Storie.setObjectName("final_Storie")
        self.final_Storie.setScaledContents(True)
        self.final_Storie.setWordWrap(False)
        self.final_Storie.setIndent(-1)
        self.final_Storie.setOpenExternalLinks(False)
        self.final_Storie.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.final_Storie.setAlignment(QtCore.Qt.AlignCenter)
        self.final_Storie.setWordWrap(True)
        self.final_Storie.setMargin(0)
        self.final_Storie.setIndent(0)

        self.pushBut_Reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushBut_Reset.setGeometry(QtCore.QRect(397, 595, 115, 50))
        self.pushBut_Reset.setIcon(
            QIcon(resource_path("/Users/dmitriykravchenko/Documents/Programirovanie/Tennis/images/reset.png")))
        self.pushBut_Reset.setIconSize(QtCore.QSize(445, 105)) 
        self.pushBut_Reset.setObjectName("pushBut_Reset")
        self.pushBut_Reset.setStyleSheet("border-radius: 25px; border: 0px solid red;")
        self.add_shadow_effect(self.pushBut_Reset, x_offset=6, y_offset=6, blur_radius=20)

        self.pushBut_Close = QtWidgets.QPushButton(self.centralwidget)
        self.pushBut_Close.setGeometry(QtCore.QRect(578, 595, 115, 50))
        self.pushBut_Close.setIcon(
            QIcon(resource_path("/Users/dmitriykravchenko/Documents/Programirovanie/Tennis/images/close.png")))
        self.pushBut_Close.setIconSize(QtCore.QSize(440, 105)) 
        self.pushBut_Close.setObjectName("pushBut_Close")
        self.pushBut_Close.setStyleSheet("border-radius: 25px; border: 0px solid red;")
        self.add_shadow_effect(self.pushBut_Close, x_offset=6, y_offset=6, blur_radius=25)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(548, 353, 280, 30))
        self.label_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_10.setObjectName("label_10")
        self.add_shadow_effect(self.label_10, x_offset=6, y_offset=6, blur_radius=25)
        self.p4_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.p4_2.setGeometry(QtCore.QRect(600, 395, 100, 30))
        self.p4_2.setStyleSheet("background-color: rgb(14, 30, 40); font-size: 24px;")
        self.p4_2.setObjectName("p4_2")
        self.p4_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.p4_1.setGeometry(QtCore.QRect(190, 395, 100, 30))
        self.p4_1.setStyleSheet("background-color: rgb(14, 30, 40); font-size: 24px;")
        self.p4_1.setObjectName("p4_1")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(138, 353, 280, 30))
        self.label_12.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_12.setLineWidth(0)
        self.label_12.setObjectName("label_12")
        self.add_shadow_effect(self.label_12, x_offset=6, y_offset=6, blur_radius=25)
        self.lWidget_history_game = QtWidgets.QListWidget(self.centralwidget)
        self.lWidget_history_game.setGeometry(QtCore.QRect(891, 60, 452, 545))
        self.lWidget_history_game.setStyleSheet("background-color: rgb(57, 57, 57);")
        self.lWidget_history_game.setObjectName("lWidget_history_game")

        self.history_label = QtWidgets.QLabel(self.centralwidget)
        self.history_label.setGeometry(self.lWidget_history_game.geometry())
        self.history_label.setPixmap(
            QtGui.QPixmap(resource_path("/Users/dmitriykravchenko/Documents/Programirovanie/Tennis/images/IMG_2.png"))
        )
        self.history_label.setScaledContents(True)
        self.lWidget_history_game.setStyleSheet("""
            background: transparent;
        """)

        self.label_14l = QtWidgets.QLabel(self.centralwidget)
        self.label_14l.setGeometry(QtCore.QRect(880, 45, 470, 570))
        self.label_14l.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_14l.setLineWidth(5)
        self.label_14l.setText("")
        self.label_14l.setObjectName("label_15licht")
        self.licht_effect(self.label_14l, x_offset=0, y_offset=-8, blur_radius=70)

        self.label_14licht = QtWidgets.QLabel(self.centralwidget)
        self.label_14licht.setGeometry(QtCore.QRect(873, 45, 480, 570))
        self.label_14licht.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_14licht.setLineWidth(5)
        self.label_14licht.setText("")
        self.label_14licht.setObjectName("label_15licht")
        self.add_shadow_effect(self.label_14licht, x_offset=-15, y_offset=6, blur_radius=80)

        self.label_14lichtd = QtWidgets.QLabel(self.centralwidget)
        self.label_14lichtd.setGeometry(QtCore.QRect(873, 45, 480, 570))
        self.label_14lichtd.setStyleSheet("background-color: rgb(00, 0, 0);")
        self.label_14lichtd.setLineWidth(5)
        self.label_14lichtd.setText("")
        self.label_14lichtd.setObjectName("label_15licht")
        self.add_shadow_effect(self.label_14lichtd, x_offset=17, y_offset=6, blur_radius=80)

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(873, 45, 485, 575))
        self.label_14.setAutoFillBackground(False)
        self.label_14.setStyleSheet("background-color: rgb(0, 0, 0); border-color: rgb(10, 22, 25);")
        self.label_14.setFrameShape(QtWidgets.QFrame.Box)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_14.setLineWidth(9)
        self.label_14.setMidLineWidth(2)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.add_shadow_effect(self.label_14, x_offset=0, y_offset=30, blur_radius=90)
        self.apply_3d_borders(self.label_14)

        self.label_15l = QtWidgets.QLabel(self.centralwidget)
        self.label_15l.setGeometry(QtCore.QRect(47, 80, 366, 41))
        self.label_15l.setStyleSheet("background-color: rgb(00, 0, 0);")
        self.label_15l.setLineWidth(5)
        self.label_15l.setText("")
        self.label_15l.setObjectName("label_15licht")
        self.licht_effect(self.label_15l, x_offset=0, y_offset=-7, blur_radius=45)

        self.label_15lichtd = QtWidgets.QLabel(self.centralwidget)
        self.label_15lichtd.setGeometry(QtCore.QRect(45, 80, 370, 41))
        self.label_15lichtd.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_15lichtd.setLineWidth(5)
        self.label_15lichtd.setText("")
        self.label_15lichtd.setObjectName("label_15licht")
        self.add_shadow_effect(self.label_15lichtd, x_offset=-10, y_offset=0, blur_radius=60)

        self.label_15licht = QtWidgets.QLabel(self.centralwidget)
        self.label_15licht.setGeometry(QtCore.QRect(45, 80, 370, 41))
        self.label_15licht.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_15licht.setLineWidth(5)
        self.label_15licht.setText("")
        self.label_15licht.setObjectName("label_15licht")
        self.add_shadow_effect(self.label_15licht, x_offset=12, y_offset=0, blur_radius=60)

        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(45, 79, 372, 44))
        self.label_15.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_15.setFrameShape(QtWidgets.QFrame.Box)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_15.setLineWidth(5)
        self.label_15.setMidLineWidth(2)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.add_shadow_effect(self.label_15, x_offset=0, y_offset=15, blur_radius=70)
        self.apply_3d_borders(self.label_15)

        self.label_16l = QtWidgets.QLabel(self.centralwidget)
        self.label_16l.setGeometry(QtCore.QRect(458, 80, 370, 42))
        self.label_16l.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_16l.setLineWidth(5)
        self.label_16l.setText("")
        self.label_16l.setObjectName("label_16licht")
        self.licht_effect(self.label_16l, x_offset=0, y_offset=-7, blur_radius=45)

        self.label_16licht = QtWidgets.QLabel(self.centralwidget)
        self.label_16licht.setGeometry(QtCore.QRect(456, 80, 370, 42))
        self.label_16licht.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_16licht.setLineWidth(5)
        self.label_16licht.setText("")
        self.label_16licht.setObjectName("label_16licht")
        self.add_shadow_effect(self.label_16licht, x_offset=-10, y_offset=0, blur_radius=60)

        self.label_16lichtr = QtWidgets.QLabel(self.centralwidget)
        self.label_16lichtr.setGeometry(QtCore.QRect(456, 80, 370, 42))
        self.label_16lichtr.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_16lichtr.setLineWidth(5)
        self.label_16lichtr.setText("")
        self.label_16lichtr.setObjectName("label_16lichtr")
        self.add_shadow_effect(self.label_16lichtr, x_offset=12, y_offset=0, blur_radius=60)

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(458, 78, 374, 46))
        self.label_16.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_16.setFrameShape(QtWidgets.QFrame.Box)
        self.label_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_16.setLineWidth(5)
        self.label_16.setMidLineWidth(2)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.add_shadow_effect(self.label_16, x_offset=0, y_offset=15, blur_radius=70)
        self.apply_3d_borders(self.label_16)

        self.label_17licht = QtWidgets.QLabel(self.centralwidget)
        self.label_17licht.setGeometry(QtCore.QRect(595, 158, 110, 20))
        self.label_17licht.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_17licht.setText("")
        self.label_17licht.setObjectName("label_17licht")
        self.licht_effect(self.label_17licht, x_offset=0, y_offset=-6, blur_radius=50)

        self.label_17links = QtWidgets.QLabel(self.centralwidget)
        self.label_17links.setGeometry(QtCore.QRect(592, 158, 116, 40))
        self.label_17links.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_17links.setText("")
        self.label_17links.setObjectName("label_17links")
        self.add_shadow_effect(self.label_17links, x_offset=-9, y_offset=0, blur_radius=50)

        self.label_17Rechts = QtWidgets.QLabel(self.centralwidget)
        self.label_17Rechts.setGeometry(QtCore.QRect(592, 158, 116, 40))
        self.label_17Rechts.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_17Rechts.setText("")
        self.label_17Rechts.setObjectName("label_17Rechts")
        self.add_shadow_effect(self.label_17Rechts, x_offset=10, y_offset=0, blur_radius=50)

        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(592, 156, 116, 40))
        self.label_17.setStyleSheet("background-color: rgb(10, 20, 20);")
        self.label_17.setFrameShape(QtWidgets.QFrame.Box)
        self.label_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_17.setLineWidth(1)
        self.label_17.setMidLineWidth(1)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.add_shadow_effect(self.label_17, x_offset=0, y_offset=10, blur_radius=50)
        self.apply_3d_borders(self.label_17)

        self.label_18licht = QtWidgets.QLabel(self.centralwidget)
        self.label_18licht.setGeometry(QtCore.QRect(595, 236, 110, 20))
        self.label_18licht.setStyleSheet("background-color: rgb(10, 22, 25);")
        self.label_18licht.setText("")
        self.label_18licht.setObjectName("label_18licht")
        self.licht_effect(self.label_18licht, x_offset=0, y_offset=-6, blur_radius=50)

        self.label_18links = QtWidgets.QLabel(self.centralwidget)
        self.label_18links.setGeometry(QtCore.QRect(592, 236, 116, 40))
        self.label_18links.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_18links.setText("")
        self.label_18links.setObjectName("label_18links")
        self.add_shadow_effect(self.label_18links, x_offset=-9, y_offset=0, blur_radius=50)

        self.label_18Rechts = QtWidgets.QLabel(self.centralwidget)
        self.label_18Rechts.setGeometry(QtCore.QRect(592, 236, 116, 40))
        self.label_18Rechts.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_18Rechts.setText("")
        self.label_18Rechts.setObjectName("label_18Rechts")
        self.add_shadow_effect(self.label_18Rechts, x_offset=10, y_offset=0, blur_radius=50)

        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(592, 234, 116, 40))
        self.label_18.setStyleSheet("background-color: rgb(10, 20, 20);")
        self.label_18.setFrameShape(QtWidgets.QFrame.Box)
        self.label_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_18.setLineWidth(1)
        self.label_18.setMidLineWidth(1)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.add_shadow_effect(self.label_18, x_offset=0, y_offset=10, blur_radius=50)
        self.apply_3d_borders(self.label_18)

        self.label_19licht = QtWidgets.QLabel(self.centralwidget)
        self.label_19licht.setGeometry(QtCore.QRect(595, 314, 110, 20))
        self.label_19licht.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_19licht.setText("")
        self.label_19licht.setObjectName("label_19licht")
        self.licht_effect(self.label_19licht, x_offset=0, y_offset=-6, blur_radius=50)

        self.label_19links = QtWidgets.QLabel(self.centralwidget)
        self.label_19links.setGeometry(QtCore.QRect(592, 314, 116, 40))
        self.label_19links.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_19links.setText("")
        self.label_19links.setObjectName("label_19links")
        self.add_shadow_effect(self.label_19links, x_offset=-9, y_offset=0, blur_radius=50)

        self.label_19Rechts = QtWidgets.QLabel(self.centralwidget)
        self.label_19Rechts.setGeometry(QtCore.QRect(592, 314, 116, 40))
        self.label_19Rechts.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_19Rechts.setText("")
        self.label_19Rechts.setObjectName("label_19Rechts")
        self.add_shadow_effect(self.label_19Rechts, x_offset=10, y_offset=0, blur_radius=50)

        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(592, 312, 116, 40))
        self.label_19.setStyleSheet("background-color: rgb(10, 20, 20);")
        self.label_19.setFrameShape(QtWidgets.QFrame.Box)
        self.label_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_19.setLineWidth(1)
        self.label_19.setMidLineWidth(1)
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.add_shadow_effect(self.label_19, x_offset=0, y_offset=10, blur_radius=50)
        self.apply_3d_borders(self.label_19)

        self.label_20licht = QtWidgets.QLabel(self.centralwidget)
        self.label_20licht.setGeometry(QtCore.QRect(595, 392, 110, 20))
        self.label_20licht.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_20licht.setText("")
        self.label_20licht.setObjectName("label_20licht")
        self.licht_effect(self.label_20licht, x_offset=0, y_offset=-6, blur_radius=50)

        self.label_20links = QtWidgets.QLabel(self.centralwidget)
        self.label_20links.setGeometry(QtCore.QRect(592, 392, 116, 40))
        self.label_20links.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_20links.setText("")
        self.label_20links.setObjectName("label_20inks")
        self.add_shadow_effect(self.label_20links, x_offset=-9, y_offset=0, blur_radius=50)

        self.label_20Rechts = QtWidgets.QLabel(self.centralwidget)
        self.label_20Rechts.setGeometry(QtCore.QRect(592, 392, 116, 40))
        self.label_20Rechts.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_20Rechts.setText("")
        self.label_20Rechts.setObjectName("label_20Rechts")
        self.add_shadow_effect(self.label_20Rechts, x_offset=10, y_offset=0, blur_radius=50)

        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(592, 390, 116, 40))
        self.label_20.setStyleSheet("background-color: rgb(10, 20, 20);")
        self.label_20.setFrameShape(QtWidgets.QFrame.Box)
        self.label_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_20.setLineWidth(1)
        self.label_20.setMidLineWidth(1)
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.add_shadow_effect(self.label_20, x_offset=0, y_offset=10, blur_radius=50)
        self.apply_3d_borders(self.label_20)

        self.label_21licht = QtWidgets.QLabel(self.centralwidget)
        self.label_21licht.setGeometry(QtCore.QRect(185, 158, 110, 20))
        self.label_21licht.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_21licht.setText("")
        self.label_21licht.setObjectName("label_21licht")
        self.licht_effect(self.label_21licht, x_offset=0, y_offset=-6, blur_radius=50)

        self.label_21links = QtWidgets.QLabel(self.centralwidget)
        self.label_21links.setGeometry(QtCore.QRect(182, 158, 116, 40))
        self.label_21links.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_21links.setText("")
        self.label_21links.setObjectName("label_21inks")
        self.add_shadow_effect(self.label_21links, x_offset=-9, y_offset=0, blur_radius=50)

        self.label_21Rechts = QtWidgets.QLabel(self.centralwidget)
        self.label_21Rechts.setGeometry(QtCore.QRect(182, 158, 116, 40))
        self.label_21Rechts.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_21Rechts.setText("")
        self.label_21Rechts.setObjectName("label_21Rechts")
        self.add_shadow_effect(self.label_21Rechts, x_offset=10, y_offset=0, blur_radius=50)

        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(182, 156, 116, 40))
        self.label_21.setStyleSheet("background-color: rgb(10, 20, 20);")
        self.label_21.setFrameShape(QtWidgets.QFrame.Box)
        self.label_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_21.setLineWidth(1)
        self.label_21.setMidLineWidth(1)
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.add_shadow_effect(self.label_21, x_offset=0, y_offset=10, blur_radius=50)
        self.apply_3d_borders(self.label_21)

        self.label_22licht = QtWidgets.QLabel(self.centralwidget)
        self.label_22licht.setGeometry(QtCore.QRect(185, 236, 110, 20))
        self.label_22licht.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_22licht.setText("")
        self.label_22licht.setObjectName("label_22licht")
        self.licht_effect(self.label_22licht, x_offset=0, y_offset=-6, blur_radius=50)

        self.label_22links = QtWidgets.QLabel(self.centralwidget)
        self.label_22links.setGeometry(QtCore.QRect(182, 236, 116, 40))
        self.label_22links.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_22links.setText("")
        self.label_22links.setObjectName("label_22inks")
        self.add_shadow_effect(self.label_22links, x_offset=-9, y_offset=0, blur_radius=50)

        self.label_22Rechts = QtWidgets.QLabel(self.centralwidget)
        self.label_22Rechts.setGeometry(QtCore.QRect(182, 236, 116, 40))
        self.label_22Rechts.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_22Rechts.setText("")
        self.label_22Rechts.setObjectName("label_22Rechts")
        self.add_shadow_effect(self.label_22Rechts, x_offset=10, y_offset=0, blur_radius=50)

        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(182, 234, 116, 40))
        self.label_22.setStyleSheet("background-color: rgb(10, 20, 20);")
        self.label_22.setFrameShape(QtWidgets.QFrame.Box)
        self.label_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_22.setLineWidth(1)
        self.label_22.setMidLineWidth(1)
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.add_shadow_effect(self.label_22, x_offset=0, y_offset=10, blur_radius=50)
        self.apply_3d_borders(self.label_22)

        self.label_23licht = QtWidgets.QLabel(self.centralwidget)
        self.label_23licht.setGeometry(QtCore.QRect(185, 314, 110, 20))
        self.label_23licht.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_23licht.setText("")
        self.label_23licht.setObjectName("label_23licht")
        self.licht_effect(self.label_23licht, x_offset=0, y_offset=-6, blur_radius=50)

        self.label_23links = QtWidgets.QLabel(self.centralwidget)
        self.label_23links.setGeometry(QtCore.QRect(182, 314, 116, 40))
        self.label_23links.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_23links.setText("")
        self.label_23links.setObjectName("label_23inks")
        self.add_shadow_effect(self.label_23links, x_offset=-9, y_offset=0, blur_radius=50)

        self.label_23Rechts = QtWidgets.QLabel(self.centralwidget)
        self.label_23Rechts.setGeometry(QtCore.QRect(182, 314, 116, 40))
        self.label_23Rechts.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_23Rechts.setText("")
        self.label_23Rechts.setObjectName("label_23Rechts")
        self.add_shadow_effect(self.label_23Rechts, x_offset=10, y_offset=0, blur_radius=50)

        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(182, 312, 116, 40))
        self.label_23.setStyleSheet("background-color: rgb(10, 20, 20);")
        self.label_23.setFrameShape(QtWidgets.QFrame.Box)
        self.label_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_23.setLineWidth(1)
        self.label_23.setMidLineWidth(1)
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.add_shadow_effect(self.label_23, x_offset=0, y_offset=10, blur_radius=50)
        self.apply_3d_borders(self.label_23)

        self.label_24licht = QtWidgets.QLabel(self.centralwidget)
        self.label_24licht.setGeometry(QtCore.QRect(185, 392, 110, 20))
        self.label_24licht.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_24licht.setText("")
        self.label_24licht.setObjectName("label_24licht")
        self.licht_effect(self.label_24licht, x_offset=0, y_offset=-6, blur_radius=50)

        self.label_24links = QtWidgets.QLabel(self.centralwidget)
        self.label_24links.setGeometry(QtCore.QRect(182, 392, 116, 40))
        self.label_24links.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_24links.setText("")
        self.label_24links.setObjectName("label_24inks")
        self.add_shadow_effect(self.label_24links, x_offset=-9, y_offset=0, blur_radius=50)

        self.label_24Rechts = QtWidgets.QLabel(self.centralwidget)
        self.label_24Rechts.setGeometry(QtCore.QRect(182, 392, 116, 40))
        self.label_24Rechts.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_24Rechts.setText("")
        self.label_24Rechts.setObjectName("label_24Rechts")
        self.add_shadow_effect(self.label_24Rechts, x_offset=10, y_offset=0, blur_radius=50)

        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(182, 390, 116, 40))
        self.label_24.setStyleSheet("background-color: rgb(10, 20, 20);")
        self.label_24.setFrameShape(QtWidgets.QFrame.Box)
        self.label_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_24.setLineWidth(1)
        self.label_24.setMidLineWidth(1)
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.add_shadow_effect(self.label_24, x_offset=0, y_offset=10, blur_radius=50)
        self.apply_3d_borders(self.label_24)

        self.label_bild = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_bild.setGeometry(QtCore.QRect(891, 60, 452, 545))
        self.label_bild.setAutoFillBackground(False)
        self.label_bild.setStyleSheet("background-color: rgba(10, 22, 15, 10); border-color: rgb(10, 22, 15);")
        pixmap = QPixmap(resource_path("/Users/dmitriykravchenko/Documents/Programirovanie/Tennis/images/IMG_1.png"))
        self.label_bild.setPixmap(pixmap)
        self.label_bild.setText("")
        self.label_bild.setObjectName("label_bild")
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_22.raise_()
        self.label_21.raise_()
        self.label_20.raise_()
        self.label_19.raise_()
        self.label_18.raise_()
        self.label_17.raise_()
        self.label_16.raise_()
        self.label_15.raise_()
        self.label_14.raise_()
        self.game_Winner.raise_()
        self.label.raise_()
        self.p1_1.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.name_1.raise_()
        self.name_2.raise_()
        self.label_4.raise_()
        self.p1_2.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.p2_2.raise_()
        self.p2_1.raise_()
        self.p3_2.raise_()
        self.p3_1.raise_()
        self.pushBut_Game.raise_()
        self.label_11.raise_()
        self.final_Storie.raise_()
        self.pushBut_Reset.raise_()
        self.pushBut_Close.raise_()
        self.label_10.raise_()
        self.p4_2.raise_()
        self.p4_1.raise_()
        self.label_12.raise_()
        self.history_label.raise_()
        self.lWidget_history_game.raise_()
        self.label_bild.raise_()
        tennis.setCentralWidget(self.centralwidget)

        self.retranslateUi(tennis)
        QtCore.QMetaObject.connectSlotsByName(tennis)
        self.pushBut_Game.clicked.connect(self.my_function_tennis)
        self.pushBut_Game.pressed.connect(self.game_press)
        self.pushBut_Game.released.connect(self.game_release)
        self.pushBut_Reset.clicked.connect(self.func_reset)
        self.pushBut_Reset.pressed.connect(self.reset_press)
        self.pushBut_Reset.released.connect(self.reset_release)
        self.pushBut_Close.clicked.connect(self.func_close)
        self.pushBut_Close.pressed.connect(self.close_press)
        self.pushBut_Close.released.connect(self.close_release)

        tennis.mousePressEvent = self.mousePressEvent 
        tennis.mouseMoveEvent = self.mouseMoveEvent 

    def retranslateUi(self, tennis):
        _translate = QtCore.QCoreApplication.translate
        tennis.setWindowTitle(_translate("tennis", "Tennis simulator"))
        self.label.setText(_translate("tennis", "GRAND CUP TENNIS SIMULATOR"))
        self.pushBut_Game.setText(_translate("tennis", ""))
        self.pushBut_Reset.setText(_translate("tennis", ""))
        self.pushBut_Close.setText(_translate("tennis", ""))
        self.label.setText(_translate("tennis",
                                      "  GRAND CUP TENNIS SIMULATOR"))
        self.label_2.setText(_translate("tennis", "Enter the name of the first player:"))
        self.label_3.setText(_translate("tennis", "Enter the second player's name:"))
        self.label_4.setText(_translate("tennis", "Enter first serve pass percentage:"))
        self.label_5.setText(_translate("tennis", "Enter first serve pass percentage:"))
        self.label_6.setText(_translate("tennis", "Enter first serve win percentage:"))
        self.label_7.setText(_translate("tennis", "Enter first serve win percentage:"))
        self.label_8.setText(_translate("tennis", "Enter second serve pass percentage:"))
        self.label_9.setText(_translate("tennis", "Enter second serve pass percentage:"))
        self.game_Winner.setText(_translate("tennis", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushBut_Game.setText(_translate("tennis", ""))
        self.label_11.setText(_translate("tennis", "RESULT :"))
        self.final_Storie.setText(
            _translate("tennis", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushBut_Reset.setText(_translate("tennis", ""))
        self.pushBut_Close.setText(_translate("tennis", ""))
        self.label_10.setText(_translate("tennis", "Enter first serve win percentage"))
        self.label_12.setText(_translate("tennis", "Enter first serve win percentage:"))

    def add_shadow_effect(self, widget, *, x_offset=0, y_offset=0, blur_radius=10):
        shadow = QtWidgets.QGraphicsDropShadowEffect(widget)
        color = QtGui.QColor(0, 0, 0, 140)
        shadow.setColor(color)
        shadow.setOffset(x_offset, y_offset)
        shadow.setBlurRadius(blur_radius)
        widget.setGraphicsEffect(shadow)

    def licht_effect(self, widget, *, x_offset=0, y_offset=0, blur_radius=10):
        licht = QtWidgets.QGraphicsDropShadowEffect(widget)
        color = QtGui.QColor(255, 255, 255, 90)
        licht.setColor(color)
        licht.setOffset(abs(x_offset), (y_offset))
        licht.setBlurRadius(blur_radius)
        widget.setGraphicsEffect(licht)

    def apply_3d_borders(self, widget):
        original_paint_event = widget.paintEvent

        def paint_with_borders(event):
            original_paint_event(event)

            painter = QPainter(widget)

            painter.setPen(QColor(120, 150, 150))
            painter.drawLine(0, 0, widget.width(), 0) 

        widget.paintEvent = paint_with_borders

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.globalPos() - self.tennis.pos() 

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.tennis.move(event.globalPos() - self.offset)
            event.accept()

    def game_press(self):
        self.pushBut_Game.setStyleSheet("""
        border-radius: 17px;
        background-color: rgba(0, 0, 0, 20);
        """)
        self.pushBut_Game.setIconSize(QtCore.QSize(400, 95))
        self.pushBut_Game.setGeometry(QtCore.QRect(207, 597, 110, 45))

    def game_release(self):
        self.pushBut_Game.setStyleSheet("""
                border-radius: 25px;
                background-color: none;
                """)
        self.pushBut_Game.setIconSize(QtCore.QSize(440, 105))
        self.pushBut_Game.setGeometry(QtCore.QRect(205, 595, 115, 50))

    def reset_press(self):
        self.pushBut_Reset.setStyleSheet("""
                border-radius: 17px;
                background-color: rgba(0, 0, 0, 20);
                """)
        self.pushBut_Reset.setIconSize(QtCore.QSize(400, 95))
        self.pushBut_Reset.setGeometry(QtCore.QRect(399, 597, 110, 45))

    def reset_release(self):
        self.pushBut_Reset.setStyleSheet("""
                        border-radius: 25px;
                        background-color: none;
                        """)
        self.pushBut_Reset.setIconSize(QtCore.QSize(440, 105))
        self.pushBut_Reset.setGeometry(QtCore.QRect(397, 595, 115, 50))

    def close_press(self):
        self.pushBut_Close.setStyleSheet("""
        border-radius: 17px;
        background-color: rgba(0, 0, 0, 20);
        """)
        self.pushBut_Close.setIconSize(QtCore.QSize(400, 95))
        self.pushBut_Close.setGeometry(QtCore.QRect(580, 597, 110, 45))

    def close_release(self):
        self.pushBut_Close.setStyleSheet("""
                border-radius: 25px;
                background-color: none;
                """)
        self.pushBut_Close.setIconSize(QtCore.QSize(440, 105))
        self.pushBut_Close.setGeometry(QtCore.QRect(578, 595, 115, 50))

    def my_function_tennis(self):
        name_1 = self.name_1.text()
        name_2 = self.name_2.text()
        p1_1 = self.p1_1.value()
        p1_2 = self.p1_2.value()
        p2_1 = self.p2_1.value()
        p2_2 = self.p2_2.value()
        p3_1 = self.p3_1.value()
        p3_2 = self.p3_2.value()
        p4_1 = self.p4_1.value()
        p4_2 = self.p4_2.value()

        self.label_bild.setVisible(False)

        if not name_1.strip():
            QMessageBox.information(
                self.centralwidget,
                "Empty name",
                "Please fill in the first player's name.",
            )
            self.name_1.setFocus()
            return

        if not name_2.strip():
            QMessageBox.information(
                self.centralwidget,
                "Empty name",
                "Please fill in the second player's name.",
            )
            self.name_2.setFocus()
            return

        if (p1_1 == 0 or p1_2 == 0 or p2_1 == 0 or
                p2_2 == 0 or p3_1 == 0 or p3_2 == 0 or
                p4_1 == 0 or p4_2 == 0 or
                not name_1.strip() or not name_2.strip()):
            QMessageBox.warning(
                self.centralwidget,
                "Input error",
                "Make sure all fields are filled in and not null!"
            )
            return
        result = {}

        def add_history_widget(text):
            font = QtGui.QFont()
            font.setPointSize(20)
            self.lWidget_history_game.setFont(font)
            item = QtWidgets.QListWidgetItem(text)
            item.setData(QtCore.Qt.TextAlignmentRole, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.lWidget_history_game.addItem(item)

        result, res = play_full_game(name_1, name_2, p1_1, p2_1, p3_1, p4_1, p1_2, p2_2, p3_2, p4_2, add_history_widget)
        if len(res) == 6 and (res[0] + res[2] + res[4]) > (res[1] + res[3] + res[5]):
            self.game_Winner.setText(' ' + 'Game' + '   ' + self.name_1.text())
            self.final_Storie.setText(
                ' ' + 'Final score:  ' + '     ' + str(res[0]) + '-' + str(res[1]) + '   ' + str(res[2]) + '-' + str(
                    res[3]) + '   ' +
                str(res[4]) + '-' + str(res[5]))
            res = []
        elif len(res) == 8 and (res[0] + res[2] + res[4] + res[6]) > (res[1] + res[3] + res[5] + res[7]):
            self.game_Winner.setText(' ' + 'Game' + '   ' + self.name_1.text())
            self.final_Storie.setText(
                ' ' + 'Final score: ' + '     ' + str(res[0]) + '-' + str(res[1]) + '   ' + str(res[2]) + '-' + str(
                    res[3]) + '   ' +
                str(res[4]) + '-' + str(res[5]) + '   ' + str(res[6]) + '-' + str(res[7]))
            res = []
        elif len(res) == 10 and (res[0] + res[2] + res[4] + res[6] + res[8]) > (
                res[1] + res[3] + res[5] + res[7] + res[9]):
            self.game_Winner.setText(' ' + 'Game' + '   ' + self.name_1.text())
            self.final_Storie.setText(
                ' ' + 'Final score:' + '     ' + str(res[0]) + '-' + str(res[1]) + '   ' + str(res[2]) + '-' + str(
                    res[3]) + '   ' +
                str(res[4]) + '-' + str(res[5]) + '   ' + str(res[6]) + '-' + str(res[7]) + '   ' + str(
                    res[8]) + '-' + str(
                    res[9]))
            res = []
        elif len(res) == 6 and (res[0] + res[2] + res[4]) < (res[1] + res[3] + res[5]):
            self.game_Winner.setText(' ' + 'Game' + '   ' + self.name_2.text())
            self.final_Storie.setText(
                ' ' + 'Final score:' + '     ' + str(res[1]) + '-' + str(res[0]) + '   ' + str(res[3]) + '-' + str(
                    res[2]) + '   ' +
                str(res[5]) + '-' + str(res[4]))
            res = []
        elif len(res) == 8 and (res[0] + res[2] + res[4] + res[6]) < (res[1] + res[3] + res[5] + res[7]):
            self.game_Winner.setText(' ' + 'Game' + '   ' + self.name_2.text())
            self.final_Storie.setText(
                ' ' + 'Final score:' + '     ' + str(res[1]) + '-' + str(res[0]) + '   ' + str(res[3]) + '-' + str(
                    res[2]) + '   ' +
                str(res[5]) + '-' + str(res[4]) + '   ' + str(res[7]) + '-' + str(res[6]))
            res = []
        elif len(res) == 10 and (res[0] + res[2] + res[4] + res[6] + res[8]) < (
                res[1] + res[3] + res[5] + res[7] + res[9]):
            self.game_Winner.setText(' ' + 'Game' + '   ' + self.name_2.text())
            self.final_Storie.setText(
                ' ' + 'Final score: ' + '     ' + str(res[1]) + '-' + str(res[0]) + '   ' + str(res[3]) + '-' + str(
                    res[2]) + '   ' +
                str(res[5]) + '-' + str(res[4]) + '   ' + str(res[7]) + '-' + str(res[6]) + '   ' + str(
                    res[9]) + '-' + str(res[8]))
            res = []

    def func_close(self):
        self.tennis.close()

    def func_reset(self):
        self.name_1.clear()
        self.name_2.clear()
        self.p1_1.setValue(0)
        self.p1_2.setValue(0)
        self.p2_1.setValue(0)
        self.p2_2.setValue(0)
        self.p3_1.setValue(0)
        self.p3_2.setValue(0)
        self.p4_1.setValue(0)
        self.p4_2.setValue(0)
        self.game_Winner.setText('')
        self.final_Storie.setText('')
        self.lWidget_history_game.clear()
        self.label_bild.setVisible(True)


def main():
    app = QtWidgets.QApplication(sys.argv)
    tennis = QtWidgets.QMainWindow()
    ui = Ui_tennis()
    ui.setupUi(tennis)
    tennis.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
