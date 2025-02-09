# Import required libraries
import csv
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
    writer = csv.writer(file)
    writer.writerow(header)    # Write header row
    writer.writerows(lines)    # Write data rows

# Read CSV file and convert to list of dictionaries
with open('randomly_generated_data.csv', 'r') as file:
    # Read and parse header row
    headers = file.readline().strip().split(',')
    data = []
    # Process each line and create dictionary with header keys
    for line in file:
        values = line.strip().split(',')
        row_dict = dict(zip(headers, values)) 
        data.append(row_dict)

# Print first row as a sample of the generated data
print(data[0]) 