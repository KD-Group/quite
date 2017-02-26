"""
Convert from https://goo.gl/6hI6d5

Contains some functions related to windows api.
Linzhou (linzhou.zhang.china@gmail.com)
"""
import sys


def get_win_dpi():
    if sys.platform == "win32":
        import win32gui
        import win32print

        para_x, para_y = 88, 90

        hdc = win32gui.GetDC(0)
        x_dpi = win32print.GetDeviceCaps(hdc, para_x)
        y_dpi = win32print.GetDeviceCaps(hdc, para_y)
        return x_dpi, y_dpi
    return 96, 96  # default dpi


def get_program_scale_factor():
    default_dpi_x = 96.0
    default_dpi_y = 96.0

    current_dpi_x, current_dpi_y = get_win_dpi()

    scale_x = current_dpi_x / default_dpi_x
    scale_y = current_dpi_y / default_dpi_y

    return scale_x, scale_y


class Scaling:
    def __init__(self):
        self.x, self.y = get_program_scale_factor()

scaling = Scaling()
