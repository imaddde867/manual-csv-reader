# Import required libraries
import datetime 
import random

# Sample data: List of names to randomly choose from
names = ['Anas','Youssef','Maryam','Anna','Trevor','Michel','Franklin','Billie','Jay','Lillu','Karoline','Clea','Lena','Alena','Imad','Ema','Jack','Wilson','Tom','Tommas','Nelso','Mila','Aurelie','Vanessa','Sarah','Rihanna','Eman','Paula','Lotti','Tiina']

# Define date range for random date generation
# Start date: January 1, 2000
date0 = int(datetime.datetime(2000, 1, 1, 00, 00).timestamp())
# End date: Current time in UTC
date1 = int(datetime.datetime.now(datetime.UTC).timestamp())

# Possible subscription status values
subscription_statuses = ['Active', 'Inactive']

# Open file for writing (this line is redundant as we use 'with' statement later)
file = open("randomly_generated_data.csv", "w")

# Define CSV header columns
header = ('name','date of joining', 'age', 'subscription status')

# List to store generated data rows
lines=[]

def line_gen():
    """
    Generate a single random data row with:
    - Random name from the names list
    - Random date between 2000 and now
    - Random age between 18 and 80
    - Random subscription status
    """
    date = random.randint(date0, date1)
    readable_date = datetime.datetime.fromtimestamp(date).strftime('%d.%m.%Y')
    line = [
        random.choice(names),
        readable_date,
        random.randint(18, 80),
        random.choice(subscription_statuses),
    ]
    lines.append(line)

# Generate random number of rows between 100 and 500
number_of_rows = random.randint(100, 500)
for _ in range(number_of_rows):
    line_gen()

# Write data to CSV file
with open("randomly_generated_data.csv", "w", newline='\n') as file:
    # Write header row (join with commas)
    file.write(','.join(str(field) for field in header) + '\n')
    # Write data rows (join each row with commas)
    for line in lines:
        file.write(','.join(str(field) for field in line) + '\n')


def read_csv_without_library(file_path):
    # Open the CSV file for reading
    with open(file_path, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    # Assume the first line is the header
    header = lines[0].strip().split(',')
    
    # Process the remaining lines into data rows
    data = []
    for line in lines[1:]:
        # Skip empty lines
        if line.strip():
            # Remove extra whitespace and split the line by comma
            row = line.strip().split(',')
            data.append(row)
    
    return header, data

# Example :
header, data = read_csv_without_library("randomly_generated_data.csv")
print("Header:", header)
print("Data:")
for row in data:
    print(row)