import sys
from PyQt5.QtWidgets import QApplication
import front_end as fe
import back_end as be


def hook (type, value, traceback):
    print(type)
    print(traceback)
    sys.__excepthook__ = hook

app = QApplication(sys.argv)
info = be.Info()
data_acquisition_thread = be.DownloadData(info)
window = fe.RealTimePlot(info, data_acquisition_thread)











window.start_data_thread()

window.show()
sys.exit(app.exec_())