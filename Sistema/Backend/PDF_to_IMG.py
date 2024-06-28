import os
import fitz  # PyMuPDF
from PIL import Image

class PDF_to_IMG:

    def  __init__( self ):
        pass
    
    def pdf_to_img( self , path_pdf , path_folder , zoom ):
        imgs_path_list = []

        pdf_document = fitz.open( path_pdf )
        
        for page_num in range( len(pdf_document) ):
            page = pdf_document.load_page(page_num)

            zoom_x = zoom  # Aumenta la resolución en el eje x
            zoom_y = zoom  # Aumenta la resolución en el eje y
            matrix = fitz.Matrix(zoom_x, zoom_y)

            pix = page.get_pixmap( matrix=matrix )
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            img.save( f"{path_folder}/{page_num + 1}.png" )
            imgs_path_list.append( f"{path_folder}/{page_num + 1}.png" )

        return imgs_path_list

    def combine_list_imgs( self , list_imgs_path , out_img_path ):
        self.make_image_transparent( list_imgs_path[0] , f"Backend/Temp/{out_img_path}" , (255, 255, 255) )
        for img_path in list_imgs_path[ 1 : len(list_imgs_path) ]:
            self.make_image_transparent( img_path , "Backend/Temp/img.png" , (255, 255, 255) )
            self.combine_images( f"Backend/Temp/{out_img_path}" , "Backend/Temp/img.png" , f"Backend/Temp/{out_img_path}" )

    def make_image_transparent( self , image_path, output_path, color_to_make_transparent):
        img = Image.open(image_path).convert("RGBA")
        datas = img.getdata()

        new_data = []
        for item in datas:
            if item[:3] == color_to_make_transparent:
                # Cambia el color especificado a transparente
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)

        img.putdata(new_data)
        img.save(output_path, "PNG")
        
    def combine_images( self , image1_path , image2_path , output_path , position=(0, 0) ):
        base_image = Image.open(image1_path).convert("RGBA")
        overlay_image = Image.open(image2_path).convert("RGBA")

        base_image.paste(overlay_image, position, overlay_image)
        base_image.save(output_path, "PNG")