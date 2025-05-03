import pycountry

# Get the band from the user input
band = input("Please enter the band for which you want to display the frequency range in Canada: ")

# Function to display the frequency ranges for a given band in Canada
def display_band_frequencies(band):
    # Get the Canada country object
    canada = pycountry.countries.get(alpha_2='CA')

    # Check if the country is found
    if canada:
        # Get the frequency range for the specified band in Canada
        frequency_range = canada.get(band)

        # Print the frequency range
        if frequency_range:
            print(f"Frequency range for the {band} band in Canada:", frequency_range)
        else:
            print(f"Frequency range for the {band} band in Canada not found.")
    else:
        print("Country not found.")

# Display the frequency range for the specified band in Canada
display_band_frequencies(band)

# This Fails "canada = pycountry.countries.get(alpha_2='CA') "fails. Because a Table of Bands is Required
# See " RAC_Band-Ranges.py " for fix