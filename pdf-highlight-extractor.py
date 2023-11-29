pip install PyMuPDF

import fitz  # PyMuPDF

def extract_highlighted_text(pdf_path, txt_path):
    pdf_document = fitz.open(pdf_path)
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            annotations = page.annots()
            if annotations:
                for annot in annotations:
                    if annot.type[0] == 8:  # Verificar si es un subrayado
                        rect = annot.rect
                        x0, y0, x1, y1 = rect
                        highlights = page.get_text("text", clip=(x0, y0, x1, y1))
                        if highlights:
                            txt_file.write(f"{highlights.strip()}\n") # ({page_num + 1}) para el número de página
    pdf_document.close()

if __name__ == "__main__":
    pdf_input_path = "C:/Users/Acer/Downloads/motivacion.pdf"
    txt_output_path = "C:/Users/Acer/Downloads/motivacion.txt"

    extract_highlighted_text(pdf_input_path, txt_output_path)

    print("Extracción completada. Los subrayados se han guardado en:", txt_output_path)
