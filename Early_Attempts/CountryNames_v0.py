import pycountry

# Get all countries
countries = pycountry.countries

# Print the names of all countries
for country in countries:
    print(country.name)
    
# Requires you to use:: "pip install pycountry"