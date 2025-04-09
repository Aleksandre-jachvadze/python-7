#- პროექტი 86 - Lines of Code
import sys

def count_code_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            code_lines = 0
            for line in file:
                stripped_line = line.strip()
                if stripped_line and not stripped_line.startswith('#'):
                    code_lines += 1
            return code_lines
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return None

def save_line_count(count):
    try:
        with open('lines/lines.py', 'w') as file:
            file.write(f'Number of code lines: {count}\n')
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 2:
        print("Please provide a file name!")
        return

    file_name = sys.argv[1]
    code_line_count = count_code_lines(file_name)

    if code_line_count is not None:
        print(f"Number of code lines: {code_line_count}")
        save_line_count(code_line_count)

if __name__ == "__main__":
    main()

2#- პროექტი 87 - Pizza Py
import csv
from tabulate import tabulate

regular_pizza = [
    ["ყველი", 13.50, 18.95],
    ["1 ტოპინგი", 14.75, 20.95],
    ["2 ტოპინგი", 15.95, 22.95],
    ["3 ტოპინგი", 16.95, 24.95],
    ["სპეციალური", 18.50, 26.95]
]

sicilian_pizza = [
    ["ყველი", 25.50, 39.95],
    ["1 ინგრედიენტი", 27.50, 41.95],
    ["2 ინგრედიენტი", 29.50, 43.95],
    ["3 ინგრედიენტი", 31.50, 45.95],
    ["სპეციალური", 33.50, 47.95]
]

def print_pizza_table(pizza_data, pizza_type):
    print(f"\n{pizza_type}:\n")
    headers = ["ტოპინგი", "პატარა", "დიდი"]
    print(tabulate(pizza_data, headers=headers, tablefmt="grid"))

print_pizza_table(regular_pizza, "პიცა Regular")
print_pizza_table(sicilian_pizza, "პიცა Sicilian")

#- პროექტი 88 - Scourgify

import csv
import sys

def process_names(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        data = list(reader)
    
    processed_data = []
    
    for row in data:
        if row:
            names = row[0].split()
            if len(names) == 2:
                processed_data.append(names)
    
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(processed_data)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    process_names(input_file, output_file)

-# პროექტი 89 - CS50 P-Shirt

from cs50 import get_string
from PIL import Image # type: ignore

def main():
    file = get_string("Enter the filename of the doll image: ")
    doll_image = Image.open(file)
    shirt = Image.open("shirt.png")
    doll_image.paste(shirt, (0, 0), shirt)
    doll_image.save("doll_with_shirt.png")

if __name__ == "__main__":
    main()

#- პროექტი 90 - Name Sorter
import csv
from tabulate import tabulate

data = []
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

data.sort(key=lambda x: x[0])

headers = ["Last", "First", "Salary"]

print("$ Last                | First             | Salary")
print("$ --------------------|-------------------|----------------")
print(tabulate(data, headers=headers, tablefmt="plain"))

