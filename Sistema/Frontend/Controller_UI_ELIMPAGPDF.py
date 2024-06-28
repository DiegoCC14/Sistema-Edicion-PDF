

class Controller_UI_ELIMPAGPDF:
    
    path_pdf = None
    list_data_pages_pdf = []

    def  __init__( self , obj_controller_backend ):

        self.obj_controller_backend = obj_controller_backend
        self.list_data_pages_pdf = []

    def set_path_pdf( self , path_pdf ):
        self.path_pdf = path_pdf

    def actualizar_data_pages_pdf( self ):
        if self.path_pdf!=None:
            self.list_data_pages_pdf = []
            for pos,page_path in enumerate( self.obj_controller_backend.get_page_pdf_preview( self.path_pdf ) ) :
                self.list_data_pages_pdf.append( { "num":pos, "img_path":page_path, "delete":False } )
    
    def delete_page( self , num_page ):
        for data_page in self.list_data_pages_pdf:
            if data_page["num"]==num_page:
                if data_page["delete"] == True: 
                    data_page["delete"] = False
                else:
                    data_page["delete"] = True
                break
                
    
    def get_data_pages_pdf( self ):
        return self.list_data_pages_pdf

    def eliminar_paginas_pdf( self , out_pdf_path ):
        list_pages_delete = [ data_page["num"] for data_page in self.list_data_pages_pdf if data_page["delete"]==True ]
        print( list_pages_delete )
        self.obj_controller_backend.delete_pages_pdf( self.path_pdf , out_pdf_path , list_pages_delete )
        