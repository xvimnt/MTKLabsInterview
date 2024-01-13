import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def normalize_company_name(name):
    # Remove legal structure indicators and normalize whitespace
    name = name.upper().replace(" INC.", "").replace(" LLC.", "").replace(" LLP.", "").strip()
    return name

def find_canonical_name(name, canonical_names):
    # Use fuzzy matching to find the best match
    best_match, _ = process.extractOne(name, canonical_names, scorer=fuzz.token_sort_ratio)
    return best_match

def main(input_file, output_file):
    # Load data from CSV with detected encoding
    df = pd.read_csv(input_file)

    # Define canonical company names
    canonical_names = ["MICROSOFT TECHNOLOGY LICENSING", "MICRON TECHNOLOGY", "ELTA SYSTEMS", "DELTA SYSTEMS"]

    # Normalize company names
    df['normalized_company_name'] = df['organization'].apply(normalize_company_name)

    # Find canonical names for each normalized name
    df['canonical_company_name'] = df['normalized_company_name'].apply(lambda x: find_canonical_name(x, canonical_names))

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
