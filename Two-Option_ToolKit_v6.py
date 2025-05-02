# ------------------------------------------------------------------------------
# Title:
#   Dipole Antenna Creation ToolKit  
#
# Authors:
#   VA3PAF
#   "AI Collaboration with Gemini"
#
# Date Created: 
#   2025-04-28
#
# Version: 
#    7.0
#
# Description: 
#   A Two part Tool to provide Dipole Antenna lengths for various RAC Bands; 
#   and a means to Adjust them.
#
# ------------------------------------------------------------------------------

import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def greet_user():
    """Prints a greeting to the user."""
    print("Welcome to the Antenna Tool Kit Program!")

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


def convert_frequency_to_mhz(freq_str):
    """
    Converts a frequency string (e.g., "14.0 MHz", "5.650 GHz") to MHz.

    Args:
        freq_str (str): The frequency string.

    Returns:
        float: The frequency in MHz.
    """
    freq_value = float(freq_str.split()[0])
    if "GHz" in freq_str:
        return freq_value * 1000
    return freq_value


def get_band_frequency(band):
    """
    Gets the CENTER frequency of an amateur radio band from the RAC band plan in MHz.

    Args:
        band (str): The amateur radio band (e.g., '20m', '9cm').

    Returns:
        float: The CENTER frequency of the band in MHz, or None if the band is not found.
    """
    if band in rac_band_plan:
        frequency_range = rac_band_plan[band]
        lower_freq_str = frequency_range.split('-')[0].strip()
        upper_freq_str = frequency_range.split('-')[1].strip()
        try:
            lower_freq_mhz = convert_frequency_to_mhz(lower_freq_str)
            upper_freq_mhz = convert_frequency_to_mhz(upper_freq_str)
            center_frequency = (lower_freq_mhz + upper_freq_mhz) / 2
            return center_frequency
        except (ValueError, IndexError):
            return None
    else:
        return None


def get_band_resonance_center_frequency(band):
    """
    Calculates the center resonance frequency of an amateur radio band in MHz.

    Args:
        band (str): The amateur radio band (e.g., '20m', '9cm').

    Returns:
        float: The center resonance frequency of the band in MHz, or None if the band is not found.
    """
    if band in rac_band_plan:
        frequency_range = rac_band_plan[band]
        try:
            lower_freq_str = frequency_range.split('-')[0].strip()
            upper_freq_str = frequency_range.split('-')[1].strip()
            lower_freq_mhz = convert_frequency_to_mhz(lower_freq_str)
            upper_freq_mhz = convert_frequency_to_mhz(upper_freq_str)
            center_frequency = lower_freq_mhz + (upper_freq_mhz - lower_freq_mhz) / 2
            return center_frequency
        except (ValueError, IndexError):
            return None
    return None


def display_bands(band_plan, items_per_line=12, indent="\t"):  # Added indent
    """
    Displays the band plan with a specified number of items per line.

    Args:
        band_plan (dict): The dictionary containing the band plan.
        items_per_line (int): The number of bands to display per line.
        indent (str): String to indent each line with (default tab).
    """
    bands = list(band_plan.keys())
    for i in range(0, len(bands), items_per_line):
        line = bands[i:i + items_per_line]
        print(indent + ", ".join(line))


def main():
    """
    Main function to run the Antenna Tool Kit Program.
    """
    clear_screen()
    greet_user()

    while True:
        print("\n\n Antenna Tool Kit Program Options:\n")
        print("\t A: Calculate antenna length from band")
        print("\t B: Calculate length correction from measured offset")
        print("\t C: Clear Screen and Start Again")
        print("\t D: Exit")

        choice = input("\t\t Enter your choice (A, B, C, or D): ").strip().upper()

        clear_screen()  # Clear screen *after* choice

        if choice == 'A':
            # Option A: Calculate antenna length from band
            print("\nCalculate Dipole Length for Any of These Available Bands: ")
            # print("\nAvailable bands: ")
            display_bands(rac_band_plan)
            print()  # newline
            print()  # 2nd Newline

            band_choice = input("By Entering Your Desired Amateur Radio Band (e.g., 20m, 40m, 160m): ").strip()
            frequency = get_band_frequency(band_choice)  # Now gets center frequency!
            if frequency:
                antenna_length = calculate_dipole_length(frequency)
                print(f"\n      Here is the Approximate half-wave dipole antenna length for {band_choice}: {antenna_length:.2f} feet.\n")
            else:
                print(f"\nInvalid band choice. \n Wrong Number or Missing Unit Designator (eg: 20m)? \n \t Please Reference provided band list or the RAC website.\n")

        elif choice == 'B':
            # Option B: Calculate length correction from measured offset
            print("\nCalculate Length Correction for Your Chosen Bands, Based on Your Measured Center Resonance : ")
            display_bands(rac_band_plan)
            print()  # newline
            print()  # 2nd Newline

            band_choice = input("Enter the amateur radio band (e.g., 20m, 40m, 160m): ").strip()
            target_frequency = get_band_resonance_center_frequency(band_choice)

            if target_frequency is None:
                print(f"\nInvalid band choice.\n Wrong Number or Missing Unit Designator (eg: 20m)? \n \t Please Reference provided band list or the RAC website.\n")
                continue  # Restart the main loop

            print(f"\nExpected Band Resonance is {target_frequency:.3f} MHz")

            try:
                measured_frequency = float(input(f"------ Enter the measured resonance center frequency for {band_choice} (in MHz): "))

            except ValueError:
                print("\nInvalid input. Please enter a numeric value for the frequency.\n")
                continue  # Restart the main loop

            length_correction_feet = calculate_length_correction(target_frequency, measured_frequency)

            if length_correction_feet is not None:
                length_correction_inches = length_correction_feet * 12
                print(f"\nTo correct the dipole's resonant frequency for the {band_choice} band:")
                if length_correction_feet > 0:
                    print(f"------ Lengthen the antenna by approximately {length_correction_inches:.2f} inches.")
                elif length_correction_feet < 0:
                    print(f"------ Shorten the antenna by approximately {abs(length_correction_inches):.2f} inches.")
                else:
                    print("  The antenna length is correct.")
            else:
                print("\n  Invalid input.  Cannot calculate correction.\n")

        elif choice == 'C':
            clear_screen()
            greet_user()

        elif choice == 'D':
            print("\nExiting Antenna Tool Kit Program. 73!\n")
            break

        else:
            print("\nInvalid choice. Please enter A, B, C, or D.\n")


if __name__ == "__main__":
    main()