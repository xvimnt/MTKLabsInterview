import xml.etree.ElementTree as ET
import zipfile

xlsx_file_path = 'input.xlsx'

# Open the XLSX file as a zip file
with zipfile.ZipFile(xlsx_file_path, 'r') as zip_file:
    # Read the content of a specific part (e.g., sheet1.xml)
    sheet_content = zip_file.read('xl/sharedStrings.xml')

# Parse the XML content
root = ET.fromstring(sheet_content)

# String to store concatenated text content
concatenated_text = ""

# Iterate through the elements and concatenate text content
for elem in root.iter():
    if elem.text:
        concatenated_text += elem.text + "\n"

# Print or return the concatenated text
print(concatenated_text)