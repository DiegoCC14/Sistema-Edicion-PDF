import os
import fitz

class PDF_Metadata:

    def __init__( self ):
        pass

    def get_size_pdf( self , pdf_path ):
        pdf_document = fitz.open( pdf_path )
        max_height = 0
        max_width = 0
        for page_num in range( len(pdf_document) ):
            page = pdf_document.load_page(page_num)
            rect = page.rect
            if rect[2] > max_height:
                max_height = rect[2]
            if rect[3] > max_width:
                max_width = rect[3]
        return int(max_height)+1,int(max_width)+1
