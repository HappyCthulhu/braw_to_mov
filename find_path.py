import os
import sys


# нужно, ибо pyinstaller не может найти пути к загруженным материалам
def find_path(f_name):
    if getattr(sys, 'frozen', False):
        # we are running in a bundle
        bundle_dir = sys._MEIPASS

    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(f_name))


    file = os.path.join(bundle_dir, f_name)
    return file

