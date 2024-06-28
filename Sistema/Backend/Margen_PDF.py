import fitz  # PyMuPDF

class Margen_PDF:

    def  __init__( self ):
        pass
    
    def change_margen_pdf( self , pdf_path , out_pdf_path , margen_superior , margen_inferior , margen_izquierdo , margen_derecha ):
        doc = fitz.open( pdf_path )
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            rect = page.rect

            new_rect = fitz.Rect(rect.x0 + margen_izquierdo, rect.y0 + margen_superior, rect.x1 - margen_derecha, rect.y1 - margen_inferior)
            page.set_cropbox(new_rect)

        doc.save(out_pdf_path)
        doc.close()
        return out_pdf_path