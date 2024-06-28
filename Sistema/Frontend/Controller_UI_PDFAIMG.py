

class Controller_UI_PDFAIMG:
    
    path_pdf = None
    path_folder = None

    def  __init__( self , obj_controller_backend ):

        self.obj_controller_backend = obj_controller_backend
        
        self.path_pdf = None
        self.path_folder = None
    
    def set_path_pdf( self , path_pdf ):
        self.path_pdf = path_pdf
        
    def set_path_folder( self , path_folder ):
        self.path_folder = path_folder

    def pdf_to_img( self ):
        if self.path_folder!=None and self.path_pdf!=None:
            self.obj_controller_backend.pdf_to_img( self.path_pdf , self.path_folder )