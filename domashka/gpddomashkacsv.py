import csv
file_path = "2019.csv"
def sorting_by_gpd(file_path):
    with open('2019.csv', 'r', encoding='utf8') as file:
        reader = csv.DictReader(file)
        sorted_rows = sorted(reader, key=lambda row: float(row["GDP per capita"]), reverse=True)

    return sorted_rows

file_path = "2019.csv"
sorted_countries = sorting_by_gpd(file_path)

for country in sorted_countries:
    print(country["Country or region"], country["GDP per capita"])