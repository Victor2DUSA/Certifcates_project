### Project: Certificate of Authenticity Automation

#### Overview

This project aims to automate the creation of certificates of authenticity for artworks sold at an art gallery. The current process involves manually transferring artwork details into a certificate template using InDesign, which is time-consuming and inefficient, especially when dealing with multiple certificates. To address this problem, the project introduces a Python script that automates the certificate generation process by extracting relevant information from a PDF pulled from the gallery's online system. This solution will significantly reduce the time required to produce certificates, making the process faster and more scalable.

#### Key Features

- **Automation**: Automatically generates certificates of authenticity using existing artwork information from a PDF file.
- **Efficiency**: Reduces the time required to create a certificate from approximately 30 minutes to just a few seconds.
- **Scalability**: Maintains consistent production time whether creating one certificate or hundreds, making it ideal for high-volume scenarios.

#### Prerequisites

- **Python**: Ensure Python is installed on your system.
- **Dependencies**: Install required Python libraries using `pip install -r requirements.txt`.
- **Input PDF**: A PDF file containing all necessary artwork information should be available.

#### Usage

1. **Prepare Input**: Obtain the PDF file with the artwork details from the online system.
2. **Run Script**: Execute the Python script to generate the certificate(s).
3. **Output**: The script will produce a certificate in the desired format, ready for printing or digital distribution.

#### Benefits

- **Time-Saving**: Significantly cuts down the time required to generate certificates.
- **Error Reduction**: Minimizes manual data entry errors by automating the transfer of information.
- **Consistency**: Ensures that all certificates adhere to the standard format.

#### Future Enhancements

- **Batch Processing**: Implement functionality to handle multiple PDFs at once.
- **Customization**: Allow for more customizable certificate templates.
- **Integration**: Explore direct integration with the online system to streamline the process further.

---
