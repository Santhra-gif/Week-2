import fitz  # PyMuPDF

# Function to extract chunks into groups of three lines
def extract_chunks_from_pdf(pdf_path, lines_per_chunk=3):
    all_lines = []
    with fitz.open(pdf_path) as doc:
        for page in doc:
            page_text = page.get_text("text")
            lines = page_text.split('\n')
            all_lines.extend([line.strip() for line in lines if line.strip()])

    # To group lines into chunks
    chunks = []
    for i in range(0, len(all_lines), lines_per_chunk):
        chunk = "\n".join(all_lines[i:i + lines_per_chunk])
        chunks.append(chunk)
    
    return chunks

# Function to display each chunks in terminal
def display_chunks(chunks):
    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i+1} ---\n{chunk}\n")

if __name__ == "__main__":
    pdf_path = "Chunk_pdf/ai_sample_revised.pdf"  # Update path if needed
    chunks = extract_chunks_from_pdf(pdf_path, lines_per_chunk=3)
    display_chunks(chunks)
