# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Work\python\bioinfo_excercise\PhyloSuite\PhyloSuite\PhyloSuite\uifiles\RSCUfig.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RSCUfig(object):
    def setupUi(self, RSCUfig):
        RSCUfig.setObjectName("RSCUfig")
        RSCUfig.resize(537, 597)
        self.gridLayout_3 = QtWidgets.QGridLayout(RSCUfig)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter = QtWidgets.QSplitter(RSCUfig)
        self.splitter.setMidLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(5)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_3.setAcceptDrops(True)
        self.listWidget_3.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.listWidget_3.setDragEnabled(True)
        self.listWidget_3.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listWidget_3.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget_3.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_3.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget_3.setObjectName("listWidget_3")
        self.gridLayout.addWidget(self.listWidget_3, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.toolButton_T = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_T.setMinimumSize(QtCore.QSize(30, 30))
        self.toolButton_T.setMaximumSize(QtCore.QSize(30, 30))
        self.toolButton_T.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/picture/resourses/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_T.setIcon(icon)
        self.toolButton_T.setIconSize(QtCore.QSize(26, 26))
        self.toolButton_T.setAutoRaise(True)
        self.toolButton_T.setObjectName("toolButton_T")
        self.verticalLayout_2.addWidget(self.toolButton_T)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setOpenExternalLinks(True)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout.addWidget(self.label_16)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = ClickedLableGif(self.groupBox)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget_2.setDragEnabled(True)
        self.listWidget_2.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listWidget_2.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_3.addWidget(self.listWidget_2)
        self.gridLayout_6.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.pushButton_color = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_color.sizePolicy().hasHeightForWidth())
        self.pushButton_color.setSizePolicy(sizePolicy)
        self.pushButton_color.setAutoFillBackground(False)
        self.pushButton_color.setStyleSheet("")
        self.pushButton_color.setText("")
        self.pushButton_color.setObjectName("pushButton_color")
        self.verticalLayout.addWidget(self.pushButton_color)
        self.pushButton_color_2 = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_color_2.sizePolicy().hasHeightForWidth())
        self.pushButton_color_2.setSizePolicy(sizePolicy)
        self.pushButton_color_2.setAutoFillBackground(False)
        self.pushButton_color_2.setStyleSheet("")
        self.pushButton_color_2.setText("")
        self.pushButton_color_2.setObjectName("pushButton_color_2")
        self.verticalLayout.addWidget(self.pushButton_color_2)
        self.pushButton_color_3 = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_color_3.sizePolicy().hasHeightForWidth())
        self.pushButton_color_3.setSizePolicy(sizePolicy)
        self.pushButton_color_3.setAutoFillBackground(False)
        self.pushButton_color_3.setStyleSheet("")
        self.pushButton_color_3.setText("")
        self.pushButton_color_3.setObjectName("pushButton_color_3")
        self.verticalLayout.addWidget(self.pushButton_color_3)
        self.pushButton_color_4 = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_color_4.sizePolicy().hasHeightForWidth())
        self.pushButton_color_4.setSizePolicy(sizePolicy)
        self.pushButton_color_4.setAutoFillBackground(False)
        self.pushButton_color_4.setStyleSheet("")
        self.pushButton_color_4.setText("")
        self.pushButton_color_4.setObjectName("pushButton_color_4")
        self.verticalLayout.addWidget(self.pushButton_color_4)
        self.gridLayout_6.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.spinBox_5 = QtWidgets.QSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_5.sizePolicy().hasHeightForWidth())
        self.spinBox_5.setSizePolicy(sizePolicy)
        self.spinBox_5.setMinimum(1)
        self.spinBox_5.setMaximum(999)
        self.spinBox_5.setProperty("value", 9)
        self.spinBox_5.setObjectName("spinBox_5")
        self.horizontalLayout_2.addWidget(self.spinBox_5)
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.spinBox_6 = QtWidgets.QSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_6.sizePolicy().hasHeightForWidth())
        self.spinBox_6.setSizePolicy(sizePolicy)
        self.spinBox_6.setMinimum(1)
        self.spinBox_6.setMaximum(999)
        self.spinBox_6.setProperty("value", 8)
        self.spinBox_6.setObjectName("spinBox_6")
        self.horizontalLayout_2.addWidget(self.spinBox_6)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 2)
        self.doubleSpinBox_2 = MyDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_2.setReadOnly(False)
        self.doubleSpinBox_2.setDecimals(1)
        self.doubleSpinBox_2.setSingleStep(0.1)
        self.doubleSpinBox_2.setProperty("value", 2.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout_2.addWidget(self.doubleSpinBox_2, 0, 2, 1, 1)
        self.doubleSpinBox_3 = MyDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_3.setToolTip("")
        self.doubleSpinBox_3.setReadOnly(False)
        self.doubleSpinBox_3.setDecimals(1)
        self.doubleSpinBox_3.setSingleStep(0.1)
        self.doubleSpinBox_3.setProperty("value", 6.5)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout_2.addWidget(self.doubleSpinBox_3, 1, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 2)
        self.gridLayout_6.addLayout(self.gridLayout_2, 2, 0, 1, 2)
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(RSCUfig)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton = ArrowPushButton(self.groupBox_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/picture/resourses/if_start_60207.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_5.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/picture/resourses/if_Delete_1493279.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_5.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(RSCUfig)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_4.addWidget(self.progressBar, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_5, 2, 0, 1, 1)

        self.retranslateUi(RSCUfig)
        QtCore.QMetaObject.connectSlotsByName(RSCUfig)

    def retranslateUi(self, RSCUfig):
        _translate = QtCore.QCoreApplication.translate
        RSCUfig.setWindowTitle(_translate("RSCUfig", "Draw RSCU Figure"))
        self.groupBox.setTitle(_translate("RSCUfig", "Input"))
        self.listWidget_3.setToolTip(_translate("RSCUfig", "Try to drag to reorder"))
        self.toolButton_T.setShortcut(_translate("RSCUfig", "Del"))
        self.label_16.setText(_translate("RSCUfig", "<html><head/><body><p>Try to drag <span style=\" font-weight:600; color:#ff0105;\">RSCU</span> tables (<span style=\" font-weight:600; color:#ff0000;\">_stack.csv</span>) and drop here</p></body></html>"))
        self.label_2.setToolTip(_translate("RSCUfig", "Brief example"))
        self.groupBox_2.setTitle(_translate("RSCUfig", "Parameters"))
        self.label_4.setText(_translate("RSCUfig", "Order on the x-axis:"))
        self.listWidget_2.setToolTip(_translate("RSCUfig", "Try to drag to reorder"))
        self.label_6.setText(_translate("RSCUfig", "Color of stacks:"))
        self.pushButton_color.setToolTip(_translate("RSCUfig", "Click to change color"))
        self.pushButton_color_2.setToolTip(_translate("RSCUfig", "Click to change color"))
        self.pushButton_color_3.setToolTip(_translate("RSCUfig", "Click to change color"))
        self.pushButton_color_4.setToolTip(_translate("RSCUfig", "Click to change color"))
        self.label_9.setText(_translate("RSCUfig", "Figure height:"))
        self.label_15.setText(_translate("RSCUfig", "Figure width:"))
        self.label_13.setText(_translate("RSCUfig", "Adjust height ratio of RSCU figure to bottom legend:"))
        self.doubleSpinBox_2.setToolTip(_translate("RSCUfig", "the input must be multiple of 0.5"))
        self.label_14.setText(_translate("RSCUfig", "Maximum value of y-axis:"))
        self.groupBox_3.setTitle(_translate("RSCUfig", "Run"))
        self.pushButton.setText(_translate("RSCUfig", "Start"))
        self.pushButton_2.setText(_translate("RSCUfig", "Close"))
        self.groupBox_5.setTitle(_translate("RSCUfig", "Progress"))

from src.CustomWidget import ArrowPushButton, ClickedLableGif, MyDoubleSpinBox
from uifiles import myRes_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RSCUfig = QtWidgets.QDialog()
    ui = Ui_RSCUfig()
    ui.setupUi(RSCUfig)
    RSCUfig.show()
    sys.exit(app.exec_())

