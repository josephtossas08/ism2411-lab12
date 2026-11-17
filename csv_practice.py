
Reflection Questions
1. #Python vs. Excel: Python is better for automating repeatable tasks and handling larger datasets, while Excel is useful for visual editing and manual calculations.
2. #Append mode: A business can record each order-processing run in a log without erasing previous records.



# Excercise 1
import csv
from datetime import datetime
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"
SALES_FILE = DATA_DIR / "sales.csv"
CLEANED_FILE = DATA_DIR / "cleaned.csv"
LOG_FILE = DATA_DIR / "run_log.txt"


# EXERCISE 2 

with open(SALES_FILE, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# EXERCISE 3 

with open(SALES_FILE, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)


# EXERCISE 4 
total_revenue = 0.0
with open(SALES_FILE, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header.
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        total_revenue += line_total
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")


# EXERCISE 5
written_count = 0
with open(SALES_FILE, "r", newline="", encoding="utf-8") as infile, \
     open(CLEANED_FILE, "w", newline="", encoding="utf-8") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    next(reader)  # Skip original header.
    writer.writerow(["Product", "Price", "Qty", "Total"])

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        if line_total > 100:
            writer.writerow([product, f"{price:.2f}", quantity, f"{line_total:.2f}"])
            written_count += 1

original_count = sum(1 for _ in open(SALES_FILE, "r", encoding="utf-8")) - 1
print(f"Rows written to cleaned.csv: {written_count}")
print(f"Original data rows: {original_count}")


# EXERCISE 6 
dict_total_revenue = 0.0
with open(SALES_FILE, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        dict_total_revenue += price * quantity

print(f"Total revenue using DictReader: ${dict_total_revenue:.2f}")

# I prefer DictReader when columns have meaningful names because row["price"]
# is easier to understand than row 1. I use csv.reader for simple files where
# I only need values by position and the column order is fixed.


# EXERCISE 7 
product_totals = {}
with open(SALES_FILE, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        line_total = float(row["price"]) * int(row["quantity"])
        product_totals[product] = product_totals.get(product, 0.0) + line_total

for product in sorted(product_totals):
    print(f"{product}: ${product_totals[product]:.2f}")


# EXERCISE 8 
timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
with open(LOG_FILE, "a", encoding="utf-8") as log_file:
    log_file.write(f"{timestamp} | Total revenue: ${total_revenue:.2f}\n")

print(f"Added one entry to {LOG_FILE}")
