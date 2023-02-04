import csv
file_path = "2019.csv"
def sorting_by_gpd(file_path):
    with open('2019.csv', 'r', encoding='utf8') as file:
        reader = csv.DictReader(file)
        sorted_rows = sorted(reader, key=lambda row: float(row["GDP per capita"]), reverse=True)

    return sorted_rows

# file_path = "2019.csv"
# sorted_countries = sorting_by_gpd(file_path)

# for country in sorted_countries:
#     print(country["Country or region"], country["GDP per capita"])

def sorting_by_corr(sorted_countries):
    sorted_by_corruption = sorted(sorted_countries, key=lambda row: float(row["Perceptions of corruption"]))
    print("Top 5 counties by Perceptions of corruption: ")
    for i in range(5):
        print(f'{i+1}.{sorted_by_corruption[i]["Country or region"]} - Corruption level: {sorted_by_corruption[i]["Perceptions of corruption"]}')

file_path = '2019.csv'
sorted_countries = sorting_by_gpd(file_path)

print('Coutries sorted by GDP by capita: ')
for country in sorted_countries:
    print(country["Country or region"], country["GDP per capita"])

sorting_by_corr(sorted_countries)