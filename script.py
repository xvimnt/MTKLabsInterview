import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from io import StringIO
import xml.etree.ElementTree as ET
import zipfile
import re


def get_string_from_file(file_path):

    # Open the XLSX file as a zip file
    with zipfile.ZipFile(file_path, 'r') as zip_file:
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

    return concatenated_text


def normalize_company_name(name):
    if isinstance(name, str):
        # Remove legal structure indicators and normalize whitespace
        name = name.upper().replace(" INC", "").replace(" LLC", "").replace(" LLP", "").strip()
    return name

def find_canonical_name(name, canonical_names):
    if isinstance(name, str):
        # Use fuzzy matching to find the best match
        best_match, _ = process.extractOne(name, canonical_names, scorer=fuzz.token_sort_ratio)
        return best_match
    return None

def main(input_file, output_file):
    # read file into string
    readed = get_string_from_file(input_file)

    # Load data from CSV with detected encoding
    COMMA_MATCHER = re.compile(r",(?=(?:[^\"']*[\"'][^\"']*[\"'])*[^\"']*$)")
    df = pd.DataFrame([COMMA_MATCHER.split(x) for x in readed.split('\n')])

    # Define the first row as header
    df.columns = df.iloc[0]
    df = df[1:]

    # Define canonical company names
    canonical_names = df['organization'].apply(normalize_company_name).unique()

    # Find canonical names for each normalized name
    df['normalized_company_name'] = df['organization'].apply(normalize_company_name).apply(lambda x: find_canonical_name(x, canonical_names))

    # Save the result to a new CSV file
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python script.py input.xlsx output_file.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    main(input_file, output_file)
