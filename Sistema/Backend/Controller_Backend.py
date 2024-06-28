
from .PDF_to_IMG import PDF_to_IMG
from .PDF_Metadata import PDF_Metadata
from .Margen_PDF import Margen_PDF
from .Delete_Pages_PDF import Delete_Pages_PDF

class Controller_Backend:
    
    obj_pdf_to_img = None
    obj_pdf_metadata = None
    obj_pdf_margen_pdf = None

    def  __init__( self ):
        self.obj_pdf_to_img = PDF_to_IMG()
        self.obj_pdf_metadata = PDF_Metadata()
        self.obj_pdf_margen_pdf = Margen_PDF()
        self.obj_pdf_delete_pages = Delete_Pages_PDF()

    def pdf_to_img( self , pdf_path , folder_path ):
        self.obj_pdf_to_img.pdf_to_img( pdf_path , folder_path , 2.0 )

    def get_size_pdf( self , pdf_path ):
        size_pdf = (0,0)
        size_pdf = self.obj_pdf_metadata.get_size_pdf( pdf_path )
        return size_pdf

    def get_img_compose( self , pdf_path ):
        path_image_pdf = ""
        imgs_path_list = self.obj_pdf_to_img.pdf_to_img( pdf_path , "Backend/Temp" , 1.0 )
        self.obj_pdf_to_img.combine_list_imgs( imgs_path_list , "base.png" )
        path_image_pdf = "Backend/Temp/base.png"
        return path_image_pdf

    def change_margen_pdf( self , pdf_path , out_pdf_path , margen_superior , margen_inferior , margen_izquierdo , margen_derecho ):
        out_path_pdf = self.obj_pdf_margen_pdf.change_margen_pdf(pdf_path,out_pdf_path,margen_superior,margen_inferior,margen_izquierdo,margen_derecho)
        return out_path_pdf
    
    def get_page_pdf_preview( self , pdf_path ):
        path_imgs = self.obj_pdf_to_img.pdf_to_img( pdf_path , "Backend/Temp/Preview" , 0.3 )
        return path_imgs

    def delete_pages_pdf( self , pdf_path , out_pdf_path , list_pdf_pages_delete ):
        self.obj_pdf_delete_pages.delete_pages_pdf( pdf_path , out_pdf_path , list_pdf_pages_delete )