
from PyQt5.QtWidgets import QApplication

from Frontend.UI import MainWindow
from Frontend.Controller_UI_PDFAIMG import Controller_UI_PDFAIMG
from Frontend.Controller_UI_MARGENPDF import Controller_UI_MARGENPDF
from Frontend.Controller_UI_ELIMPAGPDF import Controller_UI_ELIMPAGPDF

from Backend.Controller_Backend import Controller_Backend

from pathlib import Path
import sys

BASE_DIR = Path(__file__).parent

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    obj_Controller_Backend = Controller_Backend()
    
    obj_Controller_UI_PDFAIMG = Controller_UI_PDFAIMG( obj_Controller_Backend )
    obj_Controller_UI_MARGENPDF = Controller_UI_MARGENPDF( obj_Controller_Backend )
    obj_Controller_UI_ELIMPAGPDF = Controller_UI_ELIMPAGPDF( obj_Controller_Backend )

    obj_UI = MainWindow( obj_Controller_UI_PDFAIMG , obj_Controller_UI_MARGENPDF , obj_Controller_UI_ELIMPAGPDF )

    obj_UI.show()
    sys.exit(app.exec())
    
    