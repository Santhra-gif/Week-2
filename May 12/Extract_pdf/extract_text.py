import fitz 

#Function to extract the text from the pdf
def extract_pdf_text(filepath):
    doc = fitz.open(filepath)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


filepath = r'C:\Users\santh\Week-2\May 12\Extract_pdf\ai_sample_revised.pdf'
text = extract_pdf_text(filepath)
print(text)

