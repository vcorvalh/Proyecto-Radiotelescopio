import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class RealTimePlot(QMainWindow):
    def __init__(self):
        super().__init__()

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
        self.ax.set_xlim([0, 10])
        self.ax.set_ylim([-1, 1])
        self.line, = self.ax.plot([], [])

        # Start the timer to update the plot
        self.timer = self.startTimer(50)

    def timerEvent(self, event):
        # Generate some random data
        x = np.linspace(0, 10, 100)
        y = np.random.randn(100)

        # Update the plot
        self.line.set_data(x, y)
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RealTimePlot()
    window.show()
    sys.exit(app.exec_())
