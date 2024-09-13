from PIL import Image
from reportlab.lib import fonts
from reportlab.pdfgen import canvas
import os
from reportlab.lib.pagesizes import A4
from PIL import Image
import fitz  # PyMuPDFLite
import sys
from image_extract import ImageExtraction
from text_read import TextExtractror



def create_pdf_for_images(input_dir, output_dir, text_dir, logo_path):
    try:
        # Ensure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Loop through each text file in the text directory
        for text_filename in sorted(os.listdir(text_dir)):
            if text_filename.endswith(".txt"):
                text_file = os.path.join(text_dir, text_filename)
                image_filename = os.path.splitext(text_filename)[0] + ".png"  # Assumes corresponding image has same name but .jpg extension
                image_path = os.path.join(input_dir, image_filename)
                output_path = os.path.join(output_dir, os.path.splitext(text_filename)[0] + ".pdf")
                create_pdf_with_image(image_path, text_file, output_path, logo_path)
    
    except Exception as e:
        print(f"An error occurred: {e}")


def create_pdf_with_image(image_path, text_file, output_path, logo_path):
    try:
        # Open the image with PyMuPDFLite to get dimensions
        with fitz.open(image_path) as img_doc:
            page = img_doc[0]
            img_width = page.rect.width / 2
            img_height = page.rect.height / 2
        
        if img_height > 230 and img_width > 180:
            img_height = img_height * 0.275
            img_width = img_width * 0.275
            print(img_width, ": wifht")
            print(img_height,": height")

        # Create a new PDF document with A4 size
        c = canvas.Canvas(output_path, pagesize=A4)

        logo_img = Image.open(logo_path)
        logo_width, logo_height = logo_img.size

        logo_scale = 0.2  # Adjust the scale as needed
        logo_width_scaled = logo_width * logo_scale  # Adjust the width as needed
        logo_height_scaled = logo_height * logo_scale  # Adjust the height as needed

        # Adjust the x and y coordinates to move the logo down and to the right
        logo_x = 50  # Adjust the horizontal position
        logo_y = 720  # Adjust the vertical position

        c.drawImage(logo_path, logo_x, logo_y, width=logo_width_scaled, height=logo_height_scaled, mask='auto')

        # Position the image on the PDF canvas
        x = 100
        y = A4[1] - 200

        img_y_po = y - img_height - 100

        # Draw the image on the canvas (centered)
        c.drawImage(image_path, x, y - img_height - 100, width=img_width, height=img_height)

        # certificate of authenticity
        font_name = "Helvetica"  # Change to your desired font
        font_size = 30  # Change to your desired font size
        c.setFont(font_name, font_size)
        text_line = "Certificate of Authenticity"
        c.drawString(logo_x, logo_y - 100, text_line)

        bold_font = fonts.tt2ps('Helvetica', 1, 0)
        italic_font = fonts.tt2ps('Helvetica', 0, 1)

        font_name = "Helvetica"  # Change to your desired font
        font_size = 10  # Change to your desired font size
        c.setFont(font_name, font_size)
        text_long = "This is to certify that this artwork is original and authentic, as produced by the artist. All copyrights, including"
        c.drawString(logo_x, img_y_po - 50, text_long)

        text_long = "use of artworks image and rights of productions are fully retained by the Artist."
        c.drawString(logo_x, img_y_po - 50 - (font_size * 1.2 + 4), text_long)

        signature = "Signature:"
        c.drawString(logo_x + 10, img_y_po - 95 - (font_size * 1.2 + 4), signature)

        logo_name = "Southern Guild"
        c.drawString(logo_x + 10, img_y_po - 130 - (font_size * 1.2 + 4), logo_name)

        # Read the text from the text file
        with open(text_file, "r", encoding="utf-8") as file:
            lines = file.readlines()

        font_name = "Helvetica"  # Change to your desired font
        font_size = 12  # Change to your desired font size
        c.setFont(font_name, font_size)

        # Draw the text next to the image (right-aligned)
        text_y = y - img_height + (img_height / 2)  # Initial y-coordinate for the first line of text
        line_spacing = 4
        count = 0
        for line in lines:
            line = line.strip()  # Remove leading and trailing whitespace
            if count == 4 and "edition" not in line.lower():
                break
            if line:  # Skip empty lines
                if "in." in line:
                    pass
                else:
                    if count == 0:
                        c.setFont(bold_font, font_size)
                    elif count == 1:
                        c.setFont(italic_font, font_size)
                    else:
                        c.setFont(font_name, font_size)
                    if "c m" in line:
                        line = line.replace('c m', 'cm')
                    if "" in line:
                        line = line.replace("", "")

                    text_width = c.stringWidth(line, font_name, font_size)
                    c.drawString(x + img_width + 30, text_y - 60, line)  # Draw each line of text right-aligned
                    text_y -= font_size * 1.2 + line_spacing  # Move to the next line
                    count += 1
        if count == 4:
            text = "Unique"
            c.drawString(x + img_width + 30, text_y - 60, text)  # Draw each line of text right-aligned

        c.save()
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:

def make_cert_1():
    #rename pdf

    # Get the directory of the executable

    # Define paths relative to the executable directory

    executable_dir = os.getcwd()
    input_dir = os.path.join(executable_dir, "input_pdf_here")
    text_output_path = os.path.join(executable_dir,"certificates_made/text")
    pdf_path = os.path.join(input_dir,"certificates.pdf")
    image_output_path = os.path.join(executable_dir, "Certificates_made", "images", "")
    input_dir = os.path.join(executable_dir, "input_pdf_here")
    output_dir = os.path.join(executable_dir,"Certificates_made/text")


    # Extract images from PDF
    ImageExtraction(pdf_path, image_output_path)

    # Extract text from PDFs
    TextExtractror(pdf_path, input_dir, text_output_path)

    # Make certificates
    input_dir = os.path.join(executable_dir, "Certificates_made", "image")
    output_dir = os.path.join(executable_dir, "Certificates_made")
    text_dir = os.path.join(executable_dir, "Certificates_made", "text")
    logo_path = os.path.join(executable_dir, "logo", "logo.png")
    create_pdf_for_images(input_dir, output_dir, text_dir, logo_path)


make_cert_1()
