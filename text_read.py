import PyPDF2
import os

executable_dir = os.getcwd()
input_dir = os.path.join(executable_dir, "input_pdf_here")
output_dir = os.path.join(executable_dir,"certificates_made/text")
pdf_path = os.path.join(input_dir,"certificates.pdf")

def rename(input_dir):
    try:
        file_list = os.listdir(input_dir)

        for file_name in file_list:
            if file_name.endswith(".pdf"):
                old_path = os.path.join(input_dir, file_name)
                new_path = os.path.join(input_dir, "certificates.pdf")
                os.rename(old_path, new_path)

    except Exception as Failed_to_rename:
        print(f"An error occured while renaming Pdf files : {Failed_to_rename}")            

class TextExtractror:
    def __init__(self, pdf_path, input_dir, output_dir):
        self.pdf_path = pdf_path
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.extract_text()
        #print("class called")

    def __pdf_reader(self):
        reader = PyPDF2.PdfReader(open(self.pdf_path,"rb"))
        #print("i have read the file")
        return reader

    def extract_text(self,):
        #print("function called")
        try:
            #check to see if out directory exist if not first create it
            if not os.path.exists(self.output_dir):
                os.mkdir(self.output_dir)
                #print("directory checked")
            
            # read through the pdf and extract text. Each pdf page should have its own txt
            reader = self.__pdf_reader()
            #print("i have read the pdf")
            for page_number, page in enumerate(reader.pages, start = 1):
                #print(f"Im at this this page number {page_number}")
                output_file = os.path.join(self.output_dir, f"{page_number}certi.txt")
                #print(f"this is the outputfile {output_file}")
                text = page.extract_text()
                #print(f"This is the extracted text: {text}")
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(text)

        except Exception as Text_not_writen:
            print(f"writing text file error occured {Text_not_writen}")

rename(input_dir)
write_text = TextExtractror(pdf_path, input_dir, output_dir)

