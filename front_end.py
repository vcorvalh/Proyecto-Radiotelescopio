import sys
import numpy as np
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import QThread, pyqtSignal
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import back_end as be



class RealTimePlot(QMainWindow):

    def __init__(self, info, data_thread):
        super().__init__()

        self.info = info
        self.data_thread = data_thread

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
        self.ax.set_xlim(self.info.x_lim)
        self.ax.set_ylim(self.info.y_lim)
        self.line, = self.ax.plot([], [])

    
    def start_data_thread(self):
        self.data_thread.start()
        self.update_timer = self.startTimer(100)

    def stop_data_thread(self):
        self.data_thread.stop()
        self.data_thread.wait()
        self.killTimer(self.update_timer)

    def update_plot(self, x, y):
        #update the plot
        self.ax.clear()
        self.ax.plot(x, y)
        #self.ax.set_xlim(self.plot_info.x_lim)
        self.ax.set_ylim(self.plot_info.y_lim)
        self.ax.autoscale_view()
        self.canvas.draw()

    def timerEvent(self, event):
        while not self.info.data_queue.empty():
            data = self.info_data_queue.get()
            x = data[0]
            y = data[1]
            self.update_plot.plot(x, y)














if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RealTimePlot()
    window.show()
    sys.exit(app.exec_())
