import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import cv2 as cv
import numpy as np
from PIL import Image,ImageOps
import pydicom as dcm
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
class MatplotlibCanvas(FigureCanvasQTAgg):
	def __init__(self,parent=None, dpi = 120):
		fig = Figure(dpi = dpi)
		self.axes = fig.add_subplot(111)
		super(MatplotlibCanvas,self).__init__(fig)
		fig.tight_layout()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 826)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 50, 861, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.imageLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.imageLayout.setContentsMargins(0, 0, 0, 0)
        self.imageLayout.setObjectName("imageLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.imageLayout.addItem(spacerItem)
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setGeometry(QtCore.QRect(60, 560, 93, 28))
        self.open_button.setObjectName("open_button")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(60, 600, 93, 28))
        self.exit_button.setObjectName("exit_button")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(310, 560, 501, 171))
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 10, 861, 31))
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
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.open_button.clicked.connect(self.getFile)
        self.exit_button.clicked.connect(sys.exit)

        self.canvas = MatplotlibCanvas(self)
        self.plt = self.canvas.axes

        self.hideModalityInfo()

    def getFile(self):
        filename = QFileDialog.getOpenFileName()[0]
        #print("File :", filename)
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
        print(img.mode)
        if img.mode=='L':
            self.plt.imshow(img,cmap='gray')
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
        if img.mode=='L':
            self.channels_status.setText('Grayscale')
            self.bit_depth_status.setText(str(img.bits*1))
        elif img.mode=='RGB':
            self.channels_status.setText('RGB')
            self.bit_depth_status.setText(str(img.bits*3))
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Task 1 - Image Viewer"))
        self.open_button.setText(_translate("MainWindow", "Open"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.height.setText(_translate("MainWindow", "Height:"))
        self.patient_age.setText(_translate("MainWindow", "Patient Age:"))
        self.patient_name.setText(_translate("MainWindow", "Patient Name:"))
        self.modality.setText(_translate("MainWindow", "Modality:"))
        self.channels.setText(_translate("MainWindow", "Colors:"))
        self.width.setText(_translate("MainWindow", "Width:"))
        self.Bit_Depth.setText(_translate("MainWindow", "Bit Depth:"))
        self.pixels.setText(_translate("MainWindow", "Total Pixels:"))
        self.totla_bits.setText(_translate("MainWindow", "Total Bits"))
        self.File_label.setText(_translate("MainWindow", "No File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
