# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acq4/analysis/modules/STDPAnalyzer/STDPControlTemplate.ui'
#
# Created: Tue May  5 16:37:29 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(351, 463)
        self.gridLayout_7 = QtGui.QGridLayout(Form)
        self.gridLayout_7.setMargin(1)
        self.gridLayout_7.setSpacing(3)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.traceDisplayGroup = QtGui.QGroupBox(Form)
        self.traceDisplayGroup.setObjectName(_fromUtf8("traceDisplayGroup"))
        self.gridLayout_3 = QtGui.QGridLayout(self.traceDisplayGroup)
        self.gridLayout_3.setMargin(3)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.averageCheck = QtGui.QCheckBox(self.traceDisplayGroup)
        self.averageCheck.setObjectName(_fromUtf8("averageCheck"))
        self.gridLayout_3.addWidget(self.averageCheck, 0, 0, 1, 2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(1)
        self.gridLayout_2.setVerticalSpacing(3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.averageTimeRadio = QtGui.QRadioButton(self.traceDisplayGroup)
        self.averageTimeRadio.setChecked(True)
        self.averageTimeRadio.setObjectName(_fromUtf8("averageTimeRadio"))
        self.gridLayout_2.addWidget(self.averageTimeRadio, 0, 0, 1, 1)
        self.averageTimeSpin = SpinBox(self.traceDisplayGroup)
        self.averageTimeSpin.setObjectName(_fromUtf8("averageTimeSpin"))
        self.gridLayout_2.addWidget(self.averageTimeSpin, 0, 1, 1, 2)
        self.averageNumberRadio = QtGui.QRadioButton(self.traceDisplayGroup)
        self.averageNumberRadio.setObjectName(_fromUtf8("averageNumberRadio"))
        self.gridLayout_2.addWidget(self.averageNumberRadio, 1, 0, 1, 2)
        self.averageAnalysisCheck = QtGui.QCheckBox(self.traceDisplayGroup)
        self.averageAnalysisCheck.setMinimumSize(QtCore.QSize(0, 20))
        self.averageAnalysisCheck.setChecked(True)
        self.averageAnalysisCheck.setObjectName(_fromUtf8("averageAnalysisCheck"))
        self.gridLayout_2.addWidget(self.averageAnalysisCheck, 2, 0, 1, 3)
        self.averageNumberSpin = SpinBox(self.traceDisplayGroup)
        self.averageNumberSpin.setDecimals(0)
        self.averageNumberSpin.setMaximum(1000.0)
        self.averageNumberSpin.setProperty("value", 5.0)
        self.averageNumberSpin.setObjectName(_fromUtf8("averageNumberSpin"))
        self.gridLayout_2.addWidget(self.averageNumberSpin, 1, 2, 1, 1)
        self.displayTracesCheck = QtGui.QCheckBox(self.traceDisplayGroup)
        self.displayTracesCheck.setMinimumSize(QtCore.QSize(0, 20))
        self.displayTracesCheck.setObjectName(_fromUtf8("displayTracesCheck"))
        self.gridLayout_2.addWidget(self.displayTracesCheck, 3, 0, 1, 3)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 1, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 2, 1, 1)
        self.gridLayout_7.addWidget(self.traceDisplayGroup, 0, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(244, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem3, 2, 0, 1, 1)
        self.analysisGroup = QtGui.QGroupBox(Form)
        self.analysisGroup.setObjectName(_fromUtf8("analysisGroup"))
        self.gridLayout_4 = QtGui.QGridLayout(self.analysisGroup)
        self.gridLayout_4.setMargin(3)
        self.gridLayout_4.setSpacing(3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.baselineCheck = QtGui.QCheckBox(self.analysisGroup)
        self.baselineCheck.setChecked(True)
        self.baselineCheck.setObjectName(_fromUtf8("baselineCheck"))
        self.gridLayout_4.addWidget(self.baselineCheck, 0, 0, 1, 2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.analysisGroup)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.baselineStartSpin = SpinBox(self.analysisGroup)
        self.baselineStartSpin.setObjectName(_fromUtf8("baselineStartSpin"))
        self.gridLayout.addWidget(self.baselineStartSpin, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.analysisGroup)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.baselineEndSpin = SpinBox(self.analysisGroup)
        self.baselineEndSpin.setObjectName(_fromUtf8("baselineEndSpin"))
        self.gridLayout.addWidget(self.baselineEndSpin, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(1, 5)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.pspCheck = QtGui.QCheckBox(self.analysisGroup)
        self.pspCheck.setChecked(True)
        self.pspCheck.setObjectName(_fromUtf8("pspCheck"))
        self.gridLayout_4.addWidget(self.pspCheck, 2, 0, 1, 2)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setSpacing(1)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_3 = QtGui.QLabel(self.analysisGroup)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
        self.pspStartSpin = SpinBox(self.analysisGroup)
        self.pspStartSpin.setObjectName(_fromUtf8("pspStartSpin"))
        self.gridLayout_5.addWidget(self.pspStartSpin, 0, 1, 1, 2)
        self.label_4 = QtGui.QLabel(self.analysisGroup)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)
        self.pspEndSpin = SpinBox(self.analysisGroup)
        self.pspEndSpin.setObjectName(_fromUtf8("pspEndSpin"))
        self.gridLayout_5.addWidget(self.pspEndSpin, 1, 1, 1, 2)
        self.label_7 = QtGui.QLabel(self.analysisGroup)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 1)
        self.pointsToAvgCheck = QtGui.QCheckBox(self.analysisGroup)
        self.pointsToAvgCheck.setChecked(True)
        self.pointsToAvgCheck.setObjectName(_fromUtf8("pointsToAvgCheck"))
        self.gridLayout_5.addWidget(self.pointsToAvgCheck, 3, 0, 1, 2)
        self.measureModeCombo = ComboBox(self.analysisGroup)
        self.measureModeCombo.setObjectName(_fromUtf8("measureModeCombo"))
        self.gridLayout_5.addWidget(self.measureModeCombo, 2, 1, 1, 2)
        self.measureAvgSpin = SpinBox(self.analysisGroup)
        self.measureAvgSpin.setDecimals(0)
        self.measureAvgSpin.setProperty("value", 5.0)
        self.measureAvgSpin.setObjectName(_fromUtf8("measureAvgSpin"))
        self.gridLayout_5.addWidget(self.measureAvgSpin, 3, 2, 1, 1)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.gridLayout_5.setColumnStretch(2, 3)
        self.gridLayout_4.addLayout(self.gridLayout_5, 3, 1, 1, 1)
        self.healthCheck = QtGui.QCheckBox(self.analysisGroup)
        self.healthCheck.setChecked(True)
        self.healthCheck.setObjectName(_fromUtf8("healthCheck"))
        self.gridLayout_4.addWidget(self.healthCheck, 4, 0, 1, 2)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setSpacing(1)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.healthStartSpin = SpinBox(self.analysisGroup)
        self.healthStartSpin.setObjectName(_fromUtf8("healthStartSpin"))
        self.gridLayout_6.addWidget(self.healthStartSpin, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.analysisGroup)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_6.addWidget(self.label_6, 1, 0, 1, 1)
        self.healthEndSpin = SpinBox(self.analysisGroup)
        self.healthEndSpin.setObjectName(_fromUtf8("healthEndSpin"))
        self.gridLayout_6.addWidget(self.healthEndSpin, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.analysisGroup)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayout_6.setColumnStretch(1, 5)
        self.gridLayout_4.addLayout(self.gridLayout_6, 5, 1, 1, 1)
        self.analyzeBtn = QtGui.QPushButton(self.analysisGroup)
        self.analyzeBtn.setObjectName(_fromUtf8("analyzeBtn"))
        self.gridLayout_4.addWidget(self.analyzeBtn, 7, 0, 1, 3)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 6, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 3, 0, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 5, 0, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 1, 2, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem9, 3, 2, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem10, 5, 2, 1, 1)
        self.gridLayout_4.setColumnStretch(1, 5)
        self.gridLayout_7.addWidget(self.analysisGroup, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.traceDisplayGroup.setTitle(_translate("Form", "Trace Display:", None))
        self.averageCheck.setText(_translate("Form", "Average traces based on:", None))
        self.averageTimeRadio.setText(_translate("Form", "Time:", None))
        self.averageNumberRadio.setText(_translate("Form", "Number:", None))
        self.averageAnalysisCheck.setText(_translate("Form", "Use averaged traces for analysis", None))
        self.displayTracesCheck.setText(_translate("Form", "Display original traces (slow)", None))
        self.analysisGroup.setTitle(_translate("Form", "Analysis", None))
        self.baselineCheck.setText(_translate("Form", "Baseline Region (green)", None))
        self.label.setText(_translate("Form", "Start:", None))
        self.label_2.setText(_translate("Form", "End:", None))
        self.pspCheck.setText(_translate("Form", "Synaptic Event Region (red)", None))
        self.label_3.setText(_translate("Form", "Start:", None))
        self.label_4.setText(_translate("Form", "End:", None))
        self.label_7.setText(_translate("Form", "Measure:", None))
        self.pointsToAvgCheck.setText(_translate("Form", "Points to average:", None))
        self.healthCheck.setText(_translate("Form", "Cell Health Region (blue)", None))
        self.label_6.setText(_translate("Form", "End:", None))
        self.label_5.setText(_translate("Form", "Start:", None))
        self.analyzeBtn.setText(_translate("Form", "Analyze!", None))

from acq4.pyqtgraph.widgets.SpinBox import SpinBox
from acq4.pyqtgraph.widgets.ComboBox import ComboBox
