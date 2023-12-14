import pycountry

all_countries = list(pycountry.countries)
with open('countries.txt', 'w') as file:
    for country in all_countries:
        file.write(country.name + '\n')

print("Countries have been written to cared_about_countries.txt")
