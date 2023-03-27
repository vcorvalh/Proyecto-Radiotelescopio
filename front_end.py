import sys
import numpy as np
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import QThread, pyqtSignal
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


import back_end as be



class DataThread(QThread):
    
    new_data_signal = pyqtSignal(np.ndarray, np.ndarray)

    def __init__(self, data_download):
        super().__init__()
        self.data_download = data_download
        #lo que voy a hacer aca es para eliminar pq no es escalable


    def run (self):

        while True:
            #obtener los datos
            x, y = self.data_download.get_data()
            self.new_data_signal.emit(x, y)

            time.sleep(0.05)

            




class RealTimePlot(QMainWindow):
    def __init__(self):
        super().__init__()

        self.plot_info = PlotInfo()

        # Create a Matplotlib figure
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.setCentralWidget(self.canvas)

        # Initialize the plot
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel('Frecuency')
        self.ax.set_ylabel('Amplitude')

        #la idea que esto pueda cambiar en el futuro
        ###################################################
        self.ax.set_xlim(self.plot_info.x_lim)
        self.ax.set_ylim(self.plot_info.y_lim)
        self.line, = self.ax.plot([], [])


        #crear el thread para obtener nueva data
        self.data_download = be.DownloadData()
        self.data_thread = DataThread(self.data_download)
        self.data_thread.new_data_signal.connect(self.update_plot)
        self.data_thread.start()


    def update_plot(self, x, y):
        #update the plot
        self.ax.clear()
        self.ax.plot(x, y)
        #self.ax.set_xlim(self.plot_info.x_lim)
        self.ax.set_ylim(self.plot_info.y_lim)
        self.ax.autoscale_view()
        self.canvas.draw()




class PlotInfo:

    def __init__ (self, x_lim = [0,0], y_lim = [-40,70]):

        self.x_lim = x_lim
        self.y_lim = y_lim

    def update_plot_info (self):
        pass










if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RealTimePlot()
    window.show()
    sys.exit(app.exec_())
