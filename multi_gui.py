from dissolve import *
from Dither_threshold import *
from operations import *
from channels_manipulations import *
from alpha_channel import *
from HuffmanCode import *
import run_length as run
import LZW as lzw
from shannon import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QFileDialog
from output import Ui_Dialog
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        self.dialog = QDialog()
        self.dialog.ui = Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)

        Form.setObjectName("Form")
        Form.resize(630, 260)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/Python Projects/Multimedia_Tasks/test_images/icone.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QToolTip\n"
                           "{\n"
                           "     border: 1px solid black;\n"
                           "     background-color: #ffa02f;\n"
                           "     padding: 1px;\n"
                           "     border-radius: 3px;\n"
                           "     opacity: 100;\n"
                           "}\n"
                           "\n"
                           "QWidget\n"
                           "{\n"
                           "    color: #b1b1b1;\n"
                           "    background-color: #323232;\n"
                           "}\n"
                           "\n"
                           "QWidget:item:hover\n"
                           "{\n"
                           "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
                           "    color: #000000;\n"
                           "}\n"
                           "\n"
                           "QWidget:item:selected\n"
                           "{\n"
                           "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                           "}\n"
                           "\n"
                           "QMenuBar::item\n"
                           "{\n"
                           "    background: transparent;\n"
                           "}\n"
                           "\n"
                           "QMenuBar::item:selected\n"
                           "{\n"
                           "    background: transparent;\n"
                           "    border: 1px solid #ffaa00;\n"
                           "}\n"
                           "\n"
                           "QMenuBar::item:pressed\n"
                           "{\n"
                           "    background: #444;\n"
                           "    border: 1px solid #000;\n"
                           "    background-color: QLinearGradient(\n"
                           "        x1:0, y1:0,\n"
                           "        x2:0, y2:1,\n"
                           "        stop:1 #212121,\n"
                           "        stop:0.4 #343434/*,\n"
                           "        stop:0.2 #343434,\n"
                           "        stop:0.1 #ffaa00*/\n"
                           "    );\n"
                           "    margin-bottom:-1px;\n"
                           "    padding-bottom:1px;\n"
                           "}\n"
                           "\n"
                           "QMenu\n"
                           "{\n"
                           "    border: 1px solid #000;\n"
                           "}\n"
                           "\n"
                           "QMenu::item\n"
                           "{\n"
                           "    padding: 2px 20px 2px 20px;\n"
                           "}\n"
                           "\n"
                           "QMenu::item:selected\n"
                           "{\n"
                           "    color: #000000;\n"
                           "}\n"
                           "\n"
                           "QWidget:disabled\n"
                           "{\n"
                           "    color: #404040;\n"
                           "    background-color: #323232;\n"
                           "}\n"
                           "\n"
                           "QAbstractItemView\n"
                           "{\n"
                           "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
                           "}\n"
                           "\n"
                           "QWidget:focus\n"
                           "{\n"
                           "    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
                           "}\n"
                           "\n"
                           "QLineEdit\n"
                           "{\n"
                           "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
                           "    padding: 1px;\n"
                           "    border-style: solid;\n"
                           "    border: 1px solid #1e1e1e;\n"
                           "    border-radius: 5;\n"
                           "}\n"
                           "\n"
                           "QPushButton\n"
                           "{\n"
                           "    color: #b1b1b1;\n"
                           "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
                           "    border-width: 1px;\n"
                           "    border-color: #1e1e1e;\n"
                           "    border-style: solid;\n"
                           "    border-radius: 6;\n"
                           "    padding: 3px;\n"
                           "    font-size: 12px;\n"
                           "    padding-left: 5px;\n"
                           "    padding-right: 5px;\n"
                           "}\n"
                           "\n"
                           "QPushButton:pressed\n"
                           "{\n"
                           "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
                           "}\n"
                           "\n"
                           "QComboBox\n"
                           "{\n"
                           "    selection-background-color: #ffaa00;\n"
                           "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
                           "    border-style: solid;\n"
                           "    border: 1px solid #1e1e1e;\n"
                           "    border-radius: 5;\n"
                           "}\n"
                           "\n"
                           "QComboBox:hover,QPushButton:hover\n"
                           "{\n"
                           "    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                           "}\n"
                           "\n"
                           "\n"
                           "QComboBox:on\n"
                           "{\n"
                           "    padding-top: 3px;\n"
                           "    padding-left: 4px;\n"
                           "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
                           "    selection-background-color: #ffaa00;\n"
                           "}\n"
                           "\n"
                           "QComboBox QAbstractItemView\n"
                           "{\n"
                           "    border: 2px solid darkgray;\n"
                           "    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                           "}\n"
                           "\n"
                           "QComboBox::drop-down\n"
                           "{\n"
                           "     subcontrol-origin: padding;\n"
                           "     subcontrol-position: top right;\n"
                           "     width: 15px;\n"
                           "\n"
                           "     border-left-width: 0px;\n"
                           "     border-left-color: darkgray;\n"
                           "     border-left-style: solid; /* just a single line */\n"
                           "     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                           "     border-bottom-right-radius: 3px;\n"
                           " }\n"
                           "\n"
                           "QComboBox::down-arrow\n"
                           "{\n"
                           "     image: url(:/down_arrow.png);\n"
                           "}\n"
                           "\n"
                           "QGroupBox:focus\n"
                           "{\n"
                           "border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                           "}\n"
                           "\n"
                           "QTextEdit:focus\n"
                           "{\n"
                           "    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                           "}\n"
                           "\n"
                           "QScrollBar:horizontal {\n"
                           "     border: 1px solid #222222;\n"
                           "     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
                           "     height: 7px;\n"
                           "     margin: 0px 16px 0 16px;\n"
                           "}\n"
                           "\n"
                           "QScrollBar::handle:horizontal\n"
                           "{\n"
                           "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
                           "      min-height: 20px;\n"
                           "      border-radius: 2px;\n"
                           "}\n"
                           "\n"
                           "QScrollBar::add-line:horizontal {\n"
                           "      border: 1px solid #1b1b19;\n"
                           "      border-radius: 2px;\n"
                           "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                           "      width: 14px;\n"
                           "      subcontrol-position: right;\n"
                           "      subcontrol-origin: margin;\n"
                           "}\n"
                           "\n"
                           "QScrollBar::sub-line:horizontal {\n"
                           "      border: 1px solid #1b1b19;\n"
                           "      border-radius: 2px;\n"
                           "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                           "      width: 14px;\n"
                           "     subcontrol-position: left;\n"
                           "     subcontrol-origin: margin;\n"
                           "}\n"
                           "\n"
                           "QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
                           "{\n"
                           "      border: 1px solid black;\n"
                           "      width: 1px;\n"
                           "      height: 1px;\n"
                           "      background: white;\n"
                           "}\n"
                           "\n"
                           "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
                           "{\n"
                           "      background: none;\n"
                           "}\n"
                           "\n"
                           "QScrollBar:vertical\n"
                           "{\n"
                           "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
                           "      width: 7px;\n"
                           "      margin: 16px 0 16px 0;\n"
                           "      border: 1px solid #222222;\n"
                           "}\n"
                           "\n"
                           "QScrollBar::handle:vertical\n"
                           "{\n"
                           "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
                           "      min-height: 20px;\n"
                           "      border-radius: 2px;\n"
                           "}\n"
                           "\n"
                           "QScrollBar::add-line:vertical\n"
                           "{\n"
                           "      border: 1px solid #1b1b19;\n"
                           "      border-radius: 2px;\n"
                           "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                           "      height: 14px;\n"
                           "      subcontrol-position: bottom;\n"
                           "      subcontrol-origin: margin;\n"
                           "}\n"
                           "\n"
                           "QScrollBar::sub-line:vertical\n"
                           "{\n"
                           "      border: 1px solid #1b1b19;\n"
                           "      border-radius: 2px;\n"
                           "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
                           "      height: 14px;\n"
                           "      subcontrol-position: top;\n"
                           "      subcontrol-origin: margin;\n"
                           "}\n"
                           "\n"
                           "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
                           "{\n"
                           "      border: 1px solid black;\n"
                           "      width: 1px;\n"
                           "      height: 1px;\n"
                           "      background: white;\n"
                           "}\n"
                           "\n"
                           "\n"
                           "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
                           "{\n"
                           "      background: none;\n"
                           "}\n"
                           "\n"
                           "QTextEdit\n"
                           "{\n"
                           "    background-color: #242424;\n"
                           "}\n"
                           "\n"
                           "QPlainTextEdit\n"
                           "{\n"
                           "    background-color: #242424;\n"
                           "}\n"
                           "\n"
                           "QHeaderView::section\n"
                           "{\n"
                           "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
                           "    color: white;\n"
                           "    padding-left: 4px;\n"
                           "    border: 1px solid #6c6c6c;\n"
                           "}\n"
                           "\n"
                           "QCheckBox:disabled\n"
                           "{\n"
                           "color: #414141;\n"
                           "}\n"
                           "\n"
                           "QDockWidget::title\n"
                           "{\n"
                           "    text-align: center;\n"
                           "    spacing: 3px; /* spacing between items in the tool bar */\n"
                           "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
                           "}\n"
                           "\n"
                           "QDockWidget::close-button, QDockWidget::float-button\n"
                           "{\n"
                           "    text-align: center;\n"
                           "    spacing: 1px; /* spacing between items in the tool bar */\n"
                           "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
                           "}\n"
                           "\n"
                           "QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
                           "{\n"
                           "    background: #242424;\n"
                           "}\n"
                           "\n"
                           "QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
                           "{\n"
                           "    padding: 1px -1px -1px 1px;\n"
                           "}\n"
                           "\n"
                           "QMainWindow::separator\n"
                           "{\n"
                           "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
                           "    color: white;\n"
                           "    padding-left: 4px;\n"
                           "    border: 1px solid #4c4c4c;\n"
                           "    spacing: 3px; /* spacing between items in the tool bar */\n"
                           "}\n"
                           "\n"
                           "QMainWindow::separator:hover\n"
                           "{\n"
                           "\n"
                           "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
                           "    color: white;\n"
                           "    padding-left: 4px;\n"
                           "    border: 1px solid #6c6c6c;\n"
                           "    spacing: 3px; /* spacing between items in the tool bar */\n"
                           "}\n"
                           "\n"
                           "QToolBar::handle\n"
                           "{\n"
                           "     spacing: 3px; /* spacing between items in the tool bar */\n"
                           "     background: url(:/images/handle.png);\n"
                           "}\n"
                           "\n"
                           "QMenu::separator\n"
                           "{\n"
                           "    height: 2px;\n"
                           "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
                           "    color: white;\n"
                           "    padding-left: 4px;\n"
                           "    margin-left: 10px;\n"
                           "    margin-right: 5px;\n"
                           "}\n"
                           "\n"
                           "QProgressBar\n"
                           "{\n"
                           "    border: 2px solid grey;\n"
                           "    border-radius: 5px;\n"
                           "    text-align: center;\n"
                           "}\n"
                           "\n"
                           "QProgressBar::chunk\n"
                           "{\n"
                           "    background-color: #d7801a;\n"
                           "    width: 2.15px;\n"
                           "    margin: 0.5px;\n"
                           "}\n"
                           "\n"
                           "QTabBar::tab {\n"
                           "    color: #b1b1b1;\n"
                           "    border: 1px solid #444;\n"
                           "    border-bottom-style: none;\n"
                           "    background-color: #323232;\n"
                           "    padding-left: 10px;\n"
                           "    padding-right: 10px;\n"
                           "    padding-top: 3px;\n"
                           "    padding-bottom: 2px;\n"
                           "    margin-right: -1px;\n"
                           "}\n"
                           "\n"
                           "QTabWidget::pane {\n"
                           "    border: 1px solid #444;\n"
                           "    top: 1px;\n"
                           "}\n"
                           "\n"
                           "QTabBar::tab:last\n"
                           "{\n"
                           "    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
                           "    border-top-right-radius: 3px;\n"
                           "}\n"
                           "\n"
                           "QTabBar::tab:first:!selected\n"
                           "{\n"
                           " margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
                           "\n"
                           "\n"
                           "    border-top-left-radius: 3px;\n"
                           "}\n"
                           "\n"
                           "QTabBar::tab:!selected\n"
                           "{\n"
                           "    color: #b1b1b1;\n"
                           "    border-bottom-style: solid;\n"
                           "    margin-top: 3px;\n"
                           "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
                           "}\n"
                           "\n"
                           "QTabBar::tab:selected\n"
                           "{\n"
                           "    border-top-left-radius: 3px;\n"
                           "    border-top-right-radius: 3px;\n"
                           "    margin-bottom: 0px;\n"
                           "}\n"
                           "\n"
                           "QTabBar::tab:!selected:hover\n"
                           "{\n"
                           "    /*border-top: 2px solid #ffaa00;\n"
                           "    padding-bottom: 3px;*/\n"
                           "    border-top-left-radius: 3px;\n"
                           "    border-top-right-radius: 3px;\n"
                           "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
                           "}\n"
                           "\n"
                           "QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
                           "    color: #b1b1b1;\n"
                           "    background-color: #323232;\n"
                           "    border: 1px solid #b1b1b1;\n"
                           "    border-radius: 6px;\n"
                           "}\n"
                           "\n"
                           "QRadioButton::indicator:checked\n"
                           "{\n"
                           "    background-color: qradialgradient(\n"
                           "        cx: 0.5, cy: 0.5,\n"
                           "        fx: 0.5, fy: 0.5,\n"
                           "        radius: 1.0,\n"
                           "        stop: 0.25 #ffaa00,\n"
                           "        stop: 0.3 #323232\n"
                           "    );\n"
                           "}\n"
                           "\n"
                           "QCheckBox::indicator{\n"
                           "    color: #b1b1b1;\n"
                           "    background-color: #323232;\n"
                           "    border: 1px solid #b1b1b1;\n"
                           "    width: 9px;\n"
                           "    height: 9px;\n"
                           "}\n"
                           "\n"
                           "QRadioButton::indicator\n"
                           "{\n"
                           "    border-radius: 6px;\n"
                           "}\n"
                           "\n"
                           "QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
                           "{\n"
                           "    border: 1px solid #ffaa00;\n"
                           "}\n"
                           "\n"
                           "QCheckBox::indicator:checked\n"
                           "{\n"
                           "    image:url(:/images/checkbox.png);\n"
                           "}\n"
                           "\n"
                           "QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
                           "{\n"
                           "    border: 1px solid #444;\n"
                           "}")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 90, 611, 161))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.huff_btn = QtWidgets.QPushButton(self.tab)
        self.huff_btn.setGeometry(QtCore.QRect(40, 20, 111, 31))
        self.huff_btn.setObjectName("huff_btn")
        self.huff_btn.clicked.connect(self.huffman_code)
        self.runlength_btn = QtWidgets.QPushButton(self.tab)
        self.runlength_btn.setGeometry(QtCore.QRect(180, 20, 111, 31))
        self.runlength_btn.setObjectName("runlength_btn")
        self.runlength_btn.clicked.connect(self.run_length)
        self.shanon_btn = QtWidgets.QPushButton(self.tab)
        self.shanon_btn.setGeometry(QtCore.QRect(320, 20, 111, 31))
        self.shanon_btn.setObjectName("shanon_btn")
        self.shanon_btn.clicked.connect(self.shannon)

        self.arith_btn = QtWidgets.QPushButton(self.tab)
        self.arith_btn.setGeometry(QtCore.QRect(460, 20, 111, 31))
        self.arith_btn.setObjectName("arith_btn")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(40, 90, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:\"#ffaa00\"")
        self.label_6.setObjectName("label_6")
        self.lzw_btn = QtWidgets.QPushButton(self.tab)
        self.lzw_btn.setGeometry(QtCore.QRect(40, 60, 111, 31))
        self.lzw_btn.setObjectName("lzw_btn")
        self.lzw_btn.clicked.connect(self.lzw_code)

        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(210, 60, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:\"#ffaa00\"")
        self.label_10.setObjectName("label_10")
        self.alph_bet = QtWidgets.QTextEdit(self.tab)
        self.alph_bet.setGeometry(QtCore.QRect(420, 70, 181, 21))
        self.alph_bet.setObjectName("alph_bet")
        self.frequan = QtWidgets.QTextEdit(self.tab)
        self.frequan.setGeometry(QtCore.QRect(420, 100, 181, 21))
        self.frequan.setObjectName("frequan")

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.dither_btn = QtWidgets.QPushButton(self.tab_2)
        self.dither_btn.setGeometry(QtCore.QRect(40, 20, 111, 31))
        self.dither_btn.setObjectName("dither_btn")
        self.dither_btn.clicked.connect(self.dissolve_dither)
        self.cross_btn = QtWidgets.QPushButton(self.tab_2)
        self.cross_btn.setGeometry(QtCore.QRect(180, 20, 111, 31))
        self.cross_btn.setObjectName("cross_btn")
        self.cross_btn.clicked.connect(self.dissolve_cross)
        self.fadein_btn = QtWidgets.QPushButton(self.tab_2)
        self.fadein_btn.setGeometry(QtCore.QRect(320, 20, 111, 31))
        self.fadein_btn.setObjectName("fadein_btn")
        self.fadein_btn.clicked.connect(self.dissolve_fade_in)
        self.fadeout_btn = QtWidgets.QPushButton(self.tab_2)
        self.fadeout_btn.setGeometry(QtCore.QRect(460, 20, 111, 31))
        self.fadeout_btn.setObjectName("fadeout_btn")
        self.fadeout_btn.clicked.connect(self.dissolve_fade_out)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(40, 90, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:\"#ffaa00\"")
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.floyd_btn = QtWidgets.QPushButton(self.tab_3)
        self.floyd_btn.setGeometry(QtCore.QRect(40, 20, 111, 31))
        self.floyd_btn.setObjectName("floyd_btn")
        self.floyd_btn.clicked.connect(self.dither_floyed)
        self.order_btn = QtWidgets.QPushButton(self.tab_3)
        self.order_btn.setGeometry(QtCore.QRect(180, 20, 111, 31))
        self.order_btn.setObjectName("order_btn")
        self.order_btn.clicked.connect(self.dither_ordered)
        self.pattern_btn = QtWidgets.QPushButton(self.tab_3)
        self.pattern_btn.setGeometry(QtCore.QRect(320, 20, 111, 31))
        self.pattern_btn.setObjectName("pattern_btn")
        self.pattern_btn.clicked.connect(self.dither_pattern)
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(40, 90, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:\"#ffaa00\"")
        self.label_8.setObjectName("label_8")
        self.thr_btn = QtWidgets.QPushButton(self.tab_3)
        self.thr_btn.setGeometry(QtCore.QRect(460, 20, 111, 31))
        self.thr_btn.setObjectName("thr_btn")
        self.thr_btn.clicked.connect(self.dither_threshold)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.rotate_btn = QtWidgets.QPushButton(self.tab_4)
        self.rotate_btn.setGeometry(QtCore.QRect(40, 20, 111, 31))
        self.rotate_btn.setObjectName("rotate_btn")
        self.rotate_btn.clicked.connect(self.rotate_object)
        self.scale_btn = QtWidgets.QPushButton(self.tab_4)
        self.scale_btn.setGeometry(QtCore.QRect(180, 20, 111, 31))
        self.scale_btn.setObjectName("scale_btn")
        self.scale_btn.clicked.connect(self.scale_object)
        self.transl_btn = QtWidgets.QPushButton(self.tab_4)
        self.transl_btn.setGeometry(QtCore.QRect(320, 20, 111, 31))
        self.transl_btn.setObjectName("transl_btn")
        self.transl_btn.clicked.connect(self.translate_object)
        self.alpha_btn = QtWidgets.QPushButton(self.tab_4)
        self.alpha_btn.setGeometry(QtCore.QRect(460, 20, 91, 31))
        self.alpha_btn.setObjectName("alpha_btn")
        self.alpha_btn.clicked.connect(self.alpha_channel)
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(40, 90, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:\"#ffaa00\"")
        self.label_4.setObjectName("label_4")

        self.obj_value = QtWidgets.QSlider(self.tab_4)
        self.obj_value.setGeometry(QtCore.QRect(349, 60, 191, 22))
        self.obj_value.setStyleSheet("QSlider::groove:horizontal {\n"
                                     "border: 1px solid #bbb;\n"
                                     "background: white;\n"
                                     "height: 10px;\n"
                                     "border-radius: 4px;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::sub-page:horizontal {\n"
                                     "background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
                                     "    stop: 0 #66e, stop: 1 #bbf);\n"
                                     "background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
                                     "    stop: 0 #bbf, stop: 1 #55f);\n"
                                     "border: 1px solid #777;\n"
                                     "height: 10px;\n"
                                     "border-radius: 4px;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::add-page:horizontal {\n"
                                     "background: #fff;\n"
                                     "border: 1px solid #777;\n"
                                     "height: 10px;\n"
                                     "border-radius: 4px;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::handle:horizontal {\n"
                                     "background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                                     "    stop:0 #eee, stop:1 #ccc);\n"
                                     "border: 1px solid #777;\n"
                                     "width: 13px;\n"
                                     "margin-top: -2px;\n"
                                     "margin-bottom: -2px;\n"
                                     "border-radius: 4px;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::handle:horizontal:hover {\n"
                                     "background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                                     "    stop:0 #fff, stop:1 #ddd);\n"
                                     "border: 1px solid #444;\n"
                                     "border-radius: 4px;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::sub-page:horizontal:disabled {\n"
                                     "background: #bbb;\n"
                                     "border-color: #999;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::add-page:horizontal:disabled {\n"
                                     "background: #eee;\n"
                                     "border-color: #999;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::handle:horizontal:disabled {\n"
                                     "background: #eee;\n"
                                     "border: 1px solid #aaa;\n"
                                     "border-radius: 4px;\n"
                                     "}")
        self.obj_value.setOrientation(QtCore.Qt.Horizontal)
        self.obj_value.setObjectName("obj_value")
        self.obj_value.valueChanged.connect(self.value_changed)
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(40, 50, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:\"#ffaa00\"")
        self.label_9.setObjectName("label_9")
        self.value = QtWidgets.QLabel(self.tab_4)
        self.value.setGeometry(QtCore.QRect(410, 90, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.value.setFont(font)
        self.value.setStyleSheet("color:\"#ffaa00\"")
        self.value.setObjectName("value")

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.rgb2yuv_btn = QtWidgets.QPushButton(self.tab_5)
        self.rgb2yuv_btn.setGeometry(QtCore.QRect(40, 20, 111, 31))
        self.rgb2yuv_btn.setObjectName("rgb2yuv_btn")
        self.rgb2yuv_btn.clicked.connect(self.rgb2yuv)
        self.yuv2rgb_btn = QtWidgets.QPushButton(self.tab_5)
        self.yuv2rgb_btn.setGeometry(QtCore.QRect(180, 20, 111, 31))
        self.yuv2rgb_btn.setObjectName("yuv2rgb_btn")
        self.yuv2rgb_btn.clicked.connect(self.yuv2rgb)
        self.sampling_btn = QtWidgets.QPushButton(self.tab_5)
        self.sampling_btn.setGeometry(QtCore.QRect(320, 20, 111, 31))
        self.sampling_btn.setObjectName("sampling_btn")
        self.sampling_btn.clicked.connect(self.upsampling)
        self.label_7 = QtWidgets.QLabel(self.tab_5)
        self.label_7.setGeometry(QtCore.QRect(40, 90, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:\"#ffaa00\"")
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_5, "")
        self.wecome = QtWidgets.QLabel(Form)
        self.wecome.setGeometry(QtCore.QRect(20, 10, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wecome.setFont(font)
        self.wecome.setStyleSheet("color:\"#ffaa00\"")
        self.wecome.setObjectName("wecome")
        self.img_1 = QtWidgets.QPushButton(Form)
        self.img_1.setGeometry(QtCore.QRect(180, 50, 75, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("F:/Python Projects/Multimedia_Tasks/icons/main_icon.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.img_1.setIcon(icon1)
        self.img_1.setObjectName("img_1")
        self.img_1.clicked.connect(self.open_image1)

        self.img_2 = QtWidgets.QPushButton(Form)
        self.img_2.setGeometry(QtCore.QRect(470, 50, 75, 23))
        self.img_2.setIcon(icon1)
        self.img_2.clicked.connect(self.open_image2)

        self.img_2.setObjectName("img_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 45, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:\"#ffaa00\"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(290, 50, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:\"#ffaa00\"")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Images manipulation "))
        self.huff_btn.setText(_translate("Form", "Huffman code"))
        self.runlength_btn.setText(_translate("Form", "Run length"))
        self.shanon_btn.setText(_translate("Form", "Shanon fano"))
        self.arith_btn.setText(_translate("Form", "Arithmatic"))
        self.label_6.setText(_translate("Form", "Note : This task you don\'t need images at all "))
        self.lzw_btn.setText(_translate("Form", "lzw"))
        self.label_10.setText(_translate("Form", "Enter the text and the frequency :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", " Compretion "))
        self.dither_btn.setText(_translate("Form", "Dither dissolve"))
        self.cross_btn.setText(_translate("Form", "Cross dissolve"))
        self.fadein_btn.setText(_translate("Form", "Fade in"))
        self.fadeout_btn.setText(_translate("Form", "Fade out"))
        self.label_5.setText(
            _translate("Form", "Note : In fade in and fade out tasks you need one image and it\'s the first one "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", " Dissolve "))
        self.floyd_btn.setText(_translate("Form", "Floyd dithering"))
        self.order_btn.setText(_translate("Form", "Ordered dithering"))
        self.pattern_btn.setText(_translate("Form", "Pattern dithering"))
        self.label_8.setText(
            _translate("Form", "Note : In fade in and fade out tasks you need one image and it\'s the first one "))
        self.thr_btn.setText(_translate("Form", "Threshold"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", " Dithering "))
        self.rotate_btn.setText(_translate("Form", "Rotate"))
        self.scale_btn.setText(_translate("Form", "Scale"))
        self.transl_btn.setText(_translate("Form", "Translate"))
        self.alpha_btn.setText(_translate("Form", "Alpha Channel"))
        self.label_4.setText(_translate("Form", "Note : This task is perform on 2D shape not image "))
        self.label_9.setText(_translate("Form", "Use this slider to change object operation values :"))
        self.value.setText(_translate("Form", "Value = 0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", " Object operations "))
        self.rgb2yuv_btn.setText(_translate("Form", "RGB 2 YUV"))
        self.yuv2rgb_btn.setText(_translate("Form", "YUV 2 RGB"))
        self.sampling_btn.setText(_translate("Form", "Up sampling 4.2.2"))
        self.label_7.setText(
            _translate("Form", "Note : In fade in and fade out tasks you need one image and it\'s the first one "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "YUV2RGB and RGB2YUV"))
        self.wecome.setText(_translate("Form", "Choose your images and  the task you wish to preforme :"))
        self.img_1.setText(_translate("Form", "Browse"))
        self.img_2.setText(_translate("Form", "Browse"))
        self.label_2.setText(_translate("Form", "Choose your first image :"))
        self.label_3.setText(_translate("Form", "Choose your Second image :"))

    ''' open image used in the tasks'''

    def open_image1(self):
        self.image1 = QFileDialog.getOpenFileName(caption='Open the first image',
                                                  directory="F:/Python Projects/Multimedia_Tasks/test_images",
                                                  filter="Image files (*.jpg *.png)")[0]
        if self.image1:
            image_name = self.image1.split("/")
            self.label_2.setText("First image : " + image_name[-1])
        else:
            QMessageBox.critical(self.img_1, 'Error', "No image selected", QMessageBox.Ok)

    def open_image2(self):
        self.image2 = QFileDialog.getOpenFileName(caption='Open the second image',
                                                  directory="F:/Python Projects/Multimedia_Tasks/test_images",
                                                  filter="Image files (*.jpg *.png)")[0]
        if self.image2:
            image_name = self.image2.split("/")
            self.label_3.setText("Second image : " + image_name[-1])
        else:
            QMessageBox.critical(self.img_2, 'Error', "No image selected", QMessageBox.Ok)

    ''' ------- Dissolve tasks ------'''

    def dissolve_dither(self):
        try:
            if self.image1 and self.image2:

                image1 = np.array(Image.open(str(self.image1)).convert('L').resize((500, 500)))
                image2 = np.array(Image.open(str(self.image2)).convert('L').resize((500, 500)))
                dither_dissolve(image1, image2)
            else:
                QMessageBox.critical(self.dither_btn, 'Error', "Error please select two images", QMessageBox.Ok)

        except Exception:
            QMessageBox.critical(self.dither_btn, 'Error', "Error please select two images", QMessageBox.Ok)

    def dissolve_fade_in(self):
        try:
            if self.image1:
                fade_img = np.array(Image.open(str(self.image1)).convert('RGBA').resize((500, 500)))
                fade_in(fade_img)
            else:
                QMessageBox.critical(self.fadein_btn, 'Error', "Error please select a image", QMessageBox.Ok)

        except Exception:
            QMessageBox.critical(self.fadein_btn, 'Error', "Error please select a image", QMessageBox.Ok)

    def dissolve_fade_out(self):
        try:
            if self.image1:
                fade_img = np.array(Image.open(str(self.image1)).convert('RGBA').resize((500, 500)))
                fade_out(fade_img)
            else:
                QMessageBox.critical(self.fadeout_btn, 'Error', "Error please select a image", QMessageBox.Ok)

        except Exception:
            QMessageBox.critical(self.fadeout_btn, 'Error', "Error please select a image", QMessageBox.Ok)

    def dissolve_cross(self):
        try:
            if self.image1 and self.image2:
                image1 = np.array(Image.open(str(self.image1)).convert('L').resize((500, 500)))
                image2 = np.array(Image.open(str(self.image2)).convert('L').resize((500, 500)))
                cross_dissolve(image1, image2)
            else:
                QMessageBox.critical(self.cross_btn, 'Error', "Error please select two images", QMessageBox.Ok)
        except Exception:
            QMessageBox.critical(self.cross_btn, 'Error', "Error please select two images", QMessageBox.Ok)

    ''' ----- Dithering tasks ------'''

    def dither_floyed(self):
        try:
            if self.image1:
                img = np.array(Image.open(str(self.image1)).convert('L').resize((500, 500)))
                dither(img)
            else:
                QMessageBox.critical(self.floyd_btn, 'Error', "Error please select a image", QMessageBox.Ok)

        except Exception:
            QMessageBox.critical(self.floyd_btn, 'Error', "Error please select a image", QMessageBox.Ok)

    def dither_pattern(self):
        try:
            if self.image1:
                img = np.array(Image.open(str(self.image1)).convert('L').resize((500, 500)))
                dither_pattern(img)
            else:
                QMessageBox.critical(self.pattern_btn, 'Error', "Error please select a image", QMessageBox.Ok)

        except Exception:
            QMessageBox.critical(self.pattern_btn, 'Error', "Error please select a image", QMessageBox.Ok)

    def dither_ordered(self):
        try:
            if self.image1:
                img = np.array(Image.open(str(self.image1)).convert('L').resize((500, 500)))
                ordered_dithering(img)
            else:
                QMessageBox.critical(self.order_btn, 'Error', "Error please select a image", QMessageBox.Ok)

        except Exception:
            QMessageBox.critical(self.order_btn, 'Error', "Error please select a image", QMessageBox.Ok)

    def dither_threshold(self):
        try:
            if self.image1:
                img = np.array(Image.open(str(self.image1)).convert('L').resize((500, 500)))
                threshold(img)
            else:
                QMessageBox.critical(self.thr_btn, 'Error', "Error please select a image", QMessageBox.Ok)

        except Exception:
            QMessageBox.critical(self.thr_btn, 'Error', "Error please select a image", QMessageBox.Ok)

    def alpha_channel(self):
        try:
            if self.image1 and self.image2:
                foreground = np.array(Image.open(str(self.image1)).convert('RGBA').resize((150, 150)))
                background = np.array(Image.open(str(self.image2)).convert('RGBA').resize((150, 150)))

                alpha = foreground[:, :, 3]

                final = np.zeros(background.shape)
                for x in range(background.shape[0] - 1):
                    for y in range(background.shape[1] - 1):
                        final[x, y] = (foreground[x][y] * alpha[x][y]) + (background[x][y] * (255 - alpha[x][y]))

                plt.imshow(final)
                plt.show()
            else:
                print("Error please select two images ")
                QMessageBox.critical(self.alpha_btn, 'Error', "Error please select two images", QMessageBox.Ok)

        except Exception:
            QMessageBox.critical(self.alpha_btn, 'Error',
                                 "Error please select two images one of them with alpha channel", QMessageBox.Ok)

    ''' -- Object operations tasks --'''

    def show_object(self):
        show_shape()

    def rotate_object(self):
        deg = int(self.obj_value.value())
        rotate(deg, True)

    def translate_object(self):
        t1 = int(self.obj_value.value())
        t2 = int(self.obj_value.value())
        translate(t1, t2)

    def scale_object(self):
        scale = int(self.obj_value.value())
        scaling(scale)

    def value_changed(self):
        self.value.setText("Value = " + str(self.obj_value.value()))

    ''' -- YUV to RGB --'''

    def rgb2yuv(self):
        try:
            if self.image1:
                rgb_img = np.array(Image.open(str(self.image1)).convert('RGB').resize((500, 500)))
                ploting_rgb2yuv(rgb_img)

            else:
                QMessageBox.critical(self.rgb2yuv_btn, 'Error', "Error please select image ", QMessageBox.Ok)

        except Exception:
            QMessageBox.critical(self.rgb2yuv_btn, 'Error', "Error please select image ", QMessageBox.Ok)

    def yuv2rgb(self):
        try:
            if self.image1:
                rgb_img = np.array(Image.open(str(self.image1)).convert('RGB').resize((500, 500)))
                y, u, v = rgb2yuv(rgb_img)
                ploting_yuv2rgb(y, u, v)
            else:
                QMessageBox.critical(self.yuv2rgb_btn, 'Error', "Error please select image ", QMessageBox.Ok)


        except Exception:
            QMessageBox.critical(self.yuv2rgb_btn, 'Error', "Error please select image ", QMessageBox.Ok)

    def upsampling(self):
        try:
            if self.image1:
                rgb_img = np.array(Image.open(str(self.image1)).convert('RGB').resize((500, 500)))
                y, u, v = rgb2yuv(rgb_img)
                prove = upsampling(y, u, v)
                print(prove)
            else:
                QMessageBox.critical(self.sampling_btn, 'Error', "Error please select image ", QMessageBox.Ok)

        except Exception:
            QMessageBox.critical(self.sampling_btn, 'Error', "Error please select image ", QMessageBox.Ok)

    ''' -- Compression --'''
    #BLEIATSN
    #[3, 2, 2, 1, 1, 1, 1, 1]
    def huffman_code(self):
        try:
            allph = str(self.alph_bet.toPlainText())
            if allph == "":
                QMessageBox.critical(self.huff_btn, 'Error', "please fill the text ", QMessageBox.Ok)
            else:

                if allph.isalpha():
                    alphabet = list(allph)
                    fre = str(self.frequan.toPlainText())

                    if fre == "":
                        QMessageBox.critical(self.huff_btn, 'Error', "Please fill the frequency", QMessageBox.Ok)

                    else:
                        if fre.isalpha():
                            QMessageBox.critical(self.huff_btn, 'Error', "the frequency must be all numbers",
                                                 QMessageBox.Ok)
                        else:

                            freqq = list(fre)
                            li = cal_tree(freqq, alphabet)
                            tuplesList = []
                            indexRecursive(li[0], [], tuplesList)
                            rescap = "Symbol".ljust(10) + "Frequency".ljust(13) + "Huffman Code\n"
                            self.dialog.ui.result.setText(rescap)
                            rt = str(self.frequan.toPlainText())
                            freqq = list(rt)
                            count = 0
                            for inx, code in tuplesList:
                                resapp = str(inx).ljust(17) + str(freqq[count]).ljust(16) + str(code)
                                self.dialog.ui.result.append(resapp)
                                count += 1
                            self.dialog.show()

                else:
                    QMessageBox.critical(self.huff_btn, 'Error', "the text must be alphabet not numbers",
                                         QMessageBox.Ok)
        except Exception:
            QMessageBox.critical(self.huff_btn, 'Error', "un expected error occurs", QMessageBox.Ok)

    def run_length(self):
        try:
            alpha = str(self.alph_bet.toPlainText())
            fre = str(self.frequan.toPlainText())
            if alpha == "" and fre == "":
                QMessageBox.critical(self.runlength_btn, 'Error', "please fill the text ", QMessageBox.Ok)
            else:
                if alpha.isalpha():
                    encode_re = run.encode(alpha)
                    self.dialog.ui.result.setText("The encode of this text :\n")
                    self.dialog.ui.result.append(str(encode_re))
                    self.dialog.show()
                else:
                    QMessageBox.critical(self.runlength_btn, 'Error', "the text must be alphabet",
                                         QMessageBox.Ok)

            if not fre == "":
                decode_re = run.decode(str(fre))
                self.dialog.ui.result.setText("The decode of this text :\n")
                self.dialog.ui.result.append(str(decode_re))
                self.dialog.show()

        except Exception:
            QMessageBox.critical(self.runlength_btn, 'Error', "Un expected error occurs",
                                 QMessageBox.Ok)

    def lzw_code(self):
        try:
            alpha = str(self.alph_bet.toPlainText())
            if self.frequan.toPlainText() == "":
                fre = []
            else:
                fre = list(map(int, self.frequan.toPlainText().split(",")))
                print(fre)
            if alpha == "" and len(fre) == 0:
                QMessageBox.critical(self.runlength_btn, 'Error', "please fill the text ", QMessageBox.Ok)
            else:
                if alpha.isalpha():
                    encode_re = lzw.compress(alpha)
                    self.dialog.ui.result.setText("The encode of this text :\n")
                    self.dialog.ui.result.append(str(encode_re))
                    self.dialog.show()
                else:
                    if len(fre) == 0:
                        QMessageBox.critical(self.runlength_btn, 'Error', "the text must be alphabet",
                                             QMessageBox.Ok)

            if not len(fre) == 0:
                decode_re = lzw.decompress(fre)
                self.dialog.ui.result.setText("The decode of this text :\n")
                self.dialog.ui.result.append(str(decode_re))
                self.dialog.show()

        except Exception:
            QMessageBox.critical(self.runlength_btn, 'Error', "Un expected error occurs",
                                 QMessageBox.Ok)

    def shannon(self):
        try:
            allph = str(self.alph_bet.toPlainText())
            if allph == "":
                QMessageBox.critical(self.huff_btn, 'Error', "please fill the text ", QMessageBox.Ok)
            else:

                if allph.isalpha():
                    alphabet = list(allph)
                    fre = str(self.frequan.toPlainText())

                    if fre == "":
                        QMessageBox.critical(self.huff_btn, 'Error', "Please fill the frequency", QMessageBox.Ok)

                    else:
                        if fre.isalpha():
                            QMessageBox.critical(self.huff_btn, 'Error', "the frequency must be all numbers",
                                                 QMessageBox.Ok)
                        else:
                            rescap = "Symbol".ljust(10) + "Huffman Code\n"
                            self.dialog.ui.result.setText(rescap)
                            one = pr_tree(shannon(alphabet))
                            for inx, code in one:
                                resapp = (str(inx).ljust(10) + str(code))
                                self.dialog.ui.result.append(resapp)

                            self.dialog.show()

                else:
                    QMessageBox.critical(self.huff_btn, 'Error', "the text must be alphabet not numbers",
                                         QMessageBox.Ok)
        except Exception:
            QMessageBox.critical(self.huff_btn, 'Error', "un expected error occurs", QMessageBox.Ok)


app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Form()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
