import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import cv2 as cv
import numpy as np
from PIL import Image,ImageOps
import pydicom as dcm
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import pyautogui
import math
from PyQt5.QtGui import QImage,QPixmap
class MatplotlibCanvas(FigureCanvasQTAgg):
	def __init__(self,parent=None,figsize=(8,8)):
		fig = Figure(figsize=figsize)
		self.axes = fig.add_subplot(111)
		super(MatplotlibCanvas,self).__init__(fig)
		fig.tight_layout()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1114, 884)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.viewer_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.viewer_tabs.setGeometry(QtCore.QRect(10, 10, 1081, 821))
        self.viewer_tabs.setObjectName("viewer_tabs")
        self.image_tab = QtWidgets.QWidget()
        self.image_tab.setObjectName("image_tab")
        self.open_button = QtWidgets.QPushButton(self.image_tab)
        self.open_button.setGeometry(QtCore.QRect(30, 610, 111, 71))
        self.open_button.setObjectName("open_button")
        self.exit_button = QtWidgets.QPushButton(self.image_tab)
        self.exit_button.setGeometry(QtCore.QRect(30, 690, 111, 61))
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.image_tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 20, 861, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.File_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.File_label.setFont(font)
        self.File_label.setObjectName("File_label")
        self.horizontalLayout.addWidget(self.File_label)
        self.filename_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filename_label.setFont(font)
        self.filename_label.setText("")
        self.filename_label.setObjectName("filename_label")
        self.horizontalLayout.addWidget(self.filename_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.image_tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 60, 861, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.imageLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.imageLayout.setContentsMargins(0, 0, 0, 0)
        self.imageLayout.setObjectName("imageLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.imageLayout.addItem(spacerItem1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.image_tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(290, 570, 421, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.height = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.height.setFont(font)
        self.height.setObjectName("height")
        self.gridLayout.addWidget(self.height, 2, 0, 1, 1)
        self.channels_status = QtWidgets.QLabel(self.gridLayoutWidget)
        self.channels_status.setText("")
        self.channels_status.setObjectName("channels_status")
        self.gridLayout.addWidget(self.channels_status, 5, 2, 1, 1)
        self.pixels_status = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pixels_status.setText("")
        self.pixels_status.setObjectName("pixels_status")
        self.gridLayout.addWidget(self.pixels_status, 6, 2, 1, 1)
        self.patient_age = QtWidgets.QLabel(self.gridLayoutWidget)
        self.patient_age.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.patient_age.setFont(font)
        self.patient_age.setObjectName("patient_age")
        self.gridLayout.addWidget(self.patient_age, 3, 4, 1, 1)
        self.modality_status = QtWidgets.QLabel(self.gridLayoutWidget)
        self.modality_status.setText("")
        self.modality_status.setObjectName("modality_status")
        self.gridLayout.addWidget(self.modality_status, 1, 5, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.patient_name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.patient_name.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.patient_name.setFont(font)
        self.patient_name.setObjectName("patient_name")
        self.gridLayout_2.addWidget(self.patient_name, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 4, 1, 1)
        self.modality = QtWidgets.QLabel(self.gridLayoutWidget)
        self.modality.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.modality.setFont(font)
        self.modality.setObjectName("modality")
        self.gridLayout.addWidget(self.modality, 1, 4, 1, 1)
        self.name_status = QtWidgets.QLabel(self.gridLayoutWidget)
        self.name_status.setText("")
        self.name_status.setObjectName("name_status")
        self.gridLayout.addWidget(self.name_status, 2, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        self.height_status = QtWidgets.QLabel(self.gridLayoutWidget)
        self.height_status.setText("")
        self.height_status.setObjectName("height_status")
        self.gridLayout.addWidget(self.height_status, 2, 2, 1, 1)
        self.channels = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.channels.setFont(font)
        self.channels.setObjectName("channels")
        self.gridLayout.addWidget(self.channels, 5, 0, 1, 1)
        self.width = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.width.setFont(font)
        self.width.setObjectName("width")
        self.gridLayout.addWidget(self.width, 1, 0, 1, 1)
        self.width_status = QtWidgets.QLabel(self.gridLayoutWidget)
        self.width_status.setText("")
        self.width_status.setObjectName("width_status")
        self.gridLayout.addWidget(self.width_status, 1, 2, 1, 1)
        self.Bit_Depth = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Bit_Depth.setFont(font)
        self.Bit_Depth.setObjectName("Bit_Depth")
        self.gridLayout.addWidget(self.Bit_Depth, 3, 0, 1, 1)
        self.pixels = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pixels.setFont(font)
        self.pixels.setObjectName("pixels")
        self.gridLayout.addWidget(self.pixels, 6, 0, 1, 1)
        self.bit_depth_status = QtWidgets.QLabel(self.gridLayoutWidget)
        self.bit_depth_status.setText("")
        self.bit_depth_status.setObjectName("bit_depth_status")
        self.gridLayout.addWidget(self.bit_depth_status, 3, 2, 1, 1)
        self.age_status = QtWidgets.QLabel(self.gridLayoutWidget)
        self.age_status.setText("")
        self.age_status.setObjectName("age_status")
        self.gridLayout.addWidget(self.age_status, 3, 5, 1, 1)
        self.totla_bits = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.totla_bits.setFont(font)
        self.totla_bits.setObjectName("totla_bits")
        self.gridLayout.addWidget(self.totla_bits, 7, 0, 1, 1)
        self.bits_status = QtWidgets.QLabel(self.gridLayoutWidget)
        self.bits_status.setText("")
        self.bits_status.setObjectName("bits_status")
        self.gridLayout.addWidget(self.bits_status, 7, 2, 1, 1)
        self.spare2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.spare2.setText("")
        self.spare2.setObjectName("spare2")
        self.gridLayout.addWidget(self.spare2, 5, 4, 1, 1)
        self.spare2_status = QtWidgets.QLabel(self.gridLayoutWidget)
        self.spare2_status.setText("")
        self.spare2_status.setObjectName("spare2_status")
        self.gridLayout.addWidget(self.spare2_status, 5, 5, 1, 1)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.image_tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(830, 690, 231, 88))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.zooming_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.zooming_layout.setContentsMargins(0, 0, 0, 0)
        self.zooming_layout.setObjectName("zooming_layout")
        self.zoom_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.zoom_label.setFont(font)
        self.zoom_label.setAlignment(QtCore.Qt.AlignCenter)
        self.zoom_label.setObjectName("zoom_label")
        self.zooming_layout.addWidget(self.zoom_label)
        self.lineEdit_for_zooming = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_for_zooming.setObjectName("lineEdit_for_zooming")
        self.zooming_layout.addWidget(self.lineEdit_for_zooming)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton.setObjectName("pushButton")
        self.zooming_layout.addWidget(self.pushButton)
        self.viewer_tabs.addTab(self.image_tab, "")
        self.nn_tab = QtWidgets.QWidget()
        self.nn_tab.setObjectName("nn_tab")
        self.label = QtWidgets.QLabel(self.nn_tab)
        self.label.setGeometry(QtCore.QRect(380, -10, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.nn_tab)
        self.scrollArea.setGeometry(QtCore.QRect(10, 40, 1051, 591))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 10000, 10000))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(10000, 10000))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(1059, 729))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 1000000, 1000000))
        self.label_3.setMinimumSize(QtCore.QSize(1000000, 1000000))
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.nn_tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(430, 670, 187, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.zoomW = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.zoomW.setFont(font)
        self.zoomW.setObjectName("zoomW")
        self.gridLayout_3.addWidget(self.zoomW, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 2, 1, 1)
        self.zoomH_status_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.zoomH_status_2.setText("")
        self.zoomH_status_2.setObjectName("zoomH_status_2")
        self.gridLayout_3.addWidget(self.zoomH_status_2, 0, 1, 1, 1)
        self.zoomH_status = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.zoomH_status.setText("")
        self.zoomH_status.setObjectName("zoomH_status")
        self.gridLayout_3.addWidget(self.zoomH_status, 1, 1, 1, 1)
        self.zoomH = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.zoomH.setFont(font)
        self.zoomH.setObjectName("zoomH")
        self.gridLayout_3.addWidget(self.zoomH, 1, 0, 1, 1)
        self.zoomP = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.zoomP.setFont(font)
        self.zoomP.setObjectName("zoomP")
        self.gridLayout_3.addWidget(self.zoomP, 2, 0, 1, 1)
        self.zoomP_status = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.zoomP_status.setText("")
        self.zoomP_status.setObjectName("zoomP_status")
        self.gridLayout_3.addWidget(self.zoomP_status, 2, 1, 1, 1)
        self.viewer_tabs.addTab(self.nn_tab, "")
        self.LI_tab = QtWidgets.QWidget()
        self.LI_tab.setObjectName("LI_tab")
        self.linear_interpolation_label = QtWidgets.QLabel(self.LI_tab)
        self.linear_interpolation_label.setGeometry(QtCore.QRect(390, -10, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.linear_interpolation_label.setFont(font)
        self.linear_interpolation_label.setAlignment(QtCore.Qt.AlignCenter)
        self.linear_interpolation_label.setObjectName("linear_interpolation_label")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.LI_tab)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 40, 1061, 601))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 10000, 10000))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(10000, 10000))
        self.scrollAreaWidgetContents_2.setMaximumSize(QtCore.QSize(1059, 729))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 1000000, 1000000))
        self.label_4.setMinimumSize(QtCore.QSize(1000000, 1000000))
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.LI_tab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(430, 670, 187, 80))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.zoomW_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.zoomW_2.setFont(font)
        self.zoomW_2.setObjectName("zoomW_2")
        self.gridLayout_4.addWidget(self.zoomW_2, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 2, 1, 1)
        self.zoomH_status_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.zoomH_status_3.setText("")
        self.zoomH_status_3.setObjectName("zoomH_status_3")
        self.gridLayout_4.addWidget(self.zoomH_status_3, 0, 1, 1, 1)
        self.zoomH_status_4 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.zoomH_status_4.setText("")
        self.zoomH_status_4.setObjectName("zoomH_status_4")
        self.gridLayout_4.addWidget(self.zoomH_status_4, 1, 1, 1, 1)
        self.zoomH_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.zoomH_2.setFont(font)
        self.zoomH_2.setObjectName("zoomH_2")
        self.gridLayout_4.addWidget(self.zoomH_2, 1, 0, 1, 1)
        self.zoomP_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.zoomP_2.setFont(font)
        self.zoomP_2.setObjectName("zoomP_2")
        self.gridLayout_4.addWidget(self.zoomP_2, 2, 0, 1, 1)
        self.zoomP_status_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.zoomP_status_2.setText("")
        self.zoomP_status_2.setObjectName("zoomP_status_2")
        self.gridLayout_4.addWidget(self.zoomP_status_2, 2, 1, 1, 1)
        self.viewer_tabs.addTab(self.LI_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1114, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.viewer_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.open_button.clicked.connect(self.getFile)
        self.exit_button.clicked.connect(sys.exit)
        self.pushButton.clicked.connect(self.zoom)

        self.canvas = MatplotlibCanvas(self)
        self.plt = self.canvas.axes
        # self.canvas_Neighbor = MatplotlibCanvas(self, (20, 20))
        # self.plt_Neighbor = self.canvas_Neighbor.axes
        # self.canvas_Linear = MatplotlibCanvas(self, (20, 20))
        # self.plt_Linear = self.canvas_Linear.axes

        self.File_label.setText('')
        self.hideModalityInfo()
        self.zmImg = 0

    def getFile(self):
        self.filename = QFileDialog.getOpenFileName()[0]
        # print("File :", filename)
        if self.filename != '':
            if '.dcm' in self.filename:
                self.getDCMFile(self.filename)
            else:
                self.getImage(self.filename)
        else:
            # print('No File')
            self.File_label.setText('No File')
            self.filename_label.hide()

    def getDCMFile(self, filename):
        try:
            img = dcm.dcmread(filename)
        except (Exception) as e:
            # print('Bad file:', filename)  # print out the names of corrupt files
            self.File_label.setText('Corrupted File')
            self.filename_label.hide()
            self.getFile()
        else:
            self.File_label.setText('File:')
            self.filename_label.show()
            self.filename_label.setText(filename)
            self.showLabels()
            self.dcm2jpg(filename)

    def getImage(self, filename):
        try:
            img = Image.open(filename)  # open the image file
            img.verify()  # verify that it is, in fact an image
        except (IOError, SyntaxError) as e:
            # print('Bad file:', filename)  # print out the names of corrupt files
            self.File_label.setText('Corrupted File')
            self.filename_label.hide()
            self.getFile()
        else:
            # print('No error')
            self.File_label.setText('File:')
            self.filename_label.show()
            self.filename_label.setText(filename)
            if '.bmp' in filename:
                img = Image.open(filename)
                self.hideModalityInfo()
                self.openImage(img)
                self.showBMPInfo(img, filename)
            else:
                img = Image.open(filename)
                self.showLabels()
                self.hideModalityInfo()
                self.openImage(img)
                self.showJPGInfo(img)

    def openImage(self, img):
        # image for zooming
        self.zmImg = img
        # add the matplotlib canva to the layout for the image to appear in
        self.imageLayout.addWidget(self.canvas)
        # clears axes
        self.canvas.axes.cla()
        # plot the image
        #print(img.mode)
        if img.mode == 'L':
            self.plt.imshow(img, cmap='gray')
        else:
            self.plt.imshow(img)

    def dcm2jpg(self, filename):
        # Read dicom file
        img = dcm.dcmread(filename)
        # show info
        self.showModalityInfo(img)
        # converting the dicom image to jpg image for display
        # extract the array containing the values of the pixels, float to not lose information after rescaling
        jpg_img = img.pixel_array.astype(float)
        # rescale the image to view
        # convert all negative pixels into 0
        # Normalize the values by dividing by the max then *255 -> values between 0 and 255
        # Image pixels values must be from 0 to 255
        rescaled_img = (np.maximum(jpg_img, 0) / jpg_img.max()) * 255.0
        # convert array to uint8 to remove noise and have a clear image (from float to integers (unsigned))
        jpg_img = np.uint8(rescaled_img)
        # Convert array to image
        jpg_img = Image.fromarray(jpg_img)
        # plot image
        self.openImage(jpg_img)

    def showModalityInfo(self, img):
        # Show labels for the dicom file
        self.modality.show()
        self.patient_name.show()
        self.patient_age.show()
        self.modality_status.show()
        self.age_status.show()
        self.name_status.show()
        # self.spare2.show()
        # self.spare2_status.show()
        # show the patient info
        self.modality_status.setText(str(img.Modality))
        self.age_status.setText(str(img.PatientAge))
        self.name_status.setText(str(img.PatientName))
        # self.spare2.setText(str(img.BodyPartExamined))
        # Show the image info
        self.width_status.setText(str(img.Rows))
        self.height_status.setText(str(img.Columns))
        self.bit_depth_status.setText(str(img.BitsStored))
        self.pixels_status.setText(str(img.Rows * img.Columns))
        self.bits_status.setText(str(img.Rows * img.Columns * int(img.BitsStored)))
        c = img.SamplesPerPixel
        if c == 3:
            self.channels_status.setText('RGB')
        elif c == 1:
            self.channels_status.setText('Grayscale')

    def hideModalityInfo(self):
        # hide dicom labels if not used
        self.modality.hide()
        self.patient_name.hide()
        self.patient_age.hide()
        self.modality_status.hide()
        self.age_status.hide()
        self.name_status.hide()
        # self.spare2.hide()
        # self.spare2_status.hide()

    def showJPGInfo(self, img):
        # Show image info
        w, h = img.size
        self.width_status.setText(str(w))
        self.height_status.setText(str(h))
        if img.mode == 'L':
            self.channels_status.setText('Grayscale')
            self.bit_depth_status.setText(str(img.bits * 1))
            self.bits_status.setText(str(h * w * int(img.bits)))
        elif img.mode == 'RGB':
            self.channels_status.setText('RGB')
            self.bit_depth_status.setText(str(img.bits * 3))
            self.bits_status.setText(str(h * w * int(img.bits) * 3))
        self.pixels_status.setText(str(h * w))

    def showBMPInfo(self, img, filename):
        w, h = img.size
        # Show Info
        self.width_status.setText(str(w))
        self.height_status.setText(str(h))
        self.pixels_status.setText(str(h * w))
        self.channels_status.setText(str(img.mode))
        # self.bit_depth_status.setText(str(img.type))
        # Hide unused labels
        self.bit_depth_status.hide()
        self.bits_status.hide()
        self.Bit_Depth.hide()
        self.totla_bits.hide()
        # print(img)

    def showLabels(self):
        # show labels hidden in bmp
        self.bit_depth_status.show()
        self.bits_status.show()
        self.Bit_Depth.show()
        self.totla_bits.show()

    def zoom(self):
        self.label_3.setPixmap(QtGui.QPixmap())
        factor = self.lineEdit_for_zooming.text()
        if factor == '' or self.zmImg == 0:
            self.File_label.setText('Zooming factor or image missing')
            self.filename_label.clear()
        elif float(factor) <= 0:
            self.File_label.setText('Inappropriate zooming factor')
            self.filename_label.clear()
        else:
            factor = float(factor)
            self.File_label.setText('File:')
            self.filename_label.setText(self.filename)

            NNimg = self.NearestNeighbor(factor,self.zmImg)
            self.zoomH_status_2.setText(str(NNimg.shape[1]))
            self.zoomH_status.setText(str(NNimg.shape[0]))
            self.zoomP_status.setText(str(NNimg.shape[0]*NNimg.shape[1]))
            print('Nearest Neighbour Done')
            LIimg = self.BilinearInterpolation(factor,self.zmImg)
            self.zoomH_status_4.setText(str(LIimg.shape[0]))
            self.zoomH_status_3.setText(str(LIimg.shape[1]))
            self.zoomP_status_2.setText(str(LIimg.shape[0] * LIimg.shape[1]))
            print('Bilinear Done')
            self.displayZoomedImg(self.label_3, NNimg)
            self.displayZoomedImg(self.label_4, LIimg)

    def NearestNeighbor(self, factor,img):
        print('Nearest Neighbour')
        if img.mode == 'L':
            img = cv.cvtColor(np.array(img), cv.COLOR_GRAY2BGR)
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        else:
            img = cv.cvtColor(np.array(img), cv.COLOR_RGB2GRAY)

        w, h = img.shape[:2]

        xNew = math.ceil(w * factor)
        yNew = math.ceil(h * factor)

        imgNew = np.zeros([xNew, yNew])
        for i in range(xNew - 1):
            for j in range(yNew - 1):
                imgNew[i, j] = img[math.floor(i / factor), math.floor(j / factor)]
        imgNew = imgNew.astype('uint8')
        return imgNew

    def BilinearInterpolation(self, factor,img):
        print('Bilinear')
        if img.mode == 'L':
            img = cv.cvtColor(np.array(img), cv.COLOR_GRAY2BGR)
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        else:
            img = cv.cvtColor(np.array(img), cv.COLOR_RGB2GRAY)

        w, h = img.shape
        dimension = (math.ceil(w * factor), math.ceil(h * factor))
        scale = 1 / factor

        imgNew = np.zeros((math.ceil(w * factor), math.ceil(h * factor)))
        for i in range(dimension[0] - 1):
            for j in range(dimension[1] - 1):
                # project the unknown point to the input image
                x = i * scale
                y = j * scale
                # coordinate values of the 4 surrounding pixels
                # the -2 is to prevent crossing the borders of the image (-2+1=-1) alright with zero-indexed ,else:
                x1 = min(int(x), w - 2)
                x2 = x1 + 1
                y1 = min(int(y), h - 2)
                y2 = y1 + 1
                # print('x,x1,x2:')
                # print(x, x1, x2)
                # print('y,y1,y2')
                # print(y, y1, y2)
                # distance between the right neighbor and the left neighbor
                delta_x = x2 - x1
                # distance between the blue and yellow stars
                delta_y = y2 - y1
                # Values of the 4 surrounding pixels
                # Bottom left
                q11 = img[int(x1), int(y1)]
                # Upper left
                q12 = img[int(x1), int(y2)]
                # Upper Right
                q21 = img[int(x2), int(y1)]
                # Bottom right
                q22 = img[int(x2), int(y2)]
                # The 4 terms of the pixel equation
                a = (q11 * (x2 - x) * (y2 - y)) / (delta_x * delta_y)
                b = (q21 * (x - x1) * (y2 - y)) / (delta_x * delta_y)
                c = (q12 * (x2 - x) * (y - y1)) / (delta_x * delta_y)
                d = (q22 * (x - x1) * (y - y1)) / (delta_x * delta_y)

                pixel = a + b + c + d

                imgNew[i, j] = pixel

        imgNew = imgNew.astype(np.uint8)

        return imgNew

    def displayZoomedImg(self, widget, img):
        qformat = QImage.Format_Grayscale8
        # print('qformat done')
        img = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        # print('QImage generated')
        widget.setPixmap(QPixmap.fromImage(img))
        print('Image addded to widget')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_button.setText(_translate("MainWindow", "Open"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.File_label.setText(_translate("MainWindow", "File"))
        self.height.setText(_translate("MainWindow", "Height:"))
        self.patient_age.setText(_translate("MainWindow", "Patient Age:"))
        self.patient_name.setText(_translate("MainWindow", "Patient Name:"))
        self.modality.setText(_translate("MainWindow", "Modality:"))
        self.channels.setText(_translate("MainWindow", "Channels:"))
        self.width.setText(_translate("MainWindow", "Width:"))
        self.Bit_Depth.setText(_translate("MainWindow", "Bit Depth:"))
        self.pixels.setText(_translate("MainWindow", "Total Pixels:"))
        self.totla_bits.setText(_translate("MainWindow", "Total Bits"))
        self.zoom_label.setText(_translate("MainWindow", "Zooming Factor"))
        self.pushButton.setText(_translate("MainWindow", "Zoom"))
        self.viewer_tabs.setTabText(self.viewer_tabs.indexOf(self.image_tab), _translate("MainWindow", "Image Viewer"))
        self.label.setText(_translate("MainWindow", ""))
        self.zoomW.setText(_translate("MainWindow", "Width:"))
        self.zoomH.setText(_translate("MainWindow", "Height:"))
        self.zoomP.setText(_translate("MainWindow", "Total Pixels:"))
        self.viewer_tabs.setTabText(self.viewer_tabs.indexOf(self.nn_tab), _translate("MainWindow", "Nearest Neighbor Interpolation"))
        self.linear_interpolation_label.setText(_translate("MainWindow", ""))
        self.zoomW_2.setText(_translate("MainWindow", "Width:"))
        self.zoomH_2.setText(_translate("MainWindow", "Height:"))
        self.zoomP_2.setText(_translate("MainWindow", "Total Pixels:"))
        self.viewer_tabs.setTabText(self.viewer_tabs.indexOf(self.LI_tab), _translate("MainWindow", "Bilinear Interpolation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
