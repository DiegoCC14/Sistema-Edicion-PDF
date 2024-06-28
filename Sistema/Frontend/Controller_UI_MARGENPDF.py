

class Controller_UI_MARGENPDF:
    
    path_pdf = None
    new_margen_superior_pdf = 0
    new_margen_inferior_pdf = 0
    new_margen_izquierda_pdf = 0
    new_margen_derecha_pdf = 0

    def  __init__( self , obj_controller_backend ):

        self.obj_controller_backend = obj_controller_backend
        
        self.path_pdf = None
        self.new_margen_superior_pdf = 0
        self.new_margen_inferior_pdf = 0
        self.new_margen_izquierda_pdf = 0
        self.new_margen_derecha_pdf = 0

    def set_path_pdf( self , path_pdf ):
        self.path_pdf = path_pdf

    def get_size_pdf( self ):
        if self.path_pdf != None:
            return self.obj_controller_backend.get_size_pdf( self.path_pdf )

    def pdf_to_img( self ):
        if self.path_folder!=None and self.path_pdf!=None:
            self.obj_controller_backend.pdf_to_img( self.path_pdf , self.path_folder )
    
    def get_img_compose( self ):
        if self.path_pdf != None:
            return self.obj_controller_backend.get_img_compose( self.path_pdf )

    def set_margen_pdf( self , id_margen , value ):
        if id_margen == "margen_superior":
            self.new_margen_superior_pdf = value
        elif id_margen == "margen_inferior":
            self.new_margen_inferior_pdf = value
        elif id_margen == "margen_izquierda":
            self.new_margen_izquierda_pdf = value
        elif id_margen == "margen_derecha":
            self.new_margen_derecha_pdf = value

    def change_margen_pdf( self, out_pdf_path ):
        if self.path_pdf != None:
            self.obj_controller_backend.change_margen_pdf( self.path_pdf,out_pdf_path,self.new_margen_superior_pdf,self.new_margen_inferior_pdf,self.new_margen_izquierda_pdf,self.new_margen_derecha_pdf )