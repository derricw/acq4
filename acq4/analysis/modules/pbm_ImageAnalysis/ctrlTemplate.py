# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './acq4/analysis/modules/pbm_ImageAnalysis/ctrlTemplate.ui'
#
# Created: Sun Aug  3 13:12:38 2014
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(384, 410)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(384, 410))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        Form.setFont(font)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setMaximumSize(QtCore.QSize(392, 410))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setPointSize(13)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.ImagePhys_ImgNormalize = QtGui.QPushButton(self.groupBox)
        self.ImagePhys_ImgNormalize.setEnabled(False)
        self.ImagePhys_ImgNormalize.setGeometry(QtCore.QRect(195, 180, 91, 32))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImagePhys_ImgNormalize.sizePolicy().hasHeightForWidth())
        self.ImagePhys_ImgNormalize.setSizePolicy(sizePolicy)
        self.ImagePhys_ImgNormalize.setObjectName(_fromUtf8("ImagePhys_ImgNormalize"))
        self.ImagePhys_NormInfo = QtGui.QLabel(self.groupBox)
        self.ImagePhys_NormInfo.setEnabled(False)
        self.ImagePhys_NormInfo.setGeometry(QtCore.QRect(290, 185, 76, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImagePhys_NormInfo.sizePolicy().hasHeightForWidth())
        self.ImagePhys_NormInfo.setSizePolicy(sizePolicy)
        self.ImagePhys_NormInfo.setObjectName(_fromUtf8("ImagePhys_NormInfo"))
        self.ImagePhys_Update = QtGui.QPushButton(self.groupBox)
        self.ImagePhys_Update.setGeometry(QtCore.QRect(200, 155, 78, 32))
        self.ImagePhys_Update.setObjectName(_fromUtf8("ImagePhys_Update"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(190, 20, 171, 136))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.layoutWidget = QtGui.QWidget(self.groupBox_4)
        self.layoutWidget.setGeometry(QtCore.QRect(5, 20, 165, 120))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.ImagePhys_View = QtGui.QComboBox(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImagePhys_View.sizePolicy().hasHeightForWidth())
        self.ImagePhys_View.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setPointSize(13)
        self.ImagePhys_View.setFont(font)
        self.ImagePhys_View.setObjectName(_fromUtf8("ImagePhys_View"))
        self.ImagePhys_View.addItem(_fromUtf8(""))
        self.ImagePhys_View.addItem(_fromUtf8(""))
        self.ImagePhys_View.addItem(_fromUtf8(""))
        self.ImagePhys_View.addItem(_fromUtf8(""))
        self.ImagePhys_View.addItem(_fromUtf8(""))
        self.ImagePhys_View.addItem(_fromUtf8(""))
        self.verticalLayout_3.addWidget(self.ImagePhys_View)
        self.ImagePhys_ImgMethod = QtGui.QComboBox(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImagePhys_ImgMethod.sizePolicy().hasHeightForWidth())
        self.ImagePhys_ImgMethod.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setPointSize(13)
        self.ImagePhys_ImgMethod.setFont(font)
        self.ImagePhys_ImgMethod.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.ImagePhys_ImgMethod.setObjectName(_fromUtf8("ImagePhys_ImgMethod"))
        self.ImagePhys_ImgMethod.addItem(_fromUtf8(""))
        self.ImagePhys_ImgMethod.addItem(_fromUtf8(""))
        self.ImagePhys_ImgMethod.addItem(_fromUtf8(""))
        self.ImagePhys_ImgMethod.addItem(_fromUtf8(""))
        self.ImagePhys_ImgMethod.addItem(_fromUtf8(""))
        self.ImagePhys_ImgMethod.addItem(_fromUtf8(""))
        self.verticalLayout_3.addWidget(self.ImagePhys_ImgMethod)
        self.ImagePhys_DisplayTraces = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImagePhys_DisplayTraces.sizePolicy().hasHeightForWidth())
        self.ImagePhys_DisplayTraces.setSizePolicy(sizePolicy)
        self.ImagePhys_DisplayTraces.setObjectName(_fromUtf8("ImagePhys_DisplayTraces"))
        self.verticalLayout_3.addWidget(self.ImagePhys_DisplayTraces)
        self.ImagePhys_ExportTiff = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImagePhys_ExportTiff.sizePolicy().hasHeightForWidth())
        self.ImagePhys_ExportTiff.setSizePolicy(sizePolicy)
        self.ImagePhys_ExportTiff.setObjectName(_fromUtf8("ImagePhys_ExportTiff"))
        self.verticalLayout_3.addWidget(self.ImagePhys_ExportTiff)
        self.ImagePhys_FileGroup = QtGui.QGroupBox(self.groupBox)
        self.ImagePhys_FileGroup.setEnabled(True)
        self.ImagePhys_FileGroup.setGeometry(QtCore.QRect(10, 15, 151, 226))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.ImagePhys_FileGroup.sizePolicy().hasHeightForWidth())
        self.ImagePhys_FileGroup.setSizePolicy(sizePolicy)
        self.ImagePhys_FileGroup.setMinimumSize(QtCore.QSize(140, 190))
        self.ImagePhys_FileGroup.setSizeIncrement(QtCore.QSize(10, 10))
        self.ImagePhys_FileGroup.setBaseSize(QtCore.QSize(100, 250))
        self.ImagePhys_FileGroup.setObjectName(_fromUtf8("ImagePhys_FileGroup"))
        self.ImagePhys_ImageMode = QtGui.QComboBox(self.ImagePhys_FileGroup)
        self.ImagePhys_ImageMode.setGeometry(QtCore.QRect(5, 40, 131, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setPointSize(13)
        self.ImagePhys_ImageMode.setFont(font)
        self.ImagePhys_ImageMode.setObjectName(_fromUtf8("ImagePhys_ImageMode"))
        self.ImagePhys_ImageMode.addItem(_fromUtf8(""))
        self.ImagePhys_ImageMode.addItem(_fromUtf8(""))
        self.ImagePhys_clearRatio = QtGui.QPushButton(self.ImagePhys_FileGroup)
        self.ImagePhys_clearRatio.setGeometry(QtCore.QRect(0, 170, 141, 30))
        self.ImagePhys_clearRatio.setObjectName(_fromUtf8("ImagePhys_clearRatio"))
        self.ImagePhys_GetFileInfo = QtGui.QPushButton(self.ImagePhys_FileGroup)
        self.ImagePhys_GetFileInfo.setGeometry(QtCore.QRect(0, 15, 136, 31))
        self.ImagePhys_GetFileInfo.setObjectName(_fromUtf8("ImagePhys_GetFileInfo"))
        self.ImagePhys_getRatio = QtGui.QPushButton(self.ImagePhys_FileGroup)
        self.ImagePhys_getRatio.setGeometry(QtCore.QRect(0, 145, 141, 30))
        self.ImagePhys_getRatio.setObjectName(_fromUtf8("ImagePhys_getRatio"))
        self.layoutWidget1 = QtGui.QWidget(self.ImagePhys_FileGroup)
        self.layoutWidget1.setGeometry(QtCore.QRect(5, 65, 131, 26))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.ImagePhys_DataStruct = QtGui.QComboBox(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImagePhys_DataStruct.sizePolicy().hasHeightForWidth())
        self.ImagePhys_DataStruct.setSizePolicy(sizePolicy)
        self.ImagePhys_DataStruct.setMaxCount(10)
        self.ImagePhys_DataStruct.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.ImagePhys_DataStruct.setFrame(False)
        self.ImagePhys_DataStruct.setObjectName(_fromUtf8("ImagePhys_DataStruct"))
        self.ImagePhys_DataStruct.addItem(_fromUtf8(""))
        self.ImagePhys_DataStruct.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.ImagePhys_DataStruct)
        self.layoutWidget2 = QtGui.QWidget(self.ImagePhys_FileGroup)
        self.layoutWidget2.setGeometry(QtCore.QRect(5, 115, 131, 27))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.layoutWidget2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.ImagePhys_ignoreFirst = QtGui.QSpinBox(self.layoutWidget2)
        self.ImagePhys_ignoreFirst.setSuffix(_fromUtf8(""))
        self.ImagePhys_ignoreFirst.setPrefix(_fromUtf8(""))
        self.ImagePhys_ignoreFirst.setProperty("value", 1)
        self.ImagePhys_ignoreFirst.setObjectName(_fromUtf8("ImagePhys_ignoreFirst"))
        self.horizontalLayout_4.addWidget(self.ImagePhys_ignoreFirst)
        self.layoutWidget3 = QtGui.QWidget(self.ImagePhys_FileGroup)
        self.layoutWidget3.setGeometry(QtCore.QRect(5, 90, 131, 28))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.layoutWidget3)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.ImagePhys_Downsample = QtGui.QComboBox(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        self.ImagePhys_Downsample.setFont(font)
        self.ImagePhys_Downsample.setEditable(True)
        self.ImagePhys_Downsample.setMaxCount(5000)
        self.ImagePhys_Downsample.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.ImagePhys_Downsample.setObjectName(_fromUtf8("ImagePhys_Downsample"))
        self.ImagePhys_Downsample.addItem(_fromUtf8(""))
        self.ImagePhys_Downsample.addItem(_fromUtf8(""))
        self.ImagePhys_Downsample.addItem(_fromUtf8(""))
        self.ImagePhys_Downsample.addItem(_fromUtf8(""))
        self.ImagePhys_Downsample.addItem(_fromUtf8(""))
        self.ImagePhys_Downsample.addItem(_fromUtf8(""))
        self.ImagePhys_Downsample.addItem(_fromUtf8(""))
        self.ImagePhys_Downsample.addItem(_fromUtf8(""))
        self.ImagePhys_Downsample.addItem(_fromUtf8(""))
        self.ImagePhys_Downsample.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.ImagePhys_Downsample)
        self.ImagePhys_RegisterStack = QtGui.QPushButton(self.ImagePhys_FileGroup)
        self.ImagePhys_RegisterStack.setGeometry(QtCore.QRect(0, 195, 141, 29))
        self.ImagePhys_RegisterStack.setObjectName(_fromUtf8("ImagePhys_RegisterStack"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(195, 205, 116, 96))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.widget = QtGui.QWidget(self.groupBox_3)
        self.widget.setGeometry(QtCore.QRect(10, 25, 96, 62))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ImagePhys_Camera_check = QtGui.QCheckBox(self.widget)
        self.ImagePhys_Camera_check.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ImagePhys_Camera_check.setChecked(True)
        self.ImagePhys_Camera_check.setObjectName(_fromUtf8("ImagePhys_Camera_check"))
        self.verticalLayout_2.addWidget(self.ImagePhys_Camera_check)
        self.ImagePhys_PMT_check = QtGui.QCheckBox(self.widget)
        self.ImagePhys_PMT_check.setChecked(True)
        self.ImagePhys_PMT_check.setObjectName(_fromUtf8("ImagePhys_PMT_check"))
        self.verticalLayout_2.addWidget(self.ImagePhys_PMT_check)
        self.ImagePhys_Image_check = QtGui.QCheckBox(self.widget)
        self.ImagePhys_Image_check.setObjectName(_fromUtf8("ImagePhys_Image_check"))
        self.verticalLayout_2.addWidget(self.ImagePhys_Image_check)
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 235, 151, 171))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.ImagePhys_PMT_decomb_subpixel = QtGui.QCheckBox(self.groupBox_6)
        self.ImagePhys_PMT_decomb_subpixel.setGeometry(QtCore.QRect(0, 80, 81, 20))
        self.ImagePhys_PMT_decomb_subpixel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ImagePhys_PMT_decomb_subpixel.setObjectName(_fromUtf8("ImagePhys_PMT_decomb_subpixel"))
        self.label = QtGui.QLabel(self.groupBox_6)
        self.label.setGeometry(QtCore.QRect(5, 120, 62, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.ImagePhys_PMT_decomb = QtGui.QDoubleSpinBox(self.groupBox_6)
        self.ImagePhys_PMT_decomb.setGeometry(QtCore.QRect(75, 115, 71, 25))
        self.ImagePhys_PMT_decomb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_PMT_decomb.setMinimum(-500.0)
        self.ImagePhys_PMT_decomb.setMaximum(500.0)
        self.ImagePhys_PMT_decomb.setObjectName(_fromUtf8("ImagePhys_PMT_decomb"))
        self.ImagePhys_Restore_decomb = QtGui.QPushButton(self.groupBox_6)
        self.ImagePhys_Restore_decomb.setGeometry(QtCore.QRect(0, 140, 121, 32))
        self.ImagePhys_Restore_decomb.setObjectName(_fromUtf8("ImagePhys_Restore_decomb"))
        self.ImagePhys_PMT_auto_check = QtGui.QCheckBox(self.groupBox_6)
        self.ImagePhys_PMT_auto_check.setGeometry(QtCore.QRect(0, 100, 51, 20))
        self.ImagePhys_PMT_auto_check.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ImagePhys_PMT_auto_check.setObjectName(_fromUtf8("ImagePhys_PMT_auto_check"))
        self.ImagePhys_PMT_autoButton = QtGui.QPushButton(self.groupBox_6)
        self.ImagePhys_PMT_autoButton.setGeometry(QtCore.QRect(75, 85, 61, 23))
        self.ImagePhys_PMT_autoButton.setObjectName(_fromUtf8("ImagePhys_PMT_autoButton"))
        self.widget1 = QtGui.QWidget(self.groupBox_6)
        self.widget1.setGeometry(QtCore.QRect(5, 20, 136, 32))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ImagePhys_PMT_LPF_check = QtGui.QCheckBox(self.widget1)
        self.ImagePhys_PMT_LPF_check.setObjectName(_fromUtf8("ImagePhys_PMT_LPF_check"))
        self.horizontalLayout_2.addWidget(self.ImagePhys_PMT_LPF_check)
        self.ImagePhys_PMT_LPF = QtGui.QDoubleSpinBox(self.widget1)
        self.ImagePhys_PMT_LPF.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_PMT_LPF.setDecimals(1)
        self.ImagePhys_PMT_LPF.setMaximum(500.0)
        self.ImagePhys_PMT_LPF.setProperty("value", 50.0)
        self.ImagePhys_PMT_LPF.setObjectName(_fromUtf8("ImagePhys_PMT_LPF"))
        self.horizontalLayout_2.addWidget(self.ImagePhys_PMT_LPF)
        self.widget2 = QtGui.QWidget(self.groupBox_6)
        self.widget2.setGeometry(QtCore.QRect(5, 50, 138, 32))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.widget2)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.ImagePhys_PMT_Notch_check = QtGui.QCheckBox(self.widget2)
        self.ImagePhys_PMT_Notch_check.setObjectName(_fromUtf8("ImagePhys_PMT_Notch_check"))
        self.horizontalLayout_7.addWidget(self.ImagePhys_PMT_Notch_check)
        self.ImagePhys_PMT_Notch = QtGui.QDoubleSpinBox(self.widget2)
        self.ImagePhys_PMT_Notch.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_PMT_Notch.setDecimals(1)
        self.ImagePhys_PMT_Notch.setMaximum(500.0)
        self.ImagePhys_PMT_Notch.setProperty("value", 80.0)
        self.ImagePhys_PMT_Notch.setObjectName(_fromUtf8("ImagePhys_PMT_Notch"))
        self.horizontalLayout_7.addWidget(self.ImagePhys_PMT_Notch)
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(195, 310, 116, 96))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.layoutWidget4 = QtGui.QWidget(self.groupBox_5)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 25, 96, 64))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ImagePhys_PhysROIPlot = QtGui.QCheckBox(self.layoutWidget4)
        self.ImagePhys_PhysROIPlot.setObjectName(_fromUtf8("ImagePhys_PhysROIPlot"))
        self.verticalLayout.addWidget(self.ImagePhys_PhysROIPlot)
        self.ImagePhys_RectSelect = QtGui.QCheckBox(self.layoutWidget4)
        self.ImagePhys_RectSelect.setChecked(False)
        self.ImagePhys_RectSelect.setObjectName(_fromUtf8("ImagePhys_RectSelect"))
        self.verticalLayout.addWidget(self.ImagePhys_RectSelect)
        self.ImagePhys_CorrTool_BL1 = QtGui.QCheckBox(self.layoutWidget4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImagePhys_CorrTool_BL1.sizePolicy().hasHeightForWidth())
        self.ImagePhys_CorrTool_BL1.setSizePolicy(sizePolicy)
        self.ImagePhys_CorrTool_BL1.setObjectName(_fromUtf8("ImagePhys_CorrTool_BL1"))
        self.verticalLayout.addWidget(self.ImagePhys_CorrTool_BL1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Files, Corrections, and Filtering", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ImgNormalize.setText(QtGui.QApplication.translate("Form", "Normalize", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_NormInfo.setText(QtGui.QApplication.translate("Form", "NormInfo", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Update.setText(QtGui.QApplication.translate("Form", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Form", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_View.setItemText(0, QtGui.QApplication.translate("Form", "Movie", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_View.setItemText(1, QtGui.QApplication.translate("Form", "Average Image", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_View.setItemText(2, QtGui.QApplication.translate("Form", "Reference Image", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_View.setItemText(3, QtGui.QApplication.translate("Form", "Std Image", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_View.setItemText(4, QtGui.QApplication.translate("Form", "Spectrum Image", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_View.setItemText(5, QtGui.QApplication.translate("Form", "Ratio Image", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ImgMethod.setItemText(0, QtGui.QApplication.translate("Form", "dF/Fo", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ImgMethod.setItemText(1, QtGui.QApplication.translate("Form", "dF/Base", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ImgMethod.setItemText(2, QtGui.QApplication.translate("Form", "median", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ImgMethod.setItemText(3, QtGui.QApplication.translate("Form", "Norm\'d", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ImgMethod.setItemText(4, QtGui.QApplication.translate("Form", "Slow Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ImgMethod.setItemText(5, QtGui.QApplication.translate("Form", "G/R", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_DisplayTraces.setText(QtGui.QApplication.translate("Form", "dF/F -> MPL", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ExportTiff.setText(QtGui.QApplication.translate("Form", "Export TIFF", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_FileGroup.setTitle(QtGui.QApplication.translate("Form", "File Operations", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ImageMode.setItemText(0, QtGui.QApplication.translate("Form", "Non-Ratiometric (dF/Fo)", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ImageMode.setItemText(1, QtGui.QApplication.translate("Form", "Ratiometric (G/R)", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_clearRatio.setText(QtGui.QApplication.translate("Form", "Clear Ratio Image", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_GetFileInfo.setText(QtGui.QApplication.translate("Form", "Get File Info", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_getRatio.setText(QtGui.QApplication.translate("Form", "Get Ratio Image", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_DataStruct.setItemText(0, QtGui.QApplication.translate("Form", "Flat", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_DataStruct.setItemText(1, QtGui.QApplication.translate("Form", "Interleaved", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Ignore", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Downsamp", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Downsample.setItemText(0, QtGui.QApplication.translate("Form", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Downsample.setItemText(1, QtGui.QApplication.translate("Form", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Downsample.setItemText(2, QtGui.QApplication.translate("Form", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Downsample.setItemText(3, QtGui.QApplication.translate("Form", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Downsample.setItemText(4, QtGui.QApplication.translate("Form", "20", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Downsample.setItemText(5, QtGui.QApplication.translate("Form", "50", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Downsample.setItemText(6, QtGui.QApplication.translate("Form", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Downsample.setItemText(7, QtGui.QApplication.translate("Form", "200", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Downsample.setItemText(8, QtGui.QApplication.translate("Form", "500", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Downsample.setItemText(9, QtGui.QApplication.translate("Form", "1000", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_RegisterStack.setText(QtGui.QApplication.translate("Form", "Register Stack", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "Image types", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Camera_check.setText(QtGui.QApplication.translate("Form", "Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_PMT_check.setText(QtGui.QApplication.translate("Form", "PMT", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Image_check.setText(QtGui.QApplication.translate("Form", "Imaging.ma", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("Form", "PMT Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_PMT_decomb_subpixel.setText(QtGui.QApplication.translate("Form", "SubPixel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Decomb", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Restore_decomb.setText(QtGui.QApplication.translate("Form", "Restore Decomb", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_PMT_auto_check.setText(QtGui.QApplication.translate("Form", "Auto", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_PMT_autoButton.setText(QtGui.QApplication.translate("Form", "Auto", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_PMT_LPF_check.setText(QtGui.QApplication.translate("Form", "LPF", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_PMT_Notch_check.setText(QtGui.QApplication.translate("Form", "Notch", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("Form", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_PhysROIPlot.setText(QtGui.QApplication.translate("Form", "MultiPlot", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_RectSelect.setText(QtGui.QApplication.translate("Form", "1-Button", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_CorrTool_BL1.setText(QtGui.QApplication.translate("Form", "Baseline 1", None, QtGui.QApplication.UnicodeUTF8))

