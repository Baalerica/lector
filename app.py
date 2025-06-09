from pdf2docx import Converter

# Ruta al archivo PDF de entrada
archivo_pdf = 'entrada.pdf'

# Ruta al archivo DOCX de salida
archivo_word = 'salida.docx'

# Crear el convertidor
cv = Converter(archivo_pdf)

# Convertir todo el PDF a Word
cv.convert(archivo_word, start=0, end=None)

# Cerrar el convertidor
cv.close()

print("Conversión completada.")
