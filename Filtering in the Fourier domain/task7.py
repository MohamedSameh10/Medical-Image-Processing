from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import numpy as np
from PIL import Image
import pydicom as dcm
import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
class MatplotlibCanvas(FigureCanvasQTAgg):
	def __init__(self,parent=None, dpi = 120):
		fig = Figure((4,4),dpi = dpi)
		self.axes = fig.add_subplot(111)
		super(MatplotlibCanvas,self).__init__(fig)
		fig.tight_layout()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 829)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1091, 771))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 0, 921, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.File_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.File_label.setFont(font)
        self.File_label.setObjectName("File_label")
        self.horizontalLayout.addWidget(self.File_label)
        self.filename_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.filename_label.setText("")
        self.filename_label.setObjectName("filename_label")
        self.horizontalLayout.addWidget(self.filename_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 40, 961, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.imageLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.imageLayout.setContentsMargins(0, 0, 0, 0)
        self.imageLayout.setObjectName("imageLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.imageLayout.addItem(spacerItem1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(280, 560, 501, 171))
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
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab_1)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(830, 560, 221, 161))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.kernelLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.kernelLayout.setContentsMargins(0, 0, 0, 0)
        self.kernelLayout.setObjectName("kernelLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.kernelLabel = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.kernelLabel.setFont(font)
        self.kernelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.kernelLabel.setObjectName("kernelLabel")
        self.horizontalLayout_3.addWidget(self.kernelLabel)
        self.kernellineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.kernellineEdit.setObjectName("kernellineEdit")
        self.horizontalLayout_3.addWidget(self.kernellineEdit)
        self.kernelLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.factorLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.factorLineEdit.setObjectName("factorLineEdit")
        self.horizontalLayout_2.addWidget(self.factorLineEdit)
        self.kernelLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton.setObjectName("pushButton")
        self.kernelLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_1)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(30, 580, 201, 131))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.open_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.open_button.setObjectName("open_button")
        self.verticalLayout.addWidget(self.open_button)
        self.exit_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout.addWidget(self.exit_button)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(610, 170, 471, 381))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.spatialFourierLayout = QtWidgets.QVBoxLayout()
        self.spatialFourierLayout.setObjectName("spatialFourierLayout")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.spatialFourierLayout.addItem(spacerItem3)
        self.gridLayout_4.addLayout(self.spatialFourierLayout, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 1, 1, 1)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(13, 20, 581, 721))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.fourierFilterLayout = QtWidgets.QVBoxLayout()
        self.fourierFilterLayout.setObjectName("fourierFilterLayout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.fourierFilterLayout.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.fourierFilterLayout)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.spaitalLayout = QtWidgets.QVBoxLayout()
        self.spaitalLayout.setObjectName("spaitalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.spaitalLayout.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.spaitalLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 100, 1051, 531))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.beforeLayout = QtWidgets.QVBoxLayout()
        self.beforeLayout.setObjectName("beforeLayout")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.beforeLayout.addItem(spacerItem6)
        self.gridLayout_3.addLayout(self.beforeLayout, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 30, 281, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.canvas = MatplotlibCanvas(self)
        self.plt = self.canvas.axes
        self.canvas1 = MatplotlibCanvas(self)
        self.plt1 = self.canvas1.axes
        self.canvas2 = MatplotlibCanvas(self)
        self.plt2 = self.canvas2.axes
        self.canvas3 = MatplotlibCanvas(self)
        self.plt3 = self.canvas3.axes
        self.canvas4 = MatplotlibCanvas(self)
        self.plt4 = self.canvas4.axes
        self.canvas5 = MatplotlibCanvas(self)
        self.plt5 = self.canvas5.axes
        self.Img = 0
        self.factorLineEdit.hide()
        self.label.hide()
        self.open_button.clicked.connect(self.getFile)
        self.exit_button.clicked.connect(sys.exit)
        self.pushButton_2.clicked.connect(self.removePeriodic)
        self.pushButton.clicked.connect(self.filterImage)

        self.hideModalityInfo()

    def getFile(self):
        filename = QFileDialog.getOpenFileName()[0]
        # print("File :", filename)
        if filename != '':
            if '.dcm' in filename:
                self.getDCMFile(filename)
            else:
                self.getImage(filename)
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
        # add the matplotlib canva to the layout for the image to appear in
        self.imageLayout.addWidget(self.canvas)
        # clears axes
        self.canvas.axes.cla()
        # plot the image
        self.Img = img
        if img.mode == 'L':
            self.plt.imshow(img, cmap='gray')
            self.File_label.setText('File: ')
        else:
            self.plt.imshow(img)
            self.File_label.setText('File: ')

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
        elif img.mode == 'RGB':
            self.channels_status.setText('RGB')
            self.bit_depth_status.setText(str(img.bits * 3))
        self.pixels_status.setText(str(h * w))
        self.bits_status.setText(str(h * w * int(img.bits)))

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

    def convert2Graysscale(self, img):
        im1 = img.convert('L')
        return im1

    def filterImage(self):
        if self.Img == 0:
            self.File_label.setText('Choose image to be filtered')
            self.filename_label.setText('')
        elif self.kernellineEdit.text() == '':
            self.File_label.setText('kernel size missing')
            self.filename_label.setText('')
        # elif self.factorLineEdit.text() == '':
        # self.File_label.setText('factor k missing')
        # self.filename_label.setText('')
        elif int(self.kernellineEdit.text()) % 2 == 0:
            self.File_label.setText('kernel size not odd')
            self.filename_label.setText('')
        else:
            try:
                img = self.Img.copy()
                # create canvas for the enhanced image
                self.fourierFilterLayout.addWidget(self.canvas1)
                # clear axes
                self.canvas1.axes.cla()
                # get the user values
                kernelSize = int(self.kernellineEdit.text())
                imgArray = np.asarray(img)
                # create the kernel
                kernel = np.ones((kernelSize, kernelSize))
                kernel = kernel / (kernelSize ** 2)
                kernel = self.pad(kernel, kernelSize, imgArray)

                if img.mode == 'L':
                    kernel = np.fft.ifftshift(kernel)
                    multiplied = self.FFT(imgArray) * self.FFT(kernel)
                    filtered = np.real((np.fft.ifft2(multiplied)))
                    # print(filtered)
                    # filtered = np.uint8(filtered)
                    # filtered = Image.fromarray(filtered)
                    #print(filtered.shape[0], filtered.shape[1])
                    self.plt1.imshow(filtered, cmap='gray')
                    self.filterImage2(filtered)
                else:
                    # imgArray = self.FFT(imgArray)
                    multiplied = np.zeros_like(imgArray, dtype=complex)
                    imgArrayfft = np.zeros_like(imgArray, dtype=complex)
                    for i in range(imgArray.shape[2]):
                        imgArrayfft[:, :, i] = np.fft.fftshift(np.fft.fft2(imgArray[:, :, i]))
                    for i in range(imgArrayfft.shape[2]):
                        multiplied[:, :, i] = imgArrayfft[:, :, i] * np.fft.fftshift(np.fft.fft2(kernel))
                    # print('multiplied')
                    filtered = np.zeros_like(multiplied, dtype=complex)
                    for i in range(multiplied.shape[2]):
                        filtered[:, :, i] = np.abs(np.fft.ifftshift(np.fft.ifft2(multiplied[:, :, i])))
                    filtered = np.uint8(filtered)
                    filtered = Image.fromarray(filtered)

                    self.plt1.imshow(filtered)
                    self.filterImage2(filtered)

            except (Exception) as e:
                self.File_label.setText(str(e))
                self.filename_label.setText('')

    def filterImage2(self, filtered2):
        if self.Img == 0:
            self.File_label.setText('Choose image to be filtered')
            self.filename_label.setText('')
        elif self.kernellineEdit.text() == '':
            self.File_label.setText('kernel size missing')
            self.filename_label.setText('')
        # elif self.factorLineEdit.text() == '':
        # self.File_label.setText('factor k missing')
        # self.filename_label.setText('')
        elif int(self.kernellineEdit.text()) % 2 == 0:
            self.File_label.setText('kernel size not odd')
            self.filename_label.setText('')
        else:
            try:
                img = self.Img.copy()

                # create canvas for the enhanced image
                self.spatialFourierLayout.addWidget(self.canvas2)
                self.spaitalLayout.addWidget(self.canvas3)
                # clear axes
                self.canvas2.axes.cla()
                self.canvas3.axes.cla()
                # get the user values
                kernelSize = int(self.kernellineEdit.text())
                # factorK = int(self.factorLineEdit.text())
                imgArray = np.asarray(img)
                if img.mode == 'RGB':
                    imgArray = np.average(imgArray, axis=2)
                    filtered2 = np.average(filtered2, axis=2)
                # create the kernel
                kernel = np.ones((kernelSize, kernelSize))
                kernel = kernel / (kernelSize ** 2)
                # perform convolution
                convolvedImg = self.convolution(img, kernel, kernelSize)
                #print(convolvedImg.shape[0], convolvedImg.shape[1])
                # print('convolved')
                # subtract blurred image from original multiplied by a factor K
                # unsharpedMask = (imgArray - convolvedImg)
                # add the mask to the original image
                # filtered = factorK * unsharpedMask + imgArray
                # normalize to 0-255
                # filtered = self.scalingFunction(filtered)
                spatial = np.uint8(convolvedImg)
                spatial = Image.fromarray(spatial)
                self.plt3.imshow(spatial, cmap='gray')
                filtered = filtered2 - convolvedImg
                #print(filtered.shape[0], filtered.shape[1])
                # convert image array to image
                filtered = np.uint8(filtered)
                filtered = Image.fromarray(filtered)
                # plot image
                self.plt2.imshow(filtered, cmap='gray')
            except (Exception) as e:
                self.File_label.setText('')
                self.filename_label.setText(str(e))

    def convolution(self, img, kernel, kernelSize):
        w, h = img.size
        imgArray = np.asarray(img)
        if img.mode == 'RGB':
            imgArray = np.average(imgArray, axis=2)
        imgArray = self.padding(imgArray, kernelSize)
        newImg = np.zeros((h, w))
        # print(img)
        # print(kernel)
        # convolve the kernel with the padded-image
        for i in range(h):
            for j in range(w):
                newImg[i, j] = np.sum(kernel * imgArray[i:i + kernelSize, j:j + kernelSize])
        # else:
        #
        #     imgArray = np.average(imgArray, axis=2)
        #     # paddedimg=np.zeros_like(imgArray)
        #     # for i in range(imgArray.shape[2]):
        #     #     paddedimg[:,:,i] = self.padding(imgArray[:,:,i], kernelSize)
        #     #paddedimg = self.padding2(imgArray, kernelSize)
        #     # #newImg = np.zeros_like(imgArray)
        #     #
        #     # # convolve the kernel with the padded-image
        #     # for k in range(imgArray.shape[2]):
        #     #     for i in range(h):
        #     #         for j in range(w):
        #     #             newImg[i, j, k] = np.sum(kernel * paddedimg[i:i + kernelSize, j:j + kernelSize, k])
        #     imgArray = self.padding(imgArray, kernelSize)
        #     newImg = np.zeros((h, w))
        #
        #     # print(kernel)
        #     # convolve the kernel with the padded-image
        #     for i in range(h):
        #         for j in range(w):
        #             newImg[i, j] = np.sum(kernel * imgArray[i:i + kernelSize, j:j + kernelSize])

        return newImg

    def padding(self, img, kernelSize):
        w, h = img.shape
        type = 'Zero'
        padImg = np.zeros((w + kernelSize - 1, h + kernelSize - 1))
        if type == 'Zero':
            padImg[(kernelSize // 2):-(kernelSize // 2), (kernelSize // 2):-(kernelSize // 2)] = img
        elif type == 'Mirror':
            padImg = np.pad(img, (kernelSize // 2, kernelSize // 2), 'reflect')
            # padImg = np.pad(img, (kernelSize // 2, kernelSize // 2), 'constant')
        # elif type=='Replicate':

        return padImg

    def FFT(self, img):
        fft = np.fft.fft2(img)
        return fft

    def scalingFunction(self, array):
        # set the values of the image in the range of 0 to 255
        normalizedData = 255.0 * (array - np.min(array)) / (np.max(array) - np.min(array))
        # normalizedData=np.zeros_like(array)
        # for i in range(array.shape[2]):
        #     normalizedData[:,:,i] = 255.0 * (array[:,:,i] - np.min(array[:,:,i])) / (np.max(array[:,:,i]) - np.min(array[:,:,i]))
        return normalizedData

    def removePeriodic(self):
        img = Image.open('WhatsApp Image 2022-11-29 at 6.54.30 PM.jpeg')
        img = self.convert2Graysscale(img)

        self.beforeLayout.addWidget(self.canvas4)
        self.verticalLayout_4.addWidget(self.canvas5)
        self.canvas4.axes.cla()
        self.canvas5.axes.cla()

        self.plt4.imshow(img, cmap='gray')

        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)
        D0 = 15

        H1 = self.notch(f, D0, -38, 30)
        H2 = self.notch(f, D0, 42, 27)
        H3 = self.notch(f, D0, 80, 30)
        H4 = self.notch(f, D0, -82, 28)
        H = H1 * H2 * H3 * H4

        Gshift = fshift * H

        G = np.fft.ifftshift(Gshift)
        g = np.abs(np.fft.ifft2(G))

        im_new = np.uint8(g)
        im_new = Image.fromarray(im_new)

        self.plt5.imshow(im_new, cmap='gray')

    def removeSP(self, img):
        w, h = img.shape
        enhanced = img.copy()
        # median filter to remove salt and pepper
        for i in range(w):
            for j in range(h):
                filterArea = enhanced[i:i + 9, j:j + 9]
                enhanced[i][j] = np.median(filterArea)
        return enhanced

    def notch(self, f, D0, uk, vk):
        M, N = f.shape
        H = np.zeros((M, N))
        for u in range(M):
            for v in range(N):
                Dk = np.sqrt((u - M / 2 - uk) ** 2 + (v - N / 2 - vk) ** 2)
                Dk_ = np.sqrt((u - M / 2 + uk) ** 2 + (v - N / 2 + vk) ** 2)
                if Dk <= D0 or Dk_ <= D0:
                    H[u, v] = 0.0
                else:
                    H[u, v] = 1.0
        return H

    def pad(self, kernel, kernelSize, img):
        # image we want to match the kernel to
        w = img.shape[0]
        h = img.shape[1]
        # Padding amount
        w, h = (w - kernelSize, h - kernelSize)
        pad = np.pad(kernel, (((w + 1) // 2, w // 2), ((h + 1) // 2, h // 2)), 'constant')

        return pad

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.kernelLabel.setText(_translate("MainWindow", "Kernel Size"))
        self.label.setText(_translate("MainWindow", "K factor:"))
        self.pushButton.setText(_translate("MainWindow", "Filter"))
        self.open_button.setText(_translate("MainWindow", "Open"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Image"))
        self.label_3.setText(_translate("MainWindow", "Spatially filtered image - Fourier filtered image"))
        self.label_2.setText(_translate("MainWindow", "Fourier Domain Filtered Image"))
        self.label_4.setText(_translate("MainWindow", "Spaitally Filtered Image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Filtered Images"))
        self.label_5.setText(_translate("MainWindow", "Before"))
        self.label_6.setText(_translate("MainWindow", "After"))
        self.pushButton_2.setText(_translate("MainWindow", "Remove Noise"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Periodic Noise"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
