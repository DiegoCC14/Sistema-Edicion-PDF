from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QHBoxLayout, QVBoxLayout, QLabel, QListWidgetItem
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QGraphicsRectItem, QGraphicsItem
from PyQt5.QtGui import QPixmap , QPen
from PyQt5.QtCore import Qt, QThread, QRectF
from PyQt5 import uic

from pathlib import Path

class MainWindow(QMainWindow):

    obj_controller_ui_pdfaimg = None
    obj_controller_ui_margenpdf = None

    def __init__( self , obj_controller_ui_pdfaimg , obj_controller_ui_margenpdf , obj_controller_ui_elimpagpdf ):
        super(MainWindow, self).__init__()

        uic.loadUi(Path( "Frontend/UI/UI.ui" ), self)
        # Referencia Controller --->>>>>>>>>>>>
        self.obj_controller_ui_pdfaimg = obj_controller_ui_pdfaimg
        self.obj_controller_ui_margenpdf = obj_controller_ui_margenpdf
        self.obj_controller_ui_elimpagpdf = obj_controller_ui_elimpagpdf
        # ------------------------->>>>>>>>>>>>

        #PDFAIMG --------------->>>>>>>>>>>>
        self.button_Select_PDF_PDFAIMG.clicked.connect( self.agregar_pdf_PDFAIMG )
        self.button_Select_CARPETA_PDFAIMG.clicked.connect( self.agregar_folder_PDFAIMG )
        self.button_PROCESAR_PDFAIMG.clicked.connect( self.pdf_to_img_PDFAIMG )
        # ------------------------------>>>>>>>>>>>>

        #MARGENPDF --------------->>>>>>>>>>>>
        self.dicc_obj_slider_label = {}

        self.horizontalSlider_Margen_Superior_MARGENPDF.setMinimum(0)
        self.horizontalSlider_Margen_Superior_MARGENPDF.setMaximum(0)
        self.dicc_obj_slider_label[ self.horizontalSlider_Margen_Superior_MARGENPDF ] = {"id":"margen_superior","label":self.label_num_margen_superior_MARGENPDF,"cambio_margen":0}
        self.horizontalSlider_Margen_Superior_MARGENPDF.valueChanged.connect( self.update_margen_slider_MARGENPDF )
        

        self.horizontalSlider_Margen_Inferior_MARGENPDF.setMinimum(0)
        self.horizontalSlider_Margen_Inferior_MARGENPDF.setMaximum(0)
        self.dicc_obj_slider_label[ self.horizontalSlider_Margen_Inferior_MARGENPDF ] = {"id":"margen_inferior","label":self.label_num_margen_inferior_MARGENPDF,"cambio_margen":0}
        self.horizontalSlider_Margen_Inferior_MARGENPDF.valueChanged.connect( self.update_margen_slider_MARGENPDF )

        self.horizontalSlider_Margen_Derecha_MARGENPDF.setMinimum(0)
        self.horizontalSlider_Margen_Derecha_MARGENPDF.setMaximum(0)
        self.dicc_obj_slider_label[ self.horizontalSlider_Margen_Derecha_MARGENPDF ] = {"id":"margen_derecha","label":self.label_num_margen_derecha_MARGENPDF,"cambio_margen":0}
        self.horizontalSlider_Margen_Derecha_MARGENPDF.valueChanged.connect( self.update_margen_slider_MARGENPDF )

        self.horizontalSlider_Margen_Izquierda_MARGENPDF.setMinimum(0)
        self.horizontalSlider_Margen_Izquierda_MARGENPDF.setMaximum(0)
        self.dicc_obj_slider_label[ self.horizontalSlider_Margen_Izquierda_MARGENPDF ] = {"id":"margen_izquierda","label":self.label_num_margen_izquierda_MARGENPDF,"cambio_margen":0}
        self.horizontalSlider_Margen_Izquierda_MARGENPDF.valueChanged.connect( self.update_margen_slider_MARGENPDF )
        
        self.button_Select_PDF_MARGENPDF.clicked.connect( self.agregar_pdf_MARGENPDF )

        self.button_PROCESAR_MARGENPDF.clicked.connect( self.chage_margen_pdf_MARGENPDF )
        # ------------------------------>>>>>>>>>>>>
        
        #ELIMPAGPDF --------------->>>>>>>>>>>>
        self.pos_item_list = {}

        self.button_Select_PDF_ELIMPAGPDF.clicked.connect( self.agregar_pdf_ELIMPAGPDF )
        self.List_0_Paginas_PDF_ELIMPAGPFD.itemDoubleClicked.connect(self.item_seleccionado_delete_ELIMPAGPDF)
        self.List_1_Paginas_PDF_ELIMPAGPFD.itemDoubleClicked.connect(self.item_seleccionado_delete_ELIMPAGPDF)
        self.List_2_Paginas_PDF_ELIMPAGPFD.itemDoubleClicked.connect(self.item_seleccionado_delete_ELIMPAGPDF)
        self.button_Eliminar_Paginas_ELIMPAGPDF.clicked.connect( self.eliminar_paginas_pdf_ELIMPAGPDF )
        # ------------------------------>>>>>>>>>>>>
    def item_seleccionado_delete_ELIMPAGPDF( self , item ):
        self.obj_controller_ui_elimpagpdf.delete_page( self.pos_item_list[ f"{item}" ] )
        self.actualizar_data_pages_pdf_ELIMPAGPDF()

    def agregar_pdf_ELIMPAGPDF( self ):
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "*.pdf")
        if file_path:
            self.obj_controller_ui_elimpagpdf.set_path_pdf( file_path )
            self.label_path_PDF_ELIMPAGPDF.setText( file_path )

            self.obj_controller_ui_elimpagpdf.actualizar_data_pages_pdf()
            self.actualizar_data_pages_pdf_ELIMPAGPDF()

    def actualizar_data_pages_pdf_ELIMPAGPDF( self ):
        
        list_data_pages_pdf = self.obj_controller_ui_elimpagpdf.get_data_pages_pdf()

        list_0_img_path = list_data_pages_pdf[0:int(len(list_data_pages_pdf)/3)]
        list_1_img_path = list_data_pages_pdf[int(len(list_data_pages_pdf)/3):int(len(list_data_pages_pdf)/3*2)]
        list_2_img_path = list_data_pages_pdf[int(len(list_data_pages_pdf)/3*2):len(list_data_pages_pdf)]

        self.List_0_Paginas_PDF_ELIMPAGPFD.clear()
        for data_page in list_0_img_path:
            list_item_widget = ListItemWidget( f"{data_page['num']}" , data_page['img_path'] , data_page['num'] , self.obj_controller_ui_elimpagpdf , data_page['delete'] )
            list_item = QListWidgetItem(self.List_0_Paginas_PDF_ELIMPAGPFD)
            list_item.setSizeHint( list_item_widget.sizeHint() )
            self.List_0_Paginas_PDF_ELIMPAGPFD.addItem(list_item)
            self.List_0_Paginas_PDF_ELIMPAGPFD.setItemWidget(list_item, list_item_widget)
            self.pos_item_list[ f"{list_item}" ] = data_page['num']

        self.List_1_Paginas_PDF_ELIMPAGPFD.clear()
        for data_page in list_1_img_path:
            list_item_widget = ListItemWidget( f"{data_page['num']}" , data_page['img_path'] , data_page['num'] , self.obj_controller_ui_elimpagpdf , data_page['delete']  )
            list_item = QListWidgetItem(self.List_1_Paginas_PDF_ELIMPAGPFD)
            list_item.setSizeHint( list_item_widget.sizeHint() )
            self.List_1_Paginas_PDF_ELIMPAGPFD.addItem(list_item)
            self.List_1_Paginas_PDF_ELIMPAGPFD.setItemWidget(list_item, list_item_widget)
            self.pos_item_list[ f"{list_item}" ] = data_page['num']

        self.List_2_Paginas_PDF_ELIMPAGPFD.clear()
        for data_page in list_2_img_path:
            list_item_widget = ListItemWidget( f"{data_page['num']}" , data_page['img_path'] , data_page['num'] , self.obj_controller_ui_elimpagpdf , data_page['delete']  )
            list_item = QListWidgetItem(self.List_2_Paginas_PDF_ELIMPAGPFD)
            list_item.setSizeHint( list_item_widget.sizeHint() )
            self.List_2_Paginas_PDF_ELIMPAGPFD.addItem(list_item)
            self.List_2_Paginas_PDF_ELIMPAGPFD.setItemWidget(list_item, list_item_widget)
            self.pos_item_list[ f"{list_item}" ] = data_page['num']

        self.text_pages_delete_ELIMPAGPDF.clear()
        pages_delete = ""
        for data_page in list_data_pages_pdf:
            if data_page["delete"] == True:
                pages_delete += f" - { data_page["num"] }"
        self.text_pages_delete_ELIMPAGPDF.setText( pages_delete )
    
    def eliminar_paginas_pdf_ELIMPAGPDF( self ):
        fileName, _ = QFileDialog.getSaveFileName(self, "Guardar Archivo", "", "*.pdf")
        if fileName:
            self.obj_controller_ui_elimpagpdf.eliminar_paginas_pdf( fileName )

    def agregar_pdf_MARGENPDF( self ):
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "*.pdf")
        if file_path:
            self.obj_controller_ui_margenpdf.set_path_pdf( file_path )
            size_pdf = self.obj_controller_ui_margenpdf.get_size_pdf()
            self.horizontalSlider_Margen_Superior_MARGENPDF.setMaximum( size_pdf[1] )
            self.horizontalSlider_Margen_Inferior_MARGENPDF.setMaximum( size_pdf[1] )
            self.horizontalSlider_Margen_Derecha_MARGENPDF.setMaximum( size_pdf[0] )
            self.horizontalSlider_Margen_Izquierda_MARGENPDF.setMaximum( size_pdf[0] )
            self.label_path_PDF_MARGENPDF.setText( file_path )

            img_compose_path = self.obj_controller_ui_margenpdf.get_img_compose()
            self.obj_rect_img = CropTool( img_compose_path , size_pdf )
            self.obj_rect_img.show()

    def update_margen_slider_MARGENPDF( self , value ):
        
        if self.sender() in self.dicc_obj_slider_label.keys():
            
            dicc_slider = self.dicc_obj_slider_label[ self.sender() ]
            diferencia = value - dicc_slider["cambio_margen"]

            if dicc_slider["id"]=="margen_superior":
                self.obj_rect_img.update_margen_superior( diferencia )
                self.obj_controller_ui_margenpdf.set_margen_pdf("margen_superior", value )

            elif dicc_slider["id"]=="margen_inferior":
                self.obj_rect_img.update_margen_inferior( diferencia )
                self.obj_controller_ui_margenpdf.set_margen_pdf("margen_inferior", value )
            
            elif dicc_slider["id"]=="margen_izquierda":
                self.obj_rect_img.update_margen_izquierda( diferencia )
                self.obj_controller_ui_margenpdf.set_margen_pdf("margen_izquierda", value )
            
            elif dicc_slider["id"]=="margen_derecha":
                self.obj_rect_img.update_margen_derecha( diferencia )
                self.obj_controller_ui_margenpdf.set_margen_pdf("margen_derecha", value )
            
            self.obj_rect_img.update_rectangulo()
            dicc_slider["cambio_margen"] = value
            dicc_slider["label"].setText( f"{value}" )

    def chage_margen_pdf_MARGENPDF( self ):
        fileName, _ = QFileDialog.getSaveFileName(self, "Guardar Archivo", "", "*.pdf")
        if fileName:
            print(f"Archivo guardado en: {fileName}")
            self.obj_controller_ui_margenpdf.change_margen_pdf( fileName )

    def agregar_pdf_PDFAIMG( self ):
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "*.pdf")
        if file_path:
            self.obj_controller_ui_pdfaimg.set_path_pdf( file_path )
            self.label_path_PDF_PDFAIMG.setText( file_path )
        
    def agregar_folder_PDFAIMG( self ):
        folder_path = QFileDialog.getExistingDirectory(self, 'Seleccionar carpeta')
        if folder_path:
            self.obj_controller_ui_pdfaimg.set_path_folder( folder_path )
            self.label_path_CARPETA_PDFAIMG.setText( folder_path )

    def pdf_to_img_PDFAIMG( self ):
        #print("---->>>>")
        #self.obj_controller_ui_pdfaimg.pdf_to_img()
        self.thread = Thread_PDF_A_IMG( self.obj_controller_ui_pdfaimg )
        self.thread.start()


class Thread_PDF_A_IMG( QThread ):
    
    obj_controller_ui_pdfaimg = None

    def __init__(self , obj_controller_ui_pdfaimg ):
        super().__init__()
        self.obj_controller_ui_pdfaimg = obj_controller_ui_pdfaimg

    def run(self):
        self.obj_controller_ui_pdfaimg.pdf_to_img()


class ResizableRectItem(QGraphicsRectItem):
    def __init__(self, rect):
        super().__init__(rect)
        self.setPen(QPen(Qt.GlobalColor.red, 2, Qt.PenStyle.SolidLine))
        self.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | QGraphicsItem.GraphicsItemFlag.ItemIsSelectable | QGraphicsItem.GraphicsItemFlag.ItemSendsScenePositionChanges)

    def mousePressEvent(self, event):
        self.setCursor(Qt.CursorShape.SizeAllCursor)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.CursorShape.ArrowCursor)
        super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        self.update()

class CropTool(QWidget):

    def __init__(self, image_path, size_img):
        super().__init__()
        
        self.image_path = image_path

        self.x0 = 0
        self.y0 = 0
        self.x1 = size_img[0]
        self.y1 = size_img[1]

        self.view = QGraphicsView(self)
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)
        self.resize(self.x1+10, self.y1+10)
        
        self.pixmap = QPixmap(self.image_path)
        self.image_item = QGraphicsPixmapItem(self.pixmap)
        self.scene.addItem(self.image_item)
        
        self.init_crop_rect()
        
    def init_crop_rect(self):
        rect = QRectF(0, 0, self.x1 , self.y1 )
        self.crop_rect = ResizableRectItem(rect)
        self.scene.addItem(self.crop_rect)

    def update_margen_superior( self , value ):
        self.y0 = self.y0+value
        self.y1 = self.y1-value
        
    def update_margen_inferior( self , value ):
        self.y1 = self.y1-value

    def update_margen_derecha( self , value ):
        self.x1 = self.x1-value

    def update_margen_izquierda( self , value ):
        self.x0 = self.x0+value
        self.x1 = self.x1-value

    def update_rectangulo( self ):
        self.crop_rect.setRect( QRectF( self.x0, self.y0, self.x1, self.y1 ))


class ListItemWidget(QWidget):
	
    def __init__(self, titulo, dir_img , posicion , obj_mediador_ui_cliente , delete ):
        super(ListItemWidget, self).__init__()

        self.posicion = posicion
        self.obj_mediador_ui_cliente = obj_mediador_ui_cliente

        left_column_layout = QVBoxLayout()

        self.image_label = QLabel()
        pixmap = QPixmap( dir_img )
        resized_pixmap = pixmap.scaled(94, 115 )  # Redimensionar la imagen a 300x300
        self.image_label.setPixmap(resized_pixmap)
        left_column_layout.addWidget(self.image_label)
        left_column_layout.addWidget( QLabel("           " + titulo) )
        
        self.setLayout( left_column_layout )
        
        if delete == True:
            self.setStyleSheet("""
                background-color: rgba(255, 0, 0, 128); /* Rojo con 50% de opacidad */
                border: 1px solid black;
            """)

