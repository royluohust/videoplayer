# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'realplayerui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from slider import Slider
from myvideowidget import myvideowidget


class Ui_window(object):
    def setupUi(self, window):
        if not window.objectName():
            window.setObjectName(u"window")
        window.resize(810, 661)
        self.centralwidget = QWidget(window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 5)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QFrame.Raised)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.videowidget = myvideowidget(self.page)
        self.videowidget.setObjectName(u"videowidget")
        self.horizontalLayout_5 = QHBoxLayout(self.videowidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.gridLayout.addWidget(self.videowidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.play_progress_label = QLabel(self.centralwidget)
        self.play_progress_label.setObjectName(u"play_progress_label")

        self.horizontalLayout.addWidget(self.play_progress_label)

        self.play_progress_slider = Slider(self.centralwidget)
        self.play_progress_slider.setObjectName(u"play_progress_slider")
        self.play_progress_slider.setValue(0)
        self.play_progress_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.play_progress_slider)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 17)
        self.horizontalLayout.setStretch(2, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.video_line_edit = QLineEdit(self.centralwidget)
        self.video_line_edit.setObjectName(u"video_line_edit")

        self.horizontalLayout_2.addWidget(self.video_line_edit)

        self.select_video_btn = QPushButton(self.centralwidget)
        self.select_video_btn.setObjectName(u"select_video_btn")

        self.horizontalLayout_2.addWidget(self.select_video_btn)

        self.horizontalLayout_2.setStretch(0, 9)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.play_btn = QPushButton(self.centralwidget)
        self.play_btn.setObjectName(u"play_btn")

        self.horizontalLayout_3.addWidget(self.play_btn)

        self.pause_btn = QPushButton(self.centralwidget)
        self.pause_btn.setObjectName(u"pause_btn")

        self.horizontalLayout_3.addWidget(self.pause_btn)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignRight)

        self.volume_slider = Slider(self.centralwidget)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(50)
        self.volume_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.volume_slider)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 4)
        self.horizontalLayout_3.setStretch(4, 11)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        window.setCentralWidget(self.centralwidget)

        self.retranslateUi(window)

        QMetaObject.connectSlotsByName(window)
    # setupUi

    def retranslateUi(self, window):
        window.setWindowTitle(QCoreApplication.translate("window", u"\u89c6\u9891\u64ad\u653e\u5668", None))
        self.play_progress_label.setText(QCoreApplication.translate("window", u"00:00/00:00", None))
        self.select_video_btn.setText(QCoreApplication.translate("window", u"\u9009\u62e9", None))
        self.play_btn.setText(QCoreApplication.translate("window", u"\u64ad\u653e", None))
        self.pause_btn.setText(QCoreApplication.translate("window", u"\u6682\u505c", None))
        self.label.setText(QCoreApplication.translate("window", u"\u97f3\u91cf", None))
    # retranslateUi

