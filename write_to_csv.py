import csv

def write_to_csv(contents):
    
    header = ['title', 'price', 'popular']

    with open('./reommended-books.csv', 'w',newline='', encoding='shift-jis', errors='ignore') as f:
        writer = csv.DictWriter(f, header)
        writer.writeheader()
        for content in contents:
                writer.writerow(content)