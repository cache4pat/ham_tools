# Data based on Radio Amateurs of Canada (RAC) information
# Note: Always consult the official RAC website for the most accurate and up-to-date information.
rac_band_plan = {
    '160m': '1.800 - 2.000 MHz',
    '80m': '3.500 - 4.000 MHz',
    '60m': '5.330 - 5.400 MHz (various specific frequencies and ranges)',  # Simplified
    '40m': '7.000 - 7.300 MHz',
    '30m': '10.100 - 10.150 MHz',
    '20m': '14.000 - 14.350 MHz',
    '17m': '18.068 - 18.168 MHz',
    '15m': '21.000 - 21.450 MHz',
    '12m': '24.890 - 24.990 MHz',
    '10m': '28.000 - 29.700 MHz',
    '6m': '50.000 - 54.000 MHz',
    '2m': '144.000 - 148.000 MHz',
    '1.25m': '219.000 - 220.000 MHz / 222.000 - 225.000 MHz', #Combined 1.25m
    '70cm': '430.000 - 450.000 MHz',
    '33cm': '902.000 - 928.000 MHz',
    '23cm': '1240.000 - 1300.000 MHz',
    '13cm': '2300.000 - 2310.000 MHz / 2390.000 - 2450.00 MHz', #combined
    '9cm': '3.300 - 3.500 GHz',
    '6cm': '5.650 - 5.925 GHz',
    '3cm': '10.000 - 10.500 GHz',
    '1.2cm': '24.000 - 24.250 GHz',
    '6mm': '47.000 - 47.200 GHz',
    '4mm': '75.5 - 81.0 GHz', #Simplified
    '2.5mm': '122.250 - 123.000 GHz',
    '2mm': '134 - 141 GHz', #Simplified
    '1mm': '241 - 250 GHz' #Simplified
}

def display_band_frequencies_canada(band):
    """
    Displays the frequency range for a given amateur radio band in Canada,
    based on RAC data.

    Args:
        band (str): The amateur radio band (e.g., '20m', '17m', '15m', '6m').
    """
    frequency_range = rac_band_plan.get(band)  # Use .get() for safety

    if frequency_range:
        print(f"\n    Frequency range for the {band} band in Canada: {frequency_range}")
    else:
        print(f"Frequency information not found for the {band} band in Canada.")
        print("Please check the band spelling or refer to the RAC website for valid bands.")

def calculate_dipole_length(frequency_mhz):
    """
    Calculates the approximate length of a half-wave dipole antenna in feet.
    Based on Wavelength = Speed of Light / Frequency in Meters
        and the speed of light in a vacuum as approximately 299,792,458 meters per second.
    So, 468 is a constant that combines the speed of light with 
        the conversion factors to get the antenna length in feet when the frequency is in MHz

    Args:
        frequency_mhz (float): The frequency in MHz.

    Returns:
        float: The length of the dipole antenna in feet.
    """
    if frequency_mhz <= 0:
        return 0.0  # Handle invalid frequency
    length_feet = 468 / frequency_mhz #Key Physical Factor
    return length_feet

def main():
    """
    Main function to display frequency ranges for various amateur radio bands in Canada.
    Now asks the user for input and calculates dipole length.
    """
    print("\nAvailable Amateur Radio Frequency Bands in Canada (Based on RAC):")

    for band in rac_band_plan.keys():
        print(band, end=", ")
    print(f"\n\n") #newlines

    while True:
        band_choice = input("Enter an amateur radio band (e.g., 20m, 17m, 6m, 160m, or 'exit'): ").strip()
        if band_choice.lower() == 'exit':
            break  # Exit the loop

        display_band_frequencies_canada(band_choice)

        # Calculate and display dipole length
        frequency_range = rac_band_plan.get(band_choice)
        if frequency_range:
            # Extract the lower frequency from the range string
            lower_freq_str = frequency_range.split()[0]  # Get the first part of the string
            try:
                lower_freq_mhz = float(lower_freq_str)
                dipole_length = calculate_dipole_length(lower_freq_mhz)
                dipole_segment = calculate_dipole_length(lower_freq_mhz*2)
                print(f"        Approximate half-wave dipole antenna End2End length for {band_choice}: {dipole_length:.2f} feet.")
                print(f"        Approximate half-wave dipole antenna Segment Length for {band_choice}: {dipole_segment:.2f} feet.\n")
                print(f"            Trimming Rate for {band_choice}: {dipole_segment:.2f} inches.\n")
            except ValueError:
                print(f"Could not calculate dipole length for {band_choice}.  Invalid frequency range.\n")
        else:
            print(f"Could not calculate dipole length for {band_choice}.  Invalid band choice.\n")

if __name__ == "__main__":
    main()
