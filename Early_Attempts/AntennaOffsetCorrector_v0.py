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



def main():
    """
    Main function to get user input, calculate the correction, and display the result.
    """
    print("Dipole Antenna Length Correction Calculator\n")

    while True:
        try:
            target_frequency = float(input("Enter the target resonant frequency in MHz (e.g., 7.15): "))
            if target_frequency <=0:
                print("Frequency must be greater than zero. Please enter a valid number")
                continue
            measured_frequency = float(input("Enter the measured resonant frequency in MHz (e.g., 7.10): "))
            if measured_frequency <= 0:
                print("Frequency must be greater than zero. Please enter a valid number")
                continue
            break # Exit loop
        
        except ValueError:
            print("Invalid input. Please enter numeric values for the frequencies.")
            

    length_correction_feet = calculate_length_correction(target_frequency, measured_frequency)

    if length_correction_feet is not None:
        length_correction_inches = length_correction_feet * 12
        print(f"\nTo correct the dipole's resonant frequency from {measured_frequency:.2f} MHz to {target_frequency:.2f} MHz:")
        if length_correction_feet > 0:
            print(f"  Lengthen the antenna by approximately {length_correction_inches:.2f} inches.")
        elif length_correction_feet < 0:
            print(f"  Shorten the antenna by approximately {abs(length_correction_inches):.2f} inches.")
        else:
            print("  The antenna length is correct.")
    else:
        print("  Invalid input.  Cannot calculate correction.")


if __name__ == "__main__":
    main()

