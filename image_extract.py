import os 
import fitz
import PyPDF2


executable_dir = os.getcwd()
input_dir = os.path.join(executable_dir, "input_pdf_here")
output_dir = os.path.join(executable_dir,"certificates_made/image")
pdf_path = os.path.join(input_dir,"certificates.pdf")

class ImageExtraction:
    def __init__(self, pdf_path, output_dir):
        self.pdf_path = pdf_path
        self.output_dir = output_dir
        self.extract_images()

    def check_file_exist (self):
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)
        return True 

    def extract_images(self):
        reader = PyPDF2.PdfReader(self.pdf_path,)
        page = reader.pages
        count = 0
        index = 0
        for pages in page:
            #print(count)
            for image_file_object in pages.images:
                if count % 2 == 0:
                    pass
                else:
                    output_file = os.path.join(output_dir,f"{index}certi.png" )
                    with open(output_file, "wb") as fp:
                        fp.write(image_file_object.data)
                    index += 1 
                count += 1

Extract_img = ImageExtraction(pdf_path,output_dir)
