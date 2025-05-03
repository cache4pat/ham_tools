def get_band_frequency(band):
    """Returns the lower and upper frequency limits for a given amateur radio band in MHz."""
    bands = {
        "160m": (1.800, 2.000),
        "80m": (3.500, 4.000),
        "40m": (7.000, 7.300),
        "20m": (14.000, 14.350),
        "15m": (21.000, 21.450),
        "10m": (28.000, 29.700),
    }
    return bands.get(band)

def get_band_resonance_center_frequency(band):
    """Returns the center resonance frequency for a given amateur radio band in MHz."""
    limits = get_band_frequency(band)
    if limits:
        lower, upper = limits
        return upper - lower
    return None

def two_choice_program():
    """Presents two choices related to amateur radio bands and checks the user's answer."""
    import random

    bands = ["160m", "80m", "40m", "20m", "15m", "10m"]
    correct_band = random.choice(bands)
    lower_freq_mhz, upper_freq_mhz = get_band_frequency(correct_band)
    resonance_center_frequency = get_band_resonance_center_frequency(correct_band)

    print("Welcome to the Amateur Radio Band Quiz!")
    print(f"\nQuestion: Which of the following is the approximate frequency range for the {correct_band} band?")

    # Choice A: Correct answer
    print(f"A) {lower_freq_mhz:.3f} MHz - {upper_freq_mhz:.3f} MHz")

    # Choice B: Incorrect answer using the resonance center frequency as the target
    incorrect_offset = random.uniform(-1.0, 1.0)  # Add some variation to make it clearly wrong
    incorrect_frequency = resonance_center_frequency + incorrect_offset
    print(f"B) Target Frequency: {incorrect_frequency:.3f} MHz")

    while True:
        user_choice = input("Enter your choice (A or B): ").upper()
        if user_choice in ["A", "B"]:
            break
        else:
            print("Invalid choice. Please enter 'A' or 'B'.")

    if user_choice == "A":
        print("\nCorrect! Well done!")
    else:
        print(f"\nIncorrect. The correct frequency range for the {correct_band} band is {lower_freq_mhz:.3f} MHz - {upper_freq_mhz:.3f} MHz.")

if __name__ == "__main__":
    two_choice_program()