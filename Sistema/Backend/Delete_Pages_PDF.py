import PyPDF2
class Delete_Pages_PDF:

    def __init__( self ):
        pass

    def delete_pages_pdf( self , input_pdf, output_pdf, paginas_a_eliminar):

        with open(input_pdf, 'rb') as archivo_pdf:
            lector_pdf = PyPDF2.PdfReader(archivo_pdf)
            escritor_pdf = PyPDF2.PdfWriter()
            
            for numero_pagina in range(len(lector_pdf.pages)):
                if numero_pagina not in paginas_a_eliminar:
                    pagina = lector_pdf.pages[numero_pagina]
                    escritor_pdf.add_page(pagina)
            
            with open(output_pdf, 'wb') as nuevo_archivo_pdf:
                escritor_pdf.write(nuevo_archivo_pdf)
        
        return output_pdf