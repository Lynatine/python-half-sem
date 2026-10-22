import csv

def sol4():
    with open("products.csv", "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        with open("expensive.csv", "w", encoding="utf-8", newline="") as file2:
            writer = csv.DictWriter(file2, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                if float(row["price"]) > 100:
                    writer.writerow(row)


sol4()
