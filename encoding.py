import chardet


def main(input_file, output_file):
    # Detect file encoding
    with open(input_file, 'rb') as f:
        result = chardet.detect(f.read())
    file_encoding = result['encoding']

    # Load data from CSV with detected encoding
    df = pd.read_csv(input_file, encoding=file_encoding)

    # ...
