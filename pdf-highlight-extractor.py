import fitz  # Importar PyMuPDF

def extraer_subrayados(pdf_path, txt_path):
    # Abrir el archivo PDF
    pdf_document = fitz.open(pdf_path)

    # Crear un archivo de texto para escribir los fragmentos subrayados
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            annots = page.get_text("dict", clip=page.rect, flags=fitz.TEXT_DEHYPHENATE)  # Obtener las anotaciones/subrayados

            if annots:
                txt_file.write(f"Page {page_num + 1}:\n")
                for annot in annots['blocks']:
                    for line in annot['lines']:
                        for span in line['spans']:
                            # Verificar si el color del texto es diferente al color estándar del PDF
                            if span['color'] != (0, 0, 0):  # Cambiar (0, 0, 0) por el color estándar si es diferente
                                txt = span['text']
                                txt_file.write(f"{txt}\n")

if __name__ == "__main__":
    # Rutas de entrada y salida
    pdf_input_path = "ruta/del/archivo.pdf"
    txt_output_path = "ruta/del/archivo_de_texto.txt"

    # Llamar a la función para extraer subrayados
    extraer_subrayados(pdf_input_path, txt_output_path)

    print("Extracción completada. Los subrayados se han guardado en:", txt_output_path)
