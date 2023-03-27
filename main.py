import sys
from PyQt5.QtWidgets import QApplication
import front_end as fe
import back_end as ba


def hook (type, value, traceback):
    print(type)
    print(traceback)
    sys.__excepthook__ = hook


