# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SketchGUI4.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SketchGUI(object):
    def setupUi(self, SketchGUI):
        SketchGUI.setObjectName("SketchGUI")
        SketchGUI.resize(1192, 751)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SketchGUI.sizePolicy().hasHeightForWidth())
        SketchGUI.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        SketchGUI.setFont(font)
        SketchGUI.setMouseTracking(True)
        SketchGUI.setStyleSheet("alternate-background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")
        self.centralwidget = QtWidgets.QWidget(SketchGUI)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("gridline-color: rgb(21, 255, 95);")
        self.centralwidget.setObjectName("centralwidget")
        self.input = QtWidgets.QGraphicsView(self.centralwidget)
        self.input.setEnabled(True)
        self.input.setGeometry(QtCore.QRect(50, 152, 514, 514))
        self.input.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.input.setObjectName("input")
        self.output = QtWidgets.QGraphicsView(self.centralwidget)
        self.output.setEnabled(True)
        self.output.setGeometry(QtCore.QRect(640, 152, 514, 514))
        self.output.setObjectName("output")
        self.drawing_label = QtWidgets.QLabel(self.centralwidget)
        self.drawing_label.setGeometry(QtCore.QRect(230, 665, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.drawing_label.setFont(font)
        self.drawing_label.setObjectName("drawing_label")
        self.sketch_label = QtWidgets.QLabel(self.centralwidget)
        self.sketch_label.setGeometry(QtCore.QRect(840, 665, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.sketch_label.setFont(font)
        self.sketch_label.setObjectName("sketch_label")
        self.Clear_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Clear_Button.setGeometry(QtCore.QRect(350, 10, 90, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.Clear_Button.setFont(font)
        self.Clear_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Clear_Button.setObjectName("Clear_Button")
        self.Eraser_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Eraser_Button.setGeometry(QtCore.QRect(240, 10, 90, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.Eraser_Button.setFont(font)
        self.Eraser_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Eraser_Button.setObjectName("Eraser_Button")
        self.BrushSize = QtWidgets.QSlider(self.centralwidget)
        self.BrushSize.setGeometry(QtCore.QRect(155, 97, 61, 21))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.BrushSize.setFont(font)
        self.BrushSize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BrushSize.setMinimum(1)
        self.BrushSize.setMaximum(4)
        self.BrushSize.setProperty("value", 2)
        self.BrushSize.setOrientation(QtCore.Qt.Horizontal)
        self.BrushSize.setInvertedControls(False)
        self.BrushSize.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.BrushSize.setTickInterval(1)
        self.BrushSize.setObjectName("BrushSize")
        self.brush_label = QtWidgets.QLabel(self.centralwidget)
        self.brush_label.setGeometry(QtCore.QRect(450, 82, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.brush_label.setFont(font)
        self.brush_label.setObjectName("brush_label")
        self.Erase_label = QtWidgets.QLabel(self.centralwidget)
        self.Erase_label.setGeometry(QtCore.QRect(234, 82, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.Erase_label.setFont(font)
        self.Erase_label.setObjectName("Erase_label")
        self.EraseSize = QtWidgets.QSlider(self.centralwidget)
        self.EraseSize.setGeometry(QtCore.QRect(370, 97, 61, 21))
        self.EraseSize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EraseSize.setAutoFillBackground(True)
        self.EraseSize.setMinimum(3)
        self.EraseSize.setMaximum(7)
        self.EraseSize.setProperty("value", 4)
        self.EraseSize.setOrientation(QtCore.Qt.Horizontal)
        self.EraseSize.setInvertedAppearance(False)
        self.EraseSize.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.EraseSize.setTickInterval(1)
        self.EraseSize.setObjectName("EraseSize")
        self.Undo_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Undo_Button.setGeometry(QtCore.QRect(720, 10, 90, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.Undo_Button.setFont(font)
        self.Undo_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Undo_Button.setObjectName("Undo_Button")
        self.BrushNum_label = QtWidgets.QLabel(self.centralwidget)
        self.BrushNum_label.setGeometry(QtCore.QRect(130, 92, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.BrushNum_label.setFont(font)
        self.BrushNum_label.setObjectName("BrushNum_label")
        self.EraserNum_label = QtWidgets.QLabel(self.centralwidget)
        self.EraserNum_label.setGeometry(QtCore.QRect(347, 92, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.EraserNum_label.setFont(font)
        self.EraserNum_label.setObjectName("EraserNum_label")
        self.Brush_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Brush_Button.setGeometry(QtCore.QRect(130, 10, 90, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.Brush_Button.setFont(font)
        self.Brush_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Brush_Button.setObjectName("Brush_Button")
        self.Load_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Load_Button.setGeometry(QtCore.QRect(20, 10, 90, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.Load_Button.setFont(font)
        self.Load_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Load_Button.setObjectName("Load_Button")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(590, 150, 20, 571))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.bar_num = QtWidgets.QLabel(self.centralwidget)
        self.bar_num.setGeometry(QtCore.QRect(157, 80, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.bar_num.setFont(font)
        self.bar_num.setObjectName("bar_num")
        self.bar_num_2 = QtWidgets.QLabel(self.centralwidget)
        self.bar_num_2.setGeometry(QtCore.QRect(373, 80, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.bar_num_2.setFont(font)
        self.bar_num_2.setObjectName("bar_num_2")
        self.bar_num_3 = QtWidgets.QLabel(self.centralwidget)
        self.bar_num_3.setGeometry(QtCore.QRect(205, 80, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.bar_num_3.setFont(font)
        self.bar_num_3.setObjectName("bar_num_3")
        self.bar_num_4 = QtWidgets.QLabel(self.centralwidget)
        self.bar_num_4.setGeometry(QtCore.QRect(423, 80, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.bar_num_4.setFont(font)
        self.bar_num_4.setObjectName("bar_num_4")
        self.Convert_Sketch = QtWidgets.QPushButton(self.centralwidget)
        self.Convert_Sketch.setGeometry(QtCore.QRect(460, 10, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.Convert_Sketch.setFont(font)
        self.Convert_Sketch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Convert_Sketch.setCheckable(False)
        self.Convert_Sketch.setObjectName("Convert_Sketch")
        self.RealTime_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.RealTime_checkBox.setGeometry(QtCore.QRect(180, 80, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.RealTime_checkBox.setFont(font)
        self.RealTime_checkBox.setChecked(True)
        self.RealTime_checkBox.setObjectName("RealTime_checkBox")
        self.part0_Slider = QtWidgets.QSlider(self.centralwidget)
        self.part0_Slider.setGeometry(QtCore.QRect(860, 10, 22, 91))
        self.part0_Slider.setCursor(QtGui.QCursor(QtCore.Qt.SplitVCursor))
        self.part0_Slider.setMaximum(100)
        self.part0_Slider.setPageStep(1)
        self.part0_Slider.setProperty("value", 100)
        self.part0_Slider.setOrientation(QtCore.Qt.Vertical)
        self.part0_Slider.setInvertedAppearance(True)
        self.part0_Slider.setInvertedControls(False)
        self.part0_Slider.setObjectName("part0_Slider")
        self.part1_Slider = QtWidgets.QSlider(self.centralwidget)
        self.part1_Slider.setGeometry(QtCore.QRect(910, 10, 22, 91))
        self.part1_Slider.setCursor(QtGui.QCursor(QtCore.Qt.SplitVCursor))
        self.part1_Slider.setMaximum(100)
        self.part1_Slider.setPageStep(1)
        self.part1_Slider.setProperty("value", 100)
        self.part1_Slider.setOrientation(QtCore.Qt.Vertical)
        self.part1_Slider.setInvertedAppearance(True)
        self.part1_Slider.setObjectName("part1_Slider")
        self.part2_Slider = QtWidgets.QSlider(self.centralwidget)
        self.part2_Slider.setGeometry(QtCore.QRect(960, 10, 22, 91))
        self.part2_Slider.setCursor(QtGui.QCursor(QtCore.Qt.SplitVCursor))
        self.part2_Slider.setMaximum(100)
        self.part2_Slider.setPageStep(1)
        self.part2_Slider.setProperty("value", 100)
        self.part2_Slider.setOrientation(QtCore.Qt.Vertical)
        self.part2_Slider.setInvertedAppearance(True)
        self.part2_Slider.setObjectName("part2_Slider")
        self.part3_Slider = QtWidgets.QSlider(self.centralwidget)
        self.part3_Slider.setGeometry(QtCore.QRect(1010, 10, 22, 91))
        self.part3_Slider.setCursor(QtGui.QCursor(QtCore.Qt.SplitVCursor))
        self.part3_Slider.setMaximum(100)
        self.part3_Slider.setPageStep(1)
        self.part3_Slider.setProperty("value", 100)
        self.part3_Slider.setOrientation(QtCore.Qt.Vertical)
        self.part3_Slider.setInvertedAppearance(True)
        self.part3_Slider.setObjectName("part3_Slider")
        self.part4_Slider = QtWidgets.QSlider(self.centralwidget)
        self.part4_Slider.setGeometry(QtCore.QRect(1070, 10, 22, 91))
        self.part4_Slider.setCursor(QtGui.QCursor(QtCore.Qt.SplitVCursor))
        self.part4_Slider.setMaximum(100)
        self.part4_Slider.setPageStep(1)
        self.part4_Slider.setProperty("value", 100)
        self.part4_Slider.setOrientation(QtCore.Qt.Vertical)
        self.part4_Slider.setInvertedAppearance(True)
        self.part4_Slider.setObjectName("part4_Slider")
        self.Save_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Save_Button.setGeometry(QtCore.QRect(601, 10, 90, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.Save_Button.setFont(font)
        self.Save_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Save_Button.setCheckable(False)
        self.Save_Button.setObjectName("Save_Button")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(20, 130, 1151, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.Part_0 = QtWidgets.QLabel(self.centralwidget)
        self.Part_0.setGeometry(QtCore.QRect(850, 110, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Part_0.setFont(font)
        self.Part_0.setObjectName("Part_0")
        self.Part_1 = QtWidgets.QLabel(self.centralwidget)
        self.Part_1.setGeometry(QtCore.QRect(895, 110, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Part_1.setFont(font)
        self.Part_1.setObjectName("Part_1")
        self.Part_2 = QtWidgets.QLabel(self.centralwidget)
        self.Part_2.setGeometry(QtCore.QRect(950, 110, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Part_2.setFont(font)
        self.Part_2.setObjectName("Part_2")
        self.Part_3 = QtWidgets.QLabel(self.centralwidget)
        self.Part_3.setGeometry(QtCore.QRect(1000, 110, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Part_3.setFont(font)
        self.Part_3.setObjectName("Part_3")
        self.Part_4 = QtWidgets.QLabel(self.centralwidget)
        self.Part_4.setGeometry(QtCore.QRect(1060, 110, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Part_4.setFont(font)
        self.Part_4.setObjectName("Part_4")
        self.Shadow_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.Shadow_checkBox.setGeometry(QtCore.QRect(310, 80, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.Shadow_checkBox.setFont(font)
        self.Shadow_checkBox.setChecked(True)
        self.Shadow_checkBox.setObjectName("Shadow_checkBox")
        self.part5_Slider = QtWidgets.QSlider(self.centralwidget)
        self.part5_Slider.setGeometry(QtCore.QRect(1130, 10, 22, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(71, 215, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 0.077, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 169, 255, 147))
        gradient.setColorAt(0.497326, QtGui.QColor(0, 0, 0, 147))
        gradient.setColorAt(1.0, QtGui.QColor(0, 169, 255, 147))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(71, 215, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 0.077, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 169, 255, 147))
        gradient.setColorAt(0.497326, QtGui.QColor(0, 0, 0, 147))
        gradient.setColorAt(1.0, QtGui.QColor(0, 169, 255, 147))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 0.077, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 169, 255, 147))
        gradient.setColorAt(0.497326, QtGui.QColor(0, 0, 0, 147))
        gradient.setColorAt(1.0, QtGui.QColor(0, 169, 255, 147))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.part5_Slider.setPalette(palette)
        self.part5_Slider.setCursor(QtGui.QCursor(QtCore.Qt.SplitVCursor))
        self.part5_Slider.setMaximum(100)
        self.part5_Slider.setPageStep(1)
        self.part5_Slider.setProperty("value", 100)
        self.part5_Slider.setOrientation(QtCore.Qt.Vertical)
        self.part5_Slider.setInvertedAppearance(True)
        self.part5_Slider.setObjectName("part5_Slider")
        self.Part_5 = QtWidgets.QLabel(self.centralwidget)
        self.Part_5.setGeometry(QtCore.QRect(1125, 110, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Part_5.setFont(font)
        self.Part_5.setObjectName("Part_5")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1110, 10, 16, 111))
        self.line_4.setMidLineWidth(0)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.Female_Button = QtWidgets.QRadioButton(self.centralwidget)
        self.Female_Button.setGeometry(QtCore.QRect(100, 85, 89, 16))
        self.Female_Button.setChecked(True)
        self.Female_Button.setObjectName("Female_Button")
        self.Man_Button = QtWidgets.QRadioButton(self.centralwidget)
        self.Man_Button.setGeometry(QtCore.QRect(100, 105, 89, 16))
        self.Man_Button.setChecked(False)
        self.Man_Button.setObjectName("Man_Button")
        self.Sex_label = QtWidgets.QLabel(self.centralwidget)
        self.Sex_label.setGeometry(QtCore.QRect(20, 82, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Sex_label.setFont(font)
        self.Sex_label.setObjectName("Sex_label")
        SketchGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SketchGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1192, 23))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        SketchGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SketchGUI)
        self.statusbar.setObjectName("statusbar")
        SketchGUI.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(SketchGUI)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtWidgets.QAction(SketchGUI)
        self.actionQuit.setObjectName("actionQuit")
        self.menuMenu.addAction(self.actionSave)
        self.menuMenu.addAction(self.actionQuit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(SketchGUI)
        QtCore.QMetaObject.connectSlotsByName(SketchGUI)
        
        self.Undo_Button.hide()
        self.brush_label.hide()
        self.Erase_label.hide()
        self.BrushSize.hide()
        self.EraseSize.hide()
        self.BrushNum_label.hide()
        self.EraserNum_label.hide()
        self.bar_num.hide()
        self.bar_num_2.hide()
        self.bar_num_3.hide()
        self.bar_num_4.hide()
        
        self.Part_0.hide()
        self.Part_1.hide()
        self.Part_2.hide()
        self.Part_3.hide()
        self.Part_4.hide()
        self.Part_5.hide()
        
        self.part0_Slider.hide()
        self.part1_Slider.hide()
        self.part2_Slider.hide()
        self.part3_Slider.hide()
        self.part4_Slider.hide()
        self.part5_Slider.hide()
        
        
        
    def retranslateUi(self, SketchGUI):
        _translate = QtCore.QCoreApplication.translate
        SketchGUI.setWindowTitle(_translate("SketchGUI", "Tái tạo từ nét phác thảo"))
        self.drawing_label.setText(_translate("SketchGUI", "Ảnh phác thảo"))
        self.sketch_label.setText(_translate("SketchGUI", "Ảnh tái tạo"))
        self.Clear_Button.setText(_translate("SketchGUI", "Xóa"))
        self.Eraser_Button.setText(_translate("SketchGUI", "Tẩy"))
        self.brush_label.setText(_translate("SketchGUI", "Brush Size"))
        self.Erase_label.setText(_translate("SketchGUI", "Eraser Size"))
        self.Undo_Button.setText(_translate("SketchGUI", "Undo"))
        self.BrushNum_label.setText(_translate("SketchGUI", "3"))
        self.EraserNum_label.setText(_translate("SketchGUI", "3"))
        self.Brush_Button.setText(_translate("SketchGUI", "Vẽ"))
        self.Load_Button.setText(_translate("SketchGUI", "Tải"))
        self.bar_num.setText(_translate("SketchGUI", "1"))
        self.bar_num_2.setText(_translate("SketchGUI", "3"))
        self.bar_num_3.setText(_translate("SketchGUI", "5"))
        self.bar_num_4.setText(_translate("SketchGUI", "7"))
        self.Convert_Sketch.setText(_translate("SketchGUI", "Tái tạo"))
        self.RealTime_checkBox.setText(_translate("SketchGUI", "Tự động"))
        self.Save_Button.setText(_translate("SketchGUI", "Lưu"))
        self.Part_0.setText(_translate("SketchGUI", "eyeL"))
        self.Part_1.setText(_translate("SketchGUI", " eyeR"))
        self.Part_2.setText(_translate("SketchGUI", "Nose"))
        self.Part_3.setText(_translate("SketchGUI", "Mouth"))
        self.Part_4.setText(_translate("SketchGUI", "Others"))
        self.Shadow_checkBox.setText(_translate("SketchGUI", "Bóng"))
        self.Part_5.setText(_translate("SketchGUI", "ALL"))
        self.Female_Button.setText(_translate("SketchGUI", "Nữ"))
        self.Man_Button.setText(_translate("SketchGUI", "Nam"))
        self.Sex_label.setText(_translate("SketchGUI", "Giới tính"))
        self.menuMenu.setTitle(_translate("SketchGUI", "Menu"))
        self.actionSave.setText(_translate("SketchGUI", "Lưu"))
        self.actionQuit.setText(_translate("SketchGUI", "Thoát"))