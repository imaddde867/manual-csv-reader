import csv
import datetime 
import random

names = ['Karoline','Clea','Lena','Alena','Imad','Ema','Jack','Wilson','Tom','Tommas','Nelso','Mila','Aurelie','Vanessa','Sarah','Rihanna','Eman','Paula','Lotti','Tiina']
date0 = int(datetime.datetime(2000, 1, 1, 00, 00).timestamp())
date1 = int(datetime.datetime.now(datetime.UTC).timestamp())
subscription_statuses = ['Active', 'Inactive']

file = open("randomly_generated_data.csv", "w")

header = ('name','date of joining', 'age', 'subscription status')

lines=[]

def line_gen() :
    date = random.randint(date0, date1)
    readable_date = datetime.datetime.fromtimestamp(date).strftime('%d.%m.%Y')
    line = [
        random.choice(names),
        readable_date,
        random.randint(18, 80),
        random.choice(subscription_statuses),
    ]
    lines.append(line)

number_of_rows = random.randint(100, 500)
for _ in range(number_of_rows):
    line_gen()

with open("randomly_generated_data.csv", "w", newline='\n') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(lines)
