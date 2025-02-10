# CSV Data Generator and Parser

[![CSV](https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FFile%3ACSV_Logo.svg&psig=AOvVaw02GfKq2nz_xmRdWne2-Hko&ust=1739298810791000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJC6ubDfuYsDFQAAAAAdAAAAABAE)

A simple Python script that demonstrates how to generate random user data and parse CSV files without using external data manipulation libraries. This project serves as a learning exercise for manual CSV file handling in Python.

## Features

- Generates random user data including:
  - Names from a predefined list
  - Dates of joining between 2000 and present
  - Ages between 18 and 80
  - Subscription status (Active/Inactive)
- Creates a CSV file with random number of entries (100-500 rows)
- Demonstrates manual CSV parsing without using pandas or other data analysis libraries
- Converts CSV data into a list of dictionaries for easy data manipulation

## Requirements

- Python 3.x
- No external libraries required beyond Python's standard library

## Project Structure

```
.
├── README.md
├── csv_generator.py
└── randomly_generated_data.csv (generated)
```

## Code Overview

The script performs the following operations:

1. **Data Generation**
   - Randomly selects names from a predefined list
   - Generates random dates between January 1, 2000, and current date
   - Assigns random ages between 18 and 80
   - Assigns random subscription status (Active/Inactive)

2. **CSV File Operations**
   - Creates a new CSV file named "randomly_generated_data.csv"
   - Writes header row with column names
   - Writes randomly generated data rows
   - Demonstrates proper file handling using context managers (`with` statements)

3. **CSV Parsing**
   - Reads the generated CSV file
   - Converts data into a list of dictionaries
   - Maps CSV headers to values for each row

## Usage

Simply run the script:

```bash
python csv_generator.py
```

The script will:
1. Generate a new CSV file with random data
2. Parse the file and print the first row as a dictionary

## Sample Output

```python
{
    'name': 'John',
    'date of joining': '15.03.2012',
    'age': '25',
    'subscription status': 'Active'
}
```

## Learning Points

This project demonstrates several important Python concepts:

- Working with the `datetime` module
- Random data generation
- File I/O operations
- CSV file handling without external libraries
- Dictionary operations
- List comprehensions and data structures
- Context managers (`with` statements)

## Potential Improvements

1. Add error handling for file operations
2. Implement data validation
3. Add command-line arguments for customization
4. Include data statistics generation
5. Add support for different date formats
6. Implement custom data export formats

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes.
