# Company Name Normalizer

This script normalizes company names in a CSV file, attributing patents to canonical company names. The normalization process includes handling whitespace, punctuation, legal structure variations, and fuzzy matching.

## Requirements

- Python (version 3.x)
- Pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/xvimnt/MTKLabsInterview.git
   ```

````

1. Navigate to the project directory:

```bash
cd your-repository
````

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the script using the following command:

```bash
python company_name_normalizer.py input_file.csv output_file.csv
```

Replace `input_file.csv` with the path to your input CSV file and `output_file.csv` with the desired output CSV file.

## Options

- `input_file.csv`: Path to the input CSV file.
- `output_file.csv`: Path to the output CSV file.

## Algorithm Details

- The algorithm normalizes company names for whitespace, punctuation, and legal structure variations before addressing misspellings.
- It uses fuzzy matching to compare the similarity of two company names but relies on other attributes in the file to rule out potential false positives.

## Notes

- The script assumes no misspellings are possible in the country field but are possible in the city field.

## Contributing

If you find issues or have suggestions for improvements, please open an issue or submit a pull request.

```javascript
Remember to customize placeholders such as `your-username`, `your-repository`, and `[Your License Name]` with the relevant information for your script and repository.
```
