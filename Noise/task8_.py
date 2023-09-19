from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.widgets import RectangleSelector
class MatplotlibCanvas(FigureCanvasQTAgg):
	def __init__(self,parent=None, dpi = 120,w=4,h=4):
		fig = Figure((w,h),dpi = dpi)
		self.axes = fig.add_subplot(111)
		super(MatplotlibCanvas,self).__init__(fig)
		fig.tight_layout()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 829)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 1071, 671))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout_3, 3, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.gridLayout.addLayout(self.verticalLayout_4, 3, 0, 1, 1)
        self.imageLayout = QtWidgets.QVBoxLayout()
        self.imageLayout.setObjectName("imageLayout")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.imageLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.imageLayout, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 720, 371, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(510, 700, 571, 71))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 3, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 700, 101, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.open_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.open_button.setObjectName("open_button")
        self.verticalLayout.addWidget(self.open_button)
        self.exit_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout.addWidget(self.exit_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.canvas = MatplotlibCanvas(self,w=3,h=3)
        self.plt = self.canvas.axes
        self.canvas2 = MatplotlibCanvas(self,w=3,h=3)
        self.plt2 = self.canvas2.axes
        self.canvas3 = MatplotlibCanvas(self)
        self.plt3 = self.canvas3.axes
        self.canvas4 = MatplotlibCanvas(self)
        self.plt4 = self.canvas4.axes

        #self.open_button.clicked.connect(self.drawImg)
        self.drawImg()
        self.exit_button.clicked.connect(sys.exit)
        self.pushButton_3.clicked.connect(self.addNoise)
        self.pushButton.clicked.connect(self.histogram)

    def drawImg(self):
        self.imageLayout.addWidget(self.canvas)
        self.canvas.axes.cla()
        img = np.ones((256, 256), dtype=np.float32) * 50
        x_edge_gray = int(len(img) / 6)
        img[x_edge_gray:-x_edge_gray, x_edge_gray:-x_edge_gray] = 150
        center = (int(len(img) / 2), int(len(img) / 2))
        radius = min(x_edge_gray, x_edge_gray, len(img) - center[0], len(img) - center[1])
        x, y = np.ogrid[:len(img), :len(img)]
        dist = np.sqrt((x - center[0]) ** 2 + (y - center[0]) ** 2)
        circle = dist <= radius
        img[circle] = 250
        self.plt.imshow(img, cmap='gray')
        self.img = img

    def addNoise(self):
        self.verticalLayout_2.addWidget(self.canvas2)
        self.canvas2.axes.cla()
        self.noiseImg=np.add(self.noise(self.img.copy()),self.img.copy())
        # Scale noisy image to 0-255
        self.noiseImg=self.scalingFunction(self.noiseImg)
        # Plot image
        self.plt2.imshow(self.noiseImg, cmap='gray')
        rs = RectangleSelector(self.plt2, self.line_select_callback,
                               drawtype='box', useblit=True, button=[1, 3], spancoords='pixels',
                               interactive=True)
        self.plt2.figure.canvas.mpl_connect('key_press_event', rs)

    def line_select_callback(self, eclick, erelease):
        self.verticalLayout_4.addWidget(self.canvas3)
        self.canvas3.axes.cla()

        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata

        self.roi = self.noiseImg[int(y1):int(y2), int(x1):int(x2)]

        self.plt3.imshow(self.roi, cmap='gray')
        self.canvas3.draw()

    def histogram(self):
        try:
            img = np.round(self.roi.copy())
            #img=self.img
            self.verticalLayout_3.addWidget(self.canvas4)
            # clears axes
            self.canvas4.axes.cla()
            height,width = img.shape
            pixels = []
            # grayscale intensities
            for x in range(256):
                pixels.append(x)
            # initialize width and height of image
            nk = []
            imgArray = np.asarray(img)
            # to get the frequency of each pixel value
            for i in pixels:
                # counter
                c = 0
                for y in range(height):
                    for x in range(width):
                        # checking pixel intensity=grayscale intensity
                        if (imgArray[y, x] == i):
                            c += 1
                # append frequency of intensity level
                nk.append(c)
            # plot histogram
            self.plt4.bar(pixels, nk)

            self.meanSDHistogram(pixels,nk,(height*width))
        except (Exception) as e:
            print(e)

    def noise(self,img):
        height,width = img.shape
        #add Gaussian noise
        mu, sigma = 0, 5
        noise = np.random.normal(mu, sigma, size=(height, width))
        #add Unifrom noise
        mu, sigma = -10, 10
        noise += np.random.uniform(mu, sigma, size=(height, width))
        #Scale noise to 0-255
        noise=self.scalingFunction(noise)

        return noise

    def meanSDHistogram(self,pixels,nk,total):
        #Calculate and display mean
        mean=np.sum(np.multiply(pixels,nk))/total
        self.label_6.setText(str(mean))
        #Calculate and display SD
        variance=np.sum(np.multiply(np.power(pixels-mean,2),nk))/total
        self.label_8.setText(str(np.sqrt(variance)))

    def scalingFunction(self, array):
        # set the values of the image in the range of 0 to 255
        normalizedData = 255.0 * (array - np.min(array)) / (np.max(array) - np.min(array))
        return normalizedData

    # def drawImg(self):
    #     self.imageLayout.addWidget(self.canvas)
    #     self.canvas.axes.cla()
    #     img = np.ones((256, 256), dtype=np.float32) * 50
    #     x_edge_gray = int(len(img) / 6)
    #     img[x_edge_gray:-x_edge_gray, x_edge_gray:-x_edge_gray] = 150  # gray square
    #     center = (int(len(img) / 2), int(len(img) / 2))
    #     radius = min(x_edge_gray, x_edge_gray, len(img) - center[0], len(img) - center[1])
    #     x, y = np.ogrid[:len(img), :len(img)]
    #     dist = np.sqrt((x - center[0]) ** 2 + (y - center[0]) ** 2)
    #     circle = dist <= radius
    #     img[circle] = 250
    #     self.plt.imshow(img, cmap='gray')
    #     self.img = img
    #     rs = RectangleSelector(self.plt, self.line_select_callback,
    #                            drawtype='box', useblit=True, button=[1, 3], spancoords='pixels',
    #                            interactive=True)
    #     self.plt.figure.canvas.mpl_connect('key_press_event', rs)
    #
    # def addNoise(self):
    #     self.verticalLayout_2.addWidget(self.canvas2)
    #     self.canvas2.axes.cla()
    #     self.noiseImg=np.add(self.noise(self.img.copy()),self.img.copy())
    #     # Scale noisy image to 0-255
    #     self.noiseImg=self.scalingFunction(self.noiseImg)
    #     # Plot image
    #     self.plt2.imshow(self.noiseImg, cmap='gray')
    #
    # def line_select_callback(self, eclick, erelease):
    #     self.verticalLayout_4.addWidget(self.canvas3)
    #     self.canvas3.axes.cla()
    #
    #     x1, y1 = eclick.xdata, eclick.ydata
    #     x2, y2 = erelease.xdata, erelease.ydata
    #
    #     self.roi = self.img[int(y1):int(y2), int(x1):int(x2)]
    #
    #     self.plt3.imshow(self.roi, cmap='gray')
    #     self.canvas3.draw()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "ROI Histogram"))
        self.label.setText(_translate("MainWindow", "ROI"))
        self.label_3.setText(_translate("MainWindow", "Image"))
        self.label_4.setText(_translate("MainWindow", "Noisy Image"))
        self.pushButton_3.setText(_translate("MainWindow", "Generate Noise"))
        self.pushButton.setText(_translate("MainWindow", "Generate ROI Historgam"))
        self.label_7.setText(_translate("MainWindow", "Standard Deviation:"))
        self.label_5.setText(_translate("MainWindow", "Mean:"))
        self.open_button.setText(_translate("MainWindow", "Generate Image"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
