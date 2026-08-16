import pandas as pd
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import Font, Alignment

# Crear un DataFrame con datos de ejemplo
data = { 
    'Nombre': ['Juan', 'Ana', 'Luis'],
    'Edad': [25, 30, 22]
}
df = pd.DataFrame(data)


hojas = ['Lunes 2_10', 'Martes 3_10', 'Miércoles 4_10'] # Crear una lista con los nombres de las hojas

# Guardar el DataFrame en un archivo Excel, empezando en la fila 11 para dejar espacio para la imagen en el encabezado
file_path = 'mi_archivo_con_encabezado.xlsx'
with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
    for hoja in hojas:
        df.to_excel(writer, sheet_name=hoja, startrow=11, index=False)

# Cargar el archivo para agregar la imagen, formato e info específica
wb = load_workbook(file_path)

for hoja in hojas:

    ws = wb[hoja]
    
    # Escribir datos en la hoja
    ws.merge_cells('B8:E8')
    ws['B8'] = 'LISTA DE ASISTENCIA A LAS ACTIVIDADES EXTRACURRICULARES MAYO AGOSTO 2024'
    ws['B8'].font = Font(bold=True)
    ws['B8'].alignment = Alignment(horizontal='center')

    # Información específica
    ws['B9'] = 'Materia:'
    ws['B9'].font = Font(bold=True)
    ws['C9'] = 'ESCOLTA Y BANDA DE GUERRA'
    ws['D9'] = 'Docente:'
    ws['D9'].font = Font(bold=True)
    ws['E9'] = 'GUILLERMO JORGE CAMPOS MEDINA'
    ws['B10'] = 'Día:'
    ws['B10'].font = Font(bold=True)
    ws['C10'] = 'Lunes'
    ws['D10'] = 'Horario:'
    ws['D10'].font = Font(bold=True)
    ws['E10'] = '14:20 a 15:10'

    # Cargar la imagen
    img = Image('logo.png')  # Asegúrate de que la imagen esté en el mismo directorio o proporciona la ruta completa

    # Ajustar la imagen al tamaño deseado (opcional)
    img.width = 550  # Ancho en píxeles
    img.height = 100  # Alto en píxeles

    # Insertar la imagen en una posición específica
    ws.add_image(img, 'C2')

    # Ajustar automáticamente el ancho de las columnas
    for column_cells in ws.columns:
        length = max(len(str(cell.value)) for cell in column_cells)
        ws.column_dimensions[column_cells[0].column_letter].width = length + 2  # Agregar un margen para evitar cortes

    # Ajustar manualmente el ancho de la columna B para que no sea excesivo
    ws.column_dimensions['B'].width = 20  # Ajusta este valor según sea necesario

# Guardar el archivo con los formatos aplicados
wb.save(file_path)

print("Archivo Excel con encabezado de imagen creado exitosamente.")
