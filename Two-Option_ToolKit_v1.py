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
    '1.25m': '219.000 - 220.000 MHz / 222.000 - 225.000 MHz',  # Combined 1.25m
    '70cm': '430.000 - 450.000 MHz',
    '33cm': '902.000 - 928.000 MHz',
    '23cm': '1240.000 - 1300.000 MHz',
    '13cm': '2300.000 - 2310.000 MHz / 2390.000 - 2450.0 MHz',  # combined
    '9cm': '3.300 - 3.500 GHz',
    '6cm': '5.650 - 5.925 GHz',
    '3cm': '10.000 - 10.500 GHz',
    '1.2cm': '24.000 - 24.250 GHz',
    '6mm': '47.000 - 47.200 GHz',
    '4mm': '75.5 - 81.0 GHz',  # Simplified
    '2.5mm': '122.250 - 123.000 GHz',
    '2mm': '134 - 141 GHz',  # Simplified
    '1mm': '241 - 250 GHz'  # Simplified
}


def calculate_dipole_length(frequency_mhz):
    """
    Calculates the approximate length of a half-wave dipole antenna in feet.

    Args:
        frequency_mhz (float): The frequency in MHz.

    Returns:
        float: The length of the dipole antenna in feet.
    """
    if frequency_mhz <= 0:
        return 0.0  # Handle invalid frequency
    length_feet = 468 / frequency_mhz
    return length_feet


def calculate_length_correction(target_frequency_mhz, measured_frequency_mhz):
    """
    Calculates the required change in dipole length to correct the resonant frequency.

    Args:
        target_frequency_mhz (float): The desired resonant frequency in MHz.
        measured_frequency_mhz (float): The actual measured resonant frequency in MHz.

    Returns:
        float: The change in length in feet (positive value means lengthen, negative means shorten).
    """
    if target_frequency_mhz <= 0 or measured_frequency_mhz <= 0:
        return None  # Handle invalid input

    target_length_feet = calculate_dipole_length(target_frequency_mhz)
    measured_length_feet = calculate_dipole_length(measured_frequency_mhz)
    length_difference_feet = measured_length_feet - target_length_feet
    return length_difference_feet


def get_band_frequency(band):
    """
    Gets the center frequency of an amateur radio band from the RAC band plan.

    Args:
        band (str): The amateur radio band (e.g., '20m', '40m').

    Returns:
        float: The center frequency of the band in MHz, or None if the band is not found.
    """
    if band in rac_band_plan:
        frequency_range = rac_band_plan[band]
        # Split the string and take the lower frequency, then convert to float
        lower_freq_str = frequency_range.split()[0]
        try:
            lower_freq_mhz = float(lower_freq_str)
            return lower_freq_mhz
        except ValueError:
            return None
    else:
        return None



def main():
    """
    Main function to run the Antenna Tool Kit Program.
    """
    print("Antenna Tool Kit Program\n")

    while True:
        print("\nOptions:")
        print("A: Calculate antenna length from band")
        print("B: Calculate length correction from measured offset")
        print("C: Exit")

        choice = input("Enter your choice (A, B, or C): ").strip().upper()

        if choice == 'A':
            # Option A: Calculate antenna length from band
            print("\nAvailable bands: ")
            for band in rac_band_plan.keys():
                print(band, end=", ")
            print()  # newline

            band_choice = input("Enter an amateur radio band (e.g., 20m, 40m, 160m): ").strip()
            frequency = get_band_frequency(band_choice)
            if frequency:
                antenna_length = calculate_dipole_length(frequency)
                print(f"\nApproximate half-wave dipole antenna length for {band_choice}: {antenna_length:.2f} feet.\n")
            else:
                print(f"\nInvalid band choice. Please check the band spelling and refer to the list above or the RAC website.\n")

        elif choice == 'B':
            # Option B: Calculate length correction from measured offset
            band_choice = input("Enter the amateur radio band (e.g., 20m, 40m, 160m): ").strip()
            target_frequency = get_band_frequency(band_choice)
            print(f"\n Expected Band Resonance is {target_frequency} in MHz\n")

            if target_frequency is None:
                print(f"\nInvalid band choice. Please check the band spelling and refer to the RAC website.\n")
                continue  # Restart the main loop

            try:
                measured_offset = float(input(f"Enter the measured frequency offset from {band_choice} (in MHz, e.g., -0.1 for 7.05 instead of 7.15): "))
                measured_frequency = target_frequency + measured_offset
            except ValueError:
                print("\nInvalid input. Please enter a numeric value for the frequency offset.\n")
                continue  # Restart the main loop

            length_correction_feet = calculate_length_correction(target_frequency, measured_frequency)

            if length_correction_feet is not None:
                length_correction_inches = length_correction_feet * 12
                print(f"\nTo correct the dipole's resonant frequency for the {band_choice} band:")
                if length_correction_feet > 0:
                    print(f"  Lengthen the antenna by approximately {length_correction_inches:.2f} inches.")
                elif length_correction_feet < 0:
                    print(f"  Shorten the antenna by approximately {abs(length_correction_inches):.2f} inches.")
                else:
                    print("  The antenna length is correct.")
            else:
                print("\n  Invalid input.  Cannot calculate correction.\n")

        elif choice == 'C':
            print("\nExiting Antenna Tool Kit Program. 73!\n")
            break

        else:
            print("\nInvalid choice. Please enter A, B, or C.\n")


if __name__ == "__main__":
    main()
